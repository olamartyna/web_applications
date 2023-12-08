1. Design the Route Signature

method: GET
path: /artists
body parameters: name=string

2. Create Examples as Tests

# Request 1:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone



# Request 2:
POST /artists

# With body parameters:
name=Wild nothing
genre=Indie

# Expected response (200 OK)
(No content)

# Then subsequent request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing


3. Test-drive the Route
