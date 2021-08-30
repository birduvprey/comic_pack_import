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

###############################################################
# Variables
###############################################################

mylar_url="http://127.0.0.1:8090" # URL to your Mylar3 installation, to include port number
pack_dir="./packs" # Root directory where your unsorted comic packs reside
error_dir="./errors" # Directory to store errored comic files
mylar_api="XXXXXXXX" # Your Mylar3 installation's API key (Settings->Web Interface->Mylar API Key)
cv_api="XXXXXXXX" # Your ComicVine API key (https://comicvine.gamespot.com/api/)

#### TEST VARIABLES ####
comicid="4050-37737"
search_query="america%20chavez%20made%20in%20the%20usa%202021"

###############################################################
# Functions
###############################################################

function dependencies() {
#  apt install XXX -y || echo "You need to sudo su before running this script so that dependencies can install."
mkdir -p $error_dir

}

function mylar_add_comic() {
  callAPI = $mylar_url "/api?apikey=" $mylar_api "&cmd=addComic&id=" $comicid
  result=$(curl -X GET --header "Accept: */*" $callAPI)
  # Capture errors from non 'OK' response
  echo "Response from Mylar"
  echo $result
}

function cv_search_query() {
  callAPI = "https://comicvine.gamespot.com/api/search/?api_key=" $cv_api "&format=json&resources=volume&query=" \
    $search_query
  result=$(curl -X GET --header "Accetps: */*" $callAPI)
  search_comic_id= jq -r '.[] | .id'
}

function get_comic_id_json($json_text) {
  jq -r
}

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

################################################################
## Main
################################################################

mylar_add_comic
