#!/bin/bash

WORKSPACE_DIR=$(dirname $(realpath "$0"))

function install_3rd_deps() {
    if [[ ! -d $WORKSPACE_DIR/install ]]; then
        bash $WORKSPACE_DIR/scripts/install.sh 
    fi
}

function source_env() {
    unset LD_LIBRARY_PATH
    SHELL=$(ps -h -o comm -p $$)
    if [[ "$SHELL" == "zsh" ]]; then
        source $WORKSPACE_DIR/install/setup.zsh
    fi
    if [[ "$SHELL" == "bash" ]]; then
        source $WORKSPACE_DIR/install/setup.bash
    fi
}

function build() {
    cmake -S. -Bbuild
    CMAKE_GENERATOR="@CMAKE_GENERATOR"
    pushd $WORKSPACE_DIR/build > /dev/null;
        if [[ -f "build.ninja" ]]; then
                ninja
        else 
                make -j$(nproc)
        fi
    popd > /dev/null;
}

install_3rd_deps
source_env
build


