from flask import Flask,session,request,Response,url_for,render_template

app=Flask(__name__)

@app.route("/")
def login():
    return render_template("index.html")

@app.route("/submit",methods=["POST"])

def submit():
    username=request.form.get("username")
    password=request.form.get("password")

    if username=="aditya" and password=="321":
        return render_template("welcome.html",name=username)
    else:
        return "Invalid credentials"



# Running the app
if __name__ == "__main__":
    app.run(debug=True)





