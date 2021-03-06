#simple 2d animation in python

from tkinter import*
import time
WIDTH = 500
HEIGHT = 500
xVelocity = 3  #this will move the canvas image in 1 pixel everytime a coordinate is printed
yVelocity = 2  #you can set any speed and the image speed will vary and the direction too
window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

image1 = PhotoImage(file="space-earth.png")   #paste the name of the file in path, u can copy the image to your pycharm, or paste file path followed by file name!
my_images1 = canvas.create_image(0,0,image=image1)

image = PhotoImage(file="download.png")
my_images = canvas.create_image(0,0,image=image,anchor=NW)


image_width = image.width()
image_height = image.height()
while True:
    coordinates = canvas.coords(my_images)
    #print(coordinates)     #not necessary to print this just for reference
    if(coordinates[0] >WIDTH -image_width or coordinates[0] < 0):  #coordinated[0] that is x coordinate
                                                                   #we determine the width of image and minus it from the width of the window #
                                                                   # or else the image width will move past the window and then bounce back
        xVelocity = xVelocity * -1                                # when graater than 500 ie the width velocity is set to negative of velocity
                                                                  #  hence it will bounce back


    if(coordinates[1] >HEIGHT-image_height or coordinates[1]<0):
        yVelocity= yVelocity*-1
    canvas.move(my_images,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)



window.mainloop()
