# api requests to access bird information / data from wikipedia
import random

import pandas as pd
# wikipedia libary
import wikipedia

# read csv to get lables for bird classification
df = pd.read_csv('C:/Users/I538992/Desktop/AML Projekt/birds.csv')
bird_names = df.labels.unique()
bird_name = random.choice(bird_names)  # get a random bird name
bird_name = bird_name.lower()  # make bird name lowercase
print(bird_name)

wikipedia.set_lang("en")  # set language of wikipedia article


def bird_information_summary(bird):
    try:
        bird_summary = wikipedia.summary(bird + ' bird')
    except:
        search_wikipedia = wikipedia.search(bird + ' bird', results=1)
        bird_search = search_wikipedia[0]
        print(bird_search)
        bird_summary = wikipedia.summary(bird_search)
    return bird_summary


result = bird_information_summary(bird_name)
print(result)


def get_bird_summary_wikipedia(bird):
    try:
        wiki_bird_summary = wikipedia.summary(bird + ' bird')
    except:
        try:
            suggestion = wikipedia.suggest(bird)
            wiki_bird_summary = wikipedia.summary(suggestion + ' bird')
        except:
            search_result = wikipedia.search(bird + ' bird', results=1)
            if search_result is not None:
                bird_search = search_result[0]
                print(bird_search)
                wiki_bird_summary = wikipedia.summary(bird_search + ' bird')
            else:
                print('No Summary found')

    return wiki_bird_summary


def get_bird_page_wikipedia(bird):
    try:
        wiki_bird_page = wikipedia.page(bird + ' bird')
        bird_content = wiki_bird_page.content
    except:
        try:
            suggestion = wikipedia.suggest(bird)
            wiki_bird_page = wikipedia.page(suggestion + ' bird')
            bird_content = wiki_bird_page.content
        except:
            search_result = wikipedia.search(bird + ' bird', results=1)
            if search_result is not None:
                bird_search = search_result[0]
                print(bird_search)
                bird_content_page = wikipedia.page(bird_search + ' bird',
                                                   auto_suggest=False)
                bird_content = bird_content_page.content
            else:
                print('nothing here')

    return bird_content


# result = get_bird_page_wikipedia(bird_name)
# print(result)

from googlesearch import Search


def google_search_wiki_content(bird_name):
    # google search for wikipedia articles
    google_bird_results = Search(bird_name + ' bird Wiki')
    results = google_bird_results.results
    first_birdpage_result_title = results[0]  # get first google result
    first_birdpage_result_title = first_birdpage_result_title.title
    print(first_birdpage_result_title)
    string = str(first_birdpage_result_title)  # .encode().decode('ASCII')
    sub_str = "- Wikipedia"

    # slicing off after length computation
    result_bird_wiki_google_search = string[:string.index(sub_str)]

    #result_bird_wiki = s[s.find(start) + len(start):s.rfind(end)]
    print(result_bird_wiki_google_search)
    # result_bird_wiki = str(result_bird_wiki).encode('utf-8')

    # print(result_bird_wiki)
    try:
        bird_content_page = wikipedia.page(result_bird_wiki_google_search,
                                           auto_suggest=False)
        bird_content = bird_content_page.content
    except:
        print('Error')
    return bird_content


# bird_information = google_search_wiki_content(bird_name)
# print(bird_information)

#
# result = bird_information_summary(result_bird_wiki)
# print(result)


def google_search_with_and_without(bird):
    try:
        wiki_bird_page = wikipedia.page(bird + ' bird')  # ,auto_suggest=False
        bird_content = wiki_bird_page.content
    except:
        python_results = Search(bird_name + ' bird Wiki')
        results = python_results.results
        first_result_title = results[0]
        first_result_title = first_result_title.title
        print(first_result_title)
        s = str(first_result_title)  # .encode().decode('ASCII')
        print(s)
        print(type(s))
        # start = '-'
        # end = ' Wikipedia'
        sub_str = "- Wikipedia"

        # slicing off after length computation
        result_bird_wiki = s[:s.index(sub_str)]
        print(result_bird_wiki)
        # result_bird_wiki = str(result_bird_wiki).encode('utf-8')

        # print(result_bird_wiki)
        bird_content_page = wikipedia.page(result_bird_wiki,
                                           auto_suggest=False)
        bird_content = bird_content_page.content
    return bird_content


bird_information = google_search_with_and_without(bird_name)
print(bird_information)