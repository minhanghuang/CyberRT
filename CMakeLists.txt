cmake_minimum_required(VERSION 3.5)

project(cyber)

set(CMAKE_CXX_STANDARD 11)
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -pthread -latomic -mcx16")

find_package(Threads REQUIRED)
find_package(PkgConfig REQUIRED)

SET(fastcdr_LIBRARIES "/usr/local/lib/libfastcdr.so")
SET(fastrtps_LIBRARIES "/usr/local/lib/libfastrtps.so")
SET(glog_LIBRARIES "/usr/local/lib/libglog.so")
SET(gflags_LIBRARIES "/usr/local/lib/libgflags.so")
SET(Protobuf_LIBRARY "/usr/local/lib/libprotobuf.so") # /opt/protobuf3/bin/protoc -I=. --cpp_out=. *.proto

include_directories(
    /opt/protobuf3/include
    /usr/local/include
    ${CMAKE_CURRENT_SOURCE_DIR}
)

link_directories(
    /opt/protobuf3/lib
    /usr/local/lib
)

add_subdirectory(cyber/proto)
add_subdirectory(cyber/base)
add_subdirectory(cyber/blocker)
add_subdirectory(cyber/class_loader)
add_subdirectory(cyber/common)
add_subdirectory(cyber/component)
add_subdirectory(cyber/event)
add_subdirectory(cyber/croutine)
add_subdirectory(cyber/io)
add_subdirectory(cyber/logger)
add_subdirectory(cyber/message)
add_subdirectory(cyber/node)
add_subdirectory(cyber/transport)
add_subdirectory(cyber/parameter)
add_subdirectory(cyber/record)
add_subdirectory(cyber/scheduler)
add_subdirectory(cyber/sysmo)
add_subdirectory(cyber/time)
add_subdirectory(cyber/service_discovery)
add_subdirectory(cyber/task)
add_subdirectory(cyber/timer)
add_subdirectory(cyber)

# add_subdirectory(cyber/mainboard)
add_subdirectory(cyber/examples)


