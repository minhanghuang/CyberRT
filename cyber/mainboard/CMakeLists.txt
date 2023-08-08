project(mainboard VERSION 1.0.0)

add_executable(mainboard
  mainboard.cc
  module_argument.cc
  module_controller.cc
)

target_link_libraries(mainboard
    ${TARGET_NAME}
    pthread
)

set_target_properties(mainboard PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin/cyber/mainboard
)
