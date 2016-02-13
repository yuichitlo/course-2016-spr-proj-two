"""
CityOfBoston.gov API query functions

Michael Clawar and Raaid Arshad
"""
import json
from mjclawar_rarshad import reference
from mjclawar_rarshad.api import setup_repo
import urllib.request


def api_query(base_url, limit=100, order=None, select=None, where=None):
    query_url = get_query_url(base_url, limit, order, select, where)
    response = urllib.request.urlopen(query_url).read().decode('utf-8')
    r = json.loads(response)
    return r, query_url.split('?')[1]


def get_query_url(base_url, limit, order, select, where):
    # TODO make me in auth.json
    query_url = base_url + '?$$app_token=%s&' % reference.api_token + '$limit=%s' % limit

    if order is not None:
        assert isinstance(order, str)
        query_url += '&$order=%s' % order + '%20DESC'

    if select is not None:
        assert isinstance(select, list)

    if where is not None:
        assert isinstance(where, str)

    return query_url
