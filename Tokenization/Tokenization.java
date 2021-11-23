import java.io.File;
import java.util.Arrays;
import java.util.HashMap;
import java.util.ArrayList;
import java.io.IOException;
import java.util.Map.Entry;
import java.io.FileInputStream;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.nio.charset.Charset;
import java.nio.MappedByteBuffer;
import java.nio.channels.FileChannel;

public class Tokenization {

  // Retourne le contenu d'un fichier sous forme d'une chaine de caractères
	public static String readFile(String filename) {
		try {
			FileInputStream stream = new FileInputStream(new File(filename));
			FileChannel fc = stream.getChannel();
			MappedByteBuffer bb = fc.map(FileChannel.MapMode.READ_ONLY, 0, fc.size());
			stream.close();
			return Charset.defaultCharset().decode(bb).toString();
		} catch (IOException e) {
			System.out.println("Erreur lors de l'accès au fichier " + filename);
			System.exit(1);
		}
		return null;
	}

  public static ArrayList<String> segmentation(ArrayList<String> phrases, ArrayList<String> phonemes, ArrayList<String> tons) {
    String phonemeMax = "";
		ArrayList<String> phonemesTexte = new ArrayList<String>();
    for (String phrase : phrases) {
			String phonemesPhrase = "";
      while (!phrase.isEmpty()) {
        phonemeMax = phonemeMax(phrase, phonemes);
				// Si on n'a pas trouvé le caractère dans les phonèmes, on le cherche dans les tons
        if (phonemeMax.equals("")) {
          phonemeMax = phonemeMax(phrase, tons);
					// Ne pouvant utiliser le caractere "|" dans une regex, je le supprime manuellement
          if (phonemeMax.equals("") || phonemeMax.equals("|")) {
            phrase = phrase.substring(1);
          }
        }
        phrase = phrase.replaceFirst(phonemeMax, "");
				if (!phonemeMax.equals("")) {
        	phonemesPhrase += phonemeMax + " ";
				}
      }
			phonemesTexte.add(phonemesPhrase);
    }
    return phonemesTexte;
  }

  public static String phonemeMax (String phrase, ArrayList<String> listeAFouiller) {
    String phonemeMax = "";
    for (String fouille : listeAFouiller) {
      if (phrase.startsWith(fouille) && phonemeMax.length() < fouille.length()) {
        phonemeMax = fouille;
      }
    }
    return phonemeMax;
  }


  // Permet de recuperer les phonemes qui sont, dans le fichier, avant un ":"
  public static ArrayList<String> separerPhonemes(String fichier) {
    ArrayList<String> phonemes = new ArrayList<String>();
    for (String ligne : fichier.split("\n")) {
      String phoneme[] = ligne.split(":");
			phonemes.add(phoneme[0]);
    }
    return phonemes;
  }

  // Permet de recuperer les transcriptions et les segmentations
	public static ArrayList<ArrayList<String>> separerTranscriptions(String fichier) {
		ArrayList<ArrayList<String>> transEtSegm = new ArrayList<ArrayList<String>>();
    ArrayList<String> transcriptions = new ArrayList<String>();
    ArrayList<String> segmentations = new ArrayList<String>();
		for (String phrase : fichier.split("\n")) {
			String phrases[] = phrase.split(" @@@ ");
			if (phrases.length == 2) {
				transcriptions.add(phrases[0]);
				segmentations.add(phrases[1]);
			}
		}
    transEtSegm.add(transcriptions);
    transEtSegm.add(segmentations);
		return transEtSegm;
	}

