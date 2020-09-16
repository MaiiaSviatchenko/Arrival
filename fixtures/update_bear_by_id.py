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
#Update bear by id and check it
@pytest.fixture
def update_bear_by_id(url,body,add_bear):
    #define bear_id
    new_bear = add_bear
    id = new_bear.text
    #request_headers
    header = {'Content-Type':'application/json'}
    body = {"bear_id":0,"bear_type":"BROWN","bear_name":"UPDATED","bear_age":99.5}
    # convert dict to json and send request
    response = requests.put(url+'/'+id, headers = header, data=json.dumps(body,indent=4))
    response = requests.get(url+'/'+id, headers = header)
    #print request
    pretty_print_request(response.request)
    #print response
    pretty_print_response(response)
    return response
