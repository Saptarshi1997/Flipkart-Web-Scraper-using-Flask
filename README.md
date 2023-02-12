# Flipkart-Web-Scraper-using-Flask


# Basic Principle/Architechture
This project is basically works on accumulating data of a particular product(Iphone 14, 
Macbook air) by scraping data from Flipkat website and showing the data on our website.
In this project we have scraped the review of a particular product from flipkart so that
we can analyse the reviews(containing the name of the user, rating, comments & description) 
to get sentiment of the user, so that the business will take decisions with the help of
these scraped data.


Tool Used: Python, Flask, BS4, BeutifulSoup, Requests module, Pandas, Matplotlib, 
MongoDB, HTML, CSS etc.


# Step-1: Creating Virtual Environment
Use the command: python -m venv "env-name you want to set"
Example: python -m venv myenv


# Step-2: Changing directory
Use the command: cd "project directory name"
Example: cd LMS


# Step3: Installing requirements.txt
Use this command: pip install -r requirements.txt


# Step-4: Run the flask server
Example: Run with the coderunner in case of you are using VS Code

--> Please check the server which is running in console is localhost:5000 or not

--> Go to any browser and search for: http://localhost:5000


# Error/Issues
It might be possible that some packages/libraries will not be installed by commanding
'pip install -r requirements.txt'. In that case you will install the modules/packages
manually

Example: 
1. pymongo = pip install pymongo
2. BS4 = pip install bs4
3. flask = pip install flask
4. requests = pip install requests
