import datetime
import random
import string
from flask import *

app = Flask("__name__")
random_symbols = ["!@#$%^&*()_+"]


@app.route("/whoami")
def who_am_i():
    browser = request.user_agent.browser
    ip = request.remote_addr
    now_date = datetime.datetime.now()
    return f'Your browser is {browser} , your ip is {ip}    , now date is  {str(now_date)}'


@app.route("/source_code")
def code():
    with open("app.py", "r") as f:
        text = f.read()
        return text


@app.route("/random")
def param():
    length = request.args.get('length')
    digits = request.args.get('digits')
    specials = request.args.get('specials')
    if int(length) <= 0:
        return "enter a length greater than 0"
    if digits == "1":
        if specials == "1":
            return "".join(random.choices(string.ascii_letters + str(random_symbols) + string.digits, k=int(length)))
        return "".join(random.choices(string.ascii_letters + string.digits, k=int(length)))
    elif specials == "1":
        return "".join(random.choices(string.ascii_letters + str(random_symbols), k=int(length)))
    return "".join(random.choices(string.ascii_letters, k=int(length)))


if __name__ == '__main__':
    app.run(debug=True)
