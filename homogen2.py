import numpy as np # Scientific computing library
 
# Project: Homogeneous Transformation Matrices for a 2 DOF Robotic Arm
# Author: Addison Sears-Collins
# Date created: August 11, 2020
 
# Servo (joint) angles in degrees
servo_0_angle = 45 # Joint 1
servo_1_angle = 30 # Joint 2
servo_2_angle = -30 # Joint 2
 
# Link lengths in centimeters
a1 = 40 # Length of link 1
a2 = 100 # Length of link 2
a3 = 30 # Length of link 3

# Convert servo angles from degrees to radians
servo_0_angle = np.deg2rad(servo_0_angle)
servo_1_angle = np.deg2rad(servo_1_angle)
servo_2_angle = np.deg2rad(servo_2_angle)
 
rot_mat_0_1 = np.array([[np.cos(servo_0_angle), 0, np.sin(servo_0_angle)],
                        [np.sin(servo_0_angle), 0, -np.cos(servo_0_angle)],
                        [0, 1, 0]]) 
 
rot_mat_1_2 = np.array([[np.cos(servo_1_angle), -np.sin(servo_1_angle), 0],
                        [np.sin(servo_1_angle), np.cos(servo_1_angle), 0],
                        [0, 0, 1]]) 

rot_mat_2_3 = np.array([[np.cos(servo_2_angle), -np.sin(servo_2_angle), 0],
                        [np.sin(servo_2_angle), np.cos(servo_2_angle), 0],
                        [0, 0, 1]]) 

# Calculate the rotation matrix that converts the 
# end-effector frame to the servo_0 frame.
rot_mat_0_2 = rot_mat_0_1 @ rot_mat_1_2
rot_mat_0_3 = rot_mat_0_1 @ rot_mat_1_2 @ rot_mat_2_3
 
disp_vec_0_1 = np.array([[0],
                         [0],
                         [a1]])
 
disp_vec_1_2 = np.array([[a2 * np.cos(servo_1_angle)],
                        [a2 * np.sin(servo_1_angle)],
                        [0]])
 
disp_vec_2_3 = np.array([[a3 * np.cos(servo_2_angle)],
                        [a3 * np.sin(servo_2_angle)],
                        [0]])

# Row vector for bottom of homogeneous transformation matrix
extra_row_homgen = np.array([[0, 0, 0, 1]])
initial_pos = np.array([130, 0, 40])
 
# Create the homogeneous transformation matrix from frame 0 to frame 1
homgen_0_1 = np.concatenate((rot_mat_0_1, disp_vec_0_1), axis=1) # side by side
homgen_0_1 = np.concatenate((homgen_0_1, extra_row_homgen), axis=0) # one above the other
 
# Create the homogeneous transformation matrix from frame 1 to frame 2
homgen_1_2 = np.concatenate((rot_mat_1_2, disp_vec_1_2), axis=1)
homgen_1_2 = np.concatenate((homgen_1_2, extra_row_homgen), axis=0)

# Create the homogeneous transformation matrix from frame 1 to frame 2
homgen_2_3 = np.concatenate((rot_mat_2_3, disp_vec_2_3), axis=1)
homgen_2_3 = np.concatenate((homgen_2_3, extra_row_homgen), axis=0)

# Calculate the homogeneous transformation matrix from frame 0 to frame 2
homgen_0_3 = homgen_0_1 @ homgen_1_2 @ homgen_2_3
 
# Display the homogeneous transformation matrix
print(homgen_0_3)

# print()
# print(rot_mat_0_3)

# print()
# print(rot_mat_0_3 @ initial_pos)