#!/bin/bash


set -e

current_path=$(cd $(dirname $0) && pwd)
install_prefix="$current_path/../install/"
ARCH=$(uname -m)

function download() {
  URL=$1
  LIB_NAME=$2
  DOWNLOAD_PATH="$current_path/../third_party/$LIB_NAME/"
  if [ -e $DOWNLOAD_PATH ]
  then
    echo ""
  else
    echo "############### Install $LIB_NAME $URL ################"
    git clone $URL "$DOWNLOAD_PATH"
  fi
}

function build_setup() {
  echo "############### Build Setup. ################"
  local NAME="setup"
  download "https://github.com/minhanghuang/setup.git" "$NAME"
  pushd "$current_path/../third_party/$NAME/"
  mkdir -p build && cd build
  cmake -DCMAKE_INSTALL_PREFIX=$install_prefix -DBUILD_SHARED_LIBS=ON ..
  make install
  popd
}

# function build_tinyxml2() {
#   echo "############### Build Tinyxml2. ################"
#   local NAME="tinyxml2"
#   download "https://github.com/leethomason/tinyxml2.git" "$NAME"
#   pushd "$current_path/../third_party/$NAME/"
#   git checkout 9.0.0
#   mkdir -p build && cd build
#   cmake -DCMAKE_INSTALL_PREFIX=$install_prefix ..
#   make -j8
#   make install
#   popd
# }

function build_fastdds() {
  echo "############### Build Fast-DDS. ################"
  download "https://github.com/eProsima/Fast-RTPS.git" "Fast-RTPS"
  pushd "$current_path/../third_party/Fast-RTPS/"
  git checkout v1.5.0
  git submodule init
  git submodule update
  # patch -p1 < "$current_path/../scripts/FastRTPS_1.5.0.patch"
  mkdir -p build && cd build
  cmake -DEPROSIMA_BUILD=ON -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=$install_prefix ..
  make -j$(nproc)
  make install
  popd
}

function build_gfamily() {
  echo "############### Build Google Libs. ################"
  download "https://github.com/gflags/gflags.git" "gflags"
  download "https://github.com/google/glog.git" "glog"
  download "https://github.com/google/googletest.git" "googletest"
  download "https://github.com/protocolbuffers/protobuf.git" "protobuf"

  # gflags
  pushd "$current_path/../third_party/gflags/"
  git checkout v2.2.0
  mkdir -p build && cd build
  CXXFLAGS="-fPIC" cmake -DCMAKE_INSTALL_PREFIX=$install_prefix -DBUILD_SHARED_LIBS=ON ..
  make -j$(nproc)
  make install
  popd

  # glog
  pushd "$current_path/../third_party/glog/"
  git checkout v0.3.5
  mkdir -p build && cd build
  if [ "$ARCH" == "x86_64" ]; then
    CXXFLAGS="-fPIC" cmake -DCMAKE_INSTALL_PREFIX=$install_prefix -DBUILD_SHARED_LIBS=ON ..
  elif [ "$ARCH" == "aarch64" ]; then
    CXXFLAGS="-fPIC" cmake --build=armv8-none-linux -DCMAKE_INSTALL_PREFIX=$install_prefix -DBUILD_SHARED_LIBS=ON ..
  else
      echo "not support $ARCH"
  fi
  make -j$(nproc)
  make install
  popd
  
  # googletest
  pushd "$current_path/../third_party/googletest/"
  git checkout release-1.10.0
  mkdir -p build && cd build
  CXXFLAGS="-fPIC" cmake -DCMAKE_INSTALL_PREFIX=$install_prefix -DBUILD_SHARED_LIBS=ON ..
  make -j8
  make install
  popd

  # protobuf
  pushd "$current_path/../third_party/protobuf/"
  git checkout v3.14.0
  ./autogen.sh
  ./configure --prefix=$install_prefix --enable-shared
  make -j$(nproc)
  make install
  popd
}

function main() {
  echo "############### Install Third Party. ################"
  build_setup
  # build_tinyxml2
  build_fastdds
  # build_gfamily
  return
}

main "$@"
