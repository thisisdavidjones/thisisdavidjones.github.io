from bs4 import BeautifulSoup 
import re
from pathlib import Path
import datetime
# import urllib2

existingFilePath =r"C:\\Users\\DAVIDJON\\LocalDocs\\thisisdavidjones\\thisisdavidjones.github.io\\data\links.json"
oldSoup =  BeautifulSoup(open(existingFilePath, encoding="utf8"), "html.parser")

url  = r"C:\\Users\\DAVIDJON\\Downloads\\links.html"
soup = BeautifulSoup(open(url, encoding="utf8"), "html.parser")


#print(str(soup.prettify()))
linklist = soup.find_all('a')


json_snippet = []
json_snippet.append("{")
json_snippet.append("\n")
json_snippet.append("\"links\": [")
json_snippet.append("\n")

pos = -1
for element in linklist:
    pos += 1
    add_date=element.get("add_date")
    added = datetime.date.fromtimestamp(int(add_date))
    href = str(element.get('href'))
    txt = str(element.get_text())
    strDate = added.strftime("%Y-%m-%d")

    json_snippet.append("\t\t\t{")
    json_snippet.append("\n")
    json_snippet.append("\t\t\t\t\"date\":\"" + strDate + "\",")
    json_snippet.append("\n")
    json_snippet.append("\t\t\t\t\"text\":\"" + txt + "\",")
    json_snippet.append("\n")
    json_snippet.append("\t\t\t\t\"href\":\"" + href + "\"")
    json_snippet.append("\n")
    if pos == len(linklist) - 1:
        json_snippet.append("\t\t\t}")
    else:
          json_snippet.append("\t\t\t},")      
    json_snippet.append("\n")



#"date":"2023-04-13",
#"link":"https://www.eupedia.com/",
#"text": "An [encyclopedia of European] things"	
json_snippet.append("]")
json_snippet.append("}")
#print(''.join(json_snippet))

fulltext = ''.join(json_snippet)

newSoup =  BeautifulSoup(fulltext,"html.parser")

print(oldSoup(text='['))

# compare old soup with new soup, looking for [] in the text

f = open("newlinks.json", "w", encoding="utf8")
f.write(fulltext)
f.close()


