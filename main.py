import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

product_url = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(product_url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

# Getting the price of the product
product_price = soup.find(name="span", class_="a-offscreen")
product_price = product_price.string.split("$")[1]
print(product_price)

# Sending e-mail if the price is under 150$
product_title = soup.find(id="productTitle").get_text().strip()
print(product_title)

# Strip function example
# txt = "     mango     "
# x = txt.strip()
# print("of all fruits", x, "is my favorite")

buy_price = 150
if product_price < buy_price:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )

