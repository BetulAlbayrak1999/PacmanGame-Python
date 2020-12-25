from OpenGL import GL as gl
from OpenGL import GLUT as glut
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from solid_data import set_color
rangle = 0

class PacMan:
    def drawPacman(self, x, y, z):
        global rangle
        glPushMatrix()
        glColor3f(1, 1, 0.0)
        glTranslatef(x, y, z)
        glutSolidSphere(0.4, 20, 20)
        glRotate(rangle, 1, 1, 0)
        rangle += 0.05

        glPopMatrix()

        # pacman key press
    def key_pressed(self, key, x, y):
            """The function called whenever a key is pressed.
            Note the use of Python tuples to pass in: (key, x, y)

            :param args: string represented pushed key
            """

            if key == b'\033':
                sys.exit()

    def key_pressed_special_up(self, key, x, y):
            """"""
            pass

    def key_pressed_special(self, key, x, y):
            global pacmanRotate
            if key == 100:
                x -= x
                pacmanRotate = 90

            elif key == 102:
                x += x
                pacmanRotate = 270

            elif key == 101:
                y += y
                pacmanRotate = 0

            elif key == 103:
                y -= y
                pacmanRotate = 180
            else:
                pass
            x = round(x, 2)

            glutPostRedisplay()



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

