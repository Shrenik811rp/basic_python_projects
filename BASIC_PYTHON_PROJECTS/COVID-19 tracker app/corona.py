import json
import tkinter as tk
import requests
import datetime

from requests import api


def get_covid_data():
	api_key = "https://disease.sh/v3/covid-19/all"
	json_data = requests.get(api_key).json()
	total_case = str(json_data['cases'])
	total_death = str(json_data['deaths'])
	today_cases = str(json_data["todayCases"])
	today_death = str(json_data['todayDeaths'])
	today_recovered = str(json_data['todayRecovered'])

	updated_time = json_data['updated']
	#print(total_case)

	date = datetime.datetime.fromtimestamp(updated_time/1e3)

	label_var.config(text= "Total cases : " + today_cases + "\n\nTotal Deaths : " + total_death + "\n\nCases Today : "+ today_cases+ "\n\nDeaths Today : "+ today_death +"\n\n Recovered Today : " + today_recovered )

	label2_var.config(text="Current Time : " + str(date))


root = tk.Tk()
root.geometry("500x500+400+100")
root.title("COVID-19 Tracker App")
font = ("poppins",20,"bold")

heading = tk.Label(root,font=('Arial', 25,"bold"),text="COVID-19 Tracker App")
heading.pack()

button = tk.Button(root,font=font,text="Refresh Stats",command=get_covid_data)
button.pack(pady=20,padx=20)

label_var = tk.Label(root,font=font)
label_var.pack(pady=20)

label2_var = tk.Label(root,font=20)
label2_var.pack()
get_covid_data()
root.mainloop()