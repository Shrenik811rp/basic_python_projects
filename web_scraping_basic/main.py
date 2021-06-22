from bs4 import BeautifulSoup

#request information from website
import requests

#get info from website

#we are scraping data from "Times jobs and looking for job post related to python"
#get only html text form page so use 'text'
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

#'lxml' will deal with broken data from the html page
soup = BeautifulSoup(html_text,'lxml')

#if you right click and inspect on companies on the page 
#the comapnies are in a list tag and under this class name
jobs = soup.find_all('li',class_="clearfix job-bx wht-shd-bx")

#keep track of number of jobs found
count = 0
for job in jobs:

    #we want the companies which posted jobs a "few" days ago
    job_publish = job.find('span',class_='sim-posted').span.text
    #only if it contains "few" in posted date only then print them
    if 'few' in job_publish:
        print(f"\nJob published date : {job_publish}")
        #print("\n\nEntire html of that company:")
        #print(job)

        #we see from the inspect page that the company name is in h3 tag

        #which is under a class name clled
        #joblist-comp-name
        #.text is used to get only text of company instead of whole html page

        #to get rid of unwanted whitespace use replace it replaces blank with nothing
        company_name = job.find('h3',class_='joblist-comp-name').text.strip()
        print(f"Company name : {company_name}")

        #to print out even the skills for the job
        #go to the page ull see that the skills are listed under "span" tag


        #.replace replaces whitespace or blank (" ") with nothing ('') 
        job_skills = job.find('span',class_='srp-skills').text.strip()

        print(f"Skills for job: {job_skills}")

        job_experience = job.find('li').text.split('l')[-1]

        print(f"Experience for job is : {job_experience}\n")

        #200 response means it was successful
        #print(html_text)

        count += 1
        print("working fine...\n")
print(f"Nos of python related jobs found: {count}")        





