import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
import random

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')


@app.route('/hello', methods=['GET'])
def get_hello():
    return render_template('hello.html', message = 'Hello, World!')

@app.route('/goodbye', methods=['GET'])
def get_bye():
    return render_template('goodbye.html', message = 'Bye!')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

#   GET /greet?name=Kay
@app.route('/greet')
def greet():
    name = request.args.get('name')
    return render_template('greet.html', name=name)


@app.route('/weather', methods=['GET'])
def get_weather():
    return render_template('weather.html', weather = random.randint(0, 1000))

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))


