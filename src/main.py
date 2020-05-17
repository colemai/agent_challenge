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

if __name__ == '__main__':
    path_to_story = argv[1]
    story = ingest_story(path_to_story)
    test_ingest_story()
    print(story)