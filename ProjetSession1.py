### Phase 1 : Extraction des données
#Avoir accèes aux données
import zipfile
import os

# Chemin vers votre fichier ZIP
zip_file_path = 'gta431_projet.zip'

# Répertoire où extraire les données ZIP
extract_dir = 'Datas'

# Assurez-vous que le répertoire de destination existe
os.makedirs(extract_dir, exist_ok=True)

# Extraire les données ZIP
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

### Phase 2 : Transformation des données

#############################
#Consolidations des clients sur une seul liste
#Les clients en json
import json

#Création de la liste pour stocker les clients

clients = []

# Liste des noms de fichiers JSON
json_files = ['Datas/data/final/clients/clients001.json', 'Datas/data/final/clients/clients004.json', 'Datas/data/final/clients/clients005.json']

# Charger les données depuis les fichiers JSON
for json_file in json_files:
    with open(json_file, 'r') as f:
        data = json.load(f)
        clients.extend(data)

#Les clients en csv

import csv

#Charger les données depuis les fichiers CSV
for csv_file in ['Datas/data/final/clients/clients002.csv', 'Datas/data/final/clients/clients003.csv', 'Datas/data/final/clients/clients006.csv']:
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            clients.append(row)


#Charger les données depuis les fichiers xlsx

import pandas as pd

# Charger les données depuis le fichier XLSX
xlsx_file = 'Datas/data/final/clients/clients.xlsx'
df = pd.read_excel(xlsx_file)

# Ajouter les données du DataFrame à la liste de clients
clients.extend(df.to_dict(orient='records'))

#Afficher les clients
#print(clients)

#Faire un tableau avec les clients

df_clients = pd.DataFrame(clients)
pd.set_option('display.max_rows', None)  # Afficher toutes les lignes
pd.set_option('display.max_columns', None)  # Afficher toutes les colonnes
pd.set_option('display.width', None)  # Ajuster la largeur de l'affichage

# Définir l'index du DataFrame en commençant par 1
df_clients.index = range(1, len(df_clients) + 1)


# Supprimer les doublons du DataFrame en se basant sur les colonnes "nom", "prenom" et "adresse"
df_clients_sans_doublons = df_clients.drop_duplicates(subset=['nom', 'prenom', 'adresse'])

# Rétablir l'index du DataFrame pour commencer à 1
df_clients_sans_doublons.index = range(1, len(df_clients_sans_doublons) + 1)

# Afficher le DataFrame sans doublons
print(df_clients_sans_doublons)

################
#Faire une liste avec les informations des conseillers

# Charger le fichier JSON contenant les portfolios des clients
with open('Datas/data/final/portfolios/portfoliosv2.json', 'r') as f:
    portfolios = json.load(f)

# Créer une liste pour stocker les données des clients
client_data = []

# Parcourir les portfolios des clients
for portfolio in portfolios:
    client_id = portfolio['client']
    adviser_id = portfolio['conseiller']

    # Parcourir les produits du portfolio
    for produit in portfolio['produits']:
        product_name = produit['nom']

        # Parcourir le contenu de chaque produit
        for contenu in produit['contenu']:
            titre = contenu['titres']
            nb_titres = contenu['nb_titres']

            # Ajouter les données du client dans la liste
            client_data.append([client_id, adviser_id, product_name, titre, nb_titres])

# Créer un DataFrame à partir des données des clients
df_client_portfolio = pd.DataFrame(client_data,
                                   columns=['Client ID', 'Adviser ID', 'Product Name', 'Title', 'Number of Shares'])

# Supprimer les doublons basés sur les cinq colonnes spécifiées
df_client_portfolio_unique = df_client_portfolio.drop_duplicates(subset=['Client ID', 'Product Name', 'Title', 'Number of Shares'], keep='first')

# Remettre en ordre le DataFrame
df_client_portfolio_unique = df_client_portfolio_unique.sort_values(by=['Client ID', 'Product Name', 'Title', 'Number of Shares']).reset_index(drop=True)

# Réindexer le DataFrame pour faire commencer la liste à 1
df_client_portfolio_unique.index = range(1, len(df_client_portfolio_unique) + 1)

# Afficher toutes les lignes du DataFrame
pd.set_option('display.max_rows', None)
#print(df_client_portfolio_unique)

###################
#Faire une liste des différents produits

