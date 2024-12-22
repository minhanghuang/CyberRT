/******************************************************************************
 * Copyright 2018 The Apollo Authors. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *****************************************************************************/

#include "cyber/mainboard/module_argument.h"

#include "cyber/common/environment.h"

#include <getopt.h>
#include <libgen.h>

#if __has_include("gperftools/profiler.h")
#include "gperftools/profiler.h"
#endif

using apollo::cyber::common::GlobalData;

namespace apollo {
namespace cyber {
namespace mainboard {

void ModuleArgument::DisplayUsage() {
  AINFO << "Usage: \n    " << binary_name_ << " [OPTION]...\n"
        << "Description: \n"
        << "    -h, --help: help information \n"
        << "    -d, --dag_conf=CONFIG_FILE: module dag config file\n"
        << "    -p, --process_group=process_group: the process "
           "namespace for running this module, default in manager process\n"
        << "    -s, --sched_name=sched_name: sched policy "
           "conf for hole process, sched_name should be conf in cyber.pb.conf\n"
        << "    --plugin=plugin_description_file_path: the description file of "
           "plugin\n"
        << "    --disable_plugin_autoload : default enable autoload "
           "mode of plugins, use disable_plugin_autoload to ingore autoload\n"
        << "    -c, --cpuprofile: enable gperftools cpu profile\n"
        << "    -o, --profile_filename=filename: the filename to dump the "
           "profile to, default value is ${process_group}_cpu.prof. Only work "
           "with -c option\n"
        << "    -H, --heapprofile: enable gperftools heap profile\n"
        << "    -O, --heapprofile_filename=filename: the filename to dump the "
           "profile to, default value is ${process_group}_mem.prof. Only work "
           "with -c option\n"
        << "Example:\n"
        << "    " << binary_name_ << " -h\n"
        << "    " << binary_name_ << " -d dag_conf_file1 -d dag_conf_file2 "
        << "-p process_group -s sched_name\n"
        << "    " << binary_name_ << " --plugin plugin_xml_conf -d dag_conf ";
}

void ModuleArgument::ParseArgument(const int argc, char* const argv[]) {
  binary_name_ = std::string(basename(argv[0]));
  GetOptions(argc, argv);

  if (process_group_.empty()) {
    process_group_ = DEFAULT_process_group_;
  }

  if (sched_name_.empty()) {
    sched_name_ = DEFAULT_sched_name_;
  }

  if (enable_cpuprofile_ && profile_filename_.empty()) {
    auto pwd = common::GetEnv("PWD");
    profile_filename_ = pwd + "/" + process_group_ + std::string("_cpu.prof");
  }

  if (profile_filename_[0] != '/') {
    auto pwd = common::GetEnv("PWD");
    profile_filename_ = pwd + "/" + profile_filename_;
  }

  if (enable_heapprofile_ && heapprofile_filename_.empty()) {
    auto pwd = common::GetEnv("PWD");
    heapprofile_filename_ =
        pwd + "/" + process_group_ + std::string("_mem.prof");
  }

  if (heapprofile_filename_[0] != '/') {
    auto pwd = common::GetEnv("PWD");
    heapprofile_filename_ = pwd + "/" + heapprofile_filename_;
  }

  GlobalData::Instance()->SetProcessGroup(process_group_);
  GlobalData::Instance()->SetSchedName(sched_name_);
  AINFO << "binary_name_ is " << binary_name_ << ", process_group_ is "
        << process_group_ << ", has " << dag_conf_list_.size() << " dag conf";
  for (std::string& dag : dag_conf_list_) {
    AINFO << "dag_conf: " << dag;
  }
}

void ModuleArgument::GetOptions(const int argc, char* const argv[]) {
  opterr = 0;  // extern int opterr
  int long_index = 0;
  const std::string short_opts = "hd:p:s:co:HO:";
  static const struct option long_opts[] = {
      {"help", no_argument, nullptr, 'h'},
      {"dag_conf", required_argument, nullptr, 'd'},
      {"process_name", required_argument, nullptr, 'p'},
      {"sched_name", required_argument, nullptr, 's'},
      {"plugin", required_argument, nullptr, ARGS_OPT_CODE_PLUGIN},
      {"disable_plugin_autoload", no_argument, nullptr,
       ARGS_OPT_CODE_DISABLE_PLUGIN_AUTOLOAD},
      {"cpuprofile", no_argument, nullptr, 'c'},
      {"profile_filename", required_argument, nullptr, 'o'},
      {"heapprofile", no_argument, nullptr, 'H'},
      {"heapprofile_filename", required_argument, nullptr, 'O'},
      {NULL, no_argument, nullptr, 0}};

  // log command for info
  std::string cmd("");
  for (int i = 0; i < argc; ++i) {
    cmd += argv[i];
    cmd += " ";
  }
  AINFO << "command: " << cmd;

  if (1 == argc) {
    DisplayUsage();
    exit(0);
  }

  do {
    int opt =
        getopt_long(argc, argv, short_opts.c_str(), long_opts, &long_index);
    if (opt == -1) {
      break;
    }
    switch (opt) {
      case 'd':
        dag_conf_list_.emplace_back(std::string(optarg));
        for (int i = optind; i < argc; i++) {
          if (*argv[i] != '-') {
            dag_conf_list_.emplace_back(std::string(argv[i]));
          } else {
            break;
          }
        }
        break;
      case 'p':
        process_group_ = std::string(optarg);
        break;
      case 's':
        sched_name_ = std::string(optarg);
        break;
      case ARGS_OPT_CODE_PLUGIN:
        plugin_description_list_.emplace_back(std::string(optarg));
        break;
      case ARGS_OPT_CODE_DISABLE_PLUGIN_AUTOLOAD:
        disable_plugin_autoload_ = true;
        break;
      case 'c':
#ifndef BASE_PROFILER_H_
        AWARN << "gperftools not installed, ignore perf parameters";
#endif
        enable_cpuprofile_ = true;
        break;
      case 'o':
        profile_filename_ = std::string(optarg);
        break;
      case 'H':
#ifndef BASE_PROFILER_H_
        AWARN << "gperftools not installed, ignore perf parameters";
#endif
        enable_heapprofile_ = true;
        break;
      case 'O':
        heapprofile_filename_ = std::string(optarg);
        break;
      case 'h':
        DisplayUsage();
        exit(0);
      default:
        break;
    }
  } while (true);

  if (optind < argc) {
    AINFO << "Found non-option ARGV-element \"" << argv[optind++] << "\"";
    DisplayUsage();
    exit(1);
  }

  if (dag_conf_list_.empty()) {
    AINFO << "-d parameter must be specified";
    DisplayUsage();
    exit(1);
  }
}

}  // namespace mainboard
}  // namespace cyber
}  // namespace apollo
