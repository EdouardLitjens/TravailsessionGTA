## *Contexte*
L'entreprise XYZ est une société de services financiers cherchant à améliorer ses stratégies de gestion de portefeuille et à optimiser le suivi de la performance de ses conseillers financiers. Dans le cadre du cours GTA431, nous devons effectuer ce travail qui consiste à extraire, transformer et exploiter les données financières. Pour ce faire, nous utiliserons le langage de code Python.

## *Objectifs*

### Extraction des données*
Les données proviennent de différents systèmes et présentent différents formats. L'équipe de projet doit accéder à l'échantillon de données des différents fichiers à leur disposition. Ces données sont représentatives des données réelles de l'entreprise dans leurs différents systèmes. On compte dans les données fournies les fichiers de certains clients, les fichiers de certains conseillers financiers, les fichiers des produits d'investissement, les fichiers de titres financiers et les portefeuilles d'investissement. Dans un premier temps, l'extraction des données peut être faite sur les fichiers spécifiquement à votre disposition. Si le temps le permet, la version finale du projet devrait permettre l'extraction des données pour un nombre indéterminé de fichiers xlsx, csv et json ayant des structures compatibles à ceux ayant été fournis. L'accès aux données doit être faite en respectant les règles de confidentialité et de sécurité du Groupe 431.

### Transformation des données*
Les données extraites doivent être transformées en un format standardisé pour l'analyse. Les données doivent être évaluées pour leur qualité, nettoyées, normalisées et intégrées dans un format standard. Portez une attention particulière aux doublons. Les transformations appliquées doivent être documentées et justifiées. Les erreurs identifiées doivent être rapportées comme recommandations dans le rapport final, mais vous n'avez pas à inférer de valeur à des erreurs dasn les données. Les données doivent être structurées pour permettre l'analyse de la performance des conseillers financiers, des clients et des produits financiers.

### Produire des graphiques d'analyse des données*
En utilisant les données transformées, l'équipe de projet du Groupe 431 doit produire des graphiques permettant de démontrer la capacité d'analyse de la performance des conseillers financiers, des portefeuilles des clients et des produits financiers. Les graphiques doivent être produits en utilisant la bibliothèque matplotlib et leur finalité documentée. Différentes graphiques doivent être produits sur les conseillers financiers, les portefeuilles d'investissement des clients et les produits financiers.

Au minimum, les graphiques suivants doivent être produits sur les conseillers financiers :
- Un histogramme du nombre de clients par conseiller financier pour balancer la charge de travail.
- Un histogramme de la valeur totale du portefeuille d'investissement par conseiller financier en date d'aujourd'hui pour évaluer la performance des conseillers financiers.
- Un histogramme comparatif de la valeur totale du portefeuille d'investissement détenu par une femme ou un homme pour chaque conseiller financier en date d'aujourd'hui pour contrôler les biais de genre.

Au minimum, les graphiques suivants doivent être produits sur les clients et leurs portefeuilles d'investissement :
- Un histogramme de l'âge des clients pour évaluer la distribution des clients par âge et ajuster les stratégies de marketing.
- Un histogramme du revenu annuel des clients pour évaluer le potentiel de revenu des clients et ajuster les stratégies de marketing.
- Un graphique à points de la valeur actuelle du portefeuille par rapport au revenu des clients pour identifier les clients à fort potentiel de développement et ajuster les stratégies de marketing.
- Un graphique à pointes de la valeur totale des titres sous gestion par industrie en date d'aujourd'hui en vue de produire des rapports de performance de l'invesstissement et proposer des ajustements de portefeuille.
- Un graphique à barres de la valeur totale du portefeuille d'investissement par profession en date d'aujourd'hui pour mieux comprendre les besoins des clients et ajuster les stratégies de placement.

Au minimum, les graphiques suivants doivent être produits pour les produits financiers :
- Un graphique à pointes du nombre de clients par produit financiers pour évaluer la popularité des produits financiers et ajuster les stratégies de marketing.
- Un graphique à pointe montrant les pourcentages de la valeur totale sous gestion par industrie pour évaluer la performance des produits financiers et ajuster les stratégies de placement.
- Un histogramme des 10 titres les plus populaires selon leur présence dans les produits financiers pour évaluer la popularité des titres et ajuster les stratégies de placement.
- Défi : Un graphique à ligne sur la valeur des trois titres les plus populaires (voir question précédente) pour chaque mois depuis les 12 derniers mois pour évaluer la performance d'un titre et ajuster les stratégies de placement. (Veuillez synthétiser bien sûr)




## *Démarche/Manipulations* (Justifications des transformations appliquées)

### Phase 1 : Extraction des données
import zipfile
import os

#### Chemin vers votre fichier ZIP
zip_file_path = 'gta431_projet.zip'

#### Répertoire où extraire les données ZIP
extract_dir = 'Datas'

#### Assurez-vous que le répertoire de destination existe
os.makedirs(extract_dir, exist_ok=True)

#### Extraire les données ZIP
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

### Phase 2 : Transformation des données

#### Consolidations des clients sur une seul liste
import json
import csv
import pandas as pd

clients = []

#### Liste des noms de fichiers JSON
json_files = ['Datas/data/final/clients/clients001.json', 'Datas/data/final/clients/clients004.json', 'Datas/data/final/clients/clients005.json']

#### Charger les données depuis les fichiers JSON
for json_file in json_files:
    with open(json_file, 'r') as f:
        data = json.load(f)
        clients.extend(data)

#### Charger les données depuis les fichiers CSV
for csv_file in ['Datas/data/final/clients/clients002.csv', 'Datas/data/final/clients/clients003.csv', 'Datas/data/final/clients/clients006.csv']:
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            clients.append(row)

