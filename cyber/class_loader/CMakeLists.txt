cmake_minimum_required(VERSION 3.5)

project(ClassLoader VERSION 1.0.0)

find_library(pocolib libPocoFoundation.so RERUIRED)

add_library(cyber_class_loader class_loader.cc)
add_library(cyber_class_loader_manager class_loader_manager.cc)
add_library(cyber_class_factory utility/class_factory.cc)

add_library(cyber_class_loader_utility utility/class_loader_utility.cc)
target_link_libraries(cyber_class_loader_utility ${pocolib})

add_library(Cyber::class_loader ALIAS cyber_class_loader)
add_library(Cyber::class_loader_manager ALIAS cyber_class_loader_manager)
add_library(Cyber::class_factory ALIAS cyber_class_factory)
add_library(Cyber::class_loader_utility ALIAS cyber_class_loader_utility)

# file(GLOB HEADERS *.h utility/*.h)

# install(FILES ${HEADERS}
#     COMPONENT ${PROJECT_NAME}
#     DESTINATION ${CYBER_INSTALL_INCLUDE_DIR}/cyber/class_loader/
#     )

# install(TARGETS cyber_class_loader
#     cyber_class_factory
#     cyber_class_loader_manager
#     cyber_class_loader_utility
#     DESTINATION  ${CYBER_INSTALL_LIB_DIR}
#     )

#[==[
target_include_directories(${PROJECT_NAME}
    PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>
    )
#]==]

message(STATUS "PN: ${PROJECT_NAME} CPN: ${CMAKE_PROJECT_NAME}")
install(TARGETS cyber_class_loader cyber_class_loader_manager EXPORT ${PROJECT_NAME}-targets
    COMPONENT ${PROJECT_NAME}
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
    INCLUDES DESTINATION include
    )

install(EXPORT ${PROJECT_NAME}-targets
    FILE "${PROJECT_NAME}Targets.cmake"
    NAMESPACE ${CMAKE_PROJECT_NAME}::
    DESTINATION lib/cmake/${CMAKE_PROJECT_NAME}
    )

include(CMakePackageConfigHelpers)

write_basic_package_version_file(
    "${CMAKE_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake"
    VERSION ${version}
    COMPATIBILITY AnyNewerVersion
    )

configure_package_config_file("${PROJECT_NAME}Config.cmake.in"
    "${CMAKE_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
    INSTALL_DESTINATION lib/cmake/${PROJECT_NAME}
    #    @ONLY
    )


install(
    FILES
    "${CMAKE_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
    "${CMAKE_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake"
    DESTINATION lib/cmake/${CMAKE_PROJECT_NAME}
    )

#[==[
install(
    DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include
    COMPONENT ${PROJECT_NAME}
    DESTINATION ${CMAKE_INSTALL_PREFIX}
    )
#]==]
