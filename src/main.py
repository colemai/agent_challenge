#!/usr/bin/env python3

"""
Author: Ian
Purpose: Coding exercise, agent based orchestration
Input: path to json file
Output: 
Sample Run: python src/main.py data/tiny-tines-sunset.json
"""

from sys import argv
import json
import jmespath
import requests
import re
import pdb


def ingest_story(path_to_story):
	"""Takes path to story (json), returns dict"""
	with open(path_to_story) as f:
	  story = json.load(f)
	return story


def process_story(story):
	""" process a json story through agents the specified agents """
	assert type(story) is dict
	assert bool(story) == True # check not empty
	event = {}
	for agent in story['agents']:
		# print('Running agent', agent['name'])
		if agent['type'] == 'HTTPRequestAgent':
			event[agent['name']] = http_req_agent(agent['options'], event)
		elif agent['type'] == 'PrintAgent':
			event[agent['name']] = print_agent(agent['options'], event)
		else:
			sys.exit('Ruh Roh, invalid agent name')


def format_agent_arg (event, arg):
	""" If an arg has double curly brackets, replace that section with the 
	specified key from event """
	# arg = 'https://api.sunrise-sunset.or{{ }}g/json?lat={{location.latitude}}&lng={{location.longitude}}'
	pattern = r"\{\{(.*?)\}\}"
	matches = re.findall(pattern, arg)
	values = [jmespath.search(match, event) if (bool(match) and not str(match).isspace()) else match for match in matches]
	pdb.set_trace()
	new_arg = re.sub(pattern, '{}', arg).format(*values)
	return new_arg


def http_req_agent (options, event={}):
	""" Make a http req to options.url, filling in gaps from output """
	assert type(options) is dict
	assert 'url' in options
	assert isinstance(options['url'], str)
	assert bool(options) == True # check not empty

	url = options['url']
	# Incorporate previous output:
	if event != {}:
		url = format_agent_arg(event, url)

	response = requests.get(url)
	assert response.status_code in range(200, 300) #TODO account for fails
	#TODO create log file and add response.headers

	output = json.loads(response.text)
	return output


def print_agent (options, event={}):
	""" print options.message to terminal """
	assert type(options) is dict
	assert 'message' in options
	assert isinstance(options['message'], str)
	assert bool(options) == True # check not empty

	message = options['message']
	# Incorporate previous output:
	if event != {}:
		message = format_agent_arg(event, message)
	
	print(message)
	return message


if __name__ == '__main__':
    path_to_story = argv[1]
    story = ingest_story(path_to_story)
    event = process_story(story)
    #TODO save event to output file