#### Charger les données depuis le fichier XLSX
xlsx_file = 'Datas/data/final/clients/clients.xlsx'
df = pd.read_excel(xlsx_file)
clients.extend(df.to_dict(orient='records'))

#### Afficher les clients
print(clients)

### Phase 3 : Produire des graphiques d'analyse des données

#### Faire un tableau avec les clients
df_clients = pd.DataFrame(clients)
pd.set_option('display.max_rows', None)  # Afficher toutes les lignes
pd.set_option('display.max_columns', None)  # Afficher toutes les colonnes
pd.set_option('display.width', None)  # Ajuster la largeur de l'affichage

#### Définir l'index du DataFrame en commençant par 1
df_clients.index = range(1, len(df_clients) + 1)

##### Supprimer les doublons du DataFrame en se basant sur les colonnes "nom", "prenom" et "adresse"
df_clients_sans_doublons = df_clients.drop_duplicates(subset=['nom', 'prenom', 'adresse'])

#### Rétablir l'index du DataFrame pour commencer à 1
df_clients_sans_doublons.index = range(1, len(df_clients_sans_doublons) + 1)

#### Afficher le DataFrame sans doublons
print(df_clients_sans_doublons)

#### Faire une liste avec les informations des conseillers
with open('Datas/data/final/portfolios/portfoliosv2.json', 'r') as f:
    portfolios = json.load(f)

client_data = []

#### Parcourir les portfolios des clients
for portfolio in portfolios:
    client_id = portfolio['client']
    adviser_id = portfolio['conseiller']

    for produit in portfolio['produits']:
        product_name = produit['nom']

        for contenu in produit['contenu']:
            titre = contenu['titres']
            nb_titres = contenu['nb_titres']

            client_data.append([client_id, adviser_id, product_name, titre, nb_titres])

df_client_portfolio = pd.DataFrame(client_data, columns=['Client ID', 'Adviser ID', 'Product Name', 'Title', 'Number of Shares'])

df_client_portfolio_unique = df_client_portfolio.drop_duplicates(subset=['Client ID', 'Product Name', 'Title', 'Number of Shares'], keep='first')

df_client_portfolio_unique = df_client_portfolio_unique.sort_values(by=['Client ID', 'Product Name', 'Title', 'Number of Shares']).reset_index(drop=True)

df_client_portfolio_unique.index = range(1, len(df_client_portfolio_unique) + 1)

#### Histogramme du nombre de clients par conseiller financier
import matplotlib.pyplot as plt
import warnings
import dateutil.parser

warnings.filterwarnings("ignore", category=dateutil.parser.UnknownTimezoneWarning)

clients_par_conseiller = df_client_portfolio_unique.groupby('Adviser ID')['Client ID'].nunique()

plt.bar(clients_par_conseiller.index, clients_par_conseiller.values)
plt.xlabel('Conseiller financier')
plt.ylabel('Nombre de clients uniques')
plt.title('Nombre de clients uniques par conseiller financier')
plt.show()

#### Histogramme de la valeur totale du portefeuille d'investissement par conseiller financier

import yfinance as yf
from datetime import datetime

stock_data_today_dict = {}

for symbol in df_unique['symbol']:
    ticker_symbol = symbol.split("=")[-1]
    today = datetime.today().strftime('%Y-%m-%d')
    stock_data_today = yf.download(ticker_symbol, start=today, interval="1d", group_by="ticker")['Close']
    stock_data_today_string = stock_data_today.to_string(index=False)
    stock_data_today_dict[ticker_symbol] = stock_data_today_string.split()[1]

montant_portefeuille_conseiller = { '1A2B': 0 , 'F0E1': 0, '3C4D': 0 }

for index, row in df_client_portfolio_unique.iterrows():
    if stock_data_today_dict[row['Title']] != ")":
        montant_portefeuille_conseiller[row['Adviser ID']] += float(stock_data_today_dict[row['Title']]) * row['Number of Shares']

plt.bar(montant_portefeuille_conseiller.keys(), montant_portefeuille_conseiller.values())
plt.xlabel('Conseiller')
plt.ylabel('Montant portefeuille')
plt.title('Histogramme')
plt.show()

#### Histogramme comparatif de la valeur totale du portefeuille d'investissement détenu par une femme ou un homme pour chaque conseiller financier
montant_portefeuille_conseiller_sexe = { '1A2B_Homme': 0,  '1A2B_Femme': 0,  '



## Résultats 






## Analyse des résultats (Justifications des graphiques produits)


## Recommandations (Recommandations pour l'entreprise)
- Standardisation des formats de données : Définissez des normes claires pour la collecte et le stockage des données afin de garantir leur cohérence et leur compatibilité avec les outils d'analyse. Cela pourrait inclure des formats de fichier standard, des conventions de nommage cohérentes et des structures de données uniformes.
- Validation des données : Mettez en place des processus de validation des données pour détecter et corriger les erreurs, les incohérences et les valeurs aberrantes dès leur saisie. Cela garantira la qualité des données utilisées dans vos analyses et prises de décision. Mettre surtout l'emphase sur les informations manquantes.
- Utilisation de solutions technologiques : Explorez l'utilisation de technologies telles que l'intelligence artificielle, l'apprentissage automatique et l'automatisation des processus pour améliorer la collecte, le traitement et l'analyse des données. Ces solutions peuvent aider à accélérer les processus, à réduire les erreurs humaines et à fournir des informations plus précises et exploitables.
- Formation et sensibilisation du personnel : Sensibilisez votre personnel à l'importance des données de haute qualité et fournissez-leur la formation nécessaire pour collecter, stocker et manipuler efficacement les données. Cela garantira une meilleure utilisation des données dans l'ensemble de l'entreprise et réduira les erreurs liées à la manipulation des données.



## Conclusion