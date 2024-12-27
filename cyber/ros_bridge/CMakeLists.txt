project(ros_bridge VERSION 10.0.0)

find_package(PROJ REQUIRED)

include_directories(
  ${PROJ_INCLUDE_DIRS}
)

link_directories(
  ${PROJ_LIBRARY_DIRS}
)

file(GLOB_RECURSE ROS_BRIDGE_SOURCES
  "${CMAKE_CURRENT_SOURCE_DIR}/*.cc"
)

add_executable(ros_bridge
  ${ROS_BRIDGE_SOURCES}
)

target_link_libraries(ros_bridge
    ${TARGET_NAME}
    ${PROJ_LIBRARIES}
    ${GperfTools_LIBRARIES}
    profiler
    pthread
)

set_target_properties(ros_bridge PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin/cyber/ros_bridge
)
