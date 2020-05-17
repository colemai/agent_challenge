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
import pytest
# import jmespath
import requests
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
		if agent['type'] == 'HTTPRequestAgent':
			event[agent['name']] = http_req_agent(agent['options'], event)
			return event



def http_req_agent (options, event={}):
	""" Make a http req to options.url, filling in gaps from output """
	assert type(options) is dict
	assert 'url' in options
	assert isinstance(options['url'], str)
	assert bool(options) == True # check not empty
	print(options)
	response = requests.get(options['url'])
	assert response.status_code == 200 #TODO account for fails
	#TODO create log file and add response.headers

	output = json.loads(response.text)
	return output

def print_agent (options, event={}):
	""" print options.message to terminal """
	assert type(options) is dict
	assert 'message' in options
	assert isinstance(options['message'], str)
	assert bool(options) == True # check not empty



if __name__ == '__main__':
    path_to_story = argv[1]
    story = ingest_story(path_to_story)
    event = process_story(story)
    print(event)