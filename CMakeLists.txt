cmake_minimum_required(VERSION 3.5)

project(cyber)

set(CMAKE_CXX_STANDARD 11)
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -pthread -latomic -mcx16")
set(TARGET_NAME ${PROJECT_NAME})

enable_language(ASM)

find_package(Threads REQUIRED)
find_package(PkgConfig REQUIRED)
find_package(Poco REQUIRED COMPONENTS Foundation CONFIG)
pkg_check_modules(Protobuf REQUIRED protobuf)
pkg_check_modules(Glog REQUIRED libglog)
pkg_check_modules(Gflags REQUIRED gflags)

SET(fastcdr_LIBRARIES "/opt/cyber/lib/libfastcdr.so")
SET(fastrtps_LIBRARIES "/opt/cyber/lib/libfastrtps.so")
SET(glog_LIBRARIES ${Glog_LIBRARIES})
SET(gflags_LIBRARIES ${Gflags_LIBRARIES})
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

aux_source_directory("cyber/proto/" CYBER_PROTO_SRCS)

add_library(cyber_proto SHARED
  ${CYBER_PROTO_SRCS}
)

target_link_libraries(cyber_proto
  ${Protobuf_LIBRARY}
)

file(GLOB CYBER_SRCS 
	"${PROJECT_SOURCE_DIR}/cyber/base/*.cc"
	"${PROJECT_SOURCE_DIR}/cyber/blocker/*.cc"
	"${PROJECT_SOURCE_DIR}/cyber/class_loader/*.cc"
	"${PROJECT_SOURCE_DIR}/cyber/class_loader/*/*.cc"
	"${PROJECT_SOURCE_DIR}/cyber/common/*.cc" 
	"${PROJECT_SOURCE_DIR}/cyber/component/*.cc"
	"${PROJECT_SOURCE_DIR}/cyber/croutine/*.cc"
	"${PROJECT_SOURCE_DIR}/cyber/croutine/*/*.cc"
	"${PROJECT_SOURCE_DIR}/cyber/croutine/detail/swap_x86_64.S"
	"${PROJECT_SOURCE_DIR}/cyber/data/*.cc"
	"${PROJECT_SOURCE_DIR}/cyber/event/*.cc"
	"${PROJECT_SOURCE_DIR}/cyber/io/*.cc"
	"${PROJECT_SOURCE_DIR}/cyber/logger/*.cc"
	"${PROJECT_SOURCE_DIR}/cyber/message/*.cc"
	"${PROJECT_SOURCE_DIR}/cyber/node/*.cc"
	"${PROJECT_SOURCE_DIR}/cyber/parameter/*.cc"
	"${PROJECT_SOURCE_DIR}/cyber/record/*.cc"
	"${PROJECT_SOURCE_DIR}/cyber/record/*/*.cc"
	"${PROJECT_SOURCE_DIR}/cyber/scheduler/*.cc"
	"${PROJECT_SOURCE_DIR}/cyber/scheduler/*/*.cc"
	"${PROJECT_SOURCE_DIR}/cyber/service/*.cc"
	"${PROJECT_SOURCE_DIR}/cyber/service_discovery/*.cc"
	"${PROJECT_SOURCE_DIR}/cyber/service_discovery/*/*.cc"
	"${PROJECT_SOURCE_DIR}/cyber/task/*.cc" 
	"${PROJECT_SOURCE_DIR}/cyber/time/*.cc"
	"${PROJECT_SOURCE_DIR}/cyber/timer/*.cc"	
	"${PROJECT_SOURCE_DIR}/cyber/transport/*.cc"
	"${PROJECT_SOURCE_DIR}/cyber/transport/*/*.cc"
	"${PROJECT_SOURCE_DIR}/cyber/*.cc"
  	"${PROJECT_SOURCE_DIR}/cyber/sysmo/*.cc"
)

list(FILTER CYBER_SRCS EXCLUDE REGEX .*test[.]cc)

add_library(${TARGET_NAME} SHARED ${CYBER_SRCS})
target_link_libraries(${TARGET_NAME} 
    ${fastrtps_LIBRARIES}
    ${fastcdr_LIBRARIES}
    ${glog_LIBRARIES}
    ${gflags_LIBRARIES}
    ${Protobuf_LIBRARY}
    ${Poco_LIBRARIES}
    cyber_proto 
    atomic
    uuid
)

add_subdirectory(cyber/examples)

file(COPY cyber/conf/
  DESTINATION ${CMAKE_BINARY_DIR}/cyber/conf/
)
