from flask import Flask
import zodiak

app = Flask(__name__)

@app.route("/")
def home():
    return "Halo dari Python di browser"
    zodiak.main()
app.run(debug=True)
