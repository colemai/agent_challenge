#!/usr/bin/env python3

"""
Author: Ian
Purpose: test the main script
Input: -
Output: -
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


def test_http_req_agent_sunset_req ():
	sunset_ans = main.http_req_agent({'url': 'https://api.sunrise-sunset.org/json?lat={{location.latitude}}&lng={{location.longitude}}'}, {'location': {'ip': '109.78.65.85', 'success': True, 'type': 'IPv4', 'continent': 'Europe', 'continent_code': 'EU', 'country': 'Ireland', 'country_code': 'IE', 'country_flag': 'https://cdn.ipwhois.io/flags/ie.svg', 'country_capital': 'Dublin', 'country_phone': '+353', 'country_neighbours': 'GB', 'region': 'County Dublin', 'city': 'Dublin', 'latitude': '53.3165322', 'longitude': '-6.3425318', 'asn': 'AS15502', 'org': 'Vodafone Ireland', 'isp': 'Vodafone Ireland Limited', 'timezone': 'Europe/Dublin', 'timezone_name': 'Greenwich Mean Time', 'timezone_dstOffset': '0', 'timezone_gmtOffset': '0', 'timezone_gmt': 'GMT 0:00', 'currency': 'Euro', 'currency_code': 'EUR', 'currency_symbol': '€', 'currency_rates': '0.924078', 'currency_plural': 'euros', 'completed_requests': 46}})
	assert type(sunset_ans) is dict
	assert 'results' in sunset_ans
	assert 'sunrise' in sunset_ans['results']


def test_print_agent():
	ans = main.print_agent({'message': 'Sunset in {{location.city}}, {{location.country}} is at {{sunset.results.sunset}}.'}, {'location': {'ip': '109.78.65.85', 'success': True, 'type': 'IPv4', 'continent': 'Europe', 'continent_code': 'EU', 'country': 'Ireland', 'country_code': 'IE', 'country_flag': 'https://cdn.ipwhois.io/flags/ie.svg', 'country_capital': 'Dublin', 'country_phone': '+353', 'country_neighbours': 'GB', 'region': 'County Dublin', 'city': 'Dublin', 'latitude': '53.3165322', 'longitude': '-6.3425318', 'asn': 'AS15502', 'org': 'Vodafone Ireland', 'isp': 'Vodafone Ireland Limited', 'timezone': 'Europe/Dublin', 'timezone_name': 'Greenwich Mean Time', 'timezone_dstOffset': '0', 'timezone_gmtOffset': '0', 'timezone_gmt': 'GMT 0:00', 'currency': 'Euro', 'currency_code': 'EUR', 'currency_symbol': '€', 'currency_rates': '0.924078', 'currency_plural': 'euros', 'completed_requests': 48}, 'sunset': {'results': {'sunrise': '4:20:36 AM', 'sunset': '8:23:00 PM', 'solar_noon': '12:21:48 PM', 'day_length': '16:02:24', 'civil_twilight_begin': '3:35:22 AM', 'civil_twilight_end': '9:08:14 PM', 'nautical_twilight_begin': '2:29:56 AM', 'nautical_twilight_end': '10:13:40 PM', 'astronomical_twilight_begin': '12:00:01 AM', 'astronomical_twilight_end': '12:00:01 AM'}, 'status': 'OK'}})
	assert ans == "Sunset in Dublin, Ireland is at 8:23:00 PM."


def test_format_agent_arg():
	event = {'location': {'ip': '109.78.65.85', 'success': True, 'type': 'IPv4', 'continent': 'Europe', 'continent_code': 'EU', 'country': 'Ireland', 'country_code': 'IE', 'country_flag': 'https://cdn.ipwhois.io/flags/ie.svg', 'country_capital': 'Dublin', 'country_phone': '+353', 'country_neighbours': 'GB', 'region': 'County Dublin', 'city': 'Dublin', 'latitude': '53.3165322', 'longitude': '-6.3425318', 'asn': 'AS15502', 'org': 'Vodafone Ireland', 'isp': 'Vodafone Ireland Limited', 'timezone': 'Europe/Dublin', 'timezone_name': 'Greenwich Mean Time', 'timezone_dstOffset': '0', 'timezone_gmtOffset': '0', 'timezone_gmt': 'GMT 0:00', 'currency': 'Euro', 'currency_code': 'EUR', 'currency_symbol': '€', 'currency_rates': '0.924078', 'currency_plural': 'euros', 'completed_requests': 60}}
	arg = "https://api.sunrise-sunset.org/json?lat={{location.latitude}}&lng={{location.longitude}}"
	ans = main.format_agent_arg(event, arg)
	assert ans == "https://api.sunrise-sunset.org/json?lat=53.3165322&lng=-6.3425318"


def test_format_agent_arg_unknown_key():
	event = {'location': {'ip': '109.78.65.85', 'success': True, 'type': 'IPv4', 'continent': 'Europe', 'continent_code': 'EU', 'country': 'Ireland', 'country_code': 'IE', 'country_flag': 'https://cdn.ipwhois.io/flags/ie.svg', 'country_capital': 'Dublin', 'country_phone': '+353', 'country_neighbours': 'GB', 'region': 'County Dublin', 'city': 'Dublin', 'latitude': '53.3165322', 'longitude': '-6.3425318', 'asn': 'AS15502', 'org': 'Vodafone Ireland', 'isp': 'Vodafone Ireland Limited', 'timezone': 'Europe/Dublin', 'timezone_name': 'Greenwich Mean Time', 'timezone_dstOffset': '0', 'timezone_gmtOffset': '0', 'timezone_gmt': 'GMT 0:00', 'currency': 'Euro', 'currency_code': 'EUR', 'currency_symbol': '€', 'currency_rates': '0.924078', 'currency_plural': 'euros', 'completed_requests': 60}}
	arg = "https://api.sunrise-sunset.or{{location.falsestring8}}g/json?lat={{location.latitude}}&lng={{location.longitude}}"
	ans = main.format_agent_arg(event, arg)
	assert ans == "https://api.sunrise-sunset.org/json?lat=53.3165322&lng=-6.3425318"


def test_format_agent_arg_empty_key():
	event = {'location': {'ip': '109.78.65.85', 'success': True, 'type': 'IPv4', 'continent': 'Europe', 'continent_code': 'EU', 'country': 'Ireland', 'country_code': 'IE', 'country_flag': 'https://cdn.ipwhois.io/flags/ie.svg', 'country_capital': 'Dublin', 'country_phone': '+353', 'country_neighbours': 'GB', 'region': 'County Dublin', 'city': 'Dublin', 'latitude': '53.3165322', 'longitude': '-6.3425318', 'asn': 'AS15502', 'org': 'Vodafone Ireland', 'isp': 'Vodafone Ireland Limited', 'timezone': 'Europe/Dublin', 'timezone_name': 'Greenwich Mean Time', 'timezone_dstOffset': '0', 'timezone_gmtOffset': '0', 'timezone_gmt': 'GMT 0:00', 'currency': 'Euro', 'currency_code': 'EUR', 'currency_symbol': '€', 'currency_rates': '0.924078', 'currency_plural': 'euros', 'completed_requests': 60}}
	arg = "https://api.sunrise-sunset.or{{}}g/json?lat={{location.latitude}}&lng={{location.longitude}}"
	ans = main.format_agent_arg(event, arg)
	assert ans == "https://api.sunrise-sunset.org/json?lat=53.3165322&lng=-6.3425318"


def test_format_agent_arg_unmatching_braces():
	event = {'location': {'ip': '109.78.65.85', 'success': True, 'type': 'IPv4', 'continent': 'Europe', 'continent_code': 'EU', 'country': 'Ireland', 'country_code': 'IE', 'country_flag': 'https://cdn.ipwhois.io/flags/ie.svg', 'country_capital': 'Dublin', 'country_phone': '+353', 'country_neighbours': 'GB', 'region': 'County Dublin', 'city': 'Dublin', 'latitude': '53.3165322', 'longitude': '-6.3425318', 'asn': 'AS15502', 'org': 'Vodafone Ireland', 'isp': 'Vodafone Ireland Limited', 'timezone': 'Europe/Dublin', 'timezone_name': 'Greenwich Mean Time', 'timezone_dstOffset': '0', 'timezone_gmtOffset': '0', 'timezone_gmt': 'GMT 0:00', 'currency': 'Euro', 'currency_code': 'EUR', 'currency_symbol': '€', 'currency_rates': '0.924078', 'currency_plural': 'euros', 'completed_requests': 60}}
	arg = "https://api.sunrise-sunset.or{{}g/json?lat={{location.latitude}}&lng={{location.longitude}}"
	ans = main.format_agent_arg(event, arg)
	assert ans == "https://api.sunrise-sunset.or{{}g/json?lat=53.3165322&lng=-6.3425318"


def test_format_agent_arg_unmatching_braces_2():
	event = {'location': {'ip': '109.78.65.85', 'success': True, 'type': 'IPv4', 'continent': 'Europe', 'continent_code': 'EU', 'country': 'Ireland', 'country_code': 'IE', 'country_flag': 'https://cdn.ipwhois.io/flags/ie.svg', 'country_capital': 'Dublin', 'country_phone': '+353', 'country_neighbours': 'GB', 'region': 'County Dublin', 'city': 'Dublin', 'latitude': '53.3165322', 'longitude': '-6.3425318', 'asn': 'AS15502', 'org': 'Vodafone Ireland', 'isp': 'Vodafone Ireland Limited', 'timezone': 'Europe/Dublin', 'timezone_name': 'Greenwich Mean Time', 'timezone_dstOffset': '0', 'timezone_gmtOffset': '0', 'timezone_gmt': 'GMT 0:00', 'currency': 'Euro', 'currency_code': 'EUR', 'currency_symbol': '€', 'currency_rates': '0.924078', 'currency_plural': 'euros', 'completed_requests': 60}}
	arg = "https://api.sunrise-sunset.or{g}/json?lat={{location.latitude}}&lng={{location.longitude}}"
	ans = main.format_agent_arg(event, arg)
	assert ans == "https://api.sunrise-sunset.or{g}/json?lat=53.3165322&lng=-6.3425318"


def test_format_agent_arg_unmatching_braces_3():
	event = {'location': {'ip': '109.78.65.85', 'success': True, 'type': 'IPv4', 'continent': 'Europe', 'continent_code': 'EU', 'country': 'Ireland', 'country_code': 'IE', 'country_flag': 'https://cdn.ipwhois.io/flags/ie.svg', 'country_capital': 'Dublin', 'country_phone': '+353', 'country_neighbours': 'GB', 'region': 'County Dublin', 'city': 'Dublin', 'latitude': '53.3165322', 'longitude': '-6.3425318', 'asn': 'AS15502', 'org': 'Vodafone Ireland', 'isp': 'Vodafone Ireland Limited', 'timezone': 'Europe/Dublin', 'timezone_name': 'Greenwich Mean Time', 'timezone_dstOffset': '0', 'timezone_gmtOffset': '0', 'timezone_gmt': 'GMT 0:00', 'currency': 'Euro', 'currency_code': 'EUR', 'currency_symbol': '€', 'currency_rates': '0.924078', 'currency_plural': 'euros', 'completed_requests': 60}}
	arg = "https://api.sunrise-sunset.or{}}g/json?lat={{location.latitude}}&lng={{location.longitude}}"
	ans = main.format_agent_arg(event, arg)
	assert ans == "https://api.sunrise-sunset.or{}}g/json?lat=53.3165322&lng=-6.3425318"
