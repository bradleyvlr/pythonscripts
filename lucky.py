#!/usr/bin/python3
#Goal of this is to take command line arguments and search for them on duckduckgo and open in browser
#I do want to lookup using Lynx rather than default browser. This could make my life easier.
#I then have to decide how ambitious I will get. Do I want to finish this section and then immediately try to start on my data center monitor? Do I need to look into curses elsewhere? Will that be better suited to after I finish the book? I don't know

import requests, sys, webbrowser, bs4

print('DuckDuckGoing...')
res = requests.get('http://duckduckgo.com/html/?q=' + '+'.join(sys.argv[1:]))
res.raise_for_status()
soup= bs4.BeautifulSoup(res.text, "html.parser")
linkElems = soup.select('.result__a')
print(linkElems)
numOpen = min(2, len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://duckduckgo.com'+linkElems[i].get('href'))
