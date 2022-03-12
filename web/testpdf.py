import os
from fpdf import FPDF
pdf = FPDF()
# pdf.set_auto_page_break(0)
image_list=os.listdir('web/frame/') 
print(image_list)
    # add new pages with the image 
for img in image_list:
    img = os.path.join('web/frame', img)
    pdf.add_page()
    pdf.image(img)
    # save the output file   
pdf.output("Images.pdf")
print("Adding all your images into a pdf file")