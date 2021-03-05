import os
import requests
import sys

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    gateway_hostname = os.getenv("gateway_hostname", "gateway") # uses a default of "gateway" for when "gateway_hostname" is not set

    test_sentence = req

    r = requests.get("http://" + "127.0.0.1" + ":8080/function/markdown", data= test_sentence)

    if r.status_code != 200:
        sys.exit("Error with markdown, expected: %d, got: %d\n" % (200, r.status_code))

    result = r.json()

    return result