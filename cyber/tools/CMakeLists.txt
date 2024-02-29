project(tools VERSION 1.0.0)

# cyber monitor
add_executable(cyber_monitor
  cyber_monitor/cyber_topology_message.cc
  cyber_monitor/general_channel_message.cc
  cyber_monitor/general_message.cc
  cyber_monitor/general_message_base.cc
  cyber_monitor/renderable_message.cc
  cyber_monitor/screen.cc
  cyber_monitor/main.cc
)
target_link_libraries(cyber_monitor
  pthread
  ncurses
  ${TARGET_NAME}
)
set_target_properties(cyber_monitor PROPERTIES
  RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin/cyber/tools/cyber_monitor/"
)

# cyber_recorder
add_executable(cyber_recorder
  cyber_recorder/main.cc
  cyber_recorder/info.cc
  cyber_recorder/recorder.cc
  cyber_recorder/recoverer.cc
  cyber_recorder/spliter.cc
  cyber_recorder/player/play_task.cc
  cyber_recorder/player/play_task_buffer.cc
  cyber_recorder/player/play_task_consumer.cc
  cyber_recorder/player/play_task_producer.cc
  cyber_recorder/player/player.cc
)
target_link_libraries(cyber_recorder
 ${TARGET_NAME}
)
set_target_properties(cyber_recorder PROPERTIES
  RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin/cyber/tools/cyber_recorder/"
)

# cyber_channel cyber_launch cyber_node cyber_service
file(COPY
  cyber_channel/cyber_channel.py
  DESTINATION ${CMAKE_BINARY_DIR}/bin/cyber/tools/cyber_channel/
)
file(COPY
  cyber_launch/cyber_launch.py
  DESTINATION ${CMAKE_BINARY_DIR}/bin/cyber/tools/cyber_launch/
)
file(COPY
  cyber_node/cyber_node.py
  DESTINATION ${CMAKE_BINARY_DIR}/bin/cyber/tools/cyber_node/
)
file(COPY
  cyber_service/cyber_service.py
  DESTINATION ${CMAKE_BINARY_DIR}/bin/cyber/tools/cyber_service/
)
file(COPY
  cyber_tools_auto_complete.bash
  DESTINATION ${CMAKE_BINARY_DIR}
)

file(RENAME ${CMAKE_BINARY_DIR}/bin/cyber/tools/cyber_channel/cyber_channel.py ${CMAKE_BINARY_DIR}/bin/cyber/tools/cyber_channel/cyber_channel)
file(RENAME ${CMAKE_BINARY_DIR}/bin/cyber/tools/cyber_launch/cyber_launch.py ${CMAKE_BINARY_DIR}/bin/cyber/tools/cyber_launch/cyber_launch)
file(RENAME ${CMAKE_BINARY_DIR}/bin/cyber/tools/cyber_node/cyber_node.py ${CMAKE_BINARY_DIR}/bin/cyber/tools/cyber_node/cyber_node)
file(RENAME ${CMAKE_BINARY_DIR}/bin/cyber/tools/cyber_service/cyber_service.py ${CMAKE_BINARY_DIR}/bin/cyber/tools/cyber_service/cyber_service)

install(FILES
  ${CMAKE_BINARY_DIR}/bin/cyber/tools/cyber_channel/cyber_channel
  ${CMAKE_BINARY_DIR}/bin/cyber/tools/cyber_launch/cyber_launch
  ${CMAKE_BINARY_DIR}/bin/cyber/tools/cyber_node/cyber_node
  ${CMAKE_BINARY_DIR}/bin/cyber/tools/cyber_service/cyber_service
  ${CMAKE_BINARY_DIR}/bin/cyber/tools/cyber_monitor/cyber_monitor
  ${CMAKE_BINARY_DIR}/bin/cyber/tools/cyber_recorder/cyber_recorder
  PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE
  DESTINATION bin
)
install(FILES
  ${CMAKE_BINARY_DIR}/cyber_tools_auto_complete.bash
  PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE
  DESTINATION .
)
