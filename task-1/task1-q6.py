# --TASK--

"""
Render an HTML page at http://localhost:8080/html 
or an image at http://localhost:8080/image.
"""

from flask import Flask, render_template

app = Flask('__name__')

@app.route('/')
def html():
    return render_template('api-task1-q6.html')

if __name__=='__main__':
    app.run(debug=True)
