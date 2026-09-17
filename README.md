JSON Diff Tool

A web app that compares two JSON objects and shows exactly what changed — additions, removals, and value changes — including nested objects and lists.

Why

Standard diff tools compare files line-by-line as plain text, which gets noisy and unhelpful with structured data like JSON (e.g. reordered keys look like changes even when nothing meaningful changed). This tool understands the actual structure and reports differences in plain language instead.

Features
Compares flat key-value pairs
Recursively compares nested objects
Compares lists (detects added/removed items)
Simple web interface — paste two JSON blobs, click Compare
REST API endpoint (/diff) for programmatic use
Tech stack
Backend: Python, Flask
Frontend: HTML, vanilla JavaScript
Core logic: Custom recursive diffing algorithm (no external diff libraries)
Running it locally
Clone this repo:
   git clone https://github.com/kimiraikonnen-pro/diff-tool-json.git
   cd diff-tool-json
Create and activate a virtual environment:
   python -m venv venv
   venv\Scripts\Activate.ps1
Install dependencies:
   pip install flask
Run the app:
   python app.py
Open your browser to http://127.0.0.1:5000
API usage

Send a POST request to /diff:

POST /diff
Content-Type: application/json

{
  "old": { "timeout": 30 },
  "new": { "timeout": 60 }
}

Response:

{
  "changes": ["changed: 'timeout' from 30 to 60"]
}
Example

Old:

{"server": {"timeout": 30, "retries": 3}, "tags": ["prod", "stable"]}

New:

{"server": {"timeout": 60, "retries": 3}, "tags": ["prod", "stable", "critical"]}

Output:

changed: 'server.timeout' from 30 to 60
added to 'tags': critical