import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"


@app.route('/count_vowels', methods = ['POST'])
def count_vowels():
    text = request.form['text']
    
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in text:
        if letter in vowels:
            count += 1

    return f'There are {count} vowels in "{text}"'


# We separated functions, so one function does one thing, and therefore one test tests one thing
#thisistheway
# SEPARATION OF CONCERNS - between the domain and the infrastructure
# eg in names_encoder if product owner decides we need + separator and not , then it's easy to change in one place

# This is a POST request "sort-names"
# Parameters: list of names
# Return: a sorted list of names
@app.route('/sort-names', methods=['POST'])
def sort_names():           # this if infrastructure level fx
    return names_encoder(sort_names_list(names_decoder(request.form['names'])))   # separated confern of splitting from sorting

def sort_names_list(names_list):    # this if domain level fx
    # make this fx nicer eg with lambda, mapping...
    names_list.sort()
    return names_list

def names_decoder(text):
    names_list = text.split(',')
    names_no_spaces = [name.strip() for name in names_list]
    return names_no_spaces

def names_encoder(names_list):
    return ', '.join(names_list)



# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

