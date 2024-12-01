import requests
from send_email import send_email

topic = "tesla"

api_key = "17e8dd133af14e5693d712e3af2e1521"
url = "https://newsapi.org/v2/everything?" \
       f"q={topic}&" \
       "from=2024-11-01&" \
       "sortBy=publishedAt&" \
       "apiKey=17e8dd133af14e5693d712e3af2e1521&" \
       "language=en"

# Made a request
request = requests.get(url)

# Got a dictionary with data
content = request.json()

# Accessed the articles title and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" \
               + "\n" + body + article["title"] + "\n" \
               + article["description"] \
               + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)