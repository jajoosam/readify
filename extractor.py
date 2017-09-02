from newspaper import Article, Config
import nltk
import os.path
config = Config()
config.keep_article_html = True


def extract(url):
    article = Article(url=url, config=config)
    article.download()
    article.parse()
    article.nlp()
    html= "";
    html += "<html><body>"
    html += "<h1>" + article.title + "</h1>"
    html += "<img src='"+ article.top_image +"'>"
    html += "<h2>TL;DR</h2>"
    html += "<p>" + article.summary + "</p>"
    html += '<link rel="stylesheet" href="http://baruffio.com/reading.js/stylesheets/reading.css">'
    html += '<script type="text/javascript" src="http://baruffio.com/reading.js/scripts/reading.min.js"></script>'
    html += "<h2>Article Text</h2>"
    html += article.text
    html += "</body></html>"
    print("html ready")
    return html
