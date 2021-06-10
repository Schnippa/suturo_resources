cmake_minimum_required(VERSION 2.8.3)
project(knowledge_msgs)

find_package(catkin REQUIRED COMPONENTS
  rospy
  suturo_perception_msgs
  geometry_msgs
)

add_message_files(
    FILES
    ObjectState.msg
    ObjectStateArray.msg
)

add_action_files(
  FILES
  StoreObjectInfo.action
)

generate_messages(DEPENDENCIES
  suturo_perception_msgs
  actionlib_msgs std_msgs
  geometry_msgs
)

catkin_package(
  CATKIN_DEPENDS suturo_perception_msgs actionlib_msgs std_msgs geometry_msgs
)


