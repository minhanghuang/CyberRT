cmake_minimum_required(VERSION 3.5)

project(CyberEvent)

add_library(cyber_event perf_event_cache.cc)

add_library(Cyber::event ALIAS cyber_event)

# file(GLOB HEADERS *.h)

# install(FILES ${HEADERS}
#     DESTINATION ${CYBER_INSTALL_INCLUDE_DIR}/cyber/event/
#     )

# install(TARGETS cyber_event
#     DESTINATION  ${CYBER_INSTALL_LIB_DIR}
#     )
