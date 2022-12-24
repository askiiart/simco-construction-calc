import os
import csv
import pickle
from pprint import pprint

try:
    from wget import download
except ImportError as e:
    print('Error: Please install wget using "pip install wget"')
    exit(1)

def data_download(buildings_file_name, debug=False):

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
            if row[0] != 'Building' and row[0] != '':
                temp = list(row)
                buildings[temp[0].lower()] = [row[i].lower() for i in range(1, len(row))]

    pickle.dump(buildings, open(f'{buildings_file_name[:-4]}.pickle', 'wb'))

    return buildings

    os.chdir('..')


print('Downloading and processing buildings...')
buildings = data_download('buildings.tsv')  # In format {building_name: [brick, plank, rc, cu]}
print('Buildings downloaded and processed')
print()

# Can't keep track of hours because it varies by building, and it would be such a pain to figure out
total = [0, 0, 0, 0]  # Number of [rc, bricks, planks, cu] needed for upgrade (total)
running = True
while running:
    print('What building do you want to upgrade?')
    buildings_keys = list(buildings.keys())
    for i in range(len(buildings)):
        print(f'{i + 1}: {buildings_keys[i]}')

    i = int(input('Enter the number corresponding to the building:\n')) - 1
    current_level = int(input('What is the current level of the building? Enter 0 if it is not built yet.\n'))
    target_level = int(input('What is the target level of the building?\n'))
    print()

    for j in range(current_level, target_level):
        if j == 0:
            temp = 1
        else:
            temp = j
        total[0] += int(buildings[buildings_keys[i]][3]) * temp
        total[1] += int(buildings[buildings_keys[i]][4]) * temp
        total[2] += int(buildings[buildings_keys[i]][5]) * temp
        total[3] += int(buildings[buildings_keys[i]][6]) * temp
    
    print('Would you like to upgrade another building? (y/N)')
    if input().lower() != 'y':
        running = False
    print()
    print()

print('Total resources needed:')
print(f'  Reinforced Concrete: {total[0]}')
print(f'  Bricks: {total[1]}')
print(f'  Planks: {total[2]}')
print(f'  Construction Units: {total[3]}')
