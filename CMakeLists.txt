cmake_minimum_required(VERSION 3.5.1)

project(cyber VERSION 9.0.0) # Apollo Version

set(CMAKE_CXX_STANDARD 14)
set(TARGET_NAME ${PROJECT_NAME})
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release) # Debug/Release
endif()

enable_language(ASM)

include(CMakePackageConfigHelpers)
include(GNUInstallDirs)
# ccache
find_program(CCACHE_FOUND ccache)
if (CCACHE_FOUND)
  message(STATUS "### use ccache")
  set_property(GLOBAL PROPERTY RULE_LAUNCH_COMPILE ccache)
  set_property(GLOBAL PROPERTY RULE_LAUNCH_LINK ccache)
endif (CCACHE_FOUND)

# fix for gcc 9
#set(CMAKE_POSITION_INDEPENDENT_CODE ON)
#set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -pie")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fPIC")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC")

set(CROUTINE_FILE "cyber/croutine/detail/swap_x86_64.S")
if(${CMAKE_SYSTEM_PROCESSOR} STREQUAL "x86_64")
  set(CROUTINE_FILE "cyber/croutine/detail/swap_x86_64.S")
  message("### SYSTEM_PROCESSOR: ${CMAKE_SYSTEM_PROCESSOR} ${CROUTINE_FILE}")
else()
  set(CROUTINE_FILE "cyber/croutine/detail/swap_aarch64.S")
  message("### SYSTEM_PROCESSOR: ${CMAKE_SYSTEM_PROCESSOR} ${CROUTINE_FILE}")
endif(${CMAKE_SYSTEM_PROCESSOR} STREQUAL "x86_64")

find_package(Threads REQUIRED)
find_package(PkgConfig REQUIRED)
find_package(fastrtps REQUIRED)
find_package(fastcdr REQUIRED)
find_package(Poco REQUIRED COMPONENTS Foundation)
find_package(glog REQUIRED)
find_package(Protobuf REQUIRED)
# find_package(Python REQUIRED COMPONENTS Interpreter Development)
pkg_check_modules(Python REQUIRED python3)
pkg_check_modules(Uuid REQUIRED uuid)
pkg_check_modules(Gflags REQUIRED gflags)
pkg_check_modules(NlohmannJson REQUIRED nlohmann_json)

# set(Python_VERSION "${Python_VERSION_MAJOR}.${Python_VERSION_MINOR}")
set(Python_VERSION "${Python_VERSION}")
set(CYBER_PYTHON_PATH "lib/python${Python_VERSION}/site-packages/cyber/python")
set(CYBER_PYTHON_INTERNAL_PATH "${CYBER_PYTHON_PATH}/internal")
set(CYBER_PYTHON_PROTOBUF_PATH "lib/python${Python_VERSION}/site-packages/cyber/proto")
set(CYBER_MSGS_CACHE ON CACHE BOOL "generate cyber proto msgs flag.")
# set(CYBER_PYTHON_LIB "/usr/lib/python3.6/config-3.6m-x86_64-linux-gnu/libpython3.6.so")

if(NOT DEFINED glog_LIBRARIES)
  set(glog_LIBRARIES "glog")
endif()

if(NOT DEFINED Uuid_LIBRARIES)
  set(Uuid_LIBRARIES "uuid")
endif()

set(DEPENCENCY_INCLUDE_DIRS
  ${fastcdr_INCLUDE_DIR}
  ${fastrtps_INCLUDE_DIR}
  ${Protobuf_INCLUDE_DIRS}
  ${Python_INCLUDE_DIRS}
  ${Uuid_INCLUDE_DIRS}
  ${glog_INCLUDE_DIRS}
  ${Gflags_INCLUDE_DIRS}
  ${NlohmannJson_INCLUDE_DIRS}
)

