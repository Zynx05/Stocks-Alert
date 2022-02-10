import requests
from twilio.rest import Client

STOCK_NAME = "ADA"
COMPANY_NAME = "Tesla Inc"
CURRENCY = "USD"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_APIKEY = "LNU61O9DHQTAXUCC"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function": "DIGITAL_CURRENCY_DAILY",
    "symbol": STOCK_NAME,
    "market": CURRENCY,
    "apikey": STOCK_APIKEY,
}
response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
ada = response.json()['Time Series (Digital Currency Daily)']["2021-08-18"]

print(ada)

data_list = [value for (key, value) in ada.items()]
day_1 = data_list[0]["4. close"]
#TODO 2. - Get the day before yesterday's closing stock price

data_list1 = [value for (keys, value) in ada.items()]
day_2 = data_list1[1]["4. close"]

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diff = float(day_1) - float(day_2)
up_down = None
if diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
diff_int = int(diff)
day_o = int(float(day_1))
day_t = int(float(day_2))
print(abs(day_o))
print(abs(day_t))
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent = round((day_o - day_t) / day_t * 100.0)


if day_o == day_t:
    print(100.0)
try:
    print(percent)
except ZeroDivisionError:
    print(0)


#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
API_NEWS = "7f990f7f3f324e849f1ad204dccd8aa9"
tesla_params = {
       "q": "Tesla Inc",
       "from": f"{data_list[0]}",
       "apiKey": "7f990f7f3f324e849f1ad204dccd8aa9"
                }


res = requests.get(url="https://newsapi.org/v2/everything?", params=tesla_params)
articles = res.json()["articles"]
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
articles_3 = articles[:3]

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
# if percent <= 5:
print(articles_3)
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

formatted = [f"{STOCK_NAME}: {up_down}{percent}%\n\nHeadline:\n {article['title']}.\n\nBrief:\n {article['description']}" for article in articles_3]
print(formatted)
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
account_sid = "AC5b1b978b0486c34cee2843eca5d5bab3"
auth_token = "a90135de2d6352670c407e5e0574535e"
client = Client(account_sid, auth_token)
for article in formatted:
    message = client.messages \
                    .create(
                         body=article,
                         from_="+14156492104",
                         to="+923403553839"
                     )
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