# Charger le fichier JSON contenant les différents produits
with open('Datas/data/final/produits/produits.json', 'r') as f:
    data = json.load(f)

# Créer une liste pour stocker les données des produits
products_data = []

# Parcourir les produits dans le fichier JSON
for product in data:
    product_name = product['produit']

    # Parcourir le contenu de chaque produit
    for category, details in product['content'].items():
        category_weight = details['weight']  # Poids total de la catégorie

        # Parcourir les stocks de chaque catégorie
        for stock in details['stocks']:
            symbol = stock[0]
            weight_per_stock = stock[1]
            real_weight_per_stock = (weight_per_stock / 100) * category_weight  # Calcul du poids réel du titre

            # Ajouter les données du produit à la liste
            products_data.append([product_name, category, symbol, weight_per_stock, category_weight, real_weight_per_stock])

# Créer un DataFrame à partir des données des produits
df_products = pd.DataFrame(products_data, columns=['Produit', 'Catégorie', 'Symbole', 'Poids par titre', 'Poids total catégorie', 'Poids réel titre'])

# Supprimer les doublons
df_products = df_products.drop_duplicates()

# Définir l'index commençant à 1
df_products.index = df_products.index + 1

# Afficher le DataFrame
#print(df_products)

#########################
#Faire une liste avec les différents titres

# Charger le fichier CSV
# Charger le fichier CSV
df_titres = pd.read_csv('Datas/data/final/titres/titres_tsx_sp.csv', sep='\t')

# Enlever les doublons
df_unique = df_titres.drop_duplicates(subset='symbol').reset_index(drop=True)

# Réindexer à partir de 1
df_unique.index += 1

# Afficher les informations des titres uniques
#print(df_unique)

#################################################################
#### Phase 3 : Produire des graphiques d'analyse des données

#Un histogramme du nombre de clients par conseiller financier pour balancer la charge de travail
# Parcourir les portfolios des clients
import matplotlib.pyplot as plt
import warnings
import dateutil.parser

# Ignorer les avertissements UnknownTimezoneWarning
warnings.filterwarnings("ignore", category=dateutil.parser.UnknownTimezoneWarning)

# Compter le nombre de clients uniques par conseiller
clients_par_conseiller = df_client_portfolio_unique.groupby('Adviser ID')['Client ID'].nunique()

# Créer un histogramme
plt.bar(clients_par_conseiller.index, clients_par_conseiller.values)

# Ajouter des étiquettes et un titre
plt.xlabel('Conseiller financier')
plt.ylabel('Nombre de clients uniques')
plt.title('Nombre de clients uniques par conseiller financier')

# Afficher l'histogramme
plt.show()


# Un histogramme de la valeur totale du portefeuille d'investissement par conseiller financier en date d'aujourd'hui
# pour évaluer la performance des conseillers financiers.
#On doit faire un api avec les lien yahoo
# Importer la bibliothèque Pandas si ce n'est pas déjà fait
import yfinance as yf
from datetime import datetime
stock_data_today_dict = {}

for symbol in df_unique['symbol']:
    ticker_symbol = symbol.split("=")[-1]
    today = datetime.today().strftime('%Y-%m-%d')
    stock_data_today = yf.download(ticker_symbol, start='2024-04-06', end='2024-04-06', interval="1d", group_by="ticker")['Close']
    stock_data_today_string = stock_data_today.to_string(index=False)
    stock_data_today_dict[ticker_symbol] = stock_data_today_string.split()[1]

montant_portefeuille_conseiller = { '1A2B': 0 , 'F0E1': 0, '3C4D': 0 }

for index, row in df_client_portfolio_unique.iterrows():
    #montant_portefeuille_conseiller['Adviser ID'] = stock_data_today_dict[row['Title']] * row['Number of Shares']
    #print(stock_data_today_dict[row['Title']])
    #print(row['Number of Shares'])

    if stock_data_today_dict[row['Title']] != ")":
        #print(row['Adviser ID'], " : Title value (", stock_data_today_dict[row['Title']], ") * Number of Shares (",
              #row['Number of Shares'], ")")
        montant_portefeuille_conseiller[row['Adviser ID']] += float(stock_data_today_dict[row['Title']]) * row['Number of Shares']
    #else:
        #print("Error!")

#print(montant_portefeuille_conseiller)

plt.bar(montant_portefeuille_conseiller.keys(), montant_portefeuille_conseiller.values())

