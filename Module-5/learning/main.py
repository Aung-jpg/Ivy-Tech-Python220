from flask import Flask, request, jsonify

app = Flask(__name__)

# creating route
@app.route("/")
def home():
    return "Home"

# GET get data
# POST create data
# PUT update data
# DELETE remove data

# path parameter <value> is a dynamic value
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Aung Aung"
    }
    # query parameter
    # http://127.0.0.1:5000/get-user/1000?extra=hello&bruh=nope
    extra = request.args.get("extra")
    bruh = request.args.get("bruh")
    if extra:
        user_data["extra"] = extra
    if bruh:
        user_data["bruh"] = bruh
    
    return jsonify(user_data), 200

@app.route("/create-user", methods=['POST'])
def create_user():
    if request.method == "POST":
        data = request.get_json()

        # do something with data like add to database

        return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)