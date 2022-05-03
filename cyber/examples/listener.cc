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
#include "cyber/examples/proto/examples.pb.h"

using apollo::cyber::examples::proto::Chatter;

void MessageCallback(const std::shared_ptr<Chatter>& msg) {
  AINFO << "Received message seq-> " << msg->seq();
  // AINFO << "msgcontent->" << msg->content();
  // std::cout << "Received " << msg->content() << std::endl;
  // std::cout << "ssss " << std::endl;
}

int main(int argc, char* argv[]) {
  apollo::cyber::Init(argv[0]);
  auto node = apollo::cyber::CreateNode("sub");
  auto sub = node->CreateReader<Chatter>("/topic", MessageCallback);
  std::cout << "listener " << std::endl;
  apollo::cyber::WaitForShutdown();
  return 0;
}
