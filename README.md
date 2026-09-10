# price tracker
the python project which tracks the price and send to the email that the price is reached the targt and this works only on the http link 

# Price Tracker + Email Alert

A Python script that scrapes a product's price from a website and
sends an automatic email alert if the price drops below a target
value. Built as part of Week 2 (Web Scraping + Automation) of my
2-month bootcamp.

## What it does

1. Scrapes the current price of a product from its webpage
   (BeautifulSoup + Requests)
2. Compares it against a target price you set
3. If the price is below target, sends an email alert automatically
   (smtplib)

## Tech used

- Python
- `requests` — fetch the webpage
- `beautifulsoup4` — parse the HTML and extract the price
- `smtplib` / `email.mime.text` — send the email alert

## Setup

```bash
pip install requests beautifulsoup4
```

You'll also need a **Gmail App Password** (not your regular Gmail
password) to send email:
1. Enable 2-Step Verification on your Google Account
2. Generate an App Password under Security -> App Passwords
3. Use that 16-character password in the script's
   `SENDER_APP_PASSWORD` variable

## Configuration

Edit these values at the top of the script before running:

```python
PRODUCT_URL = "..."          # the product page to track
TARGET_PRICE = 55.00         # alert if price drops below this
SENDER_EMAIL = "..."         # your Gmail address
SENDER_APP_PASSWORD = "..."  # Gmail App Password
RECEIVER_EMAIL = "..."       # where to send the alert
```

## Run it

```bash
python price_tracker.py
```

## Notes

- Tested against `books.toscrape.com` (a scraping practice site).
- Sites like Amazon/Flipkart block simple scrapers like this one —
  for real e-commerce tracking, headers, proxies, or an official
  API would be needed.
- Next step: schedule this script to run automatically (cron /
  Task Scheduler) so it checks the price daily without manual runs.
