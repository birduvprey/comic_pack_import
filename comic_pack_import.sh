###############################################################
# References
###############################################################

# ComicVine API: https://comicvine.gamespot.com/api/
# Mylar github: https://github.com/mylar3/mylar3
# Thanks Aethaeran! https://github.com/Aethaeran

###############################################################
# TODOs
###############################################################

# ✓ Connect with MYLAR to add comic series to want list
# Connect to ComicVine to search for comic series, not comic issue
# Build proper regex for series name
# Build error handling and odd comic file names
#     Offload error files, log errors
# Capture error responses for Mylar3

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

#function get_calishot_db() {
#  # TODO: This should be made dynamic by parsing the reddit post's html for the links.
#  if [ ! -f "$tmp_dir/$eng_db" ]; then
#    if [ ! -f "$tmp_dir/$eng_db_zip" ]; then
#      wget "$eng_db_link" --directory-prefix "$tmp_dir/"
#    fi
#    7za x "$tmp_dir/$eng_db_zip" -o"$tmp_dir/"
#  fi
#  if [ ! -f "$tmp_dir/$non_eng_db" ]; then
#    if [ ! -f "$tmp_dir/$non_eng_db_zip" ]; then
#      wget "$non_eng_db_link" --directory-prefix "$tmp_dir/"
#    fi
#    7za x "$tmp_dir/$non_eng_db_zip" -o"$tmp_dir/"
#  fi
#}
#

#function wget_loop() {
#  # Feed list to wget loop
#  #  echo "Mapping old file to array"
#  mapfile -t library_list <"$1" # Map $1 file to list A
#  #  echo "Iterating old array"
#  for link in "${library_list[@]}"; do # for each entry in List A
#    # $1=IP:PORT#LIBRARY_ID
#    # $2=library_specific_dir
#    book_id=$(echo "$link" | sed -E "s|.*?/([[:digit:]]+)|\1|g")
#    library_specific_dir=$(echo "$link" | sed -E 's|(http://\|https://)(.*)\/get.*|\2|g' | sed -E 's/([\\/&:"*?<>|]+)/_/g')
#    library_specific_dir="$dl_dir/$library_specific_dir/$book_id"
#    mkdir -p "$library_specific_dir"
#    echo "'$link' will save to '$library_specific_dir'"
#    wget "$link" \
#    --content-disposition \
#    --no-clobber \
#    -P "$library_specific_dir" \
#    && echo "Download of $link successful." \
#    && sed -E "s|$link\n||g" -i "$1" -z
#  done
#}

################################################################
## Main
################################################################

mylar_add_comic
