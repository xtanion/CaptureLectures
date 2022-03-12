import os
from flask import Flask, render_template, request, redirect, url_for

ALLOWED_TYPE = {'mp4', 'mkv', 'webm', 'mov'}
app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def upload_video():
    if request.method=='POST':
        if request.files:
            file = request.files["file"]
            filename = "demo0.mp4"
            
            # TODO check for files type
            file.save(os.path.join(
                '/home/xtanion/Programming/Python/CaptureLectures/web/uploads', filename))
            return render_template('output.html')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)