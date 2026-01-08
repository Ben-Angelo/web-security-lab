from flask import render_template, request, session, redirect, url_for

def profile():
    if not session.get("authenticated"):
        return redirect(url_for("login_route"))
    
    allowed_themes = ["light", "dark"]
    theme = request.args.get("theme", "light").lower()
    
    if theme not in allowed_themes:
        theme = "light"

    return render_template("profile.html", theme=theme)
