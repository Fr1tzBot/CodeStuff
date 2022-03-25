#!/usr/bin/env python3
"""unblock.py: a script to find alt links for blocked sites"""

from ssl import SSLCertVerificationError
from sys import argv as urls
from requests.exceptions import SSLError, ConnectionError
from requests import head
import prettytable
from urllib3.exceptions import MaxRetryError, ProtocolError

#user agent spoofing string
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36"

#http headers to use
headers = {"User-Agent": USER_AGENT}

urls = urls[1:]

proxyUrls = [
    {"checkUrl": "https://womginx.binaryperson.repl.co", "downloadUrl": "https://womginx.binaryperson.repl.co/main/"}, #replit womginx
    {"checkUrl": "https://formulatemath.com",            "downloadUrl": "https://a.formulatemath.com/main/"},          #holyunblocker womginx 1
    {"checkUrl": "https://simplicitytracker.org",        "downloadUrl": "https://a.simplicitytracker.org/main/"},      #holyunblocker womginx 2
    {"checkUrl": "https://collegeprofile.biz",           "downloadUrl": "https://a.collegeprofile.biz/main/"},         #holyunblocker womginx 3
    {"checkUrl": "https://translatereader.us",           "downloadUrl": "https://a.translatereader.us/main/"}          #holyunblocker womginx 4
]

def cleanUrl(url: str) -> str:
    """remove the http and other things from a url"""
    for toStrip in ["http://", "https://", "www.", "/"]:
        url = url.lstrip(toStrip)
    return url

urlStatus = prettytable.PrettyTable(["url", "status"])
urlStatus.align["url"] = "l"
urlStatus.align["status"] = "c"

for i in proxyUrls:
    try:
        i["status"] = "✅" if head(i["checkUrl"], headers=headers).status_code < 400 else "❌"
    except SSLCertVerificationError:
        i["status"] = "❌"
    except MaxRetryError:
        i["status"] = "❌"
    except SSLError:
        i["status"] = "❌"
    except ConnectionError:
        i["status"] = "❌"
    except ProtocolError:
        i["status"] = "❌"
    except ConnectionResetError:
        i["status"] = "❌"
    urlStatus.add_row([cleanUrl(i["checkUrl"]), i["status"]])

print(urlStatus)

for j in urls:
    for i in proxyUrls:
        if i["status"] == "✅":
            print(i["downloadUrl"] + j)
