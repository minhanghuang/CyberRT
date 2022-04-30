cmake_minimum_required(VERSION 3.5)

project(CyberLogger)

add_library(cyber_async_logger async_logger.cc)
target_link_libraries(cyber_async_logger Cyber::logg_file_object)

add_library(cyber_logger logger.cc)

add_library(cyber_log_file_object log_file_object.cc)
target_link_libraries(cyber_log_file_object Cyber::logger_util)

add_library(cyber_logger_util logger_util.cc)

add_library(Cyber::async_logger ALIAS cyber_async_logger)
add_library(Cyber::logger ALIAS cyber_logger)
add_library(Cyber::logg_file_object ALIAS cyber_log_file_object)
add_library(Cyber::logger_util ALIAS cyber_logger_util)

# file(GLOB HEADERS *.h)

# install(FILES ${HEADERS}
#     DESTINATION ${CYBER_INSTALL_INCLUDE_DIR}/cyber/logger/
#     )

# install(TARGETS
#     cyber_async_logger
#     cyber_logger
#     cyber_log_file_object
#     cyber_logger_util
#     DESTINATION  ${CYBER_INSTALL_LIB_DIR}
#     )
