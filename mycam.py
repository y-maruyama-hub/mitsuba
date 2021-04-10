import cv2

class MyCamera:

    cap=None
    lbt=3

    def __init__(self,camsrv):
        self.cap = cv2.VideoCapture(camsrv)

    def __del__(self):
        self.cap.release()

    def setLbt(self,lbt):
        self.lbt=lbt

    def getframe(self):

        st = time.time()
        frame=None

#bufferを読み飛ばして最新のframeを取得
        while True :

            bt = time.time() - st

            if bt > self.lbt : break

            ret,frametemp = self.cap.read()

            if not ret : break

            frame=frametemp

        return frame
