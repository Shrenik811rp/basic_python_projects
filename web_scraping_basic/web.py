from bs4 import BeautifulSoup

#opening a file

#html_file is the variable that has values of home.html
with open('home.html','r') as html_file:

    #content stores the entire html file
    content = html_file.read()
    #to print content of html file uncomment
    #print(content)

    #create instance of beautifulsoup
    #takes in content of html file
    #all text so ->'lxml'
    soup = BeautifulSoup(content,'lxml')

    #find()-> searches for first method of tags
    tag_find = soup.find('h1')
    #print(tag_find)

    #to find all h5 tage use find_all() method
    find_courses = soup.find_all('h5')
    #print(find_courses)

    #to print all course neatly in text format use 'text' instead of html tag format
    for course in find_courses:
        print(course.text)

    #course_price stores the price of courses html tags for that link 

    #class_ -> is refering to html attribute and not python class
    prices = soup.find_all('div',class_ ="card")
    for price in prices:
        #if you see html file the course names are in h5 tag and prices are in a tag

        #so this is another way of accessing tags from html file
        #text convert the html tags into readable format
        course_name =price.h5.text
        course_price = price.a.text

        #to get only the price and avoid the text before it
        #split the text and get the last element which is the price in dollars
        course_rate = price.a.text.split()[-1]
        print("\n\nCourse details: ")
        print("Course name: ",course_name)
        print("Course price: ",course_price)
        print("Pice of course in dollars: ",course_rate)

        print(f"{course_name} is at cost of {course_rate}")

    #prettify()->for clean indetation uncomment to check
    #print(soup.prettify())
print("working fine...\n")