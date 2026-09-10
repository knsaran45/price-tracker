import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

PRODUCT_URL = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
TARGET_PRICE = 55.00

SENDER_EMAIL = "sender mail@gmail.com"
SENDER_APP_PASSWORD = "apppassword"
RECEIVER_EMAIL = "recivermail@gmail.com"


# -----------------------------------------------------
# STEP 1: Scrape the current price
# -----------------------------------------------------
def get_price():
    response = requests.get(PRODUCT_URL)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")

    # On this site, price is inside: <p class="price_color">£51.77</p>
    price_text = soup.find("p", class_="price_color").text
    price_value = float(price_text.replace("£", ""))

    title = soup.find("h1").text 

    return title, price_value

def send_email_alert(title, price):
    subject = f"Price Drop Alert: {title}"
    body = f"Good news! '{title}' is now £{price}, which is below your target of £{TARGET_PRICE}."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL


    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_APP_PASSWORD)
        server.send_message(msg)

    print("Email alert sent!")


def main():
    title, current_price = get_price()
    print(f"Product: {title}")
    print(f"Current price: £{current_price}")
    print(f"Target price: £{TARGET_PRICE}")

    if current_price < TARGET_PRICE:
        print("Price is below target! Sending alert...")
        send_email_alert(title, current_price)
    else:
        print("Price is still above target. No alert sent.")


if __name__ == "__main__":
    main()