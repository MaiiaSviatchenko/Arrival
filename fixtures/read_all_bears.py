import requests
import json
import pytest

#function returns request
def pretty_print_request(request):
    print( '\n{}\n{}\n\n{}\n\n{}\n'.format(
        '<-----------Request----------->',
        request.method + ' ' + request.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in request.headers.items()),
        request.body)
    )
#function returns response
def pretty_print_response(response):
    print('\n{}\n{}\n\n{}\n\n{}\n'.format(
        '<-----------Response-----------',
        'Status code:' + str(response.status_code),
        '\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items()),
        response.text)
    )
#Read all bears
@pytest.fixture
def read_all_bears(url):
    #request_headers
    header = {'Content-Type':'application/json'}
    # convert dict to json and send request
    response = requests.get(url, headers = header)
    #print request
    pretty_print_request(response.request)
    #print response
    pretty_print_response(response)
    return response
