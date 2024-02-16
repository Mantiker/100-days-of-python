import dotenv
import os
import requests
from datetime import date, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

dotenv.load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
STOCK_API_KEY = os.getenv("STOCK_API_KEY")

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.

"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()

stock_data = stock_response.json()["Time Series (Daily)"]

today_date = date.today()
yesterday_date = today_date - timedelta(days=1)
before_yesterday_date = today_date - timedelta(days=2)

yesterday_close_price = float(stock_data[str(yesterday_date)]["4. close"])
before_yesterday_close_price = float(stock_data[str(before_yesterday_date)]["4. close"])

diff_price_perc = round((yesterday_close_price / before_yesterday_close_price - 1) * 100)

if abs(diff_price_perc) > 5:
    ## STEP 2: Use https://newsapi.org/docs/endpoints/everything
    # Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
    #HINT 1: Think about using the Python Slice Operator

    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": STOCK,
        "pageSize": 3,
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()

    articles = news_response.json()["articles"]
    print(f"""
{STOCK}: {diff_price_perc}%
Headline: {articles[0]["title"]} 
Brief: {articles[0]["description"]}
""")


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.

# send mail or send SMS
# as in previous tasks

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

