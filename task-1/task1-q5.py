# --TASK--

"""
Deny requests to your http://localhost:8080/robots.txt page. 
(or you can use the response at http://httpbin.org/deny if needed)
"""

from flask import Flask, abort
app = Flask(__name__)

@app.route('/robots.txt')
def deny():
    abort(401)
    this_is_never_executed()

if __name__=='__main__':
    app.run(debug=True)    
