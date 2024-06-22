#!/usr/bin/env python3
import subprocess
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
        print("[command] {}".format(command))
        subprocess.run(command, shell=True, env=self.environment)

    def start(self):
        self._clone_setup()
        self._clone_nlohmann_json()
        self._clone_tinyxml2()
        self._clone_gfamily()
        self._clone_dds()

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
        subprocess.run(command, shell=True)

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
            "cmake -DCMAKE_CXX_FLAGS='-fPIC' -DCMAKE_INSTALL_PREFIX={} -DBUILD_SHARED_LIBS=ON ..".format(
                self._install_prefix))
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

def parse_config():
    parser = argparse.ArgumentParser(description="install")
    parser.add_argument("--platform", type=str, default=platform.machine(), help="platform")
    parser.add_argument("--install_prefix", type=str, default="install", help="install prefix")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_config()
    print(f"args.platform: {args.platform}, args.install_prefix: {args.install_prefix}")
    time.sleep(3)
    install = Install(args.platform, args.install_prefix)
    install.start()
