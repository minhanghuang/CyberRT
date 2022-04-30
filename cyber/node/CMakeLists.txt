cmake_minimum_required(VERSION 3.5)

project(CyberNode)

add_library(cyber_node node.cc)
target_link_libraries(cyber_node Cyber::role_attributes)

add_library(cyber_reader INTERFACE)
add_library(cyber_writer INTERFACE)
add_library(cyber_node_channel INTERFACE)
add_library(cyber_node_service INTERFACE)

add_library(Cyber::node ALIAS cyber_node)

# file(GLOB HEADERS *.h)

# install(FILES ${HEADERS}
#     DESTINATION ${CYBER_INSTALL_INCLUDE_DIR}/cyber/node/
#     )

# install(TARGETS
#     cyber_node
#     cyber_reader
#     cyber_writer
#     cyber_node_channel
#     cyber_node_service
#     DESTINATION  ${CYBER_INSTALL_LIB_DIR}
#     )
