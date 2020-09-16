import pytest

#TC2. Add bears with all available types(one by one)
@pytest.mark.parametrize("url,body",
[("http://0.0.0.0:8091/bear",{'bear_type':'BLACK', 'bear_name':'MIKHAIL', 'bear_age':17.5}),
("http://0.0.0.0:8091/bear",{'bear_type':'POLAR', 'bear_name':'IGOREK', 'bear_age':5}),
("http://0.0.0.0:8091/bear",{'bear_type':'BROWN', 'bear_name':'ASHOT', 'bear_age':99}),
("http://0.0.0.0:8091/bear",{'bear_type':'GUMMY', 'bear_name':'TIHON', 'bear_age':100})])
def test_add_bear(add_bear):
    response = add_bear
    assert response.status_code == 200
    assert response.text != None

#TC11.Send read all bears request
@pytest.mark.parametrize("url", [("http://0.0.0.0:8091/bear")])
def test_read_all_bears(read_all_bears):
    response = read_all_bears
    assert response.status_code == 200
    response_body = response.json()
    assert len(response_body[0]) == 4

#Send read bear by id request
@pytest.mark.parametrize("url,body", [("http://0.0.0.0:8091/bear",{'bear_type':'BLACK', 'bear_name':'GET', 'bear_age':17.5})])
def test_read_bear_by_id(read_bear_by_id):
    response = read_bear_by_id
    assert response.status_code == 200
    assert response.text != None

#TC18.Send "Udate bear" request and update all possible params and return reasult with read action
@pytest.mark.parametrize("url,body", [("http://0.0.0.0:8091/bear",{'bear_type':'BLACK', 'bear_name':'UPDATE', 'bear_age':18.5})])
def test_update_bear_by_id(update_bear_by_id):
    response = update_bear_by_id
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["bear_id"] != 0
    assert response_body["bear_type"] == "BROWN"
    assert response_body["bear_name"] == "UPDATED"
    assert response_body["bear_age"] == 99.5

#TC22.Send "delete bear by id" request and check with get that bear have been removed
@pytest.mark.parametrize("url,body", [("http://0.0.0.0:8091/bear",{'bear_type':'BLACK', 'bear_name':'UPDATE', 'bear_age':18.5})])
def test_delete_bear_by_id(delete_bear_by_id):
    response = delete_bear_by_id
    assert response.status_code == 200
    assert response.text == "EMPTY"

#TC9.Send request with '/' in th end of request
@pytest.mark.parametrize("url,body",
[("http://0.0.0.0:8091/bear/",{'bear_type':'BLACK', 'bear_name':'MIKHAIL', 'bear_age':17.5})])
def test_add_bear_wrong_url(add_bear):
    response = add_bear
    assert response.status_code == 200
    assert response.text != None

#TC3. Add bear with unsupported bear_type
@pytest.mark.parametrize("url,body",
[("http://0.0.0.0:8091/bear",{'bear_type':'BLUE', 'bear_name':'MIKHAIL', 'bear_age':17.5})])
def test_add_bear_wrong_type(add_bear):
    response = add_bear
    assert response.status_code == 500

#TC25. Send delete all bears request
@pytest.mark.parametrize("url", [("http://0.0.0.0:8091/bear")])
def test_delete_all_bears(delete_all_bears,read_all_bears):
    response1 = delete_all_bears
    response2 = read_all_bears
    assert response1.status_code == 200
    assert response2.text == "[]"
