import extraction
import clustering
import preprocessing
import classification

import pandas as pd
import argparse

if __name__ == "__main__":
    # Creation of arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--classification', dest='classification', action='store_true')
    parser.add_argument('--no-classification', dest='classification', action='store_false')
    parser.add_argument('--clustering', dest='clustering', action='store_true')
    parser.add_argument('--no-clustering', dest='clustering', action='store_false')
    parser.set_defaults(classification=True, clustering=True)
    parser.add_argument('-p', '--parameters', type=int, nargs='+')

    args = parser.parse_args()

    # Importing the data
    data = pd.read_csv('data/data.csv', sep=',')

    # If parameters argument is provided, we run the extraction with these parameters
    if args.parameters:
        extraction.extraction(args.parameters[0], args.parameters[1])
        # And we process the data
        preprocessing.main(data)

    # Importing the processed data
    processed_data = pd.read_csv('data/processed_data.csv', sep=',')
    # If clustering is set to True, we run the clustering
    if args.clustering:
        clustering.main(processed_data)
        # If classification is set to True, we run the classification
    if args.classification:
        classification.main(processed_data)
