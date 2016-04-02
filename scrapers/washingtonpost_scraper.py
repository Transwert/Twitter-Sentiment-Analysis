from bs4 import BeautifulSoup
from urllib import request


def scrape(link):
	link = str(link) #ensure that link is a string. 
	content = []
	entire_html = request.urlopen(link).read() # get the html of the link
	soup_entire_html = BeautifulSoup(entire_html, "html.parser") 
	all_paragraphs = soup_entire_html.find_all('article', {'itemprop': 'articleBody'}) 
	for p in all_paragraphs:
		for text in p.find_all('p'):
			content.append(text.getText())
			
	print(content[0])

