from launch import LaunchDescription
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node
from launch.substitutions import Command
import os
from ament_index_python.packages import get_package_share_path

def generate_launch_description():
    # Variables
    urdf_path = os.path.join(get_package_share_path('pauli'),
                             'urdf', 'dd_lidar.urdf')
    
    config_path = os.path.join(get_package_share_path('pauli'),
                             'rviz2', 'dd_lidar.rviz')

    robot_description = ParameterValue(Command(['xacro ', urdf_path]), value_type=str)

    robot_state_publisher_node = Node(
        package= "robot_state_publisher",
        executable= "robot_state_publisher",
        parameters= [{'robot_description': robot_description}]
    )
    
    joint_state_publisher_node = Node(
        package= "joint_state_publisher",
        executable= "joint_state_publisher"
    )
    
    rviz2_node = Node(
        package= "rviz2",
        executable= "rviz2",
        arguments= ['-d', config_path]
    )
    
    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_node,
        rviz2_node
    ])