  public static ArrayList<String> normalisation(ArrayList<String> transcriptions) {
    for (int i=0; i<transcriptions.size(); i++) {
      String phrase = transcriptions.get(i);
      phrase = phrase.replaceAll("\u25ca", "\u007c");
      phrase = phrase.replaceAll("\\[.*\\]?", "");
      phrase = phrase.replaceAll("<|>", "");
      phrase = phrase.replaceAll("wæ̃", "w̃æ");
      phrase = phrase.replaceAll("v\u0303\u030D", "v\u0303\u0329");
			// Je fais en sorte que tous mes "ṽ̩" soient codés dans le même ordre (le tilde avant le trait vertical)
			phrase = phrase.replaceAll("v\u0329\u0303", "v\u0303\u0329");
      phrase = phrase.replaceAll("\u0259+\u2026", "\u0259\u0259\u0259\u2026");
      phrase = phrase.replaceAll("m+\u2026", "mmm\u2026");
      Pattern p = Pattern.compile("BEGAIEMENT");
      Matcher m = p.matcher(phrase);
      if (m.find()) {
        phrase = "";
      }
      transcriptions.set(i, phrase);
    }
    return transcriptions;
  }

  public static int segmentationFinale(ArrayList<ArrayList<String>> phrases, ArrayList<String> phonemes, ArrayList<String> tons) {
    ArrayList<String> transcriptions = phrases.get(0);
    ArrayList<String> segmentationsVerifiees = phrases.get(1);
    transcriptions = normalisation(transcriptions);
    ArrayList<String> segmentations = segmentation(transcriptions, phonemes, tons);
    int bonnesSegmentations = 0;
    for (int i=0; i<segmentations.size(); i++) {
      if (identiques(segmentations.get(i), segmentationsVerifiees.get(i))) {
			  bonnesSegmentations++;
      }
    }
    return bonnesSegmentations;
  }

  public static boolean identiques(String phrase1, String phrase2) {
    int minLength = phrase2.length();
    if (phrase2.length() > phrase1.length()) {
      minLength = phrase1.length();
    }
    for (int i=0; i<minLength; i++) {
      int codePoint1 = phrase1.codePoints().toArray()[i];
      int codePoint2 = phrase2.codePoints().toArray()[i];
      if (codePoint1 != codePoint2) {
        return false;
      }
    }
    return true;
  }

	private static void printSortedFrequencies(HashMap<String, Integer> res) {
		for (Entry<String, Integer> r : MapUtil.sortByValue(res)) {
			System.out.println(r.getKey() + "->" + r.getValue());
		}
	}

	public static HashMap<String, Integer> frequences(ArrayList<String> segmentations, ArrayList<String> phonemes) {
		HashMap<String, Integer> frequences = new HashMap<String, Integer>();
		// J'intègre d'abord tous les phonèmes du Na avec 0 comme valeur, ainsi je peux voir facilement si certains ne sont pas représentés
		for (String phoneme : phonemes) {
			frequences.put(phoneme, 0);
		}
		for (String segmentation : segmentations) {
			// Chaque phonème ayant été séparé par un espace, un moyen simple de récupérer les phonèmes utilisés est de chercher les espaces
			for (String caractere : segmentation.split(" ")) {
				frequences.put(caractere, frequences.getOrDefault(caractere, 0)+1);
			}
		}
		return frequences;
	}

  public static void main(String[] args) {
    String transcriptions = readFile("Transcriptions.txt");
    String phonemesNa = readFile("Na.txt");
    ArrayList<ArrayList<String>> phrases = separerTranscriptions(transcriptions);
		int nbSegmentationsTotales = phrases.get(1).size();
    // phrases.get(0) : ArrayList<String> transcriptions
    // phrases.get(1) : ArrayList<String> segmentations
		ArrayList<String> phonemes = separerPhonemes(phonemesNa);
		ArrayList<String> tons = new ArrayList<>(Arrays.asList("\u02e9", "\u02e5", "\u02e7", "\u02e7\u02e5", "\u02e9\u02e5", "\u02e9\u02e7", "\u02e7\u02e9", "\u007c"));
		int bonnesSegmentations = segmentationFinale(phrases, phonemes, tons);
		HashMap<String, Integer> frequences = frequences(phrases.get(1), phonemes);
		printSortedFrequencies(frequences);
		System.out.println();
		System.out.println(bonnesSegmentations + " bonnes segmentations sur " + nbSegmentationsTotales + " segmentations au total.");
		System.out.println("Précision de la segmentation : " + bonnesSegmentations/(double)nbSegmentationsTotales);
  }

}
