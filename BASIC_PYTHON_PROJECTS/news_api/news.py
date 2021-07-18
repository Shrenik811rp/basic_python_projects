# api key: USER'S API KEY

import requests
import tkinter as tk


def get_news():
	
	#store your api key
	api_key = "API_KEY_FROM_NEWSAPI"
	#url path 
	url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=" + api_key
	#get data in form of json
	news_link = requests.get(url).json()
	
	#selecting the article item to be displayed
	articles = news_link["articles"]
	my_news =""
	my_articles = []
	#append all the news into my_articles
	for article in articles:
		my_articles.append(article["title"])
		
	#place all the articles into empty string my_news	
	for news in range(len(articles)-4):
		my_news = my_news + str(news + 1)+ "]  "+ my_articles[news] + "\n\n"
	
	#place the label of my_news on the window
	label.config(text=my_news)	


#calling tk()
root = tk.Tk()
root.geometry("1000x690+200+0")
root.title("news app")

#button features
button = tk.Button(root,font=15,text='Reload news',command = get_news)
button.pack(pady=2)

#text/label features
label = tk.Label(root,font=10,justify='left')
label.pack(pady=2)

#caling get_news() function
get_news()

root.mainloop()
