from flask import Flask, request, jsonify, render_template
from diff_logic import diff_dicts

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/diff", methods=["POST"])
def diff_endpoint():
    data = request.get_json()

    old = data.get("old")
    new = data.get("new")

    if old is None or new is None:
        return jsonify({"error": "Request must include 'old' and 'new' keys"}), 400

    result = diff_dicts(old, new)

    return jsonify({"changes": result})


if __name__ == "__main__":
    app.run(debug=True, port=5000)