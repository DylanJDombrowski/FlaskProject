from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

# Create Flask app instance
app = Flask(__name__)

# Set secret key for app
app.secret_key = "key"

# Set session lifetime to 5 minutes
app.permanent_session_lifetime = timedelta(minutes=5)

# Home route, rendered with index.html template
@app.route("/")
def home():
    return render_template("index.html")

# Login route, accepts both GET and POST requests
@app.route("/login", methods=["POST", "GET"])
def login():
    # If request method is POST, set session to permanent and set user variable to form input
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash("Login Successful!")
        # Redirect user to /user route
        return redirect(url_for("user"))
    # If request method is GET and user is in session, redirect to /user route
    elif "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))
    # Otherwise, render login.html template
    else:
        flash("You're Not Logged In!")
        return render_template("login.html")

# User route, displays user name if in session
@app.route("/user")
def user():
    # If user is in session, display user name
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    # If user not in session, redirect to /login route
    else:
        return redirect(url_for("login"))

# Logout route, removes user from session
@app.route("/logout")
def logout():
    # Remove user from session
    session.pop("user", None)
    # Flash logout message to user
    if "user" in session:
        user = session["user"]
        flash("You have been logged out, {user}", "info")
    # Redirect to /login route
    return redirect(url_for("login"))
    
# Run app if file is executed directly
if __name__ == "__main__":
    app.run(debug=True)
