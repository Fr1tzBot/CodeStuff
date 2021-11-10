from sys import argv
import requests

def downloadUrl(url: str) -> bytes:
    """Get the raw bytes of a url"""
    print("Sent get request for " + url)
    return requests.get(url).content

number = argv[-1]
contents = downloadUrl("https://xkcd.com/" + number)

