import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.theworldgames.org/editions/Birmingham-USA-2022-13/infosystem#//swog2022.sportresult.com/hide/en/Comp/Info/ResultList/CPOWTEAM5-------------GPB-000100--').content  
soup = BeautifulSoup(r)
print(soup)