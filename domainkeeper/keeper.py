import os
import socket

import requests
import logging
from urllib.parse import urlparse


DOMAINS = list(map(str.strip, os.getenv("DOMAINS", "").split(",")))


def keepalive_domain(url: str):
    parsed = urlparse(url)
    resp = requests.get(url)
    logging.warning("\nkeepalive url: %s\nips: %s\nresponse is: %s" % (url, socket.gethostbyname(parsed.netloc), resp.content))


if __name__ == '__main__':
    for domain in DOMAINS:
        if domain:
            keepalive_domain(domain)
