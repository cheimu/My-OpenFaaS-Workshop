import os
from urllib.parse import parse_qs

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    # Read and return a static HTML file from disk
    # path = os.environ['Http_Path']
    # pathArr = path.split("/")
    # pageName = pathArr[1]
    
    # Read the query string and return different HTML
    query = os.environ['Http_Query']
    params = parse_qs(query)
    action = params['action'][0]

    # set the path
    dirname = os.path.dirname(__file__)
    # page = os.path.join(dirname, 'html', pageName + '.html')
    page = os.path.join(dirname, 'html', action + '.html')

    with(open(page, 'r')) as file:
        html = file.read()

    return html
