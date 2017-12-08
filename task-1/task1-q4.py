# --TASK--

"""
Fetch the set cookie with 
http://localhost:8080/getcookies and display the stored 
key-values in it.
"""

from flask import Flask, make_response, request

app = Flask('__name__')

@app.route('/setcookie')
def setcookie():
    resp = make_response('Setting cookies..')
    resp.set_cookie('FirstName','Sumit')
    resp.set_cookie('Age','20')
    return resp

@app.route('/getcookie')
def getcookie():
    FirstName = request.cookies.get('FirstName')
    Age = request.cookies.get('Age')
    return 'Hello ' + FirstName + ' you are ' + Age + ' years old.'

if __name__=='__main__':
    app.run(debug=True)
