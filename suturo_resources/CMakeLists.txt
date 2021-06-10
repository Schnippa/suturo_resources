cmake_minimum_required(VERSION 2.8.3)
project(suturo_resources)

find_package(catkin REQUIRED COMPONENTS

)

catkin_package()

install(DIRECTORY
  gazebo_models
  gazebo_worlds
  maps
  rviz_configs
  urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

catkin_install_python(PROGRAMS nodes/base_scan_opening_limiter.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})