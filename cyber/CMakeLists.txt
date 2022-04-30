cmake_minimum_required(VERSION 3.5)
project(CyberCore)

add_library(cyber_core cyber.cc)

add_library(cyber_init init.cc)
target_link_libraries(cyber_init
    ${Glog_LIBRARY}
    Cyber::service_manager
    Cyber::async_logger
    Cyber::task_manager
    Cyber::timing_wheel
    Cyber::state
    Cyber::global_data
    Cyber::sysmo
    Cyber::topology_manager)

add_library(cyber_state state.cc)
add_library(cyber_binary INTERFACE)

add_library(Cyber::core ALIAS cyber_core)
add_library(Cyber::init ALIAS cyber_init)
add_library(Cyber::state ALIAS cyber_state)

# file(GLOB HEADERS *.h)

# install(FILES ${HEADERS}
#     DESTINATION ${CYBER_INSTALL_INCLUDE_DIR}/cyber/
#     )

# install(TARGETS
#     cyber_core cyber_init cyber_state
#     DESTINATION  ${CYBER_INSTALL_LIB_DIR}
#     )

# install(DIRECTORY
#     conf
#     DESTINATION  ${CYBER_INSTALL_DIR}
#     )

# install(FILES
#     setup.bash
#     DESTINATION  ${CYBER_INSTALL_DIR}
#     )
