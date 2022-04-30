cmake_minimum_required(VERSION 3.5)

project(CyberMainboad)

add_executable(cyber_mainboard
    mainboard.cc
    module_argument.cc
    module_controller.cc
    )

target_link_libraries(cyber_mainboard
    PUBLIC
    cyber_class_loader
    cyber_class_loader_utility
    cyber_class_factory
    cyber_class_loader_manager
    cyber_scheduler
    cyber_state
    cyber_file
    cyber_init
    cyber_node
    cyber_global_data
    ${Glog_LIBRARY}
    gflags
    Cyber::dag_conf
    Cyber::perf_conf
    )

file(GLOB HEADERS *.h)

install(FILES ${HEADERS}
    DESTINATION ${CYBER_INSTALL_INCLUDE_DIR}/cyber/mainboard/
    )

install(TARGETS cyber_mainboard
    DESTINATION  ${CYBER_INSTALL_DIR}/bin
    )
