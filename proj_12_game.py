"""Author: Keyhan Kouhkiloui Babarahmati
           PhD in Robotics and AI
"""

import turtle as tr
import random as r

turtle_obj_1 = tr.Turtle()
turtle_obj_1.shape("turtle")

color_list = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

angle_list = [0, 90, -90, -180]
motion_list = [0, -25, 25]

for i in range (0, 500):
    motion_rand = r.choice(motion_list)
    angle_rand = r.choice(angle_list)
    color_rand = r.choice(color_list)
    turtle_obj_1.pensize(3)

    turtle_obj_1.forward(motion_rand)
    turtle_obj_1.right(angle_rand)
    turtle_obj_1.backward(motion_rand)
    turtle_obj_1.left(angle_rand)
    turtle_obj_1.color(color_rand)

# Keep it at the end of the code
screen = tr.Screen()
screen.exitonclick()

