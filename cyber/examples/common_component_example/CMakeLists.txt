add_executable(channel_test_writer
  channel_test_writer.cc ../proto/examples.pb.cc
)

target_link_libraries(channel_test_writer
  ${TARGET_NAME}
)

add_executable(channel_prediction_writer
  channel_prediction_writer.cc ../proto/examples.pb.cc
)

target_link_libraries(channel_prediction_writer
  ${TARGET_NAME}
)

add_library(common_component_example SHARED
  common_component_example.cc
  ../proto/examples.pb.cc
)

target_link_libraries(common_component_example
  ${TARGET_NAME}
)

set_target_properties(common_component_example PROPERTIES
  LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin/cyber/examples/common_component_example/"
)

set_target_properties(common_component_example PROPERTIES
  LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/cyber/examples/common_component_example/"
)

file(COPY common.dag common.launch
  DESTINATION ${CMAKE_BINARY_DIR}/share/examples/common_component_example
)

install(FILES common.dag common.launch
  DESTINATION share/examples/common_component_example
)

install(TARGETS common_component_example
  LIBRARY DESTINATION lib
)

