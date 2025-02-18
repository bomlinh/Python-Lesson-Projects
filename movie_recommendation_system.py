from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP

# Main Function for scraping
def main(emotion):
	headers = {
		'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
	# IMDb Url for Drama genre of
	# movie against emotion Sad
	if(emotion == "Sad"):
		urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'

	# IMDb Url for Musical genre of
	# movie against emotion Disgust
	elif(emotion == "Disgust"):
		urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'

	# IMDb Url for Family genre of
	# movie against emotion Anger
	elif(emotion == "Anger"):
		urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'

	# IMDb Url for Thriller genre of
	# movie against emotion Anticipation
	elif(emotion == "Anticipation"):
		urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

	# IMDb Url for Sport genre of
	# movie against emotion Fear
	elif(emotion == "Fear"):
		urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'

	# IMDb Url for Thriller genre of
	# movie against emotion Enjoyment
	elif(emotion == "Enjoyment"):
		urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

	# IMDb Url for Western genre of
	# movie against emotion Trust
	elif(emotion == "Trust"):
		urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'

	# IMDb Url for Film_noir genre of
	# movie against emotion Surprise
	elif(emotion == "Surprise"):
		urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'
    
 #HTTP request to get the data of the whole page
	response = HTTP.get(urlhere, headers=headers)
	data = response.text

	# Parsing the data using
	# BeautifulSoup
	soup = SOUP(data, "lxml")

	# Extract movie titles from the
	# data using regex
	title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})
	return title

if __name__ == '__main__':

	emotion = input("Enter the emotion: ")
	a = main(emotion)
	count = 0

	if(emotion == "disgust" or emotion == "anger"
						or emotion=="surprise"):

		for i in a:

		
			tmp = str(i).split('>;')

			if(len(tmp) == 3):
				print(tmp[1][:-3])

			if(count > 13):
				break
			count += 1
	else:
		for i in a:
			tmp = str(i).split('>')

			if(len(tmp) == 3):
				print(tmp[1][:-3])

			if(count > 11):
				break
			count+=1
# Coded with 💙 by Mr. Unity Buddy
