# --TASK--

"""
A text box at http://localhost:8080/input 
which sends the data as POST to any endpoint of your choice. 
This endpoint should log the received the received to stdout.
"""

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField

app = Flask('__name__')
app.config['SECRET_KEY'] = 'secret'

class LoginForm(FlaskForm):
    FName = StringField('First Name')
    LName = StringField('Last Name')
    Age = IntegerField('Age')

@app.route('/form', methods=['POST','GET'])
def form():
    form = LoginForm()
    if form.validate_on_submit():
        return 'Hello {} {}!! You are {} years old!!'. format(form.FName.data,form.LName.data,form.Age.data)
    return render_template('form.html',form = form)

if __name__ == '__main__':
     app.run(debug=True)
