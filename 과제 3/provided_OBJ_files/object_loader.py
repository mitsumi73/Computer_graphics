import OpenGL
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import os
import numpy as np


# 3D 모델의 정점을 표현하는 클래스
class Vertex:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


# 다각형(삼각형 또는 사각형)을 표현하는 클래스
TRIANGLE = 0
SQUARE = 1
UNKNOWN = 2


class Face:
    def __init__(self, vertices, type):
        self.vertices = vertices  # 정점 인덱스 리스트
        self.type = type  # 다각형 타입 (삼각형, 사각형, 미지정)


vertices = []  # 정점 리스트
faces = []  # 다각형 리스트


# OBJ 파일을 불러와서 vertices와 faces 리스트를 채우는 함수
def loadOBJ(path):
    global vertices, faces

    with open(path) as f:
        lines = f.readlines()

        for line in lines:
            if line.startswith("v "):
                coords = line.split()[1:]
                v = Vertex(float(coords[0]), float(coords[1]), float(coords[2]))
                vertices.append(v)

            elif line.startswith("f "):
                indices = [int(x) - 1 for x in line.split()[1:]]

                if len(indices) == 3:
                    face_type = TRIANGLE
                elif len(indices) == 4:
                    face_type = SQUARE
                else:
                    face_type = UNKNOWN

                face = Face(indices, face_type)
                faces.append(face)


# 두 벡터의 외적을 계산하는 함수
def crossProduct(a, b):
    result = Vertex(0, 0, 0)
    result.x = a.y * b.z - a.z * b.y
    result.y = a.z * b.x - a.x * b.z
    result.z = a.x * b.y - a.y * b.x
    return result


# 벡터를 정규화하는 함수
def normalize(v):
    length = math.sqrt(v.x ** 2 + v.y ** 2 + v.z ** 2)
    if length != 0:
        v.x /= length
        v.y /= length
        v.z /= length


# OpenGL 초기화 함수
def init():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutCreateWindow("OBJ Loader")

    glEnable(GL_DEPTH_TEST)
    glClearColor(0, 0, 0, 0)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    lightpos = (0, 0, 10, 0)
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)

    glColor3f(0.8, 0.2, 1)
    mat_ambient = (0.7, 0.7, 0.7, 1)
    mat_diffuse = (0.8, 0.8, 0.8, 1)
    mat_specular = (1, 1, 1, 1)
    mat_shininess = (100,)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)


# OpenGL 창 크기 조정 함수
def resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, width / height, 0.1, 100)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


# OpenGL 화면 그리기 함수
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # 카메라 위치 설정
    # gluLookAt(0, -3, 5, 0, 0, 0, 0, 0, 1)  # gourd
    # gluLookAt(3, 3, 3, 0, 0, 0, 0, 0, 1) # icosahedron
    # gluLookAt(8, 15, 8, 0, 4, 0, 0, 1, 0) # lamp
    # gluLookAt(-10, 10, 15, 0, 0, 0, 0, 0, 1) # shuttle
    gluLookAt(3, 3, 3, 0, 0, 0, 0, 0, 1) # violin_case

    for face in faces:
        if face.type == TRIANGLE:
            glBegin(GL_TRIANGLES)

            if len(face.vertices) >= 3:
                v1 = vertices[face.vertices[0]]
                v2 = vertices[face.vertices[1]]
                v3 = vertices[face.vertices[2]]

                vector1 = Vertex(v2.x - v1.x, v2.y - v1.y, v2.z - v1.z)
                vector2 = Vertex(v3.x - v1.x, v3.y - v1.y, v3.z - v1.z)

                normal = crossProduct(vector1, vector2)
                normalize(normal)

                glNormal3f(normal.x, normal.y, normal.z)

            for idx in face.vertices:
                glVertex3f(vertices[idx].x, vertices[idx].y, vertices[idx].z)

            glEnd()

        elif face.type == SQUARE:
            glBegin(GL_QUADS)

            if len(face.vertices) >= 4:
                v1 = vertices[face.vertices[0]]
                v2 = vertices[face.vertices[1]]
                v3 = vertices[face.vertices[2]]
                v4 = vertices[face.vertices[3]]

                vector1 = Vertex(v2.x - v1.x, v2.y - v1.y, v2.z - v1.z)
                vector2 = Vertex(v3.x - v1.x, v3.y - v1.y, v3.z - v1.z)

                normal = crossProduct(vector1, vector2)
                normalize(normal)

                glNormal3f(normal.x, normal.y, normal.z)

            for idx in face.vertices:
                glVertex3f(vertices[idx].x, vertices[idx].y, vertices[idx].z)

            glEnd()

    glutSwapBuffers()


# 메인 함수
def main():
    # obj_file = "./gourd.obj"
    # obj_file = "./icosahedron.obj"
    # obj_file = "./lamp.obj"
    # obj_file = "./shuttle.obj"
    obj_file = "./violin_case.obj"

    loadOBJ(obj_file)

    init()
    glutDisplayFunc(display)
    glutReshapeFunc(resize)
    glutMainLoop()


if __name__ == "__main__":
    main()
