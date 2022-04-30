cmake_minimum_required(VERSION 3.5)
project(CyberPyWrapper)

find_package(PythonLibs REQUIRED)

add_library(cyber_py_wrapper
    py_cyber.cc
    py_parameter.cc
    py_record.cc
    py_time.cc
    py_timer.cc
    )
target_include_directories(cyber_py_wrapper PUBLIC  ${PYTHON_INCLUDE_DIRS})
target_link_libraries(cyber_py_wrapper ${PYTHON_LIBRARIES})

add_library(Cyber::py_wrapper ALIAS cyber_py_wrapper)



add_library(_cyber_py3
    py_cyber.cc
    )
target_include_directories(_cyber_py3 PUBLIC  ${PYTHON_INCLUDE_DIRS})
target_link_libraries(_cyber_py3
    ${PYTHON_LIBRARIES}
    Cyber::init
    Cyber::component_base
    Cyber::transmitter
    Cyber::blocker_manager
    Cyber::core
    Cyber::role_attributes
    )
set_target_properties(_cyber_py3 PROPERTIES OUTPUT_NAME _cyber_py3 PREFIX  "")

add_library(_cyber_record_py3
    py_record.cc
    )
target_include_directories(_cyber_record_py3 PUBLIC  ${PYTHON_INCLUDE_DIRS})
target_link_libraries(_cyber_record_py3 ${PYTHON_LIBRARIES})
set_target_properties(_cyber_record_py3 PROPERTIES OUTPUT_NAME _cyber_record_py3 PREFIX  "")

add_library(_cyber_timer_py3
    py_timer.cc
    )
target_include_directories(_cyber_timer_py3 PUBLIC  ${PYTHON_INCLUDE_DIRS})
target_link_libraries(_cyber_timer_py3 ${PYTHON_LIBRARIES})
set_target_properties(_cyber_timer_py3 PROPERTIES OUTPUT_NAME _cyber_timer_py3 PREFIX  "")

add_library(_cyber_time_py3
    py_time.cc
    )
target_include_directories(_cyber_time_py3 PUBLIC  ${PYTHON_INCLUDE_DIRS})
target_link_libraries(_cyber_time_py3
    ${PYTHON_LIBRARIES}
    Cyber::init
    Cyber::component_base
    Cyber::transmitter
    Cyber::blocker_manager
    Cyber::core
    Cyber::time
    Cyber::rate
    Cyber::duration
    )
set_target_properties(_cyber_time_py3 PROPERTIES OUTPUT_NAME _cyber_time_py3 PREFIX  "")

add_library(_cyber_parameter_py3
    py_parameter.cc
    )
target_include_directories(_cyber_parameter_py3 PUBLIC  ${PYTHON_INCLUDE_DIRS})
target_link_libraries(_cyber_parameter_py3 ${PYTHON_LIBRARIES})
set_target_properties(_cyber_parameter_py3 PROPERTIES OUTPUT_NAME _cyber_parameter_py3 PREFIX  "")

file(GLOB HEADERS *.h)

install(FILES ${HEADERS}
    DESTINATION ${CYBER_INSTALL_INCLUDE_DIR}/cyber/py_wrapper/
    )

install(TARGETS cyber_py_wrapper
    DESTINATION  ${CYBER_INSTALL_LIB_DIR}
    )

install(TARGETS _cyber_py3
    DESTINATION  ${CYBER_INSTALL_LIB_DIR}
    )
install(TARGETS _cyber_record_py3
    DESTINATION  ${CYBER_INSTALL_LIB_DIR}
    )
install(TARGETS _cyber_timer_py3
    DESTINATION  ${CYBER_INSTALL_LIB_DIR}
    )
install(TARGETS _cyber_time_py3
    DESTINATION  ${CYBER_INSTALL_LIB_DIR}
    )
install(TARGETS _cyber_parameter_py3
    DESTINATION  ${CYBER_INSTALL_LIB_DIR}
    )
