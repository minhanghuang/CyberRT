cmake_minimum_required(VERSION 3.5)

project(examples VERSION 1.0.0)

SET(CMAKE_CXX_FLAGS "-std=c++11 -pthread -latomic ")

add_executable(cyber_example_talker talker.cc proto/examples.pb.cc)
target_link_libraries(cyber_example_talker
    ${TARGET_NAME}
    pthread
)

add_executable(cyber_example_listener listener.cc proto/examples.pb.cc)
target_link_libraries(cyber_example_listener
    ${TARGET_NAME}
    pthread
)

# add_executable(cyber_example_paramserver paramserver.cc proto/examples.pb.cc)
# target_link_libraries(cyber_example_paramserver
#     ${glog_LIBRARIES}
#     ${fastrtps_LIBRARIES}
#     ${gflags_LIBRARIES}
#     ${Protobuf_LIBRARY}
#     Cyber::init
#     Cyber::parameter
#     Cyber::parameter_server
#     Cyber::parameter_client
#     Cyber::component_base
#     Cyber::core
#     Cyber::pb_parameter
# )

# add_executable(cyber_example_record record.cc proto/examples.pb.cc)
# target_link_libraries(cyber_example_record
#     ${glog_LIBRARIES}
#     ${fastrtps_LIBRARIES}
#     ${gflags_LIBRARIES}
#     ${Protobuf_LIBRARY}
#     Cyber::init
#     Cyber::component_base
#     Cyber::record_reader
#     Cyber::record_writer
#     Cyber::pb_record
# )

# add_executable(cyber_example_service service.cc proto/examples.pb.cc)
# target_link_libraries(cyber_example_service
#     ${glog_LIBRARIES}
#     ${fastrtps_LIBRARIES}
#     ${gflags_LIBRARIES}
#     ${Protobuf_LIBRARY}
#     pthread
#     Cyber::init
#     Cyber::core
#     Cyber::component_base
#     Cyber::endpoint
# )
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
