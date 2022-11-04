from html import entities
from pathlib import Path
# Import notebook
# How to import a notebook a file
import csv


# How to define a function in python with the word key
# the type date after the : is only documentation for Python
def read_csv_file(csv_file_path: str) -> list:
    
    with open(csv_file_path, newline='') as csvfile:
        csv_reader=csv.DictReader(csvfile, delimiter=";")
        result = [row_dict for row_dict in csv_reader]
        
    return result


csv_file_path = "scimagojr 2021 Subject Area - Medicine.csv"
entries = read_csv_file(csv_file_path)

num: int = 0

# listas_españa = [numEntriesSpain+=1]
lista_espa = [num + 1 for entry in entries if(entry['Country'] == 'Spain')]
toatal_list_spa = sum(lista_espa)
print(toatal_list_spa)




# print(entries[0:24])

# numEntriesSpain: int = 0
# for entry in entries:
#     if(entry['Country'] == 'Spain'):
#         numEntriesSpain+=1

# print(numEntriesSpain)

def filterUKJournalHIndex300 (entry:dict) -> bool:      
        return entry['Country'] == 'United Kingdom' and entry['Type'] == 'journal' and int(entry['H index']) > 200 
entriesUKJournalHIndex300 = list(filter(filterUKJournalHIndex300,entries))                          
print(len(entriesUKJournalHIndex300))


# def types (entry:dict) -> bool:      
#         return entry['Type'] == 'journal' 
# types_of_jurnal = list(filter(types,entries))                          
# print(types_of_jurnal)

types_set: set = set()
listita =set([entry['Type'] for entry in entries ])

print('Types of scientific publications.')
print(listita)


num_entries_type = {}
for entry in entries:
    # if Type don't exist, we add it in the dict.
    if (not (entry['Type'] in num_entries_type)):
        num_entries_type[entry['Type']]=1
    # if Type exist, we sum 1 more publication.
    else:
        num_entries_type[entry['Type']] = num_entries_type[entry['Type']] + 1

print(num_entries_type)



# num_cat_type = {}
# for entry in entries:
#     # if Type don't exist, we add it in the dict.
#     if (not (entry['Categories'] in num_cat_type)):
#         num_cat_type[entry['Categories']]=1
#     # if Type exist, we sum 1 more publication.
#     else:
#         num_cat_type[entry['Categories']] = num_cat_type[entry['Categories']] + 1

# print(num_cat_type)

# cccc =set([entry['Categories'] for entry in entries ])
# print(cccc)


list_sports_science_entries = [entry for entry in entries if 'sports medicine' in entry['Categories'].lower()]
list_sports_medicine_entries = [entry for entry in entries if 'sports science' in entry['Categories'].lower()]

print('Sports Science',len(list_sports_science_entries))
print('Sports Medicine',len(list_sports_medicine_entries))

types_set: set = set()
listita =set([entry['Region'] for entry in entries ])
print(listita)