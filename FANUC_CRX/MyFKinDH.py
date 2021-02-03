from RVBUST.RVS import *
from IPython import embed
import numpy as np

def DHToSE3Mat(dh):
    ## TODO
    a = dh[0]
    af = dh[1]
    d = dh[2]
    th = dh[3]
    mat = np.array([[np.cos(th),             -np.sin(th),             0,              a],
                    [np.sin(th)*np.cos(af),    np.cos(th)*np.cos(af), -np.sin(af),  -d*np.sin(af)],
                    [np.sin(th)*np.sin(af),    np.cos(th)*np.sin(af),  np.cos(af),  d*np.cos(af)],
                    [0,             0,                     0,                         1]])
    # print(mat)
    return mat

def main():
    #       | a |        alpha          | d         | theta |
    DH_mat = [[ 0.        ,  0.        ,  0.245     ,  0.        ],
            [ 0.        , -1.57079633,  0.        ,  -1.57079633],
            [ 0.71      ,  3.14159265,  0.        ,  3.14159265],
            [ 0.        ,  1.57079633, -0.54      ,  0.        ],
            [ 0.        , -1.57079633,  0.15      ,  0.        ],
            [ 0.        , -1.57079633,  0.16      ,  3.14159265]]
    T = SE3ToTransform([0,0,0,0,0,0,1])

    q = np.zeros(len(DH_mat))
    q = np.array([np.pi/2,np.pi,0,0,0,np.pi])
    # q = np.array([0,0,np.pi/3,np.pi/4,0,np.pi])
    for i in range(len(DH_mat)):
        dh = DH_mat[i]
        dh[3] = dh[3]+q[i]
        T = T @ DHToSE3Mat(dh)

    print(T)

if __name__=="__main__":
    main()
