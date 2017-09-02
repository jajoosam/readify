from flask import (
    Flask,
    jsonify,
    request,
    redirect
)

from extractor import extract

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return """
    <html> <head> <meta name="description" content="Read web content easily"> <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css"> <link rel="shortcut icon" type="image/x-icon" href="https://cdn.glitch.com/309c5cca-6250-4906-a738-5feca93112a4%2Ffavicon.ico?1503062906990"/> <title>Readify 📖</title> </head> <style>@import url(https://fonts.googleapis.com/css?family=Open+Sans);body{background: #f2f2f2; font-family: 'Open Sans', sans-serif;}.search{width: 100%; position: relative}.searchTerm{float: left; width: 100%; border: 3px solid #00B4CC; padding: 5px; height: 36px; border-radius: 5px; outline: none; color: #9DBFAF;}.searchTerm:focus{color: #00B4CC;}.searchButton{position: absolute; right: -50px; width: 40px; height: 36px; border: 1px solid #00B4CC; background: #00B4CC; text-align: center; color: #fff; border-radius: 5px; cursor: pointer; font-size: 20px;}/*Resize the wrap to see the search bar change!*/.wrap{width: 30%; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);}a{text-decoration: none; color: #2D96FF;}</style> <div class="wrap"> <a href="/about"><h1>Readify 📖</h1></a> <form id="form"> <div class="search"> <input type="text" class="searchTerm" id="lolz" placeholder="Link an article, with protocol (http/s://)"> <button type="submit" class="searchButton" onclick="search()"> <i class="fa fa-check"></i> </button> </div></form> </div><script>document.getElementById("lolz").focus();document.getElementById("form").addEventListener("submit", function(ev){ev.preventDefault(); var button=document.getElementById('lolz'); var location=window.location.href + "article?url=" + lolz.value; console.log(location); window.location.href=location;}); </script></html>
    """

@app.route('/article')
def extract_url():
    url = request.args.get('url', '')
    if not url:
        return jsonify(
            type='error', result='Provide a URL'), 406
    return extract(url)



if __name__ == '__main__':
    app.run(debug=True, port=5000)
