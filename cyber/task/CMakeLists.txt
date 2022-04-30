cmake_minimum_required(VERSION 3.5)

project(CyberTask)

add_library(cyber_task_manager task_manager.cc)
target_link_libraries(cyber_task_manager
    Cyber::croutine
    Cyber::scheduler)

add_library(Cyber::task_manager ALIAS cyber_task_manager)

# file(GLOB HEADERS *.h)

# install(FILES ${HEADERS}
#     DESTINATION ${CYBER_INSTALL_INCLUDE_DIR}/cyber/task
#     )

# install(TARGETS cyber_task_manager
#     DESTINATION  ${CYBER_INSTALL_LIB_DIR}
#     )
