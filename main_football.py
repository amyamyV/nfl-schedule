import footballParse
import sys


#using Python3. To run: python3 _fileName_
#to install stuff: pip3 install --user _packageName_
#to open: open _fileName_

#doesn't generate lines -> put in black lines yourself

#sys.argv[0] to want to pass in url through cmd line
string_of_week_url_espn = "https://www.espn.com/nfl/schedule"

footballParse.getFootballFormatted(string_of_week_url_espn)
