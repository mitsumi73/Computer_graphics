import sys
from OpenGL.GL import *
from OpenGL.GLUT import *


def Display():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor4f(0.0, 1.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex3f(-0.5, -0.5, 0.0)
    glVertex3f(0.5, -0.5, 0.0)
    glVertex3f(0.5, 0.5, 0.0)
    glVertex3f(-0.5, 0.5, 0.0)
    glEnd()
    glFlush()
    glutSwapBuffers()


def main(argc, argv):
    glutInit(argc, argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  # Use GLUT_DOUBLE for double buffering
    glutInitWindowPosition(150, 150)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"No 1")
    glutDisplayFunc(Display)
    glutMainLoop()


if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
