from bs4 import BeautifulSoup
import requests

# URL of the webpage to scrape
url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation='

# Send an HTTP request to the URL and get the response text
response = requests.get(url).text

# Parse the HTML content of the response using BeautifulSoup with lxml parser
soup = BeautifulSoup(response, 'lxml')

# Find all job postings on the page
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

# Loop through each job posting to extract the necessary details
for job in jobs:
    # Extract the company name and clean the text
    company_name = job.find('h3', class_='joblist-comp-name').text.strip().replace(' ', ' ')
    
    # Extract the skills required and clean the text
    skill_required = job.find('span', class_='srp-skills').text.strip().replace(' ', '')
    
    # Extract the posting time and clean the text
    post_time = job.find('span', class_='sim-posted').text.strip().replace(' ', ' ')
    
    # Print the extracted information in a formatted manner
    print(f'''Company: {company_name}
Skills Required: {skill_required}
Post Time: {post_time}
''')

# Additional comments for each section:
# - The `url` variable contains the link to the job search page for Python jobs.
# - The `requests.get(url).text` line sends an HTTP GET request to the provided URL and stores the response HTML content in the `response` variable.
# - `BeautifulSoup(response, 'lxml')` initializes a BeautifulSoup object with the HTML content and the lxml parser for parsing the page.
# - `soup.find_all('li', class_='clearfix job-bx wht-shd-bx')` finds all job posting elements on the page and stores them in the `jobs` list.
# - The `for job in jobs` loop iterates over each job posting to extract details like company name, skills required, and post time.
# - `job.find('h3', class_='joblist-comp-name').text.strip().replace(' ', ' ')` finds the company name, removes leading/trailing whitespace, and replaces multiple spaces with a single space for clean output.
# - `job.find('span', class_='srp-skills').text.strip().replace(' ', '')` finds the skills required for the job, removes leading/trailing whitespace, and replaces spaces to clean the output.
# - `job.find('span', class_='sim-posted').text.strip().replace(' ', ' ')` finds the posting time, removes leading/trailing whitespace, and replaces multiple spaces with a single space for clean output.
# - The `print` statement formats and prints the extracted information for each job posting.
