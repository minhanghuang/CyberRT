file(COPY 
    cyber_channel/cyber_channel.py
    cyber_launch/cyber_launch.py
    cyber_node/cyber_node.py
    cyber_service/cyber_service.py 
  DESTINATION ${CMAKE_BINARY_DIR}/bin/
)

file(RENAME ${CMAKE_BINARY_DIR}/bin/cyber_channel.py ${CMAKE_BINARY_DIR}/bin/cyber_channel)
file(RENAME ${CMAKE_BINARY_DIR}/bin/cyber_launch.py ${CMAKE_BINARY_DIR}/bin/cyber_launch)
file(RENAME ${CMAKE_BINARY_DIR}/bin/cyber_node.py ${CMAKE_BINARY_DIR}/bin/cyber_node)
file(RENAME ${CMAKE_BINARY_DIR}/bin/cyber_service.py ${CMAKE_BINARY_DIR}/bin/cyber_service)

install(FILES 
        ${CMAKE_BINARY_DIR}/bin/cyber_channel
        ${CMAKE_BINARY_DIR}/bin/cyber_launch
        ${CMAKE_BINARY_DIR}/bin/cyber_node
        ${CMAKE_BINARY_DIR}/bin/cyber_service
        PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE 
    DESTINATION bin
)

