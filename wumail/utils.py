from typing import List
from pickle import load

def clean_urls(urls: List[str], file_name='./cache.pkl') -> List[str]:
    """
    Finds and removes duplicate urls from a list of urls.

    Args:
        urls (List[str]): list of urls

    Returns:
        List[str]: list of unique urls

    """
    try:
        with open(file_name, 'rb') as file:
            cache = load(file)
            return list(set(urls) - set(cache))
    except FileNotFoundError:
        return urls