cmake_minimum_required(VERSION 3.5)

project(examples VERSION 1.0.0)

SET(CMAKE_CXX_FLAGS "-std=c++11 -pthread -latomic ")


add_executable(cyber_example_talker talker.cc proto/examples.pb.cc)
target_link_libraries(cyber_example_talker
    ${glog_LIBRARIES}
    ${gflags_LIBRARIES}
    ${Protobuf_LIBRARY}
    ${fastrtps_LIBRARIES}
    # gflags
    pthread
    Cyber::init
    Cyber::rate
    Cyber::time
    # FastRTPS::fastrtps
    # Protobuf::libprotobuf
    Cyber::component_base
    Cyber::transmitter
    Cyber::blocker_manager
    Cyber::core
)

add_executable(cyber_example_listener listener.cc proto/examples.pb.cc)
target_link_libraries(cyber_example_listener
    ${glog_LIBRARIES}
    ${gflags_LIBRARIES}
    ${Protobuf_LIBRARY}
    ${fastrtps_LIBRARIES}
    # gflags
    pthread
    Cyber::init
    Cyber::rate
    Cyber::time
    # FastRTPS::fastrtps
    # Protobuf::libprotobuf
    Cyber::component_base
    Cyber::transmitter
    Cyber::blocker_manager
    Cyber::core
)

# add_executable(cyber_example_paramserver paramserver.cc proto/examples.pb.cc)
# target_link_libraries(cyber_example_paramserver
#     gflags
#     Cyber::init
#     Cyber::parameter
#     Cyber::parameter_server
#     Cyber::parameter_client
#     Cyber::component_base
#     Cyber::core
#     Cyber::pb_parameter
#     )

# add_executable(cyber_example_record record.cc proto/examples.pb.cc)
# target_link_libraries(cyber_example_record
#     gflags
#     Cyber::init
#     Cyber::component_base
#     Cyber::record_reader
#     Cyber::record_writer
#     Cyber::pb_record
#     )

# add_executable(cyber_example_service service.cc proto/examples.pb.cc)
# target_link_libraries(cyber_example_service
#     pthread
#     gflags
#     Cyber::init
#     Cyber::core
#     Cyber::component_base
#     Cyber::endpoint
#     )
# add_subdirectory(common_component_example)
# add_subdirectory(timer_component_example)
# install(TARGETS
#     cyber_example_talker
#     cyber_example_listener
#     cyber_example_paramserver
#     cyber_example_record
#     cyber_example_service
#     DESTINATION ${CYBER_INSTALL_DIR}/bin
#     )
