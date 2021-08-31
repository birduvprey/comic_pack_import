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
# TODO: Sub process regex to remove symbols first, then any number of spaces with ','

###############################################################
# Imports
###############################################################

import os
import re
import requests
import difflib

###############################################################
# Variables
###############################################################

from variables import mylar_url, mylar_api, cv_api  # Make sure you personalize variables.py for these

CWD = os.getcwd()
pack_dir = os.path.join(CWD, "packs")  # Root directory where your unsorted comic packs reside
proc_dir = os.path.join(CWD, "process")  # Directory to move files for post-processing in Mylar
error_dir = os.path.join(CWD, "errors")  # Directory to store errored comic files
filename_search = []  # Create an list to store file name searches for CV search
headers = {"User-Agent": "Anything apparently. Keep it under 120 characters to appease PEP 8 though."}


###############################################################
# Functions
###############################################################


def mylar_add_comic(a_comic_id):
    response = requests.get(mylar_url + "/api?apikey=" + mylar_api + "&cmd=addComic&id=" + a_comic_id)
    print(response)


def cv_search_query():
    for filename in os.listdir(pack_dir):
        reg_file = re.sub(r"(.+?)( |)(\d{3,}|\d+ \(of \d+\)|) \(.*?(\d{4})\).*?(\n|$)", r"\1,\3,\4", filename)
        response = requests.get("https://comicvine.gamespot.com/api/search/?api_key=" + cv_api +
                                "&format=json&resources=volume&query=" + reg_file +
                                "&field_list=name,id,start_year,publisher&limit=1", headers=headers)
        if response.status_code != 200:
            print("Error while searching Comic Vine for: '" + reg_file + "' Exiting.")
            exit(1)
        comic_id = response.json().get('results')[0].get('id')
        compare_data = str(response.json().get('results')[0].get('name')) + "," + \
                       str(response.json().get('results')[0].get('start_year'))
        #    return response.json().get('results')[0].get('id')
        filename_search.append(filename + " | " + reg_file + " | " + compare_data + " | " + str(comic_id))
#        print(response.json())
        print(filename + " | " + reg_file + " | " + compare_data + " | " + str(comic_id) + " | "
              + str(difflib.SequenceMatcher(None, reg_file, compare_data).ratio()))


cv_search_query()
###############################################################
# Main
###############################################################

# comic_id = cv_search_query("america,chavez,made,in,the,usa,2021")
# mylar_add_comic(comic_id)
