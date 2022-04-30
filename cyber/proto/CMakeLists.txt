cmake_minimum_required(VERSION 3.5)

project(protos)
## TODO: make this with protoc

add_library(cyber_dag_conf dag_conf.pb.cc)
target_link_libraries(cyber_dag_conf Cyber::component_conf)
add_library(Cyber::dag_conf ALIAS cyber_dag_conf)

add_library(cyber_component_conf component_conf.pb.cc)
target_link_libraries(cyber_component_conf Cyber::qos_profile)
add_library(Cyber::component_conf ALIAS cyber_component_conf)

add_library(cyber_choreography choreography_conf.pb.cc)
add_library(Cyber::choreography_conf ALIAS cyber_choreography)

add_library(cyber_classic_conf classic_conf.pb.cc)
add_library(Cyber::classic_conf ALIAS cyber_classic_conf)

add_library(cyber_conf cyber_conf.pb.cc)
target_link_libraries(cyber_conf
    cyber_run_mode_conf
    cyber_transport_conf
    cyber_scheduler_conf
    cyber_perf_conf
    )
add_library(Cyber::cyber_conf ALIAS cyber_conf)

add_library(cyber_qos_profile qos_profile.pb.cc)
add_library(Cyber::qos_profile ALIAS cyber_qos_profile)

add_library(cyber_role_attributes role_attributes.pb.cc)
target_link_libraries(cyber_role_attributes Cyber::qos_profile)
add_library(Cyber::role_attributes ALIAS cyber_role_attributes)

add_library(cyber_pb_parameter parameter.pb.cc)
add_library(Cyber::pb_parameter ALIAS cyber_pb_parameter)

add_library(cyber_run_mode_conf run_mode_conf.pb.cc)
add_library(Cyber::run_mode_conf ALIAS cyber_run_mode_conf)

add_library(cyber_scheduler_conf scheduler_conf.pb.cc)
#target_include_directories(cyber_scheduler_conf ${Protobuf_INCLUDE_DIR})
target_link_libraries(cyber_scheduler_conf ${Protobuf_LIBRARY})
add_library(Cyber::scheduler_conf ALIAS cyber_scheduler_conf)

add_library(cyber_perception  perception.pb.cc)
add_library(Cyber::perception  ALIAS cyber_perception)

add_library(cyber_proto_desc proto_desc.pb.cc)
add_library(Cyber::proto_desc ALIAS cyber_proto_desc)

add_library(cyber_pb_record record.pb.cc)
add_library(Cyber::pb_record ALIAS cyber_pb_record)

add_library(cyber_topology_change topology_change.pb.cc)
target_link_libraries(cyber_topology_change
    ${Protobuf_LIBRARY}
    Cyber::role_attributes)
add_library(Cyber::topology_change ALIAS cyber_topology_change)


add_library(cyber_transport_conf transport_conf.pb.cc)
add_library(Cyber::transport_conf ALIAS cyber_transport_conf)

add_library(cyber_unit_test unit_test.pb.cc)
add_library(Cyber::unit_test ALIAS cyber_unit_test)

add_library(cyber_perf_conf perf_conf.pb.cc)
add_library(Cyber::perf_conf ALIAS cyber_perf_conf)

# file(GLOB HEADERS *.pb.h)

# install(FILES ${HEADERS}
#     DESTINATION ${CYBER_INSTALL_INCLUDE_DIR}/cyber/proto/
#     )

# install(TARGETS
#     cyber_choreography
#     cyber_classic_conf
#     cyber_component_conf
#     cyber_conf
#     cyber_dag_conf
#     cyber_pb_parameter
#     cyber_perception
#     cyber_perf_conf
#     cyber_proto_desc
#     cyber_qos_profile
#     cyber_pb_record
#     cyber_role_attributes
#     cyber_run_mode_conf
#     cyber_scheduler_conf
#     cyber_topology_change
#     cyber_transport_conf
#     cyber_unit_test
#     DESTINATION  ${CYBER_INSTALL_LIB_DIR}
#     )
