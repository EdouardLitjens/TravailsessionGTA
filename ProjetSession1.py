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
#print(df_clients_sans_doublons)

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
print(df_unique)

#################################################################
#### Phase 3 : Produire des graphiques d'analyse des données