# import libraries
import random
import re

import pandas as pd
# wikipedia libary
import wikipedia
from googlesearch import search

# requirements -> for googlesearch: python -m pip install google

df = pd.read_csv('C:/Users/I538992/Desktop/AML Projekt/birds.csv')
bird_names = df.labels.unique()
bird_name = random.choice(bird_names)  # get a random bird name
bird_name = bird_name.lower()  # make bird name lowercase
print(bird_name)

wikipedia.set_lang("en")  # set language of wikipedia article

# check if google library is installed
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")


def google_search(bird):
    query = f"'{bird}' site:wikipedia.org"
    for j in search(query, num=1, stop=1, pause=1):
        bird_wiki_page = j

    spl_word = "/wiki/"

    # Get String after first occurrence of substring
    match = re.search(spl_word, bird_wiki_page)
    if match:
        result_bird_wiki = bird_wiki_page[match.end():]
    else:
        result_bird_wiki = ''

    if result_bird_wiki == '':
        result_bird_wiki = bird
    print(bird_wiki_page)
    return result_bird_wiki


def bird_summary(bird):
    bird_wikipedia_page = google_search(bird)
    #
    try:
        bird_summary = wikipedia.summary(bird_wikipedia_page,
                                         auto_suggest=False)
    except wikipedia.WikipediaException as bird_summary:
        print(bird_summary)
    return bird_summary


bird__summary = bird_summary(bird_name)
print(bird__summary)


def bird_wikipedia_page(bird):
    bird_wikipedia_page_google = google_search(bird)
    try:
        bird_wikipedia_page = wikipedia.page(bird_wikipedia_page_google,
                                             auto_suggest=False)
        bird_page_content = bird_wikipedia_page.content
    except wikipedia.WikipediaException as bird_page_content:
        print(bird_page_content)
    return bird_page_content


bird_page = bird_wikipedia_page(bird_name)
bird_page
