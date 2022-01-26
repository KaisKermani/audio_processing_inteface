from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1  # MB
app.config['UPLOAD_EXTENSIONS'] = ['txt', 'csv']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def receive_file():
    file = request.files['file']

    if file.filename == "":
        return render_template('index.html')

    if file.filename.split('.')[-1].lower() not in app.config['UPLOAD_EXTENSIONS']:
        return render_template('index.html', user_warn="File uploaded is not valid!")

    # TODO: Check if file is readable (correctly formatted)
    # TODO: Check if it's a series (only 1 column)
    try:
        data = pd.read_csv(file.stream, header=None, squeeze=True)
        user_msg = f"File contains {len(data)} values, including {len(data.unique())} unique values."
    except:
        return render_template('index.html', user_warn="File uploaded is not formatted correctly!")

    return render_template('index.html', user_msg=user_msg)


if __name__ == '__main__':
    app.run()
