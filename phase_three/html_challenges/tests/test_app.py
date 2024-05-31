from playwright.sync_api import Page, expect
import random
from flask import render_template, Flask
import pytest
import os

@pytest.fixture
def app_context():     
    current_dir = os.path.dirname(os.path.abspath(__file__))     
    template_dir = os.path.join(current_dir, '..', 'templates')     
    app = Flask(__name__, template_folder=template_dir)     
    with app.app_context():         
        yield


# Tests for your routes go here

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===

# In this test we are coupling the test with implementation - not ideal
def test_get_hello(page, test_web_address):
    page.goto(f"http://{test_web_address}/hello")
    heading_tag = page.locator("h1")
    expect(heading_tag).to_have_text("Hello, World!")


def test_get_goodbye(page, test_web_address):
    page.goto(f"http://{test_web_address}/goodbye")
    heading_tag = page.locator("h1")
    expect(heading_tag).to_have_text("Bye!")


# New endpoint 3.01.24
import re
# testing the backend within backend
def test_weather_endpoint(web_client):
    response = web_client.get('/weather')
    assert response.status_code == 200

def test_bad_endpoint(web_client):
    response = web_client.get('/flibble')
    assert response.status_code == 404

# testing the backend from outside the backend
def test_weather_endpoint_exists(page, test_web_address):
    response = page.goto(f"http://{test_web_address}/weather")
    assert response.status == 200    

# testing the template itself 
def test_weather_template(app_context):
    # rendering template in the context of this test
    html = render_template('weather.html', weather = 'rain')
    message = "Weather: rain"
    # message = "<h2>Weather: rain</h2>"  # This is too much, too particular, because it checks
                                        # in precise tag h2. It is replciating the template
                                        # and that's too tightly coupled.
    assert message in html

# end to end test
def test_weather_end_to_end(page, test_web_address):
    page.goto(f"http://{test_web_address}/weather")
    pattern = re.compile("Weather: [a-zA-Z0-9]")
    heading_tag = page.locator("h2")
    expect(heading_tag).to_have_text(pattern)
