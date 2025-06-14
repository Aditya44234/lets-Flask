# Importing all required modules

from flask import Flask, request, redirect, Response, url_for, session,render_template

# Creating the Flask app
app = Flask(__name__)

# Setting a secret key for session management
app.secret_key = "123"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "aditya" and password == "123":
            session["user"] = username  # Store in session
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid credentials", mimetype="text/plain")

    return  render_template('index.html')


@app.route("/welcome")
def welcome():
    if "user" in session:
        # If user is logged in, display a welcome message
        # and a logout link
        return f'''
        <h2>Welcome, {session["user"]}!</h2>
        <a href="{url_for("logout")}">Logout</a>
        '''
    
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

# Running the app
if __name__ == "__main__":
    app.run(debug=True)




