from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL import GL as gl
from pygame import draw

from solid_data import set_color
import sys

radius = 0.5  # yaricapi



class H:
    def __init__(self, x, z):
        self.x = x
        self.z = z
        self.direction = ''
        self.next_direction = ''

        self.radius = 0.5  # yaricapi
        self.rotate = 0
        self.step = 0.1
        self.color = 1, 1, 0
        self.was_eaten = False

    def init(self):
        glClearColor(0.2, 0.0, 0.0, 0.0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(-10.0, 10.0, -10.0, 10.0)
        glMatrixMode(GL_MODELVIEW)

    def drawPacman(self):
        glPushMatrix()
        glColor3f(1, 1, 0.0)
        glTranslatef(self.x, self.z,0)
        glutSolidSphere(0.4, 20, 20)
        glRotate(self.radius, 1, 1, 0)
        self.radius += 0.05
        glPopMatrix()
        glutSwapBuffers()

    def key_pressed(self, *args):
        if args[0] == b'\033':
            sys.exit()
        glutPostRedisplay()

    def key_pressed_special(self, *args):

        if args[0] == 100:
            self.z -= self.step
            self.rotate = 0

        elif args[0] == 102:
            self.z += self.step
            self.rotate = 180

        elif args[0] == 101:
            self.x -= self.step
            self.rotate = 90

        elif args[0] == 103:
            self.x += self.step
            self.rotate = 270

            self.x, self.z = round(self.x, 2), round(self.z, 2)

        glutPostRedisplay()

    def key_pressed_special_up(self,key,x,y):
        pass




def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_DOUBLE)
    glutInitWindowSize(1000, 650)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"PACMAN GAME NEW UPDATE")
    h = H(2, 4)
    glutDisplayFunc(h.drawPacman)
    glutKeyboardFunc(h.key_pressed)
    glutSpecialFunc(h.key_pressed_special)
    glutSpecialUpFunc(h.key_pressed_special_up)
    h.init()
    glutMainLoop()


main()
