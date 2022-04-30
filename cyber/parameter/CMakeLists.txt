cmake_minimum_required(VERSION 3.5)

project(CyberParameter)

add_library(cyber_parameter parameter.cc)
add_library(cyber_parameter_client parameter_client.cc)
add_library(cyber_parameter_server parameter_server.cc)
target_link_libraries(cyber_parameter_server
    Cyber::endpoint
)

add_library(Cyber::parameter ALIAS cyber_parameter)
add_library(Cyber::parameter_client ALIAS cyber_parameter_client)
add_library(Cyber::parameter_server ALIAS cyber_parameter_server)

# file(GLOB HEADERS *.h)

# install(FILES ${HEADERS}
#     DESTINATION ${CYBER_INSTALL_INCLUDE_DIR}/cyber/parameter/
#     )

# install(TARGETS cyber_parameter cyber_parameter_client cyber_parameter_server
#     DESTINATION  ${CYBER_INSTALL_LIB_DIR}
#     )
