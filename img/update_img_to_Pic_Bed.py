import re
import os

# 设置目录路径
directory_path = 'E:/Blog/source/_posts'

# 通过目录中的所有文件进行迭代
for filename in os.listdir(directory_path):
    if filename.endswith('.md'):  # 确认文件是Markdown文件
        full_path = os.path.join(directory_path, filename)
        # 移除文件拓展名，并将其添加进URL
        prefix = f'https://cdn.jsdelivr.net/gh/SecTreeCN/Pic_Bed@main/img/{filename[:-3]}'

        # 读取文件内容
        with open(full_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 使用正则表达式添加前缀到图片链接
        updated_content = re.sub(r'!\[(.*?)\]\((?!http)(.*?)\)', r'![\1](' + prefix + r'/\2)', content)

        # 将更新后的内容写回文件
        with open(full_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)

        print(f"Images in {filename} have been updated with the file-specific prefix.")