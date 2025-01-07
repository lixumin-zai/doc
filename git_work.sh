#!/bin/bash

# 设置当前时间戳作为 commit 消息
commit_message="Auto commit $(date '+%Y-%m-%d %H:%M:%S')"
working_directory="/root/project/doc/lismin"
{
  cd "$working_directory"
  echo "Start git operation at $(date)"
  # 自动执行 git add、commit 和 push
  git add .
  echo "Staged files"
  
  # 提交并推送
  git commit -m "$commit_message"
  git push
  
  echo "End git operation at $(date)"
  echo "-----------------------------------"
} >> ./git.log 2>&1