plt.xlabel('Conseiller')
plt.ylabel('Montant portefeuille')
plt.title('Histogramme')

plt.show()

#Un histogramme comparatif de la valeur totale du portefeuille d'investissement détenu par une femme ou un homme pour
#chaque conseiller financier en date d'aujourd'hui pour contrôler les biais de genre.
#ICI NOUS LE FESONS AVEC UNIQUEMENT LES CLIENTS QU'ON A SUPER IMPORTANT DE LE DIRE DANS LE RAPPORT (ON A PAS LE SEXE DE TOUS LES CLIENTS POUR FAIRE ÇA)
#ON A PAS NON PLUS LES TITRES PAR CLIENTS
montant_portefeuille_conseiller_sexe = { '1A2B_Homme': 0,  '1A2B_Femme': 0,  '1A2B_NaN': 0, 'F0E1_Homme': 0, 'F0E1_Femme': 0, 'F0E1_NaN': 0, '3C4D_Homme': 0, '3C4D_Femme': 0, '3C4D_NaN': 0 }

for index, row in df_client_portfolio_unique.iterrows():
    if stock_data_today_dict[row['Title']] != ")":
        for index_sexe, row_sexe in df_clients_sans_doublons.iterrows():
            if row_sexe['id'] == row['Client ID']:
                #print('ID : ', row_sexe['id'], " : ", row_sexe['gendre'])

                if row_sexe['gendre'] == "Man":
                    montant_portefeuille_conseiller_sexe[row['Adviser ID'] + '_Homme'] += float(stock_data_today_dict[row['Title']]) * row['Number of Shares']
                elif row_sexe['gendre'] == "Woman":
                    montant_portefeuille_conseiller_sexe[row['Adviser ID'] + '_Femme'] += float(stock_data_today_dict[row['Title']]) * row['Number of Shares']
                else:
                    montant_portefeuille_conseiller_sexe[row['Adviser ID'] + '_NaN'] += float(stock_data_today_dict[row['Title']]) * row['Number of Shares']

#print(montant_portefeuille_conseiller_sexe)


import numpy as np

montant_Homme = np.array([montant_portefeuille_conseiller_sexe['1A2B_Homme'], montant_portefeuille_conseiller_sexe['F0E1_Homme'], montant_portefeuille_conseiller_sexe['3C4D_Homme']])
montant_Femme = np.array([montant_portefeuille_conseiller_sexe['1A2B_Femme'], montant_portefeuille_conseiller_sexe['F0E1_Femme'], montant_portefeuille_conseiller_sexe['3C4D_Femme']])
montant_NaN = np.array([montant_portefeuille_conseiller_sexe['1A2B_NaN'], montant_portefeuille_conseiller_sexe['F0E1_NaN'], montant_portefeuille_conseiller_sexe['3C4D_NaN']])

index = np.arange(3)
width = 0.5

p1 = plt.bar(index, montant_Homme, width, color='#d62728', )
p2 = plt.bar(index, montant_Femme, width, bottom=montant_Homme)
p3 = plt.bar(index, montant_NaN, width, bottom=montant_Homme+montant_Femme)

plt.ylabel('Montant')
plt.title('Montant portefeuille par conseiller par sexe')
plt.xticks(index, ('1A2B', 'F0E1', '3C4D'))
plt.legend((p1[0], p2[0], p3[0]), ('Homme', 'Femme', "NaN"))

plt.show()


#Un histogramme de l'âge des clients pour évaluer la distribution des clients par âge et ajuster les stratégies de marketing.
# Créer des intervalles pour les tranches d'âge
bins = [18, 30, 40, 50, 60, 70, 80, 90, 100]

# Regrouper les âges des clients en fonction de ces intervalles
age_groups = pd.cut(df_clients_sans_doublons['age'], bins=bins, right=False)

# Compter le nombre de clients dans chaque tranche d'âge, en incluant les NaN
age_counts = age_groups.value_counts(dropna=False)

# Créer un histogramme
plt.figure(figsize=(10, 6))
age_counts.plot(kind='bar', color='skyblue')
plt.title("Répartition des clients par âge")
plt.xlabel("Tranche d'âge")
plt.ylabel("Nombre de clients")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#Un histogramme du revenu annuel des clients pour évaluer le potentiel de revenu des clients et ajuster les stratégies
# de marketing.

