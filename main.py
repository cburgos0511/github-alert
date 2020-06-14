from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from datetime import datetime, timezone
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_address = "cburgos@nodecentric.com"
to_address = "cburgos0511@gmail.com"
# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Test email"
msg['From'] = from_address
msg['To'] = to_address
# Create the message (HTML).
html = """\
 We are sending an email using Python and Gmail, how fun! We can fill this with html, and gmail supports a decent range of css style attributes too - https://developers.google.com/gmail/design/css#example.
 """
# Record the MIME type - text/html.
part1 = MIMEText(html, 'html')
# Attach parts into message container
msg.attach(part1)
# Credentials
username = 'cburgos@nodecentric.com'
password = 'imwjjrrkjwzgtunp'
# Sending the email
# note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(username, password)
server.sendmail(from_address, to_address, msg.as_string())
server.quit()

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


if number_of_commits[0] == '0' and local_hour < 17:
    print('Hello')
