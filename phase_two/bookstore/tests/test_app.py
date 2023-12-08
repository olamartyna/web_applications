from app import sort_names_list, names_decoder, names_encoder
# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===


# File: tests/test_app.py

"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'


# When I make a POST request to /sort-names
# And I send [Joe,Alice,Zoe,Julia,Kieran]
# I should get a 200 response and sorted list of names:
# Alice,Joe,Julia,Kieran,Zoe
# def test_sort_names(web_client):
#     response = web_client.post('/sort-names', data={'names': ' Joe,Alice,Zoe,Julia,Kieran Smith'})
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == 'Alice, Joe,Julia,Kieran Smith,Zoe'

    # This test is testing the endpoint

# this is pure infrastructure test
def test_sort_names_2(web_client):
    # separating method sort_names_domain, spearating the domain logic from the infrastructure
    names = '   Joe ,  Alice,Zoe Smith,Julia, Kieran'
    sorted_names = names_encoder(sort_names_list(names_decoder(names)))

    response = web_client.post('/sort-names', data={'names': names})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == sorted_names

# This is a domain test:
def test_sort_names():
    result = sort_names_list(['Jo', 'Paul', 'Alice'])
    assert result == ['Alice', 'Jo', 'Paul']

# These tests are for application level. They are not testing the domain.
# encoder, decoder is about input and output of the data, how we want it to look like
def test_names_decoder():
    result = names_decoder(' Jo, Alice Smith,  Bernard   ')
    assert result == ['Jo', 'Alice Smith', 'Bernard']

def test_names_encoder():
    result = names_encoder(['John', 'Mary', 'Henry'])
    assert result == 'John, Mary, Henry'
