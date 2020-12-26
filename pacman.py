from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import solid_data
rangle = 0


class PacMan:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.direction = ''
        self.next_direction = ''
        self.radius = 0.5
        self.rotate = 0
        self.step = 0.1
        self.color = 1, 1, 0
        self.was_eaten = False

    def drawPacman(self):
        global rangle
        glPushMatrix()
        glColor3f(1, 1, 0.0)
        glTranslatef(self.x, self.y, self.z)  # drawPacman(self,x,y,z) elemen veremeyiz yanlış olur ok?
        glutSolidSphere(0.4, 20, 20)
        glRotate(rangle, 1, 1, 0)
        rangle += 0.05

        glPopMatrix()


    def move(self):

        if self.direction == 'N':
            self.z -= self.step
            self.rotate = 0

        elif self.direction == 'S':
            self.z += self.step
            self.rotate = 180

        elif self.direction == 'W':
            self.x -= self.step
            self.rotate = 90

        elif self.direction == 'E':
            self.x += self.step
            self.rotate = 270

        self.x, self.z = round(self.x, 2), round(self.z, 2)


    # gl.glBegin(gl.GL_TRIANGLE_FAN)
    # gl.glColor3f(0, 1, 0)
    # gl.glVertex2f(self.pos_x, self.pos_z)
    # for i in range(13):  # Rysujemy okrag z odcietym malym kawalkiem
    # Obrocony o podany offset.
    #     # i = i + DisplayFunc.dolna + DisplayFunc.off
    #     x = self.pos_x + 0.3 * sin(2 * pi * i / 24.0)
    #     y = self.pos_z + 0.3 * cos(2 * pi * i / 24.0)
    #     gl.glVertex2f(x, y)
    #     gl.glEnd()
