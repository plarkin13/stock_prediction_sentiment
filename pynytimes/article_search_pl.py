from datetime import date, datetime
from pynytimes import NYTAPI

#pip install --upgrade pynytimes


# Make sure to set parse dates to True so that the dates
# are parsed into datetime.datetime or datetime.date objects
nyt = NYTAPI(
    key="t8vriKxFjaET2Qo7jSVKTsBYVXSeGw0h",  # Get your API Key at https://developer.nytimes.com
    parse_dates=True,
)

# Search articles about President Biden
#biden = nyt.article_search("stock")

# You can optionally define the dates between which you want the articles to be
biz_sent = nyt.article_search(
    query="stock", 
    results = 5,
    dates={"start": date(2011, 1, 1), "end": date(2013, 12, 31)},
    options = {
        "sort": "oldest",
        "sources": [
            "New York Times",
            "AP",
            "Reuters",
            "International Herald Tribune"
        ],
        "news_desk": [
            "Business"
        ],
        "type_of_material": [
            "News Analysis", "Summary", "Text" ,"News", "List", "Interview", "Article"
        ]
    }
)

biz_sent
# Optionally you can also define
# biden = nyt.article_search(
#     "biden",
# )
