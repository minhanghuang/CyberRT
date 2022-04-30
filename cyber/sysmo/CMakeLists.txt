cmake_minimum_required(VERSION 3.5)
project(CyberSysmo)

add_library(cyber_sysmo sysmo.cc)

add_library(Cyber::sysmo ALIAS cyber_sysmo)

# file(GLOB HEADERS *.h)

# install(FILES ${HEADERS}
#     DESTINATION ${CYBER_INSTALL_INCLUDE_DIR}/cyber/sysmo/
#     )

# install(TARGETS cyber_sysmo
#     DESTINATION  ${CYBER_INSTALL_LIB_DIR}
#     )
