from flask import Flask, render_template, request
from proccessing import analyse_file

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1  # MB
app.config['UPLOAD_EXTENSIONS'] = ['wav', ]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def receive_file():
    file = request.files['file']

    if file.filename == "":
        return render_template('index.html', user_msg="No file uploaded!")

    if file.filename.split('.')[-1].lower() not in app.config['UPLOAD_EXTENSIONS']:
        return render_template('index.html', user_warn="File uploaded is not valid!")

    file.save('audio.wav')
    analyse_file('audio.wav', file.filename)

    return render_template('report.html')


if __name__ == '__main__':
    app.run()
