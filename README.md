# Quotes Bot

## About
Quotes bot is a [Telegram Bot](https:/t.me/Quotes13Bot) and a [Webpage](https://quotes13.herokuapp.com/) for getting popular quotes from books. It is hosted on Heroku and quotes are from GoodReads.

## Screenshots:
- [Home page](https://i.imgur.com/shNEbfq.png)
- [Quote page](https://i.imgur.com/gTRaqbW.png)


## Setup
- Clone this repo to your computer using ```git clone git@github.com:Sachin-dot-py/QuotesBot.git```
- Create a credentials.py file:
```
TOKEN = '<YOUR_TELEGRAM_TOKEN>'
URL = '<YOUR_WEBHOOK_URL>'
```
- Navigate into the directory using ```cd QuotesBot```
- Install the requirements using ```pip3 install -r requirements.txt ```
- Start your app using ```gunicorn app:app```