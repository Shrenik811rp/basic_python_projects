# api key: 9c0093bb09c94ebdb13c203de47a6009

import requests
import tkinter as tk


def get_news():
	api_key = "9c0093bb09c94ebdb13c203de47a6009"
	url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=" + api_key
	news_link = requests.get(url).json()

	articles = news_link["articles"]
	my_news =""
	my_articles = []

	for article in articles:
		my_articles.append(article["title"])

	for news in range(15):
		my_news = my_news + str(news + 1)+ "]  "+ my_articles[news] + "\n\n"

	label.config(text=my_news)	



root = tk.Tk()
root.geometry("1000x690+200+1")
root.title("news app")

button = tk.Button(root,font=25,text='Reload news',command = get_news)

button.pack(pady=20)

label = tk.Label(root,font=18,justify='left')
label.pack(pady=20)


get_news()

root.mainloop()