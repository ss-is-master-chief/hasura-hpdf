# --TASK--

"""
Add a route, for e.g. http://localhost:8080/authors, which:
Respond with only a list of authors 
and the count of their posts (a newline for each author).
"""

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/api')
def api():
    res_1 = requests.get('https://jsonplaceholder.typicode.com/users')
    res_2 = requests.get('https://jsonplaceholder.typicode.com/posts')
    array = []
    i = 0
    try:
        data_1 = res_1.json()
        data_2 = res_2.json()
    except KeyError:
        data_1 = None
        data_2 = None
    
                
    return render_template('api-task1-q2-p3.html',data_1=data_1,data_2=data_2)

if (__name__)== '__main__':
    app.run(debug=True)
