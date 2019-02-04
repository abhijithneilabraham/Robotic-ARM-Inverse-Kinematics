#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 13:56:37 2019

@author: abhijithneilabraham
"""
'''
FORWARD KINEMATICS FIRST
'''
import tinyik
arm = tinyik.Actuator(['z', [1., 0., 0.], 'x', [0., 0., 2.],'x',[0.,0.,1.]])
print('when joint angles are zero by default,angles=',arm.angles)
print('end effector position=',arm.ee)
import numpy as np
arm.angles=[np.pi/6,np.pi/3,np.pi/4]#pi is 180 in degrees,so this line gives us 30 and 60 and 45 degree angles
print('after updating angles',arm.ee)
'''
NOW ,INVERSE KINEMATICS
I am trying to reverse the same end effector position to find the original 3 angles to prove this works
'''
arm.ee=[2.21501372,-1.8365163,0.74118095]
print('The angles from inverse kinematics of 3 joint are',np.round(np.rad2deg(arm.angles)))