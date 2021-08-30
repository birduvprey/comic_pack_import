###############################################################
# References
###############################################################

# ComicVine API: https://comicvine.gamespot.com/api/
# Mylar github: https://github.com/mylar3/mylar3
# Thanks Aethaeran! https://github.com/Aethaeran

###############################################################
# TODOs
###############################################################

# TODO: Connect with MYLAR to add comic series to want list
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

###############################################################
# Variables
###############################################################

CWD = os.getcwd()
mylar_url = "http://127.0.0.1:8090"  # URL to your Mylar3 installation, to include port number
pack_dir = "./packs"  # Root directory where your unsorted comic packs reside
proc_dir = "./process"  # Directory to move files for post-processing in Mylar
error_dir = "./errors"  # Directory to store errored comic files
mylar_api = "XXXXXXXX"  # Your Mylar3 installation's API key (Settings->Web Interface->Mylar API Key)
cv_api = "XXXXXXXX"  # Your ComicVine API key (https://comicvine.gamespot.com/api/)
filename_search = ()  # Create an array to store file name searches for CV search

###############################################################
# Test Variables
###############################################################
comicid = "4050-37737"
search_query = "america,chavez,made,in,the,usa%,2021"

###############################################################
# Functions
###############################################################


def mylar_add_comic():
    response = requests.get(mylar_url + "/api?apikey=" + mylar_api + "&cmd=addComic&id=" + comicid)
    print(response)


mylar_add_comic()
###############################################################
# PREVIOUS BASH SCRIPTS

# function
# cv_search_query()
# {
#     echo
# "$(curl -X GET --header "
# Accept: * / *" "
# https: // comicvine.gamespot.com / api / search /?api_key =$cv_api & format = json
# " \
#       " & resources = volume & query =$search_query & field_list = name, id, start_year, publisher & limit = 1
# ") | jq -r '.results[] | .id'"
#
# }
#
# function
# filename_parse()
# {
# for file in "$pack_dir" / *
#             do
# pcregrep -o1 -o4 -e '(.+?)( |)(\d{3,}|\d+ \(of \d+\)|) \(.*?(\d{4})\).*?(\n|$)' "$file"
# done
# }
###############################################################
