from playwright.sync_api import Page, expect

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


def test_get_hello(page, test_web_address):
    page.goto(f"http://{test_web_address}/hello")
    heading_tag = page.locator("h1")
    expect(heading_tag).to_have_text("Hello, World!")


def test_get_goodbye(page, test_web_address):
    page.goto(f"http://{test_web_address}/goodbye")
    heading_tag = page.locator("h1")
    expect(heading_tag).to_have_text("Bye!")