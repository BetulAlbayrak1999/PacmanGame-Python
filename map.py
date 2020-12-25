from OpenGL.GL import *
from OpenGL.GL import glBegin
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image
import sys
hight = 0
width = 0
class Map :
        def drawmaze(self ,X, Y, maze=[[0 for x in range(20)] for y in range(20)]):
            global hight, width
            for i in range(15):
                for n in range(15):
                    if 1 == maze[i][n]:
                        glPushMatrix()
                        hight = 15 - i + Y
                        width = n + 1 + X
                        glBindTexture(GL_TEXTURE_2D, 1)
                        glBegin(GL_QUADS)
                        glColor3f(1, 1, 1)
                        glTexCoord2f(0, 1)
                        glVertex3f(width - 1, hight, 1)
                        glTexCoord2f(0, 0)
                        glVertex3f(width, hight, 1)
                        glTexCoord2f(1, 0)
                        glVertex3f(width, hight - 1, 1)
                        glTexCoord2f(1, 1)
                        glVertex3f(width - 1, hight - 1, 1)

                        glColor3f(1, 1, 1)
                        glTexCoord2f(0, 1)
                        glVertex3f(width - 1, hight, 1)
                        glTexCoord2f(0, 0)
                        glVertex3f(width, hight, 1)
                        glTexCoord2f(1, 0)
                        glVertex3f(width, hight, 0)
                        glTexCoord2f(1, 1)
                        glVertex3f(width - 1, hight, 0)

                        glColor3f(1, 1, 1)
                        glTexCoord2f(0, 1)
                        glVertex3f(width, hight, 1)
                        glTexCoord2f(0, 0)
                        glVertex3f(width, hight - 1, 1)
                        glTexCoord2f(1, 0)
                        glVertex3f(width, hight - 1, 0)
                        glTexCoord2f(1, 1)
                        glVertex3f(width, hight, 0)

                        glColor3f(1, 1, 1)
                        glTexCoord2f(0, 1)
                        glVertex3f(width, hight - 1, 1)
                        glTexCoord2f(0, 0)
                        glVertex3f(width - 1, hight - 1, 1)
                        glTexCoord2f(1, 0)
                        glVertex3f(width - 1, hight - 1, 0)
                        glTexCoord2f(1, 1)
                        glVertex3f(width, hight - 1, 0)

                        glColor3f(1, 1, 1)
                        glTexCoord2f(0, 1)
                        glVertex3f(width - 1, hight - 1, 1)
                        glTexCoord2f(0, 0)
                        glVertex3f(width - 1, hight, 1)
                        glTexCoord2f(1, 0)
                        glVertex3f(width - 1, hight, 0)
                        glTexCoord2f(1, 1)
                        glVertex3f(width - 1, hight - 1, 0)

                        glColor3f(1, 1, 1)
                        glTexCoord2f(0, 1)
                        glVertex3f(width - 1, hight, 0)
                        glTexCoord2f(0, 0)
                        glVertex3f(width, hight, 0)
                        glTexCoord2f(1, 0)
                        glVertex3f(width, hight - 1, 0)
                        glTexCoord2f(1, 1)
                        glVertex3f(width - 1, hight - 1, 0)
                        glEnd()
                        glPopMatrix()
                    if 0 == maze[i][n]:
                        glPushMatrix()
                        hight = 15 - i + Y
                        width = n + 1 + X
                        glBindTexture(GL_TEXTURE_2D, 2)
                        glBegin(GL_QUADS)
                        glColor3f(1, 1, 1)
                        glTexCoord2f(0, 1)
                        glVertex3f(width - 1, hight, 0)
                        glTexCoord2f(0, 0)
                        glVertex3f(width, hight, 0)
                        glTexCoord2f(1, 0)
                        glVertex3f(width, hight - 1, 0)
                        glTexCoord2f(1, 1)
                        glVertex3f(width - 1, hight - 1, 0)
                        glEnd()
                        glPopMatrix()