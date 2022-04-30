cmake_minimum_required(VERSION 3.5)

project(CyberTransport)

find_package(PkgConfig REQUIRED)
pkg_check_modules(UUID REQUIRED IMPORTED_TARGET uuid)


add_library(cyber_transport transport.cc)
target_link_libraries(cyber_transport
    Cyber::intra_dispatcher
    cyber_notifier_factory
    cyber_underlay_message
    cyber_shm_dispatcher
    cyber_rtps_dispatcher
    )

add_library(cyber_endpoint common/endpoint.cc)
add_library(cyber_identity common/identity.cc)
target_link_libraries(cyber_identity PUBLIC ${UUID_LIBRARIES})
add_library(cyber_dispatcher dispatcher/dispatcher.cc)

add_library(cyber_intra_dispatcher dispatcher/intra_dispatcher.cc)
target_link_libraries(cyber_intra_dispatcher
    cyber_dispatcher
    )

add_library(cyber_rtps_dispatcher dispatcher/rtps_dispatcher.cc)
target_link_libraries(cyber_rtps_dispatcher cyber_sub_listener)

add_library(cyber_shm_dispatcher dispatcher/shm_dispatcher.cc)
target_link_libraries(cyber_shm_dispatcher
    Cyber::segment_factory
    cyber_segement
    cyber_message_info)

add_library(cyber_message_info message/message_info.cc)
target_link_libraries(cyber_message_info cyber_identity)

add_library(cyber_qos_profile_conf qos/qos_profile_conf.cc)

add_library(cyber_attributes_filter rtps/attributes_filler.cc)

add_library(cyber_underlay_message_type rtps/underlay_message_type.cc)
target_link_libraries(cyber_underlay_message_type ${fastrtps_LIBRARIES})

add_library(cyber_participant rtps/participant.cc)
target_link_libraries(cyber_participant
    cyber_underlay_message_type
)

add_library(cyber_sub_listener rtps/sub_listener.cc)
add_library(cyber_underlay_message rtps/underlay_message.cc)
target_link_libraries(cyber_underlay_message
    ${fastcdr_LIBRARIES}
    ${fastrtps_LIBRARIES}
)

add_library(cyber_block shm/block.cc)
add_library(cyber_condition_notifier shm/condition_notifier.cc)

add_library(cyber_muticast_notifiler shm/multicast_notifier.cc)
target_link_libraries(cyber_muticast_notifiler cyber_readable_info)

add_library(cyber_notifier_factory shm/notifier_factory.cc)
target_link_libraries(cyber_notifier_factory cyber_condition_notifier cyber_muticast_notifiler)

add_library(cyber_readable_info shm/readable_info.cc)

add_library(cyber_segement shm/segment.cc)
target_link_libraries(cyber_segement
    cyber_block
    cyber_shm_state
    cyber_shm_conf)

add_library(cyber_shm_conf shm/shm_conf.cc)
add_library(cyber_shm_state shm/state.cc)

add_library(cyber_segement_factory shm/segment_factory.cc)
target_link_libraries(cyber_segement
    Cyber::xsi_segment
    Cyber::posix_segemnt)

add_library(Cyber::segment_factory ALIAS cyber_segement_factory)

add_library(cyber_posix_segemnt shm/posix_segment.cc)
target_link_libraries(cyber_posix_segemnt rt)
add_library(Cyber::posix_segemnt ALIAS cyber_posix_segemnt)

add_library(cyber_xsi_segment shm/xsi_segment.cc)
target_link_libraries(cyber_xsi_segment cyber_shm_state)
add_library(Cyber::xsi_segment ALIAS cyber_xsi_segment)

add_library(cyber_transmitter INTERFACE)
target_link_libraries(cyber_transmitter INTERFACE cyber_endpoint)
add_library(Cyber::transmitter ALIAS cyber_transmitter)


add_library(Cyber::transport ALIAS cyber_transport)
add_library(Cyber::endpoint ALIAS cyber_endpoint)
add_library(Cyber::identity ALIAS cyber_identity)
add_library(Cyber::dispatcher ALIAS cyber_dispatcher)
add_library(Cyber::participant ALIAS cyber_participant)
add_library(Cyber::intra_dispatcher ALIAS cyber_intra_dispatcher)
add_library(Cyber::rtps_dispatcher ALIAS cyber_rtps_dispatcher)
add_library(Cyber::shm_dispatcher ALIAS cyber_shm_dispatcher)
add_library(Cyber::message_info ALIAS cyber_message_info)
add_library(Cyber::qos_profile_conf ALIAS cyber_qos_profile_conf)

# file(GLOB HEADERS *.h)

# install(FILES ${HEADERS}
#     DESTINATION ${CYBER_INSTALL_INCLUDE_DIR}/cyber/transport/
#     )

# install(DIRECTORY common dispatcher message qos rtps shm transceiver transmitter
#     DESTINATION ${CYBER_INSTALL_INCLUDE_DIR}/cyber/transport/
#     FILES_MATCHING PATTERN "*.h"
#     )

# install(TARGETS cyber_transport
#     cyber_transport
#     cyber_endpoint
#     cyber_identity
#     cyber_dispatcher
#     cyber_intra_dispatcher
#     cyber_rtps_dispatcher
#     cyber_shm_dispatcher
#     cyber_message_info
#     cyber_qos_profile_conf
#     cyber_attributes_filter
#     cyber_participant
#     cyber_sub_listener
#     cyber_underlay_message
#     cyber_underlay_message_type
#     cyber_block
#     cyber_condition_notifier
#     cyber_muticast_notifiler
#     cyber_notifier_factory
#     cyber_readable_info
#     cyber_segement
#     cyber_shm_conf
#     cyber_shm_state
#     cyber_segement_factory
#     cyber_posix_segemnt
#     cyber_xsi_segment
#     cyber_transmitter
#     DESTINATION  ${CYBER_INSTALL_LIB_DIR}
#     )
