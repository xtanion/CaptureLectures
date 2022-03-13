
# CaptureLectures

It is a web application, with a flask backend, to capture video lectures and convert them to pdf which helps in saving precious time of students. It uses machine learning along with various libraries.



## Overview
- To build this project
- Run command : git clone https://github.com/xtanion/CaptureLectures or git clone https://github.com/aryanasura/CaptureLectures

## Getting started
After uploading the video on the website(index.html), app.py file is supposed to run which takes this video and gives the output in the form of pdf in the folder 'pdf-file'. The website output.html should work properly after integration.
## Libraries used
- [OpenCV](https://opencv.org) - OpenCV is a huge open-source library for computer vision, machine learning, and image processing
- [numpy](https://numpy.org) - The fundamental package for scientific computing with Python.
- os - The OS module in Python provides functions for interacting with the operating system.
- json - Used to work with json data
- threading - Used to distribute workload between CPU's threads. 
- [fpdf](https://pypi.org/project/fpdf/) - Allows us to convert data to pdf format.
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Web application framework.
- [PIL](https://pypi.org/project/Pillow/) - The Python Imaging Library(PIL) adds image processing capabilities to your Python interpreter
- skrimage.metrics - Used to measure image similarity.

## Documentation

- capture_frame.py file compares consecutive frames of video, compares pixel between the two and decides if the pictures are similar or not depending upon the threshold limit passed in purge_duplicate function.
- frame folder holds the final frames which gets converted in a pdf. After finishing the process, it deletes the frames.
- pdf-file folder holds the final pdf
- app.py file takes the video input, uses openCV to remove similar images from each frame that has been captured. It also converts images to pdf, has multithreading to make the aplication faster.
- index.html is a web page that helps in taking .mp4 format videos that is processed in flask backend. 
- output.html is a web page that when completed will give option to download pdf and download slides as images.



## Problems
Due to time constraints, we missed out on improving the following features-
- Deployement of web application 
- We are unable to show the pdf output on main html page due to problems with chrome, however that pdf is saved in the 'pdf-file' folder

## Missed out
Due to time constraints, we missed out on executing the following features-
- ML model could have been developed further
- Option for user to select required frames from the output frames before forming the pdf
## Authors

- Shivam Sahu 
- Aryan Khanuja
- Aaryan Gupta
- Akshat Jain

