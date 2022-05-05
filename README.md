# Apollo(v7.0.0) Cyber 

![example](docs/example.png)

## #1 env

```shell
Ubuntu18
```

```shell
sudo apt install libpoco-dev
sudo apt install uuid-dev
sudo apt install libtinyxml2-dev 
```


## #2 build

1. download

```shell
git clone https://github.com/minhanghuang/CyberRT.git
cd CyberRT
```

2. export library path

> third party(gflag gtest glog fastrtps fastcdr...)

```shell
sudo mkdir /opt/cyber
sudo cp -r env/ /opt/cyber/env
```

```shell
// bash 
source /opt/cyber/env/setup.bash

// zsh 
source /opt/cyber/env/setup.zsh
```

3. generate protobuf

```shell
/opt/cyber/env/bin/protoc -I=cyber/proto/ --cpp_out=cyber/proto cyber/proto/*.proto

/opt/cyber/env/bin/protoc -I=cyber/examples/proto/ --cpp_out=cyber/examples/proto cyber/examples/proto/*.proto
```

4. build

```shell
mkdir build && cd build
cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON ..
make 
```

5. run examples

```shell
export GLOG_alsologtostderr=1
export CYBER_PATH=cyber/
./cyber/examples/cyber_example_talker
```

```shell
export GLOG_alsologtostderr=1
export CYBER_PATH=cyber/
./cyber/examples/cyber_example_talker
```
