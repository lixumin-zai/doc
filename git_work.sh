#!/bin/bash

# 设置当前时间戳作为 commit 消息
commit_message="Auto commit $(date '+%Y-%m-%d %H:%M:%S')"

# 自动执行 git add、commit 和 push
git add .

# 提示输入 commit 消息（如果需要）
echo "Commit message: $commit_message"
git commit -m "$commit_message"

# 推送到远程仓库
git push

# 输出完成提示
echo "Changes pushed to remote repository."