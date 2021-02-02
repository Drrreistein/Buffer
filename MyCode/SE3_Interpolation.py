#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright (c) RVBUST, Inc - All rights reserved.
# @example UseConstraintTransportTrajectory.py

from RVBUST.RVS import *
from IPython import embed
import numpy as np

rm = RobotModel()
rm.InitFromRVDF(
    "/home/rvbust/Rvbust/RVT_Data/Multibody/RobotModels/FANUC/CRX_10iA_L/CRX_10iA_L.rvdf")

DH_mat = [
    [ 0.        ,  0.        ,  0.71      ,  0.        ,  0.        ,0.        ],
    [ 0.        , -1.57079633,  3.14159265,  1.57079633, -1.57079633, -1.57079633],
    [ 0.245     ,  0.        ,  0.        ,  0.54      ,  0.15      ,0.16      ],
    [ 0.        ,  0.        ,  0.        ,  0.        ,  0.        ,0.        ]]

joints_types = []
for i in range(6):
    joints_types.append(JointType.JointType_Revolute)
DH_type = DHType.DHType_Mdf

rm.SetActiveManipulator("Arm")
manip = rm.GetActiveManipulator()

s_list = manip.ComputeSlist()
rv = RobotVis()
env = Environment()
rv.LoadEnvironment(env)

v1 = [2.6586620807647705, 1.8155426979064941, 2.139530658721924]
v2 = [1.918289303779602, 1.2871607542037964, 1.7240062952041626]
v3 = [-0.33165839314460754, -0.2505359649658203, 0.9095242619514465]
rv.m_viewer.SetCameraPose(v1, v2, v3)
env.AddBody(rm)
rv.ChooseShowMode(rm, 5)

rc = SimController.Create(manip)
rc.Connect()
rc.EnableRobot()

P1 = SE3([0,0,0,0,0,0.5,0.86602])
P2 = SE3([1,1,1,0.5,0,0,0.86602])
se3 = (P2-P1)
rv.PlotFrame(P1)
rv.PlotFrame(P2)

## interpotion
num = 20
list = []
for i in range(num):
     list.append(se3.Coeffs()*i/num)
     Pt = P1 * SE3Tangent(list[i]).Exp()
     time.sleep(0.2)
     rv.PlotFrame(Pt)
embed()