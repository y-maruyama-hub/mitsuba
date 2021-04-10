import cv2

class MyCamera:

    cap=None
    lastframe=None
    lbt=3

    def __init__(self,camsrv):
        self.cap = cv2.VideoCapture(camsrv)

    def __del__(self):
        self.cap.release()

    def setLbt(self,in)
        self.lbt=in

    def getframe(self):

        st = time.time()
        frame=None

        while True :

            bt = time.time() - st

            if bt > self.lbt : break

            ret,frametemp = self.cap.read()

            if not ret : break

            frame=frametemp

        return frame
