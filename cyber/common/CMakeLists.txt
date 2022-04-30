cmake_minimum_required(VERSION 3.5)

project(CyberCommon)

add_library(cyber_file file.cc)
target_link_libraries(cyber_file ${Protobuf_LIBRARY})
add_library(Cyber::file ALIAS cyber_file)

add_library(cyber_global_data global_data.cc)
target_link_libraries(cyber_global_data
    Cyber::file
    Cyber::cyber_conf
)
add_library(Cyber::global_data ALIAS cyber_global_data)

# file(GLOB HEADERS *.h)

# install(FILES ${HEADERS}
#     DESTINATION ${CYBER_INSTALL_INCLUDE_DIR}/cyber/common
#     )

# install(TARGETS cyber_file cyber_global_data
#     DESTINATION  ${CYBER_INSTALL_LIB_DIR}
#     )
