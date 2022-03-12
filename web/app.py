#from crypt import methods
import os
import json
from fpdf import FPDF
from flask import Flask, render_template, request, redirect, url_for, jsonify
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

            threading.Thread(target=get_images).start()
            make_pdf()
            return render_template('output.html')

    return render_template('index.html')

# Using Scikit-Learn to get Image data


@app.route('/update_list', methods=['POST'])
def update_list():
    path = os.path.join(os.path.dirname('web/frame'), 'frame')
    list_dir = os.listdir(path)
    # print(list_dir)
    return jsonify(render_template('list_items.html', x=list_dir))


def make_pdf():

    pdf = FPDF()
    pdf.set_auto_page_break(0)
    image_list=os.listdir('web/frame') 
    print(image_list)
    # add new pages with the image 
    for img in image_list:
        img = os.path.join('web/frame', img)
        pdf.add_page()
        pdf.image(img)
    # save the output file   
    pdf.output("web/pdf-file/Images.pdf")
    print("Adding all your images into a pdf file")

def get_images():
    print('Running on thread')
    try:
        path = os.path.join('web/uploads', 'demo0.mp4')
        print("Path found")
    except:
        print('ERROR occured')
    
    image_dir = os.listdir('web/frame')
    if(len(image_dir)>0):
        for items in image_dir:
            r = os.path.join('web/frame', items)
            os.remove(r)

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
    make_pdf()
    capture.release()
    # with app.app_context(), app.test_request_context():
    #     print("Got App Context")
    #     return "go Away emo kid!!"

def purge_duplicate(img0, img1, threshold, i=0):
    sim, diff = structural_similarity(img0, img1, full=True)
    if(sim < threshold):
        return True
    else:
        return False

if __name__ == '__main__':
    app.run(debug=True)