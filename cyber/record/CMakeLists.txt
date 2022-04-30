cmake_minimum_required(VERSION 3.5)

project(CyberRecord)

add_library(cyber_record_file_base file/record_file_base.cc)
add_library(cyber_record_file_reader file/record_file_reader.cc)
add_library(cyber_record_file_writer file/record_file_writer.cc)
add_library(cyber_header_builder header_builder.cc)

add_library(cyber_record_reader record_reader.cc)
target_link_libraries(cyber_record_reader
    cyber_record_file_reader
    cyber_record_file_base)

add_library(cyber_record_writer record_writer.cc)
target_link_libraries(cyber_record_writer
    cyber_header_builder
    cyber_record_file_writer
    cyber_record_file_base)

add_library(cyber_record_viewer record_viewer.cc)

add_library(Cyber::record_reader ALIAS cyber_record_reader)
add_library(Cyber::record_writer ALIAS cyber_record_writer)
add_library(Cyber::record_viewer ALIAS cyber_record_viewer)

add_library(Cyber::record_header_builder ALIAS cyber_header_builder)
add_library(Cyber::record_file_base ALIAS cyber_record_file_base)
add_library(Cyber::record_file_reader ALIAS cyber_record_file_reader)
add_library(Cyber::record_file_writer ALIAS cyber_record_file_writer)

# file(GLOB HEADERS *.h)

# install(FILES ${HEADERS}
#     DESTINATION ${CYBER_INSTALL_INCLUDE_DIR}/cyber/record/
#     )

# install(TARGETS cyber_record_reader
#     cyber_record_writer
#     cyber_record_viewer
#     cyber_record_file_base
#     cyber_record_file_reader
#     cyber_record_file_writer
#     cyber_header_builder
#     DESTINATION  ${CYBER_INSTALL_LIB_DIR}
#     )
