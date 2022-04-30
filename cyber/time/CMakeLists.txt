cmake_minimum_required(VERSION 3.5)

project(CyberTime)

add_library(cyber_duration duration.cc)
add_library(cyber_rate rate.cc)

add_library(cyber_time  time.cc)
target_link_libraries(cyber_time cyber_duration)

add_library(Cyber::duration ALIAS cyber_duration)
add_library(Cyber::rate ALIAS cyber_rate)
add_library(Cyber::time ALIAS cyber_time)

# file(GLOB HEADERS *.h)

# install(FILES ${HEADERS}
#     DESTINATION ${CYBER_INSTALL_INCLUDE_DIR}/cyber/time/
#     )

# install(TARGETS cyber_duration cyber_rate cyber_time
#     DESTINATION  ${CYBER_INSTALL_LIB_DIR}
#     )
