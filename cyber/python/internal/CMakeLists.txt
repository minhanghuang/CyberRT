add_library(_cyber_wrapper SHARED 
  py_cyber.cc
)
target_link_libraries(_cyber_wrapper
  ${TARGET_NAME}
  # ${CYBER_PYTHON_LIB}
  ${Python_LIBRARIES}
)
add_library(py_cyber ALIAS _cyber_wrapper)

add_library(_cyber_record_wrapper SHARED 
  py_record.cc
)
target_link_libraries(_cyber_record_wrapper
  ${TARGET_NAME}
  # ${CYBER_PYTHON_LIB}
  ${Python_LIBRARIES}
)
add_library(py_record ALIAS _cyber_record_wrapper)

add_library(_cyber_time_wrapper SHARED
  py_time.cc
)
target_link_libraries(_cyber_time_wrapper
  ${TARGET_NAME}
  # ${CYBER_PYTHON_LIB}
  ${Python_LIBRARIES}
)
add_library(py_time ALIAS _cyber_time_wrapper)

add_library(_cyber_parameter_wrapper SHARED 
  py_parameter.cc
)
target_link_libraries(_cyber_parameter_wrapper
  ${TARGET_NAME}
  # ${CYBER_PYTHON_LIB}
  ${Python_LIBRARIES}
)
add_library(py_parameter ALIAS _cyber_parameter_wrapper)

set_target_properties(_cyber_wrapper
    PROPERTIES PREFIX ""
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/${CYBER_PYTHON_INTERNAL_PATH}"
)
set_target_properties(_cyber_record_wrapper
  PROPERTIES PREFIX ""
  LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/${CYBER_PYTHON_INTERNAL_PATH}"
)
set_target_properties(_cyber_time_wrapper 
  PROPERTIES PREFIX "" 
  LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/${CYBER_PYTHON_INTERNAL_PATH}"
)
set_target_properties(_cyber_parameter_wrapper
  PROPERTIES PREFIX ""
  LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/${CYBER_PYTHON_INTERNAL_PATH}"
)

install(TARGETS
  _cyber_wrapper 
  _cyber_record_wrapper
  _cyber_time_wrapper
  _cyber_parameter_wrapper
  DESTINATION ${CYBER_PYTHON_INTERNAL_PATH}
)

