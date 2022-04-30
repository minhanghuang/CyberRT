cmake_minimum_required(VERSION 3.5)

project(timer_component_example VERSION 1.0.0)

set(proto_src ../proto/examples.pb.cc)
add_library(timer_component_example SHARED timer_component_example.cc
    ${proto_src})

target_link_libraries(timer_component_example
    ${Glog_LIBRARY}
    gflags
    Cyber::init
    Cyber::rate
    Cyber::time
    FastRTPS::fastrtps
    Protobuf::libprotobuf
    Cyber::component_base
    Cyber::transmitter
    Cyber::blocker_manager
    Cyber::core)
# install(TARGETS
#     timer_component_example
#     DESTINATION  ${CYBER_INSTALL_LIB_DIR}
#     )
