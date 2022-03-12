import os
from flask import Flask, render_template, request, redirect, url_for
import cv2
from PIL import Image
from skimage.metrics import structural_similarity
import  threading

ALLOWED_TYPE = {'mp4', 'mkv', 'webm', 'mov'}
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_video():
    if request.method=='POST':
        if request.files:
            file = request.files["file"]
            filename = "demo0.mp4"
            
            # TODO check for files type
            file.save(os.path.join(
                'web/uploads', filename))

            with app.app_context(), app.test_request_context():
                threading.Thread(target=getImages).start()
            # getImages()

            return render_template('output.html')

    return render_template('index.html')

# Using Scikit-Learn to get Image data

def getImages():
    print('Running on thread')
    try:
        path = os.path.join('web/uploads', 'demo0.mp4')
        print("Path found")
    except:
        print('ERROR occured')
    capture = cv2.VideoCapture(path)
    i = 0
    print("captured")
    lag, frame = capture.read()
    img0 = frame
    img0_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    while(capture.isOpened()):
        img0 = frame
        img0_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        flag, frame = capture.read()
        if(flag == False):
            break

        img1_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if (purge_duplicate(img0_bw, img1_bw, 0.65, i) == True):
            path = 'web/frame/'+str(i)+'.jpg'
            print(path)
            cv2.imwrite(path, img0)
            i += 1

    capture.release()
    return render_template('output.html')

def purge_duplicate(img0, img1, threshold, i=0):
    sim, diff = structural_similarity(img0, img1, full=True)
    if(sim < threshold):
        return True
    else:
        return False

if __name__ == '__main__':
    app.run(debug=True)