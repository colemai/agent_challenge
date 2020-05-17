#!/usr/bin/env python3

"""
Author: Ian
Purpose: Coding exercise, agent based orchestration
Input: 
Output:
Sample Run:
"""

from sys import argv
import json
import pytest


def ingest_story(path_to_story):
	"""Takes path to story (json), returns dict"""
	with open(path_to_story) as f:
	  story = json.load(f)
	return story

def process_story(story):
	""" process a json story through agents the specified agents """
	assert type(story) is dict
	assert bool(story) == True # check not empty



def http_req_agent (options, output={}):
	""" Make a http req to options.url, filling in gaps from output """
	assert type(options) is dict
	assert 'url' in options
	assert isinstance(options['url'], str)
	assert bool(options) == True # check not empty


def print_agent (options, output={}):
	""" print options.message to terminal """
	assert type(options) is dict
	assert 'message' in options
	assert isinstance(options['message'], str)
	assert bool(options) == True # check not empty



if __name__ == '__main__':
    path_to_story = argv[1]
    story = ingest_story(path_to_story)
    http_req_agent(story)
    print(story)