from flask import Flask,session,request,Response,url_for,render_template

app=Flask(__name__)

@app.route("/")
def login():
    return render_template("index.html")

@app.route("/submit",methods=["POST"])

def submit():
    username=request.form.get("username")
    password=request.form.get("password")

    # Pair of usernames their Passwords

    valid_users={
        #  Username : Password
         'aditya':'939',
         'pratibha':'630',
         'mohan':'855'
     }
    
    



    if username in valid_users and password==valid_users[username]:
        return render_template("welcome.html",name=username)
    else:
        return "Invalid credentials"


# Running the app
if __name__ == "__main__":
    app.run(debug=True)





