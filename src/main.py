import numpy as np
import pandas as pd
import json
#import sys
#sys.path.append('/home/grace/Documents/Projets-Data/Projet_Servier/sample/helpers.py')

# import sample.helpers

drugs = pd.read_csv('../data/drugs.csv')
data_drugs = drugs.iloc[:, :].values


pubmed = pd.read_csv('../data/pubmed.csv')
data_pubmed = pubmed.iloc[:, :].values


clinical_trials = pd.read_csv('../data/clinical_trials.csv')
data_clinical_trials = clinical_trials.iloc[:, :].values

# Traitement des données manquantes dans le fichier data_clinical_trials
###
#  Non véritablement nécéssaire de réaliser un traitement à priori des valeurs manquantes
#  car les données ne sont pas numériques.
###

# Transformation des donées
drug_pubmed = []
drug_journal = []
drug_clinical_trials = []

# Obtention d'un médicament et des titres des pubmed dans lesquelles son nom a été cité ainsi que la date de publication
data_drugs = data_drugs.astype('str')
data_pubmed = data_pubmed.astype('str')
data_clinical_trials = data_clinical_trials.astype('str')


drugs_name = np.char.capitalize(data_drugs[:, 1])

for drug in drugs_name:
    for i in range(len(data_pubmed[:, 1])) :
        if drug.lower() in data_pubmed[i,1].lower():
            drug_list1 = [drug, data_pubmed[i, 1], data_pubmed[i, 2]]
            drug_list4 = [drug, data_pubmed[i, -1], data_pubmed[i, 2]]
            drug_journal.append(drug_list4)
            drug_pubmed.append(drug_list1)

print(drug_pubmed)

# Obtention d'un médicament et des titres des clinical_trials dans lesquelles son nom a été cité ainsi que la date de publication
print("\n\n------------------------------------------------------------------------------------------------------------------\n\n")
for drug in drugs_name:
    for i in range(len(data_clinical_trials[:, 1])) :
        if drug.lower() in data_clinical_trials[i,1].lower():
            drug_list2 = [drug, data_clinical_trials[i, 1], data_clinical_trials[i, 2]]
            drug_list3 = [drug, data_clinical_trials[i, -1], data_clinical_trials[i, 2]]
            drug_journal.append(drug_list3)
            drug_clinical_trials.append(drug_list2)

print(drug_clinical_trials)

# Obtention d'un médicament et des titres des journaux dans lesquelles son nom a été cité ainsi que la date de publication
print("\n\n------------------------------------------------------------------------------------------------------------------\n\n")
print(drug_journal)

#   Écriture dans le fichier Json
data = []

for j in range(len(drugs_name)):
    info_drug = {}
    pubmed_dict = {}
    clinical_trials_dict = {}
    journal_dict = {}
    info_drug["drug"] = drugs_name[j]
    for k in range(len(drug_pubmed)) :
        if drugs_name[j] == drug_pubmed[k][0] :
            pubmed_dict[drug_pubmed[k][1]] = drug_pubmed[k][2]

    info_drug["pubmed"] = pubmed_dict

    for l in range(len(drug_clinical_trials)) :
        if drugs_name[j] == drug_clinical_trials[l][0] :
            clinical_trials_dict[drug_clinical_trials[l][1]] = drug_clinical_trials[l][2]
    
    info_drug["clinical_trials"] = clinical_trials_dict


    for m in range(len(drug_journal)) :
        if drugs_name[j] == drug_journal[m][0] :
            journal_dict[drug_journal[m][1]] = drug_journal[m][2]

    info_drug["journal"] = journal_dict

    data.append(info_drug)
    
print("\n\n------------------------------------------------------------------------------------------------------------------\n\n")
print(data)

with open("relation.json", "w") as f:
    json.dump(data, f, indent=4)

        
