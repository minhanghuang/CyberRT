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

#ifndef CYBER_TRANSPORT_DISPATCHER_RTPS_DISPATCHER_H_
#define CYBER_TRANSPORT_DISPATCHER_RTPS_DISPATCHER_H_

#include <cstdint>
#include <iostream>
#include <memory>
#include <mutex>
#include <string>
#include <unordered_map>

#include "cyber/common/log.h"
#include "cyber/common/macros.h"
#include "cyber/message/message_traits.h"
#include "cyber/statistics/statistics.h"
#include "cyber/time/time.h"
#include "cyber/transport/dispatcher/dispatcher.h"
#include "cyber/transport/dispatcher/subscriber_listener.h"
#include "cyber/transport/qos/qos_filler.h"
#include "cyber/transport/rtps/attributes_filler.h"
#include "cyber/transport/rtps/participant.h"
#include "cyber/transport/rtps/subscriber.h"

namespace apollo {
namespace cyber {
namespace transport {

class RtpsDispatcher;
using RtpsDispatcherPtr = RtpsDispatcher*;

using ParticipantPtr =
    std::shared_ptr<Participant>;

class RtpsDispatcher : public Dispatcher {
 public:
  virtual ~RtpsDispatcher();

  void Shutdown() override;

  template <typename MessageT>
  void AddListener(const RoleAttributes& self_attr,
                   const MessageListener<MessageT>& listener);

  template <typename MessageT>
  void AddListener(const RoleAttributes& self_attr,
                   const RoleAttributes& opposite_attr,
                   const MessageListener<MessageT>& listener);

  void SetParticipant(const ParticipantPtr& participant) {
    participant_ = participant;
  }

 private:
  void OnMessage(uint64_t channel_id,
                 const std::shared_ptr<std::string>& msg_str,
                 const MessageInfo& msg_info);
  void AddSubscriber(const RoleAttributes& self_attr);
  // key: channel_id
  std::unordered_map<uint64_t,
                     std::shared_ptr<transport::Subscriber>>
      subs_;
  std::mutex subs_mutex_;

  ParticipantPtr participant_;

  DECLARE_SINGLETON(RtpsDispatcher)
};

template <typename MessageT>
void RtpsDispatcher::AddListener(const RoleAttributes& self_attr,
                                 const MessageListener<MessageT>& listener) {
  auto listener_adapter = [listener, self_attr](
                              const std::shared_ptr<std::string>& msg_str,
                              const MessageInfo& msg_info) {
    auto msg = std::make_shared<MessageT>();
    RETURN_IF(!message::ParseFromString(*msg_str, msg.get()));
    uint64_t recv_time = Time::Now().ToNanosecond();
    uint64_t send_time = msg_info.send_time();
    if (send_time > recv_time) {
      AWARN << "The message is received (" << recv_time
            << ") earlier than the message is sent (" << send_time << ")";
    } else {
      uint64_t diff = recv_time - send_time;
      // sample transport latency in microsecond
      statistics::Statistics::Instance()->SamplingTranLatency<uint64_t>(
          self_attr, diff);
    }
    statistics::Statistics::Instance()->SetProcStatus(self_attr, recv_time);
    listener(msg, msg_info);
  };

  Dispatcher::AddListener<std::string>(self_attr, listener_adapter);
  AddSubscriber(self_attr);
}

template <typename MessageT>
void RtpsDispatcher::AddListener(const RoleAttributes& self_attr,
                                 const RoleAttributes& opposite_attr,
                                 const MessageListener<MessageT>& listener) {
  auto listener_adapter = [listener, self_attr](
                              const std::shared_ptr<std::string>& msg_str,
                              const MessageInfo& msg_info) {
    auto msg = std::make_shared<MessageT>();
    RETURN_IF(!message::ParseFromString(*msg_str, msg.get()));
    uint64_t recv_time = Time::Now().ToNanosecond();
    uint64_t send_time = msg_info.send_time();
    if (send_time > recv_time) {
      AWARN << "The message is received (" << recv_time
            << ") earlier than the message is sent (" << send_time << ")";
    } else {
      uint64_t diff = recv_time - send_time;
      // sample transport latency in microsecond
      statistics::Statistics::Instance()->SamplingTranLatency<uint64_t>(
          self_attr, diff);
    }
    statistics::Statistics::Instance()->SetProcStatus(self_attr, recv_time);
    listener(msg, msg_info);
  };

  Dispatcher::AddListener<std::string>(self_attr, opposite_attr,
                                       listener_adapter);
  AddSubscriber(self_attr);
}

}  // namespace transport
}  // namespace cyber
}  // namespace apollo

#endif  // CYBER_TRANSPORT_DISPATCHER_RTPS_DISPATCHER_H_