# Convertir la colonne 'revenu_annuel' en type numérique
df_clients_sans_doublons.loc[:, 'revenu_annuel'] = pd.to_numeric(df_clients_sans_doublons['revenu_annuel'], errors='coerce')

# Définir les intervalles pour l'histogramme
bins = list(range(0, 400001, 30000))

# Créer un histogramme
plt.hist(df_clients_sans_doublons['revenu_annuel'], bins=bins)

# Ajouter des étiquettes et un titre
plt.xlabel('Revenu Annuel')
plt.ylabel('Nombre de Clients')
plt.title('Répartition des Clients par Revenu Annuel')

# Afficher l'histogramme
plt.show()


#Un graphique à points de la valeur actuelle du portefeuille par rapport au revenu des clients pour identifier les clients
# à fort potentiel de développement et ajuster les stratégies de marketing.
montant_portefeuille_client = {}

for index, row in df_client_portfolio_unique.iterrows():
    if stock_data_today_dict[row['Title']] != ")":
        if row['Client ID'] in montant_portefeuille_client:
            montant_portefeuille_client[row['Client ID']] += float(stock_data_today_dict[row['Title']]) * row['Number of Shares']
        else:
            montant_portefeuille_client[row['Client ID']] = float(stock_data_today_dict[row['Title']]) * row['Number of Shares']

revenu_annuel_client = {}

for index_client, row_client in df_clients_sans_doublons.iterrows():
    revenu_annuel_client[row_client['id']] = row_client['revenu_annuel']

montant_portefeuille_client_converted = {int(key): value for key, value in montant_portefeuille_client.items()}
revenu_annuel_client_converted = {int(key): value for key, value in revenu_annuel_client.items()}

montant_portefeuille_client_sorted = dict(sorted(montant_portefeuille_client_converted.items(), key=lambda item: item[0]))
revenu_annuel_client_sorted = dict(sorted(revenu_annuel_client_converted.items(), key=lambda item: item[0]))

print(montant_portefeuille_client_sorted)
print(revenu_annuel_client_sorted)

plt.figure(figsize=(10, 6))
plt.plot(range(0, len(montant_portefeuille_client_sorted)), list(montant_portefeuille_client_sorted.values()), marker='o', linestyle='-', color='blue')
plt.plot(range(0, len(revenu_annuel_client_sorted)), list(revenu_annuel_client_sorted.values()), marker='o', linestyle='-', color='red')

plt.xticks(range(0, len(revenu_annuel_client_sorted)), list(montant_portefeuille_client_sorted.keys()))
plt.tight_layout()

plt.show()




#Un graphique à pointes de la valeur totale des titres sous gestion par industrie en date d'aujourd'hui en vue de produire
# des rapports de performance de l'invesstissement et proposer des ajustements de portefeuille.


#Un graphique à barres de la valeur totale du portefeuille d'investissement par profession en date d'aujourd'hui pour mieux
# comprendre les besoins des clients et ajuster les stratégies de placement.



#Un graphique à pointes du nombre de clients par produit financiers pour évaluer la popularité des produits financiers et
# ajuster les stratégies de marketing.

# Compter le nombre de clients uniques par produit
clients_par_produit = df_client_portfolio_unique.groupby('Product Name')['Client ID'].nunique()

# Convertir le résultat en DataFrame pour faciliter la manipulation
df_clients_par_produit = clients_par_produit.reset_index(name='Nombre de Clients')

# Trier les produits par nombre de clients décroissant
df_clients_par_produit = df_clients_par_produit.sort_values(by='Nombre de Clients', ascending=False)

# Créer un graphique à points
plt.figure(figsize=(10, 6))
plt.plot(df_clients_par_produit['Product Name'], df_clients_par_produit['Nombre de Clients'], marker='o', linestyle='-')

# Ajouter des étiquettes et un titre
plt.xlabel('Nom du Produit')
plt.ylabel('Nombre de Clients Uniques')
plt.title('Nombre de Clients Uniques par Produit')

# Faire pivoter les étiquettes de l'axe des x pour éviter le chevauchement
plt.xticks(rotation=90)

# Afficher le graphique
plt.tight_layout()
plt.show()


#Un graphique à pointe montrant les pourcentages de la valeur totale sous gestion par industrie pour évaluer la performance
# des produits financiers et ajuster les stratégies de placement.



#Un histogramme des 10 titres les plus populaires selon leur présence dans les produits financiers pour évaluer la
# popularité des titres et ajuster les stratégies de placement.


