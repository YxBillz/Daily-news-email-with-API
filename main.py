import requests

api_key = "17e8dd133af14e5693d712e3af2e1521"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2024-10-30&sortBy=publishedAt&apiKey="
       "17e8dd133af14e5693d712e3af2e1521")

# Made a request
request = requests.get(url)

# Got a dictionary with data
content = request.json()

# Accessed the articles title and description
for article in content["articles"]:
    print(article["title"])
    print(content["description"])