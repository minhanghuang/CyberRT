export CYBER_PATH=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
binary_path="$CYBER_PATH/bin"
lib_path="$CYBER_PATH/lib"
proto_path="$CYBER_PATH/../../lib"

PYTHON_LD_PATH="/apollo/bazel-bin/cyber/py_wrapper"

qt_path=/usr/local/Qt5.5.1/5.5/gcc_64
export LD_LIBRARY_PATH=${proto_path}:${lib_path}:$LD_LIBRARY_PATH
export QT_QPA_PLATFORM_PLUGIN_PATH=${qt_path}/plugins
export PATH=${binary_path}:${recorder_path}:${monitor_path}:${launch_path}:${channel_path}:${node_path}:${service_path}:${qt_path}/bin:${visualizer_path}:${rosbag_to_record_path}:$PATH
export PYTHONPATH=${PYTHON_LD_PATH}:${CYBER_PATH}/python:$PYTHONPATH

export CYBER_DOMAIN_ID=80
export CYBER_IP=127.0.0.1

export GLOG_log_dir=$CYBER_PATH/log
export GLOG_alsologtostderr=0
export GLOG_colorlogtostderr=1
export GLOG_minloglevel=0

export sysmo_start=0

# for DEBUG log
#export GLOG_minloglevel=-1
#export GLOG_v=4

#source ${CYBER_PATH}/tools/cyber_tools_auto_complete.bash
