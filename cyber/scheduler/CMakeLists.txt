cmake_minimum_required(VERSION 3.5)

project(CyberScheduler)

add_library(cyber_scheduler_factory scheduler_factory.cc)
target_link_libraries(cyber_scheduler_factory
    cyber_scheduler_classic
    cyber_scheduler_choreography
    )

add_library(cyber_scheduler scheduler.cc)
target_link_libraries(cyber_scheduler
    cyber_scheduler_factory
    cyber_pin_thread
    )

add_library(cyber_processor processor.cc)
add_library(cyber_processor_context processor_context.cc)

add_library(cyber_choreography_context policy/choreography_context.cc)

add_library(cyber_scheduler_choreography policy/scheduler_choreography.cc)
target_link_libraries(cyber_scheduler_choreography
    Cyber::choreography_conf
    cyber_choreography_context)

add_library(cyber_classic_context policy/classic_context.cc)
target_link_libraries(cyber_classic_context  Cyber::processor_context)

add_library(cyber_scheduler_classic policy/scheduler_classic.cc)
target_link_libraries(cyber_scheduler_classic
    Cyber::processor
    Cyber::classic_conf
    Cyber::classic_context)

add_library(cyber_pin_thread common/pin_thread.cc)
add_library(Cyber::pin_thread ALIAS cyber_pin_thread)

add_library(Cyber::classic_context ALIAS cyber_classic_context)
add_library(Cyber::scheduler ALIAS cyber_scheduler)
add_library(Cyber::scheduler_factory ALIAS cyber_scheduler_factory)
add_library(Cyber::processor ALIAS cyber_processor)
add_library(Cyber::processor_context ALIAS cyber_processor_context)
#TODO: add more alias

# file(GLOB HEADERS *.h)

# install(FILES ${HEADERS}
#     DESTINATION ${CYBER_INSTALL_INCLUDE_DIR}/cyber/scheduler/
#     )

# install(TARGETS cyber_scheduler
#     cyber_scheduler_factory
#     cyber_scheduler
#     cyber_processor
#     cyber_processor_context
#     cyber_choreography_context
#     cyber_scheduler_choreography
#     cyber_classic_context
#     cyber_scheduler_classic
#     cyber_pin_thread
#     DESTINATION  ${CYBER_INSTALL_LIB_DIR}
#     )
