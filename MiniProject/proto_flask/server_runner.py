from datetime import datetime
from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

current_time = datetime.today().strftime("%H-%M-%S")
save_time = str()

def check_out():
    global save_time

    if save_time == "":
        _today = str(int(current_time.replace("-", " ").replace(" ", "")) - 1)
        hour = _today[0:2]
        Minute = _today[2:4]
        seconds = _today[4:6]

        convert = hour + ':' + Minute + ':' + seconds

        save_time = convert
        return save_time

    else:
        _today = str(int(save_time.replace(":", " ").replace(" ", "")) - 1)
        hour = _today[0:2]
        Minute = _today[2:4]
        seconds = _today[4:6]

        convert = hour + ':' + Minute + ':' + seconds

        save_time = convert
        return save_time


@app.route('/')
def hellothipage():
    return 'Hello Visitor'

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/show_info', methods=['POST','GET'])
def show_info():
    print("call it")
    print(request.form['fir_name'])

    return  request.form['fir_name']

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="9090")
