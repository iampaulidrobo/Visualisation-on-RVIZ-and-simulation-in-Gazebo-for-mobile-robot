from launch import LaunchDescription
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node
from launch.substitutions import Command
import os
from ament_index_python.packages import get_package_share_path

def generate_launch_description():
    # Variables
    urdf_path = os.path.join(get_package_share_path('pauli'),
                             'urdf', 'xacro', 'model_pauli.xacro')
    
    config_path = os.path.join(get_package_share_path('pauli'),
                             'rviz2', 'differential_drive.rviz')

    robot_description = ParameterValue(Command(['xacro ', urdf_path]), value_type=str)

    # Creating Nodes
    # Combine joint values
    robot_state_publisher_node = Node(
        package= "robot_state_publisher",
        arguments= ['-d', config_path],
        executable= "robot_state_publisher",
        parameters= [{'robot_description': robot_description}]
    )
    # Control joint values
    joint_state_publisher_gui_node = Node(
        package= "joint_state_publisher_gui",
        executable= "joint_state_publisher_gui"
    )
    # Show in rviz2
    rviz2_node = Node(
        package= "rviz2",
        executable= "rviz2",
        arguments= ['-d', config_path]
    )

    # Launch Nodes
    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz2_node
    ])