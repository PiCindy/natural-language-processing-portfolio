Automatic Tokenization of Yongning Na

Segmentation phonémique du Yongning Na

L’objectif de ce TP est d’implémenter un système capable de segmenter des transcriptions phonémiques en séquence de phonèmes pour le Yongning Na. Le Yongning Na est une langue tonale de la famille des langues sino-tibétaines parlée dans le centre sud de la province du Sichuan en Chine. C’est une langue aujourd’hui considérée en danger et développer des outils de TAL pour aider à sa documentation est un sujet de recherche particulièrement actif.
Le développement de système de transcription phonémique automatique constitue une première étape pour aider les linguistes de terrain dans leur travail de description et de documentation de la langue. Une première série d’expériences 2 a montré qu’il était possible, à l’aide de technique d’apprentissage automatique, de développer de tels systèmes à partir des annotations produites par des linguistes de terrain. Il faut toutefois, avant d’utiliser de tels systèmes, transformer les transcriptions en séquences de phonèmes (contenant uniquement les unités devant être prédites par le système). Par exemple la phrase :
si˧dzi˩-ʈʂʰɯ˩,␣|␣ʈʰææ̃ ˧␣|␣ʈʂʰɯ˧-bv̩˧-ɻ ̍˧␣| dɑ˧-kv̩˥-mæ˩ !␣|
devra être transformée en :
s␣i␣˧␣dz␣i␣˩␣ʈʂʰ␣ɯ␣˩␣|␣ʈʰ␣æ␣æ̃ ␣˧␣|␣ʈʂʰ␣ɯ␣˧␣b␣v̩␣˧␣ɻ ̍␣˧␣|␣d␣ɑ␣˧␣k␣v̩␣˥␣m␣æ␣˩␣|
L’objectif de ce TP est de développer un système capable de faire cette segmentation.

