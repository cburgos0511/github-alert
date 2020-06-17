from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from datetime import datetime, timezone
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

# Find todays date and local hour
today = datetime.today().strftime('%Y-%m-%d')
local_hour = datetime.now(timezone.utc).astimezone().hour  # UTC time

# Make a request to url
my_url = 'https://github.com/cburgos0511'
uClient = uReq(my_url)

# Extract the entire html page
page_html = uClient.read()

# Close the server sense
uClient.close()

# Parse the html page
page_soup = soup(page_html, 'html.parser')

# Find the last rect and put the data-count value to an array
number_of_commits = [item['data-count']
                     for item in page_soup.find_all('rect', attrs={'data-date': today})]


#
def commit_check():
    print('Scheduler running everyday at 10pm')
    if number_of_commits[0] == '0':
        pass_fail = "PASS" if number_of_commits[0] > "0" else "FAIL"
        f = open("commit_log.txt", "a")
        f.write(
            f"  {today}             {number_of_commits[0]}              {pass_fail}  \n-------------|---------------------|------------ \n")
        f.close()

schedule.every().day.at('10:00').do(commit_check)

while True:
    schedule.run_pending()
    time.sleep(1)
