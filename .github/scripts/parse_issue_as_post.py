import sys
import frontmatter
from datetime import datetime


def run_parser(body: str, title: str, number: str) -> None:
    try:
        # 解析 Front-Matter 和正文
        post = frontmatter.loads(body)
    except:
        post = frontmatter.Post(body)

    # 补全 Hexo 必要字段
    if 'title' not in post.metadata:
        post.metadata['title'] = title
    if 'date' not in post.metadata:
        post.metadata['date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 生成文件名（格式：YYYY-MM-DD-标题.md）
    clean_title = title.lower().replace(' ', '-').replace('/', '')[:50]
    filename = f"source/_posts/{datetime.now().strftime('%Y-%m-%d')}-issue-{number}-{clean_title}.md"

    print(frontmatter.dumps(post))

    # 保存文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post))


if __name__ == '__main__':
    # 获取输入参数
    issue_body = sys.argv[1]
    issue_title = sys.argv[2]
    issue_number = sys.argv[3]

    run_parser(body=issue_body, title=issue_title, number=issue_number)
