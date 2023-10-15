#!/usr/bin/env python
# coding: utf-8

# # Question 1
# For the provided Python module, the following steps occur:
# 
# 1. a = 0: The global variable a is initialized with the value 0.
# 2. b(): The function b() is called. Inside b(), the global keyword is used to indicate that we are referring to the global variable a. The value of a is passed to function c().
# 3. c(a): The function c() takes an argument and returns the argument incremented by 2. On the first call, it receives 0 and returns 2. This updates the global variable a to 2.
# 4. b(): The function b() is called again. The current value of a, which is 2, is passed to function c().
# 5. c(a): On this call, it receives 2 and returns 4. The global variable a is now updated to 4.
# 6. b(): The function b() is called once more. The current value of a, which is 4, is passed to function c().
# 7. c(a): On this call, it receives 4 and returns 6. The global variable a is now updated to 6.
# 
# After executing the last expression a, the displayed value is 6.
# 

# In[1]:


a = 0

def b():
    global a
    a = c(a)

def c(a):
    return a + 2

# Executing the functions as mentioned
b()
b()
b()

# Return the value of a
a
    


# # Question 2

# In[14]:


def file_length(file_name=r'E:\Downloads\Filelength.txt'):
    try:
        file = open(file_name, 'r')
        contents = file.read()
        file.close()
        print(len(contents))
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        
file_length()


# # Question 3

# In[19]:


class Marsupial:
    def __init__(self):
        self.pouch = []
    
    def put_in_pouch(self, item):
        self.pouch.append(item)
    
    def pouch_contents(self):
        return self.pouch


# In[20]:


m = Marsupial()
m.put_in_pouch('doll')
m.put_in_pouch('firetruck')
m.put_in_pouch('kitten')
print(m.pouch_contents())


# In[21]:


