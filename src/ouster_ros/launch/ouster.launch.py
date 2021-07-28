
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    rviz_config_dir = os.path.join(
        get_package_share_directory('ouster_ros'),
        'rviz',
        'ouster.rviz')

    return LaunchDescription([

        Node(
            package='ouster_ros',
            executable='os_node',
            name='os_node',
			),

        Node(
            package='ouster_ros',
            executable='os_cloud_node',
            name='os_cloud_node',
			),

	Node(
            package='rviz2',
            node_executable='rviz2',
            arguments=['-d', rviz_config_dir],
			),
    ])

