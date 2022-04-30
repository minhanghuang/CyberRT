cmake_minimum_required(VERSION 3.5)
project(CyberTimer)

add_library(cyber_timer timer.cc)
target_link_libraries(cyber_timer Cyber::rate)

add_library(cyber_timer_task INTERFACE)
add_library(cyber_timer_bucket INTERFACE)

add_library(cyber_timing_wheel timing_wheel.cc)
target_link_libraries(cyber_timing_wheel Cyber::timer)

add_library(Cyber::timing_wheel ALIAS cyber_timing_wheel)
add_library(Cyber::timer ALIAS cyber_timer)

# file(GLOB HEADERS *.h)

# install(FILES ${HEADERS}
#     DESTINATION ${CYBER_INSTALL_INCLUDE_DIR}/cyber/timer/
#     )

# install(TARGETS
#     cyber_timing_wheel
#     DESTINATION  ${CYBER_INSTALL_LIB_DIR}
#     )
