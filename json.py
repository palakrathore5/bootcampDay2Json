var jsonObject = [{

        "FirstName": "Code",
        "Lastname": "Handbook"
    }, {
        "FirstName": "Ravi",
        "Lastname": "Shanker"
    }, {
        "FirstName": "Salman",
        "Lastname": "Khan"
    }, {
        "FirstName": "Ali",
        "Lastname": "Zafar"
    }

];

from flask import Flask
app = Flask(__name__)

@app.route("/getEmployeeList")
def getEmployeeList():
    return "Return Employee JSON data"

if __name__ == "__main__":
    app.run()