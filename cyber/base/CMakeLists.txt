cmake_minimum_required(VERSION 3.5)

project(CyberBase)

add_library(cyber_signal INTERFACE)
#target_sources(cyber_signal INTERFACE signal.h)
target_include_directories(cyber_signal INTERFACE
    "${PROJECT_SOURCE_DIR}"
    )
add_library(Cyber::signal ALIAS cyber_signal)

#add_executable(signal_test signal_test.cc)
#target_link_libraries(signal_test Cyber::signal)

add_library(cyber_atomic_fifo INTERFACE)
#target_sources(cyber_signal INTERFACE signal.h)
target_include_directories(cyber_atomic_fifo INTERFACE
    "${PROJECT_SOURCE_DIR}"
    )

add_library(Cyber::atomic_fifo ALIAS cyber_atomic_fifo)

add_library(cyber_base INTERFACE)
target_include_directories(cyber_base INTERFACE
    "${PROJECT_SOURCE_DIR}"
    )
add_library(Cyber::base ALIAS cyber_base)

add_library(cyber_atomic_hash_map INTERFACE)
add_library(cyber_atomic_rw_lock INTERFACE)
add_library(cyber_bounded_queue INTERFACE)
add_library(cyber_concurrent_object_pool INTERFACE)
add_library(cyber_for_each INTERFACE)
add_library(cyber_object_pool INTERFACE)
add_library(cyber_reentrant_rw_lock INTERFACE)
add_library(cyber_rw_lock_guard INTERFACE)
add_library(cyber_unbounded_queue INTERFACE)
add_library(cyber_thread_safe_queue INTERFACE)
add_library(cyber_macros INTERFACE)
add_library(cyber_thread_pool INTERFACE)
add_library(cyber_wait_strategy INTERFACE)

file(GLOB HEADERS *.h)

install(FILES ${HEADERS}
    DESTINATION ${CYBER_INSTALL_INCLUDE_DIR}/cyber/base/
    )
