from flask import Flask

app = Flask('__name__') #creating an object called app

@app.route('/')
# the function simple would be called on reaching the index directory

def simple():
    return 'Hello World - Sumit'

# for being able to run directly from terminal
if __name__=='__main__':
    app.run(debug=True) # the debug option is for real time code debugging
