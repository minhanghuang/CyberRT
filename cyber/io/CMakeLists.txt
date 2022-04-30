cmake_minimum_required(VERSION 3.5)
project(CyberIo)

add_library(cyber_poller poller.cc)
add_library(cyber_poll_handler poll_handler.cc)
add_library(cyber_session session.cc)

add_library(Cyber::poller ALIAS cyber_poller)
add_library(Cyber::poll_handler ALIAS cyber_poll_handler)
add_library(Cyber::session ALIAS cyber_session)

# file(GLOB HEADERS *.h)

# install(FILES ${HEADERS}
#     DESTINATION ${CYBER_INSTALL_INCLUDE_DIR}/cyber/io/
#     )

# install(TARGETS cyber_poller cyber_poll_handler cyber_session
#     DESTINATION  ${CYBER_INSTALL_LIB_DIR}
#     )
