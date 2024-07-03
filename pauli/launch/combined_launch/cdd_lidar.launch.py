import os
from ament_index_python.packages import get_package_share_path
from launch import LaunchDescription

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue
from launch.actions import IncludeLaunchDescription
from launch.substitutions import Command

from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    # Variables
    urdf_path = os.path.join(get_package_share_path('pauli'),
                             'urdf', 'c_dd_lidar.urdf')
    config_path = os.path.join(get_package_share_path('pauli'),
                             'rviz2', 'c_dd_lidar.rviz')
    maze_world = os.path.join(get_package_share_path('pauli'),
                             'worlds', 'maze.world')

    robot_description = ParameterValue(Command(['xacro ', urdf_path]), value_type=str)

    # Creating Nodes
    # Combine joint values
    robot_state_publisher_node = Node(
        package= "robot_state_publisher",
        executable= "robot_state_publisher",
        parameters= [{'robot_description': robot_description}]
    )
    # Control joint values
    joint_state_publisher_node = Node(
        package= "joint_state_publisher",
        executable= "joint_state_publisher"
    )
    # Show in rviz2
    rviz2_node = Node(
        package= "rviz2",
        executable= "rviz2",
        arguments= ['-d', config_path]
    )

    launch_gazebo = IncludeLaunchDescription(
                        PythonLaunchDescriptionSource([
                            FindPackageShare("gazebo_ros"), '/launch', '/gazebo.launch.py'
                        ]),
                        launch_arguments={'world': maze_world}.items()
                    )
    spawn_robot = Node(
        package = "gazebo_ros",
        executable= "spawn_entity.py",
        arguments= ['-topic', 'robot_description',
                    '-entity', 'pauli'
            ]
    )

    # Launch Nodes    
    return LaunchDescription([
        launch_gazebo,
        robot_state_publisher_node,
        joint_state_publisher_node,
        spawn_robot,
        rviz2_node
    ])