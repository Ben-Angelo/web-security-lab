from flask import Flask, render_template, redirect, url_for, session
from auth import login, logout




app = Flask(__name__)
app.secret_key = "dev-secret-key"  # WILL be abused later

@app.before_request
def debug_session():
    print("Session contents:", dict(session))


@app.route("/", methods=["GET", "POST"])
def login_route():
    return login()

@app.route("/dashboard")
def dashboard():
    if not session.get("authenticated"):
        return redirect(url_for("login_route"))


    return render_template("dashboard.html", user=session["user"])

@app.route("/logout")
def logout_route():
    return logout()

if __name__ == "__main__":
    app.run(debug=True)
