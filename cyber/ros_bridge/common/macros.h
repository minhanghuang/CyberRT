/******************************************************************************
 * Copyright 2024 The Apollo Authors. All Rights Reserved.
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

#ifndef ROS_BRIDGE_MACROS_H_
#define ROS_BRIDGE_MACROS_H_

// replacement macro for eprosima namespace to eprosima_wrap
// for adapting different version fastdds on a single process
#ifndef eprosima
// #define eprosima eprosima_wrap
#endif

#endif  // ROS_BRIDGE_MACROS_H_
