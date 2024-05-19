import re
import os

# 设置目录路径
directory_path = 'E:/Blog/source/_posts'

# 通过目录中的所有文件进行迭代
for filename in os.listdir(directory_path):
    if filename.endswith('.md'):  # 确认文件是Markdown文件
        full_path = os.path.join(directory_path, filename)
        # 移除文件拓展名，并将其添加进URL
        prefix = f'https://mypic.treesec.cn/img/{filename[:-3]}'

        # 读取文件内容
        with open(full_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 使用正则表达式添加前缀到图片链接
        updated_content = re.sub(r'!\[(.*?)\]\((?!http)(.*?)\)', r'![\1](' + prefix + r'/\2)', content)

        # 将更新后的内容写回文件
        with open(full_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)

        print(f"Images in {filename} have been updated with the file-specific prefix.")
"""
def update_image_links(md_file_path, img_folder_name):
    # 生成前缀字符串
    prefix = f"https://mypic.treesec.cn/img/{img_folder_name}/"

    # 校验路径是否存在
    if not os.path.isfile(md_file_path):
        print(f"The file {md_file_path} does not exist.")
        return

    # 读取原Markdown文件
    with open(md_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 使用正则表达式寻找图片链接
    # 假设Markdown中的图片链接是这样的 ![alt text](image_url)
    pattern = r'!\[.*?\]\((?!http)(.*?)(?="\))\)'
    updated_content = re.sub(pattern, lambda m: f"![{m.group(1)}]({prefix}{m.group(1)})", content)

    # 写入新的Markdown文件（或覆盖原文件）
    with open(md_file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

    print(f"Updated image links in {md_file_path}")

# 假设我们要更新 'CISCN.md' 文件中的链接
update_image_links('E:/Blog/source/_posts/CISCN2024.md', 'CISCN2024')

# 以后如果您想更新 'xxx.md' 文件中的链接，只需调用函数并传入相应参数
# update_image_links('path_to_your_markdown_file/xxx.md', 'xxx')"""