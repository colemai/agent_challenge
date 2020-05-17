#!/usr/bin/env python3

"""
Author: Ian
Purpose: test the main script
Input: 
Output:
Sample Run: pytest
"""

import pytest

from src import main

def test_ingest_story():
	"""pytest for test case input"""
	assert main.ingest_story("data/tiny-tines-sunset.json") == {'agents': [{'type': 'HTTPRequestAgent', 'name': 'location', 'options': {'url': 'http://free.ipwhois.io/json/'}}, {'type': 'HTTPRequestAgent', 'name': 'sunset', 'options': {'url': 'https://api.sunrise-sunset.org/json?lat={{location.latitude}}&lng={{location.longitude}}'}}, {'type': 'PrintAgent', 'name': 'print', 'options': {'message': 'Sunset in {{location.city}}, {{location.country}} is at {{sunset.results.sunset}}.'}}]}

def test_http_req_agent():
	ip_ans = main.http_req_agent({'url': 'http://free.ipwhois.io/json/'})
	assert type(ip_ans) is dict 
	assert 'ip' in ip_ans