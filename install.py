#!/usr/bin/env python3
import subprocess
import re
import os
import argparse
import time
import platform

class Install:

    def __init__(self, platform, install_prefix) -> None:
        self._machine = platform
        self._home_path = os.path.expanduser("~")
        self._current_path = os.path.abspath(os.path.dirname(__file__))
        self._dowload_path = os.path.join(self._current_path, "third_party")
        self._install_prefix = os.path.join(self._current_path, "install")
        if (install_prefix != "install"):
            self._install_prefix = install_prefix

        if not os.path.exists(self._install_prefix):
            os.makedirs(self._install_prefix)

        self.environment = self._load_environment()

    def _load_environment(self):
        '''
            In case of cross-compilation, we need to load the environment setup file
        :return: env
        '''
        env = os.environ.copy()
        return env


    def _cmd(self, command):
        """执行系统命令，使用指定的环境变量"""
        if command is None:
            return None
        print("[command] {}".format(command))
        subprocess.run(command, shell=True, env=self.environment)

    def start(self):
        self._clone_gcc()
        self._clone_cmake()
        self._clone_setup()
        self._clone_tinyxml2()
        # # self._clone_dds()
        self._clone_dds2()
        self._clone_nlohmann_json()
        self._clone_proj() # ros_bridge of apollo v10
        self._clone_gfamily()
        self._clone_gperftools() # apollo v10
        self._unpack_bvar() # apollo v10

    def _clone_github_repo(self, repo_url, repo_name, *args):
        dowload_path = os.path.join(self._dowload_path, repo_name)
        if os.path.exists(dowload_path):
            print("repo exists: {}".format(dowload_path))
            return None
        command = "git clone {} {}".format(
            repo_url,
            dowload_path
        )
        for arg in args:
            command += " " + arg
        print("clone: {}".format(command))
        result = subprocess.run(command, shell=True)
        if result.returncode != 0:
            print("clone failed: {}".format(repo_url))
            raise Exception("clone failed: {}".format(repo_url))

    def _clone_setup(self):
        self._clone_github_repo(
            "https://github.com/minhanghuang/setup.git",
            "setup",
            "--depth=1"
        )
        os.chdir(os.path.join(self._dowload_path, "setup"))
        self._cmd("mkdir -p build")
        os.chdir("build")
        self._cmd(
            "cmake -DCMAKE_INSTALL_PREFIX={} ..".format(self._install_prefix))
        self._cmd("make install -j$(nproc)")
        os.chdir(self._current_path)

    def _clone_gcc(self):
        print("start to install gcc")
        gcc_version = "0.0"
        try:
            result = subprocess.run(['gcc', '--version'], stdout=subprocess.PIPE, universal_newlines=True, check=True)
            output = result.stdout.splitlines()[0]
            match = re.search(r'(\d+\.\d+\.\d+)', output)
            if match:
                gcc_version = match.group(1)
                print(f"GCC version: {gcc_version}")
            if "8.1" < gcc_version:
                print("GCC version is greater than or equal to 8.1.0, skip installation")
                return None
        except Exception as e:
            print("gcc error: {}".format(e))

        self._cmd("sudo apt update")
        self._cmd("sudo apt install -y software-properties-common")
        self._cmd("sudo add-apt-repository -y ppa:ubuntu-toolchain-r/test")
        self._cmd("sudo apt update")
        self._cmd("sudo apt install -y gcc-9 g++-9")
        self._cmd("sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 100")
        self._cmd("sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-9 100")
        self._cmd("sudo ldconfig")
        self._cmd("gcc --version")
        self._cmd("g++ --version")
        return None

    def _clone_cmake(self):
        print("start to install cmake")
        cmake_version = "0.0.0"
        try:
            result = subprocess.run(['cmake', '--version'], stdout=subprocess.PIPE, universal_newlines=True, check=True)
            output = result.stdout.splitlines()[0]
            match = re.search(r'(\d+\.\d+\.\d+)', output)
            if match:
                cmake_version = match.group(1)
                print(f"CMake version: {cmake_version}")
            if "3.20" < cmake_version:
                print("CMake version is greater than 3.20, skip installation")
                return None
        except Exception as e:
            print("cmake error: {}".format(e))

        cmake_name = "cmake-3.22.0-linux-x86_64"
        if "x86_64" == self._machine:
            pass
        else:
            cmake_name = "cmake-3.22.0-linux-aarch64"
        print("CMake version is less than 3.20, start installation ({})".format(cmake_name))
        self._cmd("wget -t 10 {} -P {}".format("https://cmake.org/files/v3.22/{}.tar.gz".format(cmake_name), self._dowload_path))
        os.chdir(self._dowload_path)
        self._cmd("tar -zxvf {}.tar.gz".format(cmake_name))
        self._cmd("cp -r {}/bin/* /usr/local/bin".format(cmake_name))
        self._cmd("cp -r {}/doc/* /usr/local/doc".format(cmake_name))
        self._cmd("cp -r {}/share/* /usr/local/share".format(cmake_name))
        self._cmd("rm -rf {}*".format(cmake_name))
        self._cmd("sudo ldconfig")
        self._cmd("cmake --version")
        os.chdir(self._current_path)
        return None

    def _clone_nlohmann_json(self):
        self._clone_github_repo(
            "https://github.com/nlohmann/json.git",
            "nlohmann_json",
            "--depth=1"
        )
        os.chdir(os.path.join(self._dowload_path, "nlohmann_json"))
        self._cmd("mkdir -p build")
        os.chdir("build")
        self._cmd(
            "cmake -DCMAKE_INSTALL_PREFIX={} -DBUILD_SHARED_LIBS=ON ..".format(self._install_prefix))
        self._cmd("make install -j$(nproc)")
        os.chdir(self._current_path)

    def _clone_tinyxml2(self):
        self._clone_github_repo(
            "https://github.com/leethomason/tinyxml2.git",
            "tinyxml2",
            "--single-branch",
            "--branch=8.0.0",
            "--depth=1"
        )
        os.chdir(os.path.join(self._dowload_path, "tinyxml2"))
        self._cmd("mkdir -p build")
        os.chdir("build")
        self._cmd(
            "cmake -DCMAKE_INSTALL_PREFIX={} -DBUILD_SHARED_LIBS=ON ..".format(self._install_prefix))
        self._cmd("make install -j$(nproc)")
        os.chdir(self._current_path)

    def _clone_gperftools(self):
        self._clone_github_repo(
            "https://github.com/gperftools/gperftools.git",
            "gperftools",
            "--single-branch",
            "--branch=gperftools-2.8",
            "--depth=1"
        )
        os.chdir(os.path.join(self._dowload_path, "gperftools"))
        self._cmd("./autogen.sh || sleep 1 && ./autogen.sh")
        self._cmd(
            "./configure --disable-libunwind --prefix={} --libdir={}".format(
                self._install_prefix, os.path.join(self._install_prefix, "lib")
            )
        )
        self._cmd("make install -j$(nproc)")
        os.chdir(self._current_path)

        return None

    def _clone_proj(self):
        self._clone_github_repo(
            "https://github.com/OSGeo/PROJ.git",
            "PROJ",
            "--single-branch",
            "--branch=7.1.0",
            "--depth=1"
        )
        os.chdir(os.path.join(self._dowload_path, "PROJ"))
        self._cmd("patch -p1 < {}".format(os.path.join(self._current_path,"scripts/PROJ-7.1.0.patch")))
        self._cmd("mkdir -p build")
        os.chdir("build")
        self._cmd(
            "cmake -DBUILD_TESTING=OFF -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX={} -DBUILD_SHARED_LIBS=ON ..".format(
                self._install_prefix
            )
        )
        self._cmd("make install -j$(nproc)")
        os.chdir(self._current_path)

        return None

    def _clone_gfamily(self):
        self._clone_github_repo(
            "https://github.com/gflags/gflags.git",
            "gflags",
            "--single-branch",
            "--branch=v2.2.0",
            "--depth=1"
        )
        self._clone_github_repo(
            "https://github.com/google/glog.git",
            "glog",
            "--single-branch",
            "--branch=v0.4.0",
            "--depth=1"
        )
        self._clone_github_repo(
            "https://github.com/google/googletest.git",
            "googletest",
            "--single-branch",
            "--branch=release-1.10.0",
            "--depth=1"
        )
        self._clone_github_repo(
            "https://github.com/protocolbuffers/protobuf.git",
            "protobuf",
            "--single-branch",
            "--branch=v3.14.0",
            "--depth=1"
        )

        os.chdir(os.path.join(self._dowload_path, "gflags"))
        self._cmd("mkdir -p build")
        os.chdir("build")
        self._cmd(
            "cmake -DCMAKE_CXX_FLAGS='-fPIC' -DREGISTER_INSTALL_PREFIX=OFF -DCMAKE_INSTALL_PREFIX={} -DBUILD_SHARED_LIBS=ON ..".format(
                self._install_prefix
            )
        )
        self._cmd("make install -j$(nproc)")
        os.chdir(self._current_path)

        os.chdir(os.path.join(self._dowload_path, "glog"))
        self._cmd("mkdir -p build")
        os.chdir("build")
        self._cmd(
            "cmake -DCMAKE_CXX_FLAGS='-fPIC' -DCMAKE_INSTALL_PREFIX={} -DBUILD_SHARED_LIBS=ON ..".format(
                self._install_prefix))
        self._cmd("make install -j$(nproc)")
        os.chdir(self._current_path)

        os.chdir(os.path.join(self._dowload_path, "googletest"))
        self._cmd("mkdir -p build")
        os.chdir("build")
        self._cmd(
            "cmake -DCMAKE_CXX_FLAGS='-fPIC -w' -DCMAKE_INSTALL_PREFIX={} -DBUILD_SHARED_LIBS=ON ..".format(
                self._install_prefix))
        self._cmd("make install -j$(nproc)")
        os.chdir(self._current_path)

        os.chdir(os.path.join(self._dowload_path, "protobuf"))
        os.chdir("cmake")
        self._cmd("mkdir -p build")
        os.chdir("build")
        self._cmd(
            "cmake -Dprotobuf_BUILD_SHARED_LIBS=ON -Dprotobuf_BUILD_TESTS=OFF -DCMAKE_INSTALL_PREFIX={} ..".format(
                self._install_prefix))
        self._cmd("make install -j$(nproc)")
        os.chdir(self._current_path)

    def _clone_dds(self):
        # self._clone_github_repo(
        #     "https://github.com/eProsima/Fast-RTPS.git",
        #     "Fast-RTPS",
        #     "--single-branch",
        #     "--branch=v1.5.0",
        #     "--depth=1"
        # )
        # os.chdir(os.path.join(self._dowload_path, "Fast-RTPS"))
        # self._cmd("git submodule update --init")
        # self._cmd("patch -p1 < {}".format(os.path.join(self._current_path,
        #           "scripts/FastRTPS_1.5.0.patch")))
        # self._cmd("mkdir -p build")
        # self._cmd(
        #     "cmake -DEPROSIMA_BUILD=ON -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX={} ..".format(
        #         self._install_prefix))
        # os.chdir(self._current_path)

        dds_name = "fast-rtps-1.5.0-1.prebuilt.x86_64.tar.gz"
        if "x86_64" == self._machine:
            pass
        else:
            dds_name = "fast-rtps-1.5.0-1.prebuilt.aarch64.tar.gz"

        if not os.path.exists(os.path.join(self._dowload_path, dds_name)):
            self._cmd(
                "wget -t 10 {} -P {}".format(
                    "https://apollo-system.cdn.bcebos.com/archive/6.0/{}".format(dds_name),
                    self._dowload_path),
            )

        os.chdir(self._dowload_path)
        self._cmd("tar -zxvf {}".format(dds_name))
        self._cmd("cp -r fast-rtps-1.5.0-1/* {}".format(self._install_prefix))
        self._cmd("rm -rf fast-rtps-1.5.0-1/")
        os.chdir(self._current_path)

    def _clone_dds2(self):
        self._clone_github_repo(
            "https://github.com/chriskohlhoff/asio.git",
            "asio",
            "--single-branch",
            "--branch=asio-1-18-1",
            "--depth=1"
        )
        self._clone_github_repo(
            "https://github.com/eProsima/foonathan_memory_vendor.git",
            "foonathan_memory_vendor",
            "--single-branch",
            "--branch=v1.3.1",
            "--depth=1"
        )
        self._clone_github_repo(
            "https://github.com/eProsima/Fast-CDR.git",
            "Fast-CDR",
            "--single-branch",
            "--branch=v2.2.2",
            "--depth=1"
        )
        self._clone_github_repo(
            "https://github.com/eProsima/Fast-DDS.git",
            "Fast-DDS",
            "--single-branch",
            "--branch=v2.14.3",
            "--depth=1"
        )
        os.chdir(os.path.join(self._dowload_path, "asio/asio"))
        self._cmd("./autogen.sh")
        self._cmd("./configure --prefix={}".format(self._install_prefix))
        self._cmd("make install -j$(nproc)")
        os.chdir(self._current_path)

        os.chdir(os.path.join(self._dowload_path, "foonathan_memory_vendor"))
        self._cmd("mkdir -p build")
        os.chdir("build")
        self._cmd("cmake -DCMAKE_INSTALL_PREFIX={} -DBUILD_SHARED_LIBS=ON ..".format(
                self._install_prefix))
        self._cmd("make install -j$(nproc)")
        os.chdir(self._current_path)

        os.chdir(os.path.join(self._dowload_path, "Fast-CDR"))
        self._cmd("patch -p1 < {}".format(os.path.join(self._current_path,"scripts/Fast-CDR_v2.2.2.patch")))
        self._cmd("mkdir -p build")
        os.chdir("build")
        self._cmd("cmake -DCMAKE_INSTALL_PREFIX={} -DBUILD_SHARED_LIBS=ON ..".format(
                self._install_prefix))
        self._cmd("make install -j$(nproc)")
        os.chdir(self._current_path)

        os.chdir(os.path.join(self._dowload_path, "Fast-DDS"))
        self._cmd("mkdir -p build")
        os.chdir("build")
        self._cmd("cmake -DCMAKE_INSTALL_PREFIX={} -DBUILD_SHARED_LIBS=ON ..".format(
                self._install_prefix))
        self._cmd("make install -j$(nproc)")
        os.chdir(self._current_path)

        return None

    def _unpack_bvar(self):
        download_url = "https://raw.githubusercontent.com/wiki/minhanghuang/CyberRT/libs"
        bvar_name = "bvar_9.0.0-rc-r2_amd64.deb"
        if "x86_64" == self._machine:
            pass
        else:
            bvar_name = "bvar_9.0.0-rc-r3_arm64.deb"
        download_url = download_url + "/" + bvar_name
        self._cmd("wget -t 10 {} -O {}".format(download_url, os.path.join(self._dowload_path, "bvar.deb")))
        self._cmd("dpkg -x {} {}".format(os.path.join(self._dowload_path, "bvar.deb"), os.path.join(self._dowload_path, "bvar")))
        self._cmd("cp -r {}* {}".format(os.path.join(self._dowload_path, "bvar/usr/local/"), self._install_prefix))
        return None

def parse_config():
    parser = argparse.ArgumentParser(description="install")
    parser.add_argument("--platform", type=str, default=platform.machine(), help="platform")
    parser.add_argument("--install_prefix", type=str, default="install", help="install prefix")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_config()
    print(f"args.platform: {args.platform}, args.install_prefix: {args.install_prefix}")
    # time.sleep(3)
    install = Install(args.platform, args.install_prefix)
    install.start()
