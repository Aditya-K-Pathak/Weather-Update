import requests
import json

def news():
    template = '''<h2>headline</h2>
        <p>content</p>
        <p>Reference: url</p>'''

    url = ('https://newsapi.org/v2/top-headlines?'
        'country=in&'
        'apiKey=8e5f7b2891284ff393980e4c976b8fad')
    response = requests.get(url)

    response = response.json()

    json_object = json.dumps(response, indent=4)


    data = ""
    with open("new.txt", "w") as file:
        count = 1
        for i in response["articles"]:
            data += f"<h2>{count}. {i['title']}</h2>"+f"<p style = 'color: blue'>Source: {i['url']}<image src = {i['urlToImage']}></image></p><p>{i['description']}</p><br><hr>"
            count += 1

    html = '''<html>
        <body>
        <h1 style: 'text-decoration: underline; text-align: center; color: red'>Daily News Update</h1>
        content
        </body>
    </html>'''

    html = html.replace("content", data)

    return html
