import requests
from send_email import send_email

api_key = "17e8dd133af14e5693d712e3af2e1521"
url = "https://newsapi.org/v2/top-headlines?country=us&category=business&" \
      "apiKey=17e8dd133af14e5693d712e3af2e1521&" \
      "language=en"

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the articles title and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] is not None and article["url"] is not None:
        body += article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2 * "\n"

body = body.encode("utf-8")

# Pass a subject explicitly
send_email(message=body, subject="Today's news")