set(DEPENCENCY_LIB_DIRS
  ${fastcdr_LIB_DIR}
  ${fastrtps_LIB_DIR}
  ${Protobuf_LIBRARIES_DIRS}
  ${Python_LIBRARIES_DIRS}
  ${Uuid_LIBRARIES_DIRS}
  ${glog_LIBRARY_DIRS}
  ${Gflags_LIBRARY_DIRS}
  ${NlohmannJson_LIBRARY_DIRS}
)

set(DEPENCENCY_LIBS
  ${glog_LIBRARIES}
  ${Gflags_LIBRARIES}
)

include_directories(
  ${CMAKE_CURRENT_SOURCE_DIR}
  ${DEPENCENCY_INCLUDE_DIRS}
)

link_directories(${DEPENCENCY_LIB_DIRS})

file(GLOB CYBER_PROTO_FILES
  "${CMAKE_CURRENT_SOURCE_DIR}/modules/common_msgs/**/*.proto"
  "${CMAKE_CURRENT_SOURCE_DIR}/cyber/proto/*.proto"
  "${CMAKE_CURRENT_SOURCE_DIR}/cyber/examples/proto/*.proto"
)

if(${CYBER_MSGS_CACHE})
  set(CYBER_MSGS_CACHE OFF CACHE BOOL "generate cyber proto msgs flag." FORCE)
  FOREACH(FIL ${CYBER_PROTO_FILES})
    message("### generate proto file: ${FIL}")
    GET_FILENAME_COMPONENT(FIL_WE ${FIL} NAME_WE)
    string(REGEX REPLACE ".+/(.+)\\..*" "\\1" FILE_NAME ${FIL})
    string(REGEX REPLACE "(.+)\\${FILE_NAME}.*" "\\1" FILE_PATH ${FIL})
    EXECUTE_PROCESS(
      COMMAND
      ${PROTOBUF_PROTOC_EXECUTABLE}
      -I${CMAKE_CURRENT_SOURCE_DIR}
      --cpp_out=${CMAKE_CURRENT_SOURCE_DIR}
      --python_out=${CMAKE_CURRENT_SOURCE_DIR}
      ${FIL}
    )
  ENDFOREACH()
endif(${CYBER_MSGS_CACHE})

file(GLOB CYBER_PROTO_SRCS
    "cyber/proto/*.pb.cc"
    "cyber/proto/*.pb.h"
    "cyber/examples/proto/*.pb.cc"
    "cyber/examples/proto/*.pb.h"
    "modules/common_msgs/**/*.pb.cc"
    "modules/common_msgs/**/*.pb.h"
)

file(GLOB CYBER_SRCS
    "cyber/base/*.cc"
    "cyber/blocker/*.cc"
    "cyber/class_loader/*.cc"
    "cyber/class_loader/*/*.cc"
    "cyber/common/*.cc"
    "cyber/component/*.cc"
    "cyber/croutine/*.cc"
    "cyber/croutine/*/*.cc"
    "cyber/data/*.cc"
    "cyber/event/*.cc"
    "cyber/io/*.cc"
    "cyber/logger/*.cc"
    "cyber/message/*.cc"
    "cyber/node/*.cc"
    "cyber/parameter/*.cc"
    "cyber/plugin_manager/*.cc"
    "cyber/record/*.cc"
    "cyber/record/*/*.cc"
    "cyber/scheduler/*.cc"
    "cyber/scheduler/*/*.cc"
    "cyber/service/*.cc"
    "cyber/service_discovery/*.cc"
    "cyber/service_discovery/*/*.cc"
    "cyber/task/*.cc"
    "cyber/time/*.cc"
    "cyber/timer/*.cc"
    "cyber/transport/*.cc"
    "cyber/transport/*/*.cc"
    "cyber/*.cc"
    "cyber/sysmo/*.cc"
    ${CROUTINE_FILE}
)

list(FILTER CYBER_SRCS EXCLUDE REGEX .*test[.]cc)

add_library(${TARGET_NAME} SHARED
    ${CYBER_PROTO_SRCS}
    ${CYBER_SRCS}
)

