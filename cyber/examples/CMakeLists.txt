project(examples VERSION 1.0.0)

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

add_executable(cyber_example_paramserver paramserver.cc)
target_link_libraries(cyber_example_paramserver
    ${TARGET_NAME}
)

add_executable(cyber_example_record record.cc)
target_link_libraries(cyber_example_record
    ${TARGET_NAME}
)

add_executable(cyber_example_server server.cc proto/examples.pb.cc)
target_link_libraries(cyber_example_server
    ${TARGET_NAME}
)

add_executable(cyber_example_cilent client.cc proto/examples.pb.cc)
target_link_libraries(cyber_example_cilent
    ${TARGET_NAME}
)

