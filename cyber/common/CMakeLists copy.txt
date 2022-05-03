cmake_minimum_required(VERSION 3.5)

project(CyberComponent)

add_library(cyber_timer_component timer_component.cc)

add_library(cyber_component_base INTERFACE)
target_include_directories(cyber_component_base INTERFACE
    $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/>
    $<INSTALL_INTERFACE:include>
    )
target_link_libraries(cyber_component_base INTERFACE
    Cyber::node
    )

add_library(Cyber::component ALIAS cyber_timer_component)
add_library(Cyber::component_base ALIAS cyber_component_base)

# file(GLOB HEADERS *.h)

# install(FILES ${HEADERS}
#     DESTINATION ${CYBER_INSTALL_INCLUDE_DIR}/cyber/component/
#     )

# install(TARGETS cyber_timer_component
#     DESTINATION  ${CYBER_INSTALL_LIB_DIR}
#     )
