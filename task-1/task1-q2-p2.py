# --TASK--

"""
Add a route, for e.g. http://localhost:8080/authors, which:
fetches a list of posts 
from a request to https://jsonplaceholder.typicode.com/posts
"""

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/api')
def api():
    res = requests.get('https://jsonplaceholder.typicode.com/posts')
    try:
        data = res.json()
    except KeyError:
        data = None
    return render_template('api-task1-q2-p2.html', data=data)

if (__name__)== '__main__':
    app.run(debug=True)
