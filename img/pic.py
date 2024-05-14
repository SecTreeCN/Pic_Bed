import os

# 设置目录路径
directory_path = 'E:/Blog/source/_posts'

# 通过目录中的所有Markdown文件进行迭代
for filename in os.listdir(directory_path):
    if filename.endswith('.md'):  # 确认文件是Markdown文件
        full_path = os.path.join(directory_path, filename)

        # 读取文件的内容
        with open(full_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 替换图片链接的基础部分
        updated_content = content.replace(
            'https://pic.treesec.cn/', 
            'https://mypic.treesec.cn/'
        )

        # 将更新后的内容写回文件
        with open(full_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)

        print(f"Links in {filename} have been updated.")