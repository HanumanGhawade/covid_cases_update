import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import schedule
import time
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

account_sid = "AC7d3faa311027187450c6c8dbf08ce370"
auth_token = "095b6e1eec2c1b570116f9850c389e7f"


response = requests.get(url="https://www.worldometers.info/coronavirus/country/india/")

daily = response.text
# print(daily)
soup = BeautifulSoup(daily, "html.parser")

article = soup.find(name="li", class_="news_li")
cases = article.getText()
case = cases[:45]
print(case)


def task():
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body= f" today's update {case}",
        from_="+17752568683",
        to="+919503429216"
    )
    print(message.body)


schedule.every().day.at("17:20").do(task)

while True:
    schedule.run_pending()
    time.sleep(1)