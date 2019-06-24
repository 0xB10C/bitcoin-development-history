#!/usr/bin/env python

""" This script checks the `bitcoin-history.json` file for: 
  - id (not empty, valid format)
  - type (is valid)
  - title (not empty)
  - paragraps (no empty paragraphs)
  - links (no empty label or link)
""" 

import json

VALID_TYPES = ["release", "other", "post", "bug", "company"]

def load_file(filename):
  with open(filename) as json_file:  
    data = json.load(json_file)
    json_file.close()
    return data

def check_timepoint_id(timepoint):
    check_timepoint_id_exist(timepoint)
    check_timepoint_id_format(timepoint)

def check_timepoint_id_exist(timepoint):
    assert timepoint["id"] != "" , "The id is empty: " + str(timepoint)
      
def check_timepoint_id_format(timepoint):
    split = timepoint["id"].split("-")
    assert len(split[0]) == 4 and int(split[0]) > 2000 and int(split[0]) < 3000, "The id does not start with a (valid) year: " + str(timepoint)
    assert split[1] in VALID_TYPES, "The id does not contain a valid timempoint type: " + str(timepoint)    
    assert split[1] == timepoint["type"], "The type in the id does not match the type: " + str(timepoint)  

def check_timepoint_type(timepoint):
    assert timepoint["type"] in VALID_TYPES , "The type is invalid: " + str(timepoint)

def check_timepoint_title(timepoint):
    assert timepoint["title"] != "", "The title is empty: " + str(timepoint)

def check_timepoint_paragraphs(timepoint):
    for paragraph in timepoint["paragraphs"]:
        assert paragraph != "", "There is an empty paragraph in: " + str(timepoint)

def check_timepoint_links(timepoint):
    if "links" in timepoint:
      for link in timepoint["links"]:
          assert link["link"] != "", "There is an empty link in: " + str(timepoint)
          assert link["label"] != "", "There is an empty link-label in: " + str(timepoint)

if __name__ == '__main__':
    data = load_file('bitcoin-history.json')
    
    for timepoint in data:
      check_timepoint_id(timepoint)
      check_timepoint_type(timepoint)
      check_timepoint_title(timepoint)
      check_timepoint_paragraphs(timepoint)
      check_timepoint_links(timepoint)

    print("File bitcoin-history.json checked successfully. No errors found.")


