from flask import Flask

app = Flask(__name__)

@app.route("/print_uuid", methods=['GET', 'POST'])
def print_uuid():

    return "printing....."





if __name__ == '__main__':

    app.run(debug=True, port=8000)