target_link_libraries(${TARGET_NAME}
    ${glog_LIBRARIES}
    ${Gflags_LIBRARIES}
    ${NlohmannJson_LIBRARIES}
    ${Protobuf_LIBRARIES}
    ${Uuid_LIBRARIES}
    ${Poco_LIBRARIES}
    fastrtps
    fastcdr
    atomic
)

add_subdirectory(cyber/mainboard)
add_subdirectory(cyber/examples)
add_subdirectory(cyber/python)
add_subdirectory(cyber/tools)
# --------------------------------------------------------------
#                      CPack
# --------------------------------------------------------------
# 打包方式
include(InstallRequiredSystemLibraries)
if (APPLE)
elseif (UNIX)
  set (CPACK_GENERATOR        "DEB")
  set (CPACK_SOURCE_GENERATOR "TGZ;ZIP")
endif ()

# system/architecture
if (WINDOWS)
  if (CMAKE_CL_64)
    set (CPACK_SYSTEM_NAME "win64")
  else ()
    set (CPACK_SYSTEM_NAME "win32")
  endif ()
  set (CPACK_PACKAGE_ARCHITECTURE)
elseif (APPLE)
  set (CPACK_PACKAGE_ARCHITECTURE "darwin")
else ()
  string (TOLOWER "${CMAKE_SYSTEM_NAME}" CPACK_SYSTEM_NAME)
  if (CMAKE_CXX_FLAGS MATCHES "-m32")
    set (CPACK_PACKAGE_ARCHITECTURE i386)
  else ()
    execute_process (
      COMMAND         dpkg --print-architecture
      RESULT_VARIABLE RV
      OUTPUT_VARIABLE CPACK_PACKAGE_ARCHITECTURE
      )
    if (RV EQUAL 0)
          string (STRIP "${CPACK_PACKAGE_ARCHITECTURE}" CPACK_PACKAGE_ARCHITECTURE)
    else ()
      execute_process (COMMAND uname -m OUTPUT_VARIABLE CPACK_PACKAGE_ARCHITECTURE)
      if (CPACK_PACKAGE_ARCHITECTURE MATCHES "x86_64")
            set (CPACK_PACKAGE_ARCHITECTURE amd64)
      else ()
        set (CPACK_PACKAGE_ARCHITECTURE i386)
      endif ()
    endif ()
  endif ()
endif ()

set(CPACK_PACKAGE_NAME   "${TARGET_NAME}")
set(CPACK_PACKAGE_CONTACT "job@minhang.me")
set(CPACK_PACKAGE_VERSION "${PROJECT_VERSION}")
set(CPACK_PACKAGE_VERSION_MAJOR "${PROJECT_VERSION_MAJOR}")
set(CPACK_PACKAGE_VERSION_MINOR "${PROJECT_VERSION_MINOR}")
set(CPACK_PACKAGE_VERSION_PATCH "${PROJECT_VERSION_PATCH}")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "Apollo CyberRT")
set(CPACK_INSTALL_PREFIX              "${CMAKE_INSTALL_PREFIX}")
set(CPACK_OUTPUT_FILE_PREFIX          "packages")
set(CPACK_PACKAGE_RELOCATABLE         TRUE)
set(CPACK_MONOLITHIC_INSTALL          TRUE)
set(CPACK_PACKAGING_INSTALL_PREFIX ${CMAKE_INSTALL_PREFIX})
set(CPACK_RPM_PACKAGE_GROUP "Development/Libraries")
set(CPACK_RPM_PACKAGE_LICENSE "MIT")
set(CPACK_DEBIAN_PACKAGE_HOMEPAGE "https://github.com/minhanghuang/CyberRT")
set(CPACK_PACKAGE_FILE_NAME   "lib${CPACK_PACKAGE_NAME}")
set(CPACK_PACKAGE_FILE_NAME   "${CPACK_PACKAGE_FILE_NAME}_${CPACK_PACKAGE_VERSION}_${CPACK_PACKAGE_ARCHITECTURE}")

