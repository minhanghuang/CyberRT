cmake_minimum_required(VERSION 3.5)

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

