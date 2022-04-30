cmake_minimum_required(VERSION 3.5)

project(CyberMessage)

add_library(cyber_protobuf_factory protobuf_factory.cc)
target_link_libraries(cyber_protobuf_factory cyber_proto_desc)

add_library(message_traits INTERFACE)
add_library(protobuf_traits INTERFACE)
add_library(py_message_traits INTERFACE)
add_library(raw_message_traits INTERFACE)

add_library(Cyber::protobuf_factory ALIAS cyber_protobuf_factory)

# file(GLOB HEADERS *.h)

# install(FILES ${HEADERS}
#     DESTINATION ${CYBER_INSTALL_INCLUDE_DIR}/cyber/message/
#     )

# install(TARGETS
#     cyber_protobuf_factory
#     message_traits
#     protobuf_traits
#     py_message_traits
#     raw_message_traits
#     DESTINATION  ${CYBER_INSTALL_LIB_DIR}
#     )
