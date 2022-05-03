cmake_minimum_required(VERSION 3.5)

project(common_component_example VERSION 1.0.0)

SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC")
add_library(common_component_example SHARED 
  common_component_example.cc
  ../proto/examples.pb.cc
)

target_link_libraries(common_component_example
    Cyber::init
    Cyber::transmitter
)
