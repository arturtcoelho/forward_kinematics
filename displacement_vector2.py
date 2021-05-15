import numpy as np # Scientific computing library
 
# Project: Displacement Vectors for a 2 DOF Robotic Arm
# Author: Addison Sears-Collins
# Date created: August 10, 2020
    
# Servo (joint) angles in degrees
servo_0_angle = 45 # Joint 1 (Theta 1)
servo_1_angle = 30 # Joint 2 (Theta 2)
servo_2_angle = -30 # Joint 2 (Theta 2)
 
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
 
rot_mat_0_2 = rot_mat_0_1 @ rot_mat_1_2
 
disp_vec_0_1 = np.array([[0],
                         [0],
                         [a1]])
 
disp_vec_1_2 = rot_mat_0_1 @ np.array([[a2 * np.cos(servo_1_angle)],
                                        [a2 * np.sin(servo_1_angle)],
                                        [0]])
 
disp_vec_2_3 = rot_mat_0_2 @ np.array([[a3 * np.cos(servo_2_angle)],
                                        [a3 * np.sin(servo_2_angle)],
                                        [0]])

# Display the displacement vectors
print() # Add a space
print(disp_vec_0_1)
 
print() # Add a space
print(disp_vec_1_2)

print() # Add a space
print(disp_vec_2_3)

print() # Add a space
print(disp_vec_0_1 + disp_vec_1_2 + disp_vec_2_3)