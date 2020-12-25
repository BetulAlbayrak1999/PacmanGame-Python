from OpenGL.GL import *
from OpenGL.GL import glBegin
from OpenGL.raw.GLU import gluPerspective
from OpenGL.GLUT import *
from array import *
from OpenGL.GLU import *
from PIL import Image

import sys

mazes = [[0 for x in range(20)] for y in range(20)]



class Readfromoutside :
            def readObj(self,file , number):
                global mazes
                my_file = open(file, "r")
                lines = my_file.readlines()
                i = 0
                for l in lines:
                    splitted_l = l.split(" , ")
                    if splitted_l[0] == 'v':
                        for n in range(1, 16):
                                mazes[i][n - 1] = (int)(splitted_l[n])
                    i += 1
                my_file.close()
                return mazes

            def LoadTexture(self,file1, numrasi):

                image = Image.open(file1)
                ix = image.size[0]
                iy = image.size[1]
                image = image.tobytes("raw", "RGB")

                glBindTexture(GL_TEXTURE_2D, numrasi)
                glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
                glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
                glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
                glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
                glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGB, GL_UNSIGNED_BYTE, image)
                glEnable(GL_TEXTURE_2D)
