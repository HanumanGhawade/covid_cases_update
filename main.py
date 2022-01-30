import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
account_sid = "AC7d3faa311027187450c6c8dbf08ce370"
auth_token = "4421b596cbe4f7e8283b2cfbf435e2fd"

response = requests.get(url="https://www.worldometers.info/coronavirus/country/india/")

daily = response.text
# print(daily)
soup = BeautifulSoup(daily, "html.parser")

article = soup.find(name="li", class_="news_li")
cases = article.getText()
case = cases[:45]
print(case)

client = Client(account_sid, auth_token)

message = client.messages \
    .create(
    body= f"{case}",
    from_="+17752568683",
    to="+919503429216"
)
print(message.sid)



