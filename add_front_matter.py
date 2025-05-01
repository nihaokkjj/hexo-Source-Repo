import os
from datetime import datetime

# 定义目标文件夹路径
posts_dir = r'd:\blog\blog_k\source\_posts'

# 定义需要添加的 YAML 头部
front_matter = """---
title: 
date: 2025-05-01 13:59:06
tags:
---
"""

# 遍历文件夹中的所有 .md 文件
for root, _, files in os.walk(posts_dir):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r+', encoding='utf-8') as f:
                content = f.read()
                # 检查文件是否已经包含 YAML 头部
                if not content.strip().startswith('---'):
                    # 在文件开头添加 YAML 头部
                    f.seek(0, 0)
                    f.write(front_matter + '\n' + content)
                    print(f"已为文件添加头部: {file_path}")