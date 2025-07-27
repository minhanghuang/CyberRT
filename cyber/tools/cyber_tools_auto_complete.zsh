# usage: source cyber_tools_auto_complete.zsh

_cyber_launch() {
  local context state state_descr line
  typeset -A opt_args

  _arguments -C \
    "1: :->cmds" \
    "*::arg:->args"

  case $state in
    cmds)
      local -a commands=(
        "start:启动launch文件"
        "stop:停止launch文件"
      )
      _describe "command" commands
      ;;
    args)
      case $line[1] in
        start|stop)
          _files -g "*.launch"
          ;;
      esac
      ;;
  esac
}

_cyber_recorder() {
  _arguments -C \
    "1: :(play info record split recover)"
}

_cyber_channel() {
  _arguments -C \
    "1: :(echo list info hz bw type)"
}

_cyber_node() {
  _arguments -C \
    "1: :(list info)"
}

_cyber_service() {
  _arguments -C \
    "1: :(list info)"
}

compdef _cyber_launch cyber_launch
compdef _cyber_recorder cyber_recorder
compdef _cyber_channel cyber_channel
compdef _cyber_node cyber_node
compdef _cyber_service cyber_service
