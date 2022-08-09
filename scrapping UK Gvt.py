import requests
url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)

# print(page.content) vérifier si c'est la bonne pas en regarddant le code source

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# récupération des noms des liens

class_name = "gem-c-document-list__item-title"
titres = soup.find_all("a", class_=class_name)
# print(titres) je vérifie que j'ai bien récupéré les liens

# récupération du titre dans une liste

titre_texte = [] # création de la liste

for titre in titres:
    titre_texte.append(titre.string)

print(titre_texte)

# récupération de la description des liens

description_bs = soup.find_all("p", class_='gem-c-document-list__item-description')

description = []

for desc in description_bs:
    description.append(desc.string)

print(description)

# création d'un fichier csv

import csv_etl
en_tete = ['titre', 'description']

import pandas as pd

# transformer mes listes en dictionnaire
dict_article = dict(zip(titre_texte, description))
print(dict_article)

# création du dataframe

data = pd.DataFrame(list(dict_article.items()), columns=["titre","description"])

data.to_csv('UK ARTICLES.xlsx')
