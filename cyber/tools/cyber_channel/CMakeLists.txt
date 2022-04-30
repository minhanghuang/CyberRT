cmake_minimum_required(VERSION 3.5)
project(CyberChannel)

install(FILES cyber_channel
    DESTINATION  ${CYBER_INSTALL_DIR}/bin
    PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE GROUP_READ GROUP_EXECUTE
    )
