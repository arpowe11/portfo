from flask import (
    Flask, 
    render_template, 
    request, 
    url_for, 
    redirect
)

import csv

DATABASE_PATH: str = "./database.txt"
DATABASE2_PATH: str = "./database.csv"

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/<string:page_name>")
def web_pages(page_name: str):
    return render_template(page_name)


def write_to_file(data):
    with open(DATABASE_PATH, mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
    with open(DATABASE2_PATH, mode='a', newline="") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou.html")
        except:
            return "Did not save to the database"
    return "something went wrong, try again"
     


if __name__ == "__main__":
    app.run(debug=True, port=5000)
