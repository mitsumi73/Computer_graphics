import sys
import math
from OpenGL.GL import *
from OpenGL.GLUT import *


def main(argc, argv):
    glutInit(argc, argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(150, 150)
    glutCreateWindow("AI컴퓨터공학전공 2021115O9(보꾸옥안)".encode("utf-8"))
    glutDisplayFunc(Display)
    glutMainLoop()


def Display():
    glClearColor(0.0, 0.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    glColor4f(1.0, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    for i in range(360):
        angle = i * math.pi / 180.0
        x = 0.2 * math.cos(angle)
        y = 0.2 * math.sin(angle)
        glVertex2f(x, y)
    glEnd()

    glFlush()
    glutSwapBuffers()


if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
