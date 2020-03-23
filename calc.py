from PIL import Image

'''
This script calculates how many white pixels there are in the given image
Can and was used to calculate percentage of a intersection once.
'''

img = Image.open('original_area.png') # Can be many different formats.
pix = img.load()
size = img.size
# print(size)  # Get the width and hight of the image for iterating over
# print(pix[10,10])  # Get the RGBA Value of the a pixel of an image
# pix[x,y] = value  # Set the RGBA Value of the image (tuple)

'''now calculates the field total area and paints it blue'''

field_area = 0
for row in range(0,size[0]):
    for col in range(0,size[1]):
        pixel = pix[row,col]
        if(pixel[0] > 200 and pixel[1] > 200 and pixel[2] > 200):
            pix[row,col] = (0,0,255)
            field_area += 1
img.save('detected_area.png')  # Save the modified pixels as .png


'''now calculates the area of the intersection paints it blue'''

img = Image.open('original_intersec.png') # Can be many different formats.
pix = img.load()
size = img.size

intersec_area = 0
for row in range(0,size[0]):
    for col in range(0,size[1]):
        pixel = pix[row,col]
        if(pixel[0] > 200 and pixel[1] > 200 and pixel[2] > 200):
            pix[row,col] = (0,0,255)
            intersec_area += 1
img.save('detected_intersec.png')  # Save the modified pixels as .png

print(f'Intersection of {100*intersec_area/field_area}%')