class Kangaroo(Marsupial):
    def __init__(self, x, y):
        super().__init__()  # Call the parent class constructor
        self.x = x
        self.y = y
        
    def jump(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def __str__(self):
        return f"I am a Kangaroo located at coordinates ({self.x},{self.y})"


# In[22]:


k = Kangaroo(0, 0)
print(k)  # Should display "I am a Kangaroo located at coordinates (0,0)"
k.put_in_pouch('doll')
k.put_in_pouch('firetruck')
k.put_in_pouch('kitten')
print(k.pouch_contents())  # Should display ['doll', 'firetruck', 'kitten']
k.jump(1, 0)
k.jump(1, 0)
k.jump(1, 0)
print(k)  # Should display "I am a Kangaroo located at coordinates (3,0)"


# # Question 4

# In[26]:


def collatz(x):
    # Print the current number
    print(x)
    
    # Base case: if x is 1, stop
    if x == 1:
        return
    # If x is even
    elif x % 2 == 0:
        collatz(x // 2)
    # If x is odd
    else:
        collatz(3 * x + 1)
        
collatz(1)


# In[27]:


collatz(10)


# # Question 5

# In[46]:


def binary(n):
    # Base case: if n is 0 or 1, print it
    if n == 0 or n == 1:
        print(n, end='')
        return
    
    # Recursive call for the quotient of n divided by 2
    binary(n // 2)
    
    # Print the remainder
    print(n % 2, end='')


# In[47]:


binary(0)


# In[48]:


binary(1)


# In[49]:


binary(3)


# In[50]:


binary(9)


# # Question 6

# In[60]:


# Import the necessary class from the html.parser module
from html.parser import HTMLParser


# In[61]:


class HeadingParser(HTMLParser):
    
    # Initialize the parser with default attributes
    def __init__(self):
        super().__init__()
        self.in_heading = False
        self.indentation = 0
        
     # This method is called when the parser encounters a starting tag
    def handle_starttag(self, tag, attrs):
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.in_heading = True
            self.indentation = int(tag[1]) - 1

    # This method is called when the parser encounters an ending tag
    def handle_endtag(self, tag):
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.in_heading = False
    # This method handles the actual content/data between tags
    def handle_data(self, data):
        if self.in_heading:
            print(' ' * self.indentation + data)


# In[62]:


# Open and read the HTML file
with open('w3c.html', 'r') as infile:
    content = infile.read()

# Initialize the parser and feed it the HTML content
hp = HeadingParser()
hp.feed(content)


# # Question 7

# In[63]:


get_ipython().system('pip install requests beautifulsoup4')


# In[64]:


import requests
from bs4 import BeautifulSoup


# In[65]:


def webdir(url, depth, indent):
    # Base case: if depth is negative, do not proceed
    if depth < 0:
        return
    
    # Print the URL with appropriate indentation
    print(' ' * indent + url)
    
    # Try fetching the content of the web page
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for error codes
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all links in the page
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href.startswith('http'):  # Check if it's a valid URL (this is a basic check)
                webdir(href, depth-1, indent+2)  # Recursive call with decremented depth and increased indentation

    except requests.RequestException:
        # Error occurred (e.g., page not found, no internet), skip this URL
        pass


# In[66]:


webdir('http://reed.cs.depaul.edu/lperkovic/csc242/test1.html', 2, 0)


# # Questions 7 Reference:
# 
# 1. https://www.geeksforgeeks.org/python-program-to-recursively-scrape-all-the-urls-of-the-website/
# 
# 2. https://stackoverflow.com/questions/69890568/how-to-understand-recursive-with-beautifulsoup-in-python
# 
# 3. https://www.digitalocean.com/community/tutorials/how-to-work-with-web-data-using-requests-and-beautiful-soup-with-python-3
# 
# 4. https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/
# 

# # Question 8 (SQL Queries)

# 
# Assuming the table is named WeatherData, here are the SQL queries:
# 
# a) All the temperature data:
# ```sql
# SELECT [Temperature(C)] 
# FROM WeatherData;
# ```
# 
# 
# b) All the cities, but without repetition:
# ```sql
# SELECT DISTINCT City 
# FROM WeatherData;
# ```
# 
# c) All the records for India:
# ```sql
# SELECT * 
# FROM WeatherData 
# WHERE Country = 'India';
# ```
# 
# d) All the Fall records:
# ```sql
# SELECT * 
# FROM WeatherData
# WHERE Season = 'Fall';
# ```
# 
# e) The city, country, and season for which the average rainfall is between 200 and 400 millimeters:
# ```sql
# SELECT City, Country, Season 
# FROM WeatherData 
# WHERE [Rainfall(mm)] BETWEEN 200 AND 400;
# ```
# 
# f) The city and country for which the average Fall temperature is above 20 degrees, in increasing temperature order:
# ```sql
# SELECT City, Country, AVG([Temperature (C)]) as AvgTemperature
# FROM WeatherData
# WHERE Season = 'Fall'
# GROUP BY City, Country
# HAVING AVG([Temperature (C)]) > 20
# ORDER BY AVG([Temperature (C)]);
# ```
# 
# g) The total annual rainfall for Cairo:
# ```sql
# SELECT SUM["Rainfall(mm)"]
# FROM WeatherData
# WHERE City = 'Cairo';
# ```
# 
# h) The total rainfall for each season:
# ```sql
# SELECT Season, SUM["Rainfall(mm)"] AS TotalRainfall 
# FROM WeatherData
# GROUP BY Season;
# ```

# # Question 9

# In[75]:


words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']


# In[ ]:


words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

# a) Convert each word to uppercase
uppercase_words = [word.upper() for word in words]

# b) Convert each word to lowercase
lowercase_words = [word.lower() for word in words]

# c) Get the length of each word
word_lengths = [len(word) for word in words]

# d) Create a list for every word containing its uppercase, lowercase, and length
word_details = [[word.upper(), word.lower(), len(word)] for word in words]

# e) Get words that have 4 or more characters
long_words = [word for word in words if len(word) >= 4]

uppercase_words, lowercase_words, word_lengths, word_details, long_words
    


# In[76]:


# a) Convert each word to uppercase
uppercase_words = [word.upper() for word in words]
uppercase_words


# In[77]:


# b) Convert each word to lowercase
lowercase_words = [word.lower() for word in words]
lowercase_words


# In[78]:


# c) Get the length of each word
word_lengths = [len(word) for word in words]
word_lengths


# In[81]:


# d) Create a list for every word containing its uppercase, lowercase, and length
word_details = [[word.upper(), word.lower(), len(word)] for word in words]
word_details


# In[85]:


# e) Get words that have 4 or more characters
four_or_more_chars = [word for word in words if len(word) >= 4]
four_or_more_chars


# In[ ]:




