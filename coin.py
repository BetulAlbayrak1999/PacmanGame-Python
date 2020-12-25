from OpenGL.GL import *
from OpenGL.GL import glBegin
from OpenGL.GLUT import *
from array import *
from OpenGL.GLU import *
from PIL import Image

import sys
hight1 = 0
width1 = 0
class Coin :
    def drawcoin(self,X,Y,maze = [[0 for x in range(20)] for y in range(20)] ):
        global hight1, width1
        for i in range(15):
            for n in range(15):
                if 0 == maze[i][n]:
                    glPushMatrix()
                    glColor3f(0.70, 0.54, 0.0)
                    width1 = n + 0.5 + X
                    hight1 = 15 - i - 0.5 + Y
                    glTranslate(width1, hight1, 1)
                    glutSolidSphere(0.1, 20, 20)
                    glPopMatrix()
    def score(self):
        self.total = 0
        return self.total