Projet de Prédiction du Risque de Crédit
1. Introduction
Ce projet vise à analyser et à modéliser le risque de crédit en utilisant des techniques d'apprentissage automatique. L'analyse comprend plusieurs étapes clés, notamment le prétraitement des données, l'analyse exploratoire des données (EDA) et la construction de modèles, afin de prédire la probabilité de défaut de paiement sur un prêt.

2. Description des Données
Le jeu de données utilisé dans ce projet contient des informations sur le risque de crédit. Chaque entrée représente un demandeur de prêt et comprend divers attributs liés à son historique financier et aux détails du prêt. Les attributs clés comprennent :

person_age : Âge du demandeur
person_income : Revenu annuel du demandeur
person_home_ownership : Statut de propriété du logement (par exemple, LOYER, PROPRIÉTAIRE, HYPOTHÈQUE)
person_emp_length : Durée d'emploi en années
loan_amnt : Montant du prêt
loan_int_rate : Taux d'intérêt du prêt
loan_percent_income : Montant du prêt en pourcentage du revenu
loan_status : Statut du prêt (variable cible, indiquant le défaut (1) ou le non-défaut (0))
loan_intent : Objectif du prêt (par exemple, PERSONNEL, ÉDUCATION, MÉDICAL)
loan_grade : Catégorie du prêt (par exemple, A, B, C)
cb_person_default_on_file : Information de défaut au bureau de crédit (O/N)
cb_person_cred_hist_length : Durée de l'historique de crédit
Le jeu de données est composé de 32 581 lignes et 12 colonnes.    

3. Prétraitement des Données
Les étapes de prétraitement des données ont été cruciales pour préparer le jeu de données à l'analyse et à la modélisation. Les étapes suivantes ont été effectuées :

Gestion des Valeurs Manquantes : Les valeurs manquantes dans les colonnes person_emp_length et loan_int_rate ont été imputées à l'aide de la médiane. Les valeurs manquantes dans les colonnes catégorielles ont été remplacées par 'Missing'.    
Encodage des Variables Catégorielles : Les variables catégorielles ont été converties en format numérique à l'aide de l'encodage one-hot.    
Mise à l'échelle des Caractéristiques Numériques : Les caractéristiques numériques ont été standardisées à l'aide de StandardScaler pour garantir que toutes les caractéristiques contribuent de manière égale à l'entraînement du modèle.    
Suppression des Duplicats : 165 lignes dupliquées ont été supprimées du jeu de données.    
4. Analyse Exploratoire des Données (EDA)
La phase d'Analyse Exploratoire des Données (EDA) visait à comprendre les caractéristiques des données et à identifier les modèles potentiels. Les étapes clés de l'EDA comprenaient :

Analyse de la Distribution : Des histogrammes et des tracés de densité de noyau ont été utilisés pour visualiser la distribution des variables numériques.    
Analyse de la Corrélation : Une matrice de corrélation a été générée pour explorer les relations entre les variables numériques et la variable cible (loan_status).    
Détection des Valeurs Aberrantes : Des boîtes à moustaches ont été utilisées pour identifier les valeurs aberrantes potentielles dans les variables numériques.    
L'EDA a révélé que des variables telles que person_age, person_income, loan_amnt, loan_int_rate et person_emp_length sont des facteurs importants dans la prédiction du risque de crédit.    

5. Développement du Modèle
Plusieurs modèles d'apprentissage automatique ont été développés et évalués pour prédire le risque de crédit. Les principaux modèles comprenaient :

Régression Logistique : Un modèle de régression logistique a été entraîné pour prédire la probabilité de défaut de paiement sur un prêt.    
Arbre de Décision Classificateur : Un arbre de décision classificateur a été entraîné pour prédire le statut du prêt.    
Le jeu de données a été divisé en ensembles d'entraînement et de test pour évaluer les performances des modèles.    

6. Résultats
Les modèles ont été évalués à l'aide de diverses métriques, notamment la précision, le rappel, le score F1 et l'AUC-ROC. Les résultats ont mis en évidence les points suivants :

Régression Logistique : A atteint une précision de 0,8627, un rappel de 0,5467, un score F1 de 0,6384 et une AUC-ROC de 0,8684.    
Arbre de Décision Classificateur : A atteint une précision de 0,8888, un rappel de 0,7675, un score F1 de 0,7537 et une AUC-ROC de 0,8454.    
L'Arbre de Décision Classificateur a surpassé le modèle de Régression Logistique, en particulier en termes de rappel, ce qui est essentiel pour minimiser les faux négatifs dans l'évaluation du risque de crédit.    

7. Conclusion
L'Arbre de Décision Classificateur a été sélectionné comme modèle préféré pour la prédiction du risque de crédit en raison de ses performances supérieures en matière de rappel. Le modèle identifie efficacement les emprunteurs à haut risque, ce qui est essentiel pour la gestion du risque de crédit.    

Une analyse plus approfondie, telle que le classement de l'importance des caractéristiques, pourrait fournir des informations supplémentaires sur les facteurs qui influencent le plus significativement le défaut de paiement sur un prêt.    

8. Déploiement
Le modèle d'Arbre de Décision entraîné a été sauvegardé et est prêt pour le déploiement.    

Le modèle est accessible via une application Streamlit : https://riskcredit-bgqhwpvq2f3mw93pcnbzum.streamlit.app/    

Sources et contenu associé
