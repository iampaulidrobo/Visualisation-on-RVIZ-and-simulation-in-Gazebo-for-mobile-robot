# Visualisation on RVIZ and simulation in Gazebo for mobile robot in ROS1
 The package contain mobile robot with different module attached with different design and texture added.
 
 (I)URDF
   1)model_pauli.urdf-Contains Robot body with different component attached.
   2)differential_drive.urdf-Contains Robot body with wheel movement attached for teleop.
   3)dd_lidar.urdf-Contains Robot body with Lidar module attached.
   4)c_dd_lidar.urdf-Contains Robot body with differential drive and Lidar attached for teleop and scan(SLAM).
   5)c_dd_imu.urdf-Contains Robot body with IMU sensor integrated.
   6)c_dd_fir.urdf-Contains Robot body with IR sensor integrated.
   7)c_dd_camera.urdf-Contains Robot body with monocular camera integrated.
   8)Xacro-
       (i)mode_pauli.xacro-Contains Robot body with xacro description for coloring of the component.
       (ii)model_pauli_colored.xacro-Defines the range of colors which are then taken into xacro.
       (iii)pauli_plugibs_gazebo.xacro-Contains the plugins for the sensor to be utilised in the gazebo.
       
  (II)Launch-the nomenclature of the launch file are linked with the urdf specified.
  (III)rviz-the nomenclature of the rviz file are linked with the urdf specified.
  (IV)config-Contains the joint configuration of the robot model.
  (V)Buidding_model-Contains model of the maze in sdf file.
  (VI)worlds-The model file in sdf is imported in the world format along with ground and sun addition.
  
  
       
