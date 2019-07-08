import json
import sys
sys.path.append('../')
from ScribeDriver import ScribeDriver

# Fetch login data from json
with open('../../UserData.json') as json_file:  
    data = json.load(json_file) 
    scribeUsr = data["AccessControl"]["Scribe"][0]
    scribePswrd = data["AccessControl"]["Scribe"][1]
print scribePswrd

scribe = ScribeDriver()
scribe.accountLogin(scribeUsr, scribePswrd)


#driver.close()