include(CPack)
# --------------------------------------------------------------
#                       package
# --------------------------------------------------------------
configure_file("cmake/${TARGET_NAME}.pc.in"
  "${PROJECT_BINARY_DIR}/pkgconfig/${TARGET_NAME}.pc" @ONLY)

configure_package_config_file(
  "${CMAKE_CURRENT_SOURCE_DIR}/cmake/${TARGET_NAME}-config.cmake.in"
  "cmake/${TARGET_NAME}-config.cmake"
  INSTALL_DESTINATION "${CMAKE_INSTALL_LIBDIR}/cmake/${TARGET_NAME}"
  NO_CHECK_REQUIRED_COMPONENTS_MACRO
  PATH_VARS CMAKE_INSTALL_INCLUDEDIR CMAKE_INSTALL_LIBDIR TARGET_NAME
)

write_basic_package_version_file(cmake/${TARGET_NAME}-config-version.cmake
  VERSION ${PROJECT_VERSION}
  COMPATIBILITY AnyNewerVersion
)

install(FILES
  "${PROJECT_BINARY_DIR}/pkgconfig/${TARGET_NAME}.pc"
  DESTINATION "${CMAKE_INSTALL_DATADIR}/pkgconfig"
)

install(FILES
  "${PROJECT_BINARY_DIR}/cmake/${TARGET_NAME}-config.cmake"
  "${PROJECT_BINARY_DIR}/cmake/${TARGET_NAME}-config-version.cmake"
  DESTINATION "${CMAKE_INSTALL_DATADIR}/cmake/${TARGET_NAME}"
)

install(EXPORT ${TARGET_NAME}-targets
  DESTINATION "${CMAKE_INSTALL_DATADIR}/cmake/${TARGET_NAME}"
)

# cyber .h files
install(DIRECTORY cyber/
    DESTINATION include/cyber/
    FILES_MATCHING
    PATTERN "*.h"
)

# apollo conf
file(COPY cyber/conf/
  DESTINATION ${CMAKE_BINARY_DIR}/share/conf/
)
install(DIRECTORY ${CMAKE_BINARY_DIR}/share/conf/
  DESTINATION share/conf/
)

# setup.zsh
configure_file("setup.bash.in" "${CMAKE_BINARY_DIR}/setup.bash" @ONLY)
configure_file("setup.zsh.in" "${CMAKE_BINARY_DIR}/setup.zsh" @ONLY)
install(FILES ${CMAKE_BINARY_DIR}/setup.zsh ${CMAKE_BINARY_DIR}/setup.bash
  DESTINATION .
)

# cyber python api
file(COPY cyber/python/
  DESTINATION ${CMAKE_BINARY_DIR}/${CYBER_PYTHON_PATH}
)
install(DIRECTORY ${CMAKE_BINARY_DIR}/${CYBER_PYTHON_PATH}/
  DESTINATION ${CYBER_PYTHON_PATH}
  FILES_MATCHING
  PATTERN "*.py"
)

# cyber python protobuf
file(WRITE ${CMAKE_BINARY_DIR}/${CYBER_PYTHON_PROTOBUF_PATH}/__init__.py "import os\n")
file(APPEND ${CMAKE_BINARY_DIR}/${CYBER_PYTHON_PROTOBUF_PATH}/__init__.py "import sys\n")
file(APPEND ${CMAKE_BINARY_DIR}/${CYBER_PYTHON_PROTOBUF_PATH}/__init__.py "sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))\n")
file(COPY cyber/proto/
  DESTINATION ${CMAKE_BINARY_DIR}/${CYBER_PYTHON_PROTOBUF_PATH}
  FILES_MATCHING
  PATTERN "*.py"
)

install(DIRECTORY ${CMAKE_BINARY_DIR}/${CYBER_PYTHON_PROTOBUF_PATH}/
  DESTINATION ${CYBER_PYTHON_PROTOBUF_PATH}
)

# install
install(TARGETS ${TARGET_NAME}
    EXPORT ${TARGET_NAME}-targets
    ARCHIVE DESTINATION lib
    LIBRARY DESTINATION lib
    RUNTIME DESTINATION bin
)

