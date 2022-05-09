cmake_minimum_required(VERSION 3.5.1)

project(cyber)

set(CMAKE_CXX_STANDARD 14)
set(TARGET_NAME ${PROJECT_NAME})

enable_language(ASM)

find_package(Threads REQUIRED)
find_package(PkgConfig REQUIRED)
find_package(fastrtps REQUIRED)
find_package(fastcdr REQUIRED)
find_package(Poco REQUIRED COMPONENTS Foundation)
pkg_check_modules(Protobuf REQUIRED protobuf)
pkg_check_modules(Glog REQUIRED libglog)
pkg_check_modules(Gflags REQUIRED gflags)

include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${fastcdr_INCLUDE_DIR}
    ${fastrtps_INCLUDE_DIR}
    ${Protobuf_INCLUDE_DIRS}
    ${Glog_INCLUDE_DIRS}
    ${Gflags_INCLUDE_DIRS}
)

link_directories(
    ${fastcdr_LIB_DIR}
    ${fastrtps_LIB_DIR}
    ${Protobuf_LIBRARIES_DIRS}
    ${Glog_LIBRARY_DIRS}
    ${Gflags_LIBRARY_DIRS}
)

aux_source_directory("cyber/proto/" CYBER_PROTO_SRCS)

file(GLOB CYBER_SRCS 
    "cyber/base/*.cc"
    "cyber/blocker/*.cc"
    "cyber/class_loader/*.cc"
    "cyber/class_loader/*/*.cc"
    "cyber/common/*.cc" 
    "cyber/component/*.cc"
    "cyber/croutine/*.cc"
    "cyber/croutine/*/*.cc"
    "cyber/croutine/detail/swap_x86_64.S"
    "cyber/data/*.cc"
    "cyber/event/*.cc"
    "cyber/io/*.cc"
    "cyber/logger/*.cc"
    "cyber/message/*.cc"
    "cyber/node/*.cc"
    "cyber/parameter/*.cc"
    "cyber/record/*.cc"
    "cyber/record/*/*.cc"
    "cyber/scheduler/*.cc"
    "cyber/scheduler/*/*.cc"
    "cyber/service/*.cc"
    "cyber/service_discovery/*.cc"
    "cyber/service_discovery/*/*.cc"
    "cyber/task/*.cc" 
    "cyber/time/*.cc"
    "cyber/timer/*.cc"	
    "cyber/transport/*.cc"
    "cyber/transport/*/*.cc"
    "cyber/*.cc"
    "cyber/sysmo/*.cc"
)

list(FILTER CYBER_SRCS EXCLUDE REGEX .*test[.]cc)

add_library(${TARGET_NAME} SHARED ${CYBER_PROTO_SRCS} ${CYBER_SRCS})
target_link_libraries(${TARGET_NAME} 
    ${Glog_LIBRARIES}
    ${Gflags_LIBRARIES}
    ${Protobuf_LIBRARIES}
    ${Poco_LIBRARIES}
    fastrtps
    fastcdr
    atomic
    uuid
)

add_subdirectory(cyber/examples)
add_subdirectory(cyber/python)
add_subdirectory(cyber/tools)

install(DIRECTORY cyber/
    DESTINATION include/cyber/
    FILES_MATCHING
    PATTERN "*.h"
)

file(COPY cyber/conf/
  DESTINATION ${CMAKE_BINARY_DIR}/share/conf/
)
install(DIRECTORY ${CMAKE_BINARY_DIR}/share/conf/ 
  DESTINATION share/conf/
)

file(COPY setup.zsh setup.bash 
  DESTINATION ${CMAKE_BINARY_DIR}
)
install(FILES ${CMAKE_BINARY_DIR}/setup.zsh ${CMAKE_BINARY_DIR}/setup.bash
  DESTINATION . 
)

file(COPY cyber/python/
  DESTINATION ${CMAKE_BINARY_DIR}/cyber/python/
)
install(DIRECTORY ${CMAKE_BINARY_DIR}/cyber/python/
  DESTINATION lib/python3.6/site-packages/cyber/python/
)

install(TARGETS ${TARGET_NAME}
    EXPORT ${TARGET_NAME}-targets
    ARCHIVE DESTINATION lib
    LIBRARY DESTINATION lib
    RUNTIME DESTINATION bin
)


