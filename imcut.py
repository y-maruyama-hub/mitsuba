import math

def cut(frame,dv):

    height, width, channels = frame.shape[:3]

    #un = (int(cap_size[0]/dv),int(cap_size[1]/dv))
    un = (int(width/dv),int(height/dv))

    shw = int(un[0]/2)
    shh = int(un[1]/2)

    dc = int(width/shw) - 1

    iml = []

    for j in range(dc):
        y=j*shh

        imy = []

        for i in range(dc):
            x=i*shw

            expimg=frame[y:y+un[1],x:x+un[0]]
            imy.append(expimg)

            #expimg = cv2.resize(expimg,image_size)
            #f = "{0}/{1}_{2}_{3}.jpg".format(tempcap,name,i,j)
            #ret = cv2.imwrite(f, expimg)
        iml.append(imy)

    return iml

def cut_over(center,size,mx):

    s1 = int(size/2.0)
    s2 = size-s1

    z1=center - s1
    z2=center + s2

    if size >= mx :
        return (0,mx)

    if z1<0 :
        z1=0
        z2=z1+size

    if z2>mx :
        z1=mx-size
        z2=mx

    return (z1,z2)


def adjust_size(area,ratio,cutsize) :

    x=cutsize[0]
    y=cutsize[1]
    xyr = y/x

    while True :
        rectarea = x*y

        if rectarea*ratio > area : break

        x = x + 0.1*x
        y = x*xyr

    x=math.ceil(x)
    y=x*xyr

    return int(x),int(y)


#if __name__ == '__main__':
#
#    x,y=adjust_size(50000,0.8,(200,150))
#    print(x,y)
#
#    res = cut_over(100.0,x,300.0)
#    print(res)
