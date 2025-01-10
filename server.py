#
# Description: Server side code for my web portfolio
# Author: Alexander Powell
# Version: v1.2
# Dependencies: See "requirements.txt" file 
#

# TODO: Add doc comments to all functions
# TODO: Fix the way the data base for the emails works
# TODO: Make email system



from flask import (
    Flask, 
    render_template, 
    request, 
    url_for, 
    redirect
)

from dotenv import load_dotenv, find_dotenv
from src import email_system

import csv
import os


app = Flask(__name__)

load_dotenv(find_dotenv(), override=True)


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/<string:page_name>")
def web_pages(page_name: str):
    return render_template(page_name)


def write_to_csv(data):
    with open(os.environ["DATABASE_PATH"], mode='a', newline="") as database:
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]

        csv_writer.writerow([name,email,subject,message])
        email_system.send_email(data=data)


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou.html")
        except Exception as err:
            print(f"Error: {err}")
            return '<h1 style="text-align: center">Oops... Looks like something went wrong.</h1>'
    return '<h1 style="text-align: center">Oops... Looks like something went wrong, try again.</h1>'
     


if __name__ == "__main__":
    app.run(debug=True, port=5002)
