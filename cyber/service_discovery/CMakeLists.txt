cmake_minimum_required(VERSION 3.5)

project(CyberServiceDiscovery)

add_library(cyber_service_manager specific_manager/service_manager.cc)
target_link_libraries(cyber_service_manager
    cyber_qos_profile
    Cyber::manager
    Cyber::role
    Cyber::transport
    ${fastrtps_LIBRARIES}
    Cyber::multi_value_warehouse
)
add_library(Cyber::service_manager ALIAS cyber_service_manager)

add_library(cyber_single_value_warehouse container/single_value_warehouse.cc)
add_library(Cyber::single_value_warehouse ALIAS cyber_single_value_warehouse)

add_library(cyber_participant_listener communication/participant_listener.cc)
add_library(Cyber::participant_listener ALIAS cyber_participant_listener)

add_library(cyber_channel_manager specific_manager/channel_manager.cc)
target_link_libraries(cyber_channel_manager
    cyber_protobuf_factory
    Cyber::graph
)
add_library(Cyber::channel_manager ALIAS cyber_channel_manager)

add_library(cyber_node_manager specific_manager/node_manager.cc)
target_link_libraries(cyber_node_manager INTERFACE ${fastrtps_LIBRARIES})
add_library(Cyber::node_manager ALIAS cyber_node_manager)

add_library(cyber_topology_manager topology_manager.cc)
target_link_libraries(cyber_topology_manager
    PUBLIC
    Cyber::service_manager
    Cyber::single_value_warehouse
    Cyber::participant_listener
    Cyber::channel_manager
    Cyber::time
    Cyber::transport
    Cyber::participant
    Cyber::node_manager
    cyber_topology_change
)
# add_dependencies(cyber_topology_manager ${fastrtps_LIBRARIES})


add_library(cyber_subscriber_listener communication/subscriber_listener.cc)

add_library(cyber_graph container/graph.cc)

add_library(cyber_multi_value_warehouse container/multi_value_warehouse.cc)


add_library(cyber_role role/role.cc)

add_library(cyber_manager specific_manager/manager.cc)
# add_dependencies(cyber_manager ${fastrtps_LIBRARIES})
target_link_libraries(cyber_manager INTERFACE ${fastrtps_LIBRARIES}
    cyber_qos_profile_conf
    cyber_attributes_filter
    Cyber::subscriber_listener
    Cyber::transport
    ${fastrtps_LIBRARIES}
    ${FastRTPS_LIBRARY}
)






add_library(Cyber::topology_manager ALIAS cyber_topology_manager)
add_library(Cyber::subscriber_listener ALIAS cyber_subscriber_listener)
add_library(Cyber::graph ALIAS cyber_graph)
add_library(Cyber::multi_value_warehouse ALIAS cyber_multi_value_warehouse)
add_library(Cyber::role ALIAS cyber_role)
add_library(Cyber::manager ALIAS cyber_manager)


# file( GLOB HEADERS *.h communication/*.h container/*.h role/*.h  specific_manager/*.h )

# install(FILES ${HEADERS}
#     DESTINATION ${CYBER_INSTALL_INCLUDE_DIR}/cyber/service_discovery/
#     )

# install(TARGETS
#     cyber_topology_manager
#     cyber_participant_listener
#     cyber_subscriber_listener
#     cyber_graph
#     cyber_multi_value_warehouse
#     cyber_single_value_warehouse
#     cyber_role
#     cyber_manager
#     cyber_channel_manager
#     cyber_node_manager
#     cyber_service_manager
#     DESTINATION  ${CYBER_INSTALL_LIB_DIR}
#     )
