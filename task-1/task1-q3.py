# --TASK--

"""
Set a simple cookie (if it has not already been set) at 
http://localhost:8080/setcookie with the following values: 
name=<your-first-name> and age=<your-age>.
"""

from flask import Flask, make_response

app = Flask('__name__')

@app.route('/setcookie')
def setcookie():
    resp = make_response('Setting cookies..')
    resp.set_cookie('FirstName','Sumit')
    resp.set_cookie('Age','20')
    return resp

if __name__=='__main__':
    app.run(debug=True)
