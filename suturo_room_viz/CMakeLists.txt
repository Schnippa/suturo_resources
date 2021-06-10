cmake_minimum_required(VERSION 2.8.3)
project(suturo_room_viz)

find_package(catkin REQUIRED COMPONENTS
    rospy
)

catkin_package()

catkin_install_python(PROGRAMS scripts/suturo_room_viz.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

install(DIRECTORY
  launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)