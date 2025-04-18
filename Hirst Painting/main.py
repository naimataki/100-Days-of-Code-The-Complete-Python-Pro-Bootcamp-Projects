from turtle import Turtle, Screen, colormode
from random import choice

colormode(255)
color_list = [(190, 172, 0), (208, 0, 103), (0, 148, 60), (253, 69, 0), (217, 229, 234), (167, 0, 0), (0, 128, 205), (89, 0, 95), (254, 223, 0), (232, 234, 232), (42, 192, 234), (0, 0, 0), (248, 19, 152), (253, 7, 4), (235, 11, 143), (253, 4, 6), (15, 190, 234), (236, 153, 69), (250, 51, 17), (238, 215, 82), (16, 167, 127), (224, 126, 168), (234, 163, 190), (114, 193, 156), (160, 210, 177), (142, 209, 228), (239, 170, 157), (106, 120, 184)]

tim = Turtle()
tim.speed(0)

tim.color(choice(color_list))
tim.dot(20)
tim.setpos(50); tim.dot(20); tim.setpos(50)



screen = Screen()
screen.exitonclick()

#import colorgram as cg

#colors_raw = cg.extract('Hirst Painting/painting.jpg', -1)

#print(colors)

#first_color = colors_raw[0]
#rgb = first_color.rgb
#print(rgb)

#colors = []
#for color in colors_raw:
#    r = color.rgb[0]
#    g = color.rgb[1]
#    b = color.rgb[2]
#    colors.append((r, g, b))
#
#print(colors)

#print(len(colors))

#import os  
#print("Current working directory:", os.getcwd()) 