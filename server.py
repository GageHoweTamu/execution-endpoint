from flask import Flask, request
import io, sys

app = Flask(__name__)

@app.route('/', methods=['POST'])
def execute_file():
    file_content = request.form['file']
    old_stdout, sys.stdout = sys.stdout, io.StringIO()
    try:
        exec(file_content)
        output = sys.stdout.getvalue()
    except Exception as e:
        output = str(e)
    finally:
        sys.stdout = old_stdout
    return output

if __name__ == '__main__':
    app.run(port=8000)
