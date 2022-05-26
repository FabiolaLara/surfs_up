from flask import Flask
app=Flask(__name__) 
Flask=DEVELOP_DIST
@app.route('/')
def hello_world():
    print ('Hello World')
    