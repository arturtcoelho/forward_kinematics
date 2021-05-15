import numpy as np # Scientific computing library
 
# Project: Homogeneous Transformation Matrices for a 2 DOF Robotic Arm
# Author: Addison Sears-Collins
# Date created: August 11, 2020
 
# Servo (joint) angles in degrees
servo_0_angle = 45 # Joint 1
servo_1_angle = 30 # Joint 2
 
# Link lengths in centimeters
a1 = 40 # Length of link 1
a2 = 100 # Length of link 2
a3 = 30 # Length of link 3
a4 = 15 # Length of link 4
 
# Convert servo angles from degrees to radians
servo_0_angle = np.deg2rad(servo_0_angle)
servo_1_angle = np.deg2rad(servo_1_angle)
 
# Define the first rotation matrix.
# This matrix helps convert servo_1 frame to the servo_0 frame.
# There is only rotation around the z axis of servo_0.
rot_mat_0_1 = np.array([[np.cos(servo_0_angle), -np.sin(servo_0_angle), 0],
                        [np.sin(servo_0_angle), np.cos(servo_0_angle), 0],
                        [0, 0, 1]]) 
 
# Define the second rotation matrix.
# This matrix helps convert the 
# end-effector frame to the servo_1 frame.
# There is only rotation around the z axis of servo_1.
rot_mat_1_2 = np.array([[np.cos(servo_1_angle), -np.sin(servo_1_angle), 0],
                        [np.sin(servo_1_angle), np.cos(servo_1_angle), 0],
                        [0, 0, 1]]) 
 
# Calculate the rotation matrix that converts the 
# end-effector frame to the servo_0 frame.
rot_mat_0_2 = rot_mat_0_1 @ rot_mat_1_2
 
# Displacement vector from frame 0 to frame 1. This vector describes
# how frame 1 is displaced relative to frame 0.
disp_vec_0_1 = np.array([[a2 * np.cos(servo_0_angle)],
                         [a2 * np.sin(servo_0_angle)],
                         [a1]])
 
# Displacement vector from frame 1 to frame 2. This vector describes
# how frame 2 is displaced relative to frame 1.
disp_vec_1_2 = np.array([[a4 * np.cos(servo_1_angle)],
                         [a4 * np.sin(servo_1_angle)],
                         [a3]])
  
# Row vector for bottom of homogeneous transformation matrix
extra_row_homgen = np.array([[0, 0, 0, 1]])
initial_pos = np.array([115, 0, 70])
 
# Create the homogeneous transformation matrix from frame 0 to frame 1
homgen_0_1 = np.concatenate((rot_mat_0_1, disp_vec_0_1), axis=1) # side by side
homgen_0_1 = np.concatenate((homgen_0_1, extra_row_homgen), axis=0) # one above the other
 
# Create the homogeneous transformation matrix from frame 1 to frame 2
homgen_1_2 = np.concatenate((rot_mat_1_2, disp_vec_1_2), axis=1)
homgen_1_2 = np.concatenate((homgen_1_2, extra_row_homgen), axis=0)
 
# Calculate the homogeneous transformation matrix from frame 0 to frame 2
homgen_0_2 = homgen_0_1 @ homgen_1_2
 
# Display the homogeneous transformation matrix
print(homgen_0_2)

print()
print(rot_mat_0_2)

print()
print(rot_mat_0_2 @ initial_pos)