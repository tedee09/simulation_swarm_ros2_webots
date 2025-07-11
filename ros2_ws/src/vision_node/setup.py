from setuptools import find_packages, setup

package_name = 'vision_node'

setup(
    name=package_name,
    version='0.0.0',
    packages=['vision_node'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/camera', ['resource/camera/default.ros2']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tedee',
    maintainer_email='septedy44@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'vision_node = vision_node.vision_node:main',
        ],
    },
)