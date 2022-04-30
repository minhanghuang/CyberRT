cmake_minimum_required(VERSION 3.5)
project(CyberService)

add_library(cyber_client INTERFACE)
target_sources(cyber_client INTERFACE
    client_base.h
    client.h
    )
add_library(cyber_server INTERFACE)
target_sources(cyber_server INTERFACE
    service_base.h
    service.h
    )

add_library(Cyber::client ALIAS cyber_client)
add_library(Cyber::server ALIAS cyber_server)

file(GLOB HEADERS *.h)

install(FILES ${HEADERS}
    DESTINATION ${CYBER_INSTALL_INCLUDE_DIR}/cyber/service/
    )
