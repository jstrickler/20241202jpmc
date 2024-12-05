from flask import Flask, Response

app = Flask(__name__)  # create Flask application object

@app.route('/')  # assign this view function to '/' (i.e., the "root: of the web site)
def index():  # define the view function
    return '<h1>Hello, Flask world!</h1>' # return HTML for the page to display

@app.route('/login')
def login():
    return Response('<h3>Login here...</h3>', status=200, mimetype="text/html")

@app.route('/api/wombat/<int:id>')
def wombat(id):
    return Response("{" + f'"id": "{id}"' +  "}", mimetype="application/json")

# app.register_route(index, '/')

if __name__ == '__main__':
    app.run(debug=True) # start the development server
