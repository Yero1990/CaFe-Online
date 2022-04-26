#!/bin/bash


git_cmd_1='git submodule update --init'
git_cmd_2='git submodule update --recursive --remote'

if   [ -z "$1" ]; then
    echo -e "Usage: \n initialize all submodule (only ONCE) | ./git_submodule.sh init \n update all git submodules | ./git_submodule.sh update"
elif [ "$1" == "init" ]; then
    eval $git_cmd_1
elif [ "$1" == "update" ]; then
    eval $git_cmd_2
fi

# initialize submodules
