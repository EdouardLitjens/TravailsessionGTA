# Plan de projet (à usage interne seulement)

Le projet consiste à démontrer la possibilité d'analyser la performance de l'entreprise à partir des données provenant de différents systèmes internes afin d'offrir une vue d'ensemble sur les conseillers, les portefeuilles des clients et les produits financiers de Summit Investment. Pour ce faire, le Groupe 431 doit intégrer les données provenant de différentes sources, les transformer en un format standardisé et démontrer le potentiel d'analyse au moyen de visualisations. Le projet doit être réalisé en utilisant le langage Python natif et les bibliothèques `pandas` et `matplotlib`.

## Découpage interne du projet

Le projet est divisé en 4 étapes principales :

### Phase 1 : Extraction des données 
Les données proviennent de différents systèmes et présentent différents formats. L'équipe de projet doit accéder à l'échantillon de données des différents fichiers à leur disposition. Ces données sont représentatives des données réelles de l'entreprise dans leurs différents systèmes. On compte dans les données fournies les fichiers de certains clients, les fichiers de certains conseillers financiers, les fichiers des produits d'investissement, les fichiers de titres financiers et les portefeuilles d'investissement. Dans un premier temps, l'extraction des données peut être faite sur les fichiers spécifiquement à votre disposition. Si le temps le permet, la version finale du projet devrait permettre l'extraction des données pour un nombre indéterminé de fichiers xlsx, csv et json ayant des structures compatibles à ceux ayant été fournis. L'accès aux données doit être faite en respectant les règles de confidentialité et de sécurité du Groupe 431. 

### Phase 2 : Transformation des données
Les données extraites doivent être transformées en un format standardisé pour l'analyse. Les données doivent être évaluées pour leur qualité, nettoyées, normalisées et intégrées dans un format standard. Portez une attention particulière aux doublons. Les transformations appliquées doivent être documentées et justifiées. Les erreurs identifiées doivent être rapportées comme recommandations dans le rapport final, mais vous n'avez pas à inférer de valeur à des erreurs dasn les données. Les données doivent être structurées pour permettre l'analyse de la performance des conseillers financiers, des clients et des produits financiers. 

Il peut être nécessaire de compléter les données 

### Phase 3 : Produire des graphiques d'analyse des données
En utilisant les données transformées, l'équipe de projet du Groupe 431 doit produire des graphiques permettant de démontrer la capacité d'analyse de la performance des conseillers financiers, des portefeuilles des clients et des produits financiers. Les graphiques doivent être produits en utilisant la bibliothèque `matplotlib` et leur finalité documentée. Différentes graphiques doivent être produits sur les conseillers financiers, les portefeuilles d'investissement des clients et les produits financiers.

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
- Défi : Un graphique à ligne sur la valeur des trois titres les plus populaires (voir question précédente) pour chaque mois depuis les 12 derniers mois pour évaluer la performance d'un titre et ajuster les stratégies de placement.

### Phase 4 : Production du rapport

Un rapport doit être produit pour documenter les résultats de la manipulation des données au format `markdown`. Le rapport contient les sections élémentaires d'un rapport d'analyse de manipulation de données incluant le contexte, les objectifs, la démarche générale, la documentation des données sources, les manipulations, les résultats observables des manipulations et des visualisations, une brève discussion des résultats, les recommandations et une conclusion favorisant le réengagement du client. Plus spécifiquement, une attention particulière doit être portée sur les justifications des transformations appliquées, les justifications des graphiques produits et les recommandations pour l'entreprise. En annexe, les fichiers contenant les données finales au format json et les scripts Python utilisés pour la manipulation des données et la production des graphiques, en plus le lien vers le projet doivent être inclus. Le rapport doit être produit pour la direction de l'entreprise et leur permettre de voir le potentiel de suivi et d'analyse de la performance des conseillers financiers, des clients et des produits financiers et l'effort à déployer pour s'assurer que les données sont de bonne qualité.