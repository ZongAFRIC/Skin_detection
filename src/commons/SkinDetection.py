import cv2
import os
import numpy as np

class SkinDetection:
    def __init__(self, image, skinModelFile, nonSkinModeFile=None):
        self.skinModel = skinModelFile
        if not nonSkinModeFile is None:
            self.nonSkinModel = nonSkinModeFile
        else:
            self.nonSkinModel = ""
        self.imgMatrix = cv2.imread(image)


    def detectSkin(self):
        x, y, z = self.imgMatrix.shape
        print(" x "+str(x))
        print(" y "+str(y))
        print(" z "+str(z))
        emptyImage = np.zeros((x, y, 3))
        R, G, B = cv2.split(emptyImage)
        Lab = cv2.cvtColor(self.imgMatrix, cv2.COLOR_BGR2Lab)
        l, a, b = cv2.split(Lab)
        count = 0
        for i in range(x):
            for j in range(y):
                ca = a[i][j]
                cb = b[i][j]
                #print("a"+str(ca))
                #print("b" + str(cb))
                fileObject = open(self.skinModel, "r+")
                count = count +1
                #print("parcours "+str(count))
                for line in fileObject.readlines():
                    newline = line.split()
                    #print(newline[0])
                    #print(newline[1])
                    if str(newline[0]) == str(ca) and str(newline[1]) == str(cb):
                        print("match"+str(count))
                        R[i][j] = 255
                        G[i][j] = 255
                        B[i][j] = 255
                fileObject.close()
                if count % 50000 == 0:
                    result = cv2.merge([R, G, B])
                    cv2.imwrite(str(count)+".jpg", result)
        print(" fin detection ")