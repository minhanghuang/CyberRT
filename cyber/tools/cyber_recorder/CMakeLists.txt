cmake_minimum_required(VERSION 3.5)
project(CyberRecorder)

add_executable(cyber_recorder
    player/player.cc
    player/play_task.cc
    player/play_task_buffer.cc
    player/play_task_consumer.cc
    player/play_task_producer.cc
    info.cc
    main.cc
    recorder.cc
    recoverer.cc
    spliter.cc
    )

target_link_libraries(cyber_recorder
    pthread
    gflags
    Cyber::pb_record
    Cyber::record_reader
    Cyber::record_viewer
    Cyber::record_writer
    Cyber::init
    Cyber::component_base
    Cyber::core
    Cyber::blocker_manager
    Cyber::endpoint
    )

file(GLOB HEADERS *.h)

install(FILES ${HEADERS}
    DESTINATION ${CYBER_INSTALL_INCLUDE_DIR}/cyber/monitor
    )

install(TARGETS cyber_recorder
    DESTINATION  ${CYBER_INSTALL_DIR}/bin
    )

