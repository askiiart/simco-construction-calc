import os
import csv
import pickle
from pprint import pprint

try:
    from wget import download
except ImportError as e:
    print('Error: Please install wget using "pip install wget"')
    exit(1)

def download_and_process(buildings_file_name, debug=False):

    if 'data' not in os.listdir():
        os.mkdir('data')
    os.chdir('data')
    if debug:
        print(os.listdir())

    # Buildings download
    if f'{buildings_file_name[:-4]}.pickle' in os.listdir():
        pickle.load(open(f'{buildings_file_name[:-4]}.pickle', 'rb'))
    elif buildings_file_name not in os.listdir():
        if debug:
            print('Downloading building info...')
        download(
            'https://docs.google.com/spreadsheets/d/16J269YAFTVy_IPuzGUXfV_4-Rplzk1LVk7YpsvDcEVY/export?format=tsv',
            buildings_file_name)
        if debug:
            print('Building info downloaded')
    else:
        print('Building info already downloaded, but not pickled')

    # Buildings tsv processing
    with open(buildings_file_name) as file:
        reader = csv.reader(file, delimiter='\t')  # Changes delimiter to tab for .tsv files
        buildings = {}
        for row in reader:
            temp = list(row)
            buildings[temp[0].lower()] = [row[i].lower() for i in range(1, len(row))]
    pickle.dump(buildings, open(f'{buildings_file_name[:-4]}.pickle', 'wb'))

    return buildings

    os.chdir('..')


print('Downloading and processing buildings...')
buildings = download_and_process('buildings.tsv')
print('Buildings downloaded and processed')
print()
