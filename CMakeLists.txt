cmake_minimum_required(VERSION 3.5)

project(cyber)

set(CMAKE_CXX_STANDARD 11)
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -pthread -latomic -mcx16")

find_package(Threads REQUIRED)
find_package(PkgConfig REQUIRED)
pkg_check_modules(Protobuf REQUIRED protobuf)
pkg_check_modules(Glog REQUIRED libglog)
pkg_check_modules(Gflags REQUIRED gflags)

message(${Protobuf_INCLUDE_DIRS})
message(${Protobuf_LIBRARY_DIRS})
message(${Protobuf_LIBRARIES})
message(${Glog_INCLUDE_DIRS})
message(${Glog_LIBRARY_DIRS})
message(${Glog_LIBRARIES})
message(${Gflags_INCLUDE_DIRS})
message(${Gflags_LIBRARY_DIRS})
message(${Gflags_LIBRARIES})



SET(fastcdr_LIBRARIES "/opt/cyber/lib/libfastcdr.so")
SET(fastrtps_LIBRARIES "/opt/cyber/lib/libfastrtps.so")
# SET(glog_LIBRARIES "/usr/local/lib/libglog.so")
SET(glog_LIBRARIES ${Glog_LIBRARIES})
# SET(gflags_LIBRARIES "/usr/local/lib/libgflags.so")
SET(gflags_LIBRARIES ${Gflags_LIBRARIES})
# SET(Protobuf_LIBRARY "/usr/local/lib/libprotobuf.so") # /opt/protobuf3/bin/protoc -I=. --cpp_out=. *.proto
SET(Protobuf_LIBRARY ${Protobuf_LIBRARIES}) # /opt/protobuf3/bin/protoc -I=. --cpp_out=. *.proto

include_directories(
    /opt/cyber/include
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${Protobuf_INCLUDE_DIRS}
    ${Glog_INCLUDE_DIRS}
    ${Gflags_INCLUDE_DIRS}
)

link_directories(
    /opt/cyber/lib
    ${Protobuf_LIBRARY_DIRS}
    ${Glog_LIBRARY_DIRS}
    ${Gflags_LIBRARY_DIRS}
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
add_subdirectory(cyber/mainboard)
add_subdirectory(cyber/py_wrapper)

# add_subdirectory(cyber/mainboard)
add_subdirectory(cyber/examples)

file(COPY cyber/conf/
  DESTINATION ${CMAKE_BINARY_DIR}/cyber/conf/
)
