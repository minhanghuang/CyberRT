cmake_minimum_required(VERSION 3.5)

project(common_component_example VERSION 1.0.0)

set(proto_src ../proto/examples.pb.cc)
add_library(common_component_example SHARED common_component_example.cc
    ${proto_src})

target_link_libraries(common_component_example
    Cyber::init
    Cyber::transmitter
)
# install(TARGETS
#     common_component_example
#     DESTINATION  ${CYBER_INSTALL_LIB_DIR}
#     )
