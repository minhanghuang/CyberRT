cmake_minimum_required(VERSION 3.5)

project(CyberBlocker)

add_library(cyber_blocker_manager blocker_manager.cc)
add_library(cyber_intra_reader INTERFACE)
add_library(cyber_intra_writer INTERFACE)
add_library(cyber_intra_blocker INTERFACE)

add_library(Cyber::blocker_manager ALIAS cyber_blocker_manager)

# file(GLOB HEADERS *.h)

# install(FILES ${HEADERS}
#     DESTINATION ${CYBER_INSTALL_INCLUDE_DIR}/cyber/blocker/
#     )

# install(TARGETS cyber_blocker_manager
#     DESTINATION  ${CYBER_INSTALL_LIB_DIR}
#     )
