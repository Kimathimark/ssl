from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulated users with roles
users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "userpass", "role": "user"},
    "mark": {"password": "mark123", "role": "superuser"}
}

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = users.get(username)
        if user and user["password"] == password:
            message = f"✅ Welcome {username}, Role: {user['role']}"
        else:
            message = "❌ Invalid username or password."

    return render_template("login.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
