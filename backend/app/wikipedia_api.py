"""Module containing functions related to Wikipedia and information retrieval."""
import re

from urllib.error import HTTPError
import wikipedia
from googlesearch import search

wikipedia.set_lang("en")  # set language of wikipedia article


def google_search(bird: str) -> str:
    """Conduct a Google search to find a better match for Wikipedia pages.

    Args:
        bird (str): Name of the bird to look up information for.

    Returns:
        str: The bird name as used in Wikipedia, or as input if not found.
    """
    query = f"'{bird}' site:wikipedia.org"

    bird_wiki_page = None

    try:
        for j in search(query, num=1, stop=1, pause=1):
            bird_wiki_page = j
    except HTTPError:
        return bird

    if bird_wiki_page is None:
        return bird

    spl_word = "/wiki/"

    # Get String after first occurrence of substring
    match = re.search(spl_word, bird_wiki_page)
    if match:
        result_bird_wiki = bird_wiki_page[match.end():]
    else:
        result_bird_wiki = bird

    return result_bird_wiki


def get_bird_information(bird_name: str, detailed: bool = False) -> str:
    """Retrieve information about a species of bird from the English Wikipedia.

    Calls APIs of Google as well as Wikipedia.

    Args:
        bird_name (str): Name of the bird to look up information for.
        detailed (bool, optional): Whether to return the full page or just the summary. Defaults to False.

    Returns:
        str: Information about the bird.
    """

    bird_wiki_page = google_search(bird_name)

    try:
        if detailed:
            wiki_page = wikipedia.page(bird_wiki_page, auto_suggest=False)
            information = wiki_page.content
        else:
            information = wikipedia.summary(bird_wiki_page, auto_suggest=False)
    except wikipedia.WikipediaException as e:
        return (f'{str(e)} \n\nThis might be due to too many requests being sent in too little time' /
                ', so trying again later might lead to better results.')

    return information
