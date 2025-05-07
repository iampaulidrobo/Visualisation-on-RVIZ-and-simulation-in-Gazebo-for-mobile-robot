# Visualisation on RVIZ and simulation in Gazebo for a mobile robot in ROS1
 The package contains a mobile robot with different modules attached with different designs and textures.
 
## (I)URDF
 
   1)model_pauli.URDF-Contains Robot body with different components attached.
   
   2)differential_drive.urdf-Contains Robot body with wheel movement attached for teleop.
   
   3)dd_lidar.urdf-Contains Robot body with Lidar module attached.
   
   4)c_dd_lidar. urdf- Contains Robot body with differential drive and Lidar attached for teleop and scan(SLAM).
   
   5)c_dd_imu.urdf-Contains Robot body with IMU sensor integrated.
   
   6)c_dd_fir.urdf-Contains Robot body with an IR sensor integrated.
   
   7)c_dd_camera.urdf-Contains Robot body with monocular camera integrated.
   
   8)Xacro-
   
       (i)mode_pauli.xacro-Contains Robot body with xacro description for colouring of the component.
       
       (ii)model_pauli_colored. xacro- Defines the range of colours, which are then taken into xacro.
       
       (iii)pauli_plugibs_gazebo. xacro- Contains the plugins for the sensor to be utilised in the Gazebo.
       

       
  ## (II)launch-
  The nomenclature of the launch files is linked to the URDF specified.
  
  ## (III)rviz-
  The nomenclature of the RViz files is linked with the URDF specified.
  
  ## (IV)config-
  Contains the joint configuration of the robot model.
  
  ## (V)Buidding_model-
  Contains a model of the maze in sdf file.
  
  ## (VI)worlds-
  The model file in SDF has ground and sun additions that are imported in the world format.
  
  
       
