from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as uReq

my_url = "https://www.flipkart.com/search?q=IPHONE&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

uclinet = uReq(my_url)
page_html = uclinet.read()
uclinet.close()
page_soup= soup(page_html , "html.parser")

containers = page_soup.findAll("div", {"class":"_3wU53n"})

print((containers))
#print(soup.prettify(containers[0]))
container = containers[0]
