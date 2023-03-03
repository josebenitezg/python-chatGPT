from flask import Flask, render_template, request
from chatgpt import get_response

app = Flask(__name__)

# Define route for home page
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get user input
        user_input = request.form["user_input"]

        # Generate response
        if user_input:
            response = get_response(user_input)
            return render_template('index.html', user_input=user_input, response=response)
        else:
            return render_template('index.html')
        #response = get_response(user_input)

        return render_template("index.html", user_input=user_input, response=response)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False)
