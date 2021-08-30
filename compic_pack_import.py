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
from variables import cv_api, mylar_api

###############################################################
# Variables
###############################################################

CWD = os.getcwd()
pack_dir = os.path.join(CWD,"packs")  # Root directory where your unsorted comic packs reside
proc_dir = os.path.join(CWD,"process")  # Directory to move files for post-processing in Mylar
error_dir = os.path.join(CWD,"errors")  # Directory to store errored comic files
filename_search = ()  # Create an array to store file name searches for CV search
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

###############################################################
# Test Variables
###############################################################
comicid = "4050-37737"
search_query = "america,chavez,made,in,the,usa,2021"

###############################################################
# Functions
###############################################################


def mylar_add_comic():
    response = requests.get(mylar_url + "/api?apikey=" + mylar_api + "&cmd=addComic&id=" + comicid)
    print(response)


def cv_search_query():

    response = requests.get("https://comicvine.gamespot.com/api/search/?api_key=" + cv_api +
                            "&format=json&resources=volume&query=" + search_query +
                            "&field_list=name,id,start_year,publisher&limit=1", headers=headers)

    if response.status_code != 200:
        print("Error handling")

    json_response = response.json()
    print(json_response.get('results')[0].get('id'))


cv_search_query()


# mylar_add_comic()
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
