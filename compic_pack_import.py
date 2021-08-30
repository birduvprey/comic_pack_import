###############################################################
# References
###############################################################

# ComicVine API: https://comicvine.gamespot.com/api/
# Mylar github: https://github.com/mylar3/mylar3
# Thanks Aethaeran! https://github.com/Aethaeran

###############################################################
# TODOs
###############################################################

# TODO: ✓ Connect with MYLAR to add comic series to want list
# TODO: Connect to ComicVine to search for comic series, not comic issue
# TODO: Build proper regex for series name
# TODO: Build error handling for odd comic file names
# TODO:     Offload error files, log errors
# TODO: Capture error responses for Mylar3
# TODO: Sub process regex to remove symbols first, then any number of psaces with ','

###############################################################
# Imports
###############################################################

import logging
import os
import wget
import re
import requests
import json
from variables import mylar_url, mylar_api, cv_api

###############################################################
# Variables
###############################################################

CWD = os.getcwd()
pack_dir = os.path.join(CWD,"packs")  # Root directory where your unsorted comic packs reside
proc_dir = os.path.join(CWD,"process")  # Directory to move files for post-processing in Mylar
error_dir = os.path.join(CWD,"errors")  # Directory to store errored comic files
filename_search = []  # Create an list to store file name searches for CV search
headers = {"User-Agent": "Anything apparently. Keep it under 120 characters to appease PEP 8 though."}

###############################################################
# Test Variables
###############################################################
comic_id = "4050-37737"
search_query = "america,chavez,made,in,the,usa,2021"

###############################################################
# Functions
###############################################################

def mylar_add_comic():
    response = requests.get(mylar_url + "/api?apikey=" + mylar_api + "&cmd=addComic&id=" + comic_id)
    print(response)


def cv_search_query():

    response = requests.get("https://comicvine.gamespot.com/api/search/?api_key=" + cv_api +
                            "&format=json&resources=volume&query=" + search_query +
                            "&field_list=name,id,start_year,publisher&limit=1", headers=headers)

    if response.status_code != 200:
        print("Error while searching Comic Vine for: '" + search_query + "' Exiting.")
        exit(1)

    print(response.json().get('results')[0].get('id'))


###############################################################
# Main
###############################################################

# mylar_add_comic()
cv_search_query()
