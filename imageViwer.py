import random
import os
import cv2
import sys
directory = str(sys.argv[1])
time = str(sys.argv[2])
files=[]
for dire in os.walk(directory):
    for x in dire[1]:
        for filename in os.listdir(directory+'/'+x):
            files.append(str(directory+'/'+x+'/'+filename))
while True:
    ab = random.choice(files)
    print(ab)
    img = cv2.imread(ab, cv2.IMREAD_ANYCOLOR)
    b = False
    while b == False:
        cv2.imshow(ab, img)
        cv2.waitKey(int(time)*1000)
        cv2.destroyAllWindows()
        b = True
