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

#include "cyber/cyber.h"
#include "cyber/parameter/parameter_client.h"
#include "cyber/parameter/parameter_server.h"

using apollo::cyber::Parameter;
using apollo::cyber::ParameterClient;
using apollo::cyber::ParameterServer;

int main(int argc, char** argv) {
  apollo::cyber::Init(*argv);

  std::string server_node_name = "parameter";
  std::shared_ptr<apollo::cyber::Node> server_node =
      apollo::cyber::CreateNode(server_node_name);
  std::shared_ptr<apollo::cyber::Node> client_node =
      apollo::cyber::CreateNode("example_client");
  auto param_server = std::make_shared<ParameterServer>(server_node);
  auto param_client =
      std::make_shared<ParameterClient>(client_node, server_node_name);

  param_server->SetParameter(
      Parameter("map_path", "/opt/apollo/shared/hdmap/data/map.json"));

  Parameter parameter;
  param_server->GetParameter("map_path", &parameter);
  AINFO << "map_path: "
        << parameter.AsString();  // /opt/apollo/shared/hdmap/data/map.json

  param_client->SetParameter(
      Parameter("config_path", "/opt/apollo/config.yaml"));
  param_client->GetParameter("config_path", &parameter);
  AINFO << "config_path: " << parameter.AsString();  // /opt/apollo/config.yaml

  return 0;
}

