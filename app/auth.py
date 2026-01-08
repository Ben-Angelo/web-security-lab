from flask import request, session, redirect, url_for, render_template

# Temporary in-memory user store (INTENTIONALLY SIMPLE for now)
USERS = {
    "admin": "admin123",
    "user": "password"
}

def login():
    error = None

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")


        if username in USERS and USERS[username] == password:
         
         session.clear()

    # Intentionally NOT clearing or regenerating session
         session["authenticated"] = True
         session["user"] = username
         return redirect(url_for("dashboard"))

        else:
            error = "Invalid credentials"

    return render_template("login.html", error=error)


def logout():
    session.pop("user", None)
    return redirect(url_for("login_route"))
