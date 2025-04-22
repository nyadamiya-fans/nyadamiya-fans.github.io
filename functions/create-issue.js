export async function onRequestPost(context) {
    const { request, env } = context;
    try {
      // 解析前端提交的 JSON 数据
      const { title, issue_body } = await request.json();
  
      // 调用 GitHub API 创建 Issue
      const response = await fetch(`https://api.github.com/repos/${env.REPO}/issues`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${env.GITHUB_TOKEN}`,
          'User-Agent': 'Cloudflare-Worker',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          title: title,
          body: issue_body,
          labels: ['post']
        })
      });
  
      // 返回结果给前端
      const data = await response.json();
      return new Response(JSON.stringify(data), {
        headers: { 'Content-Type': 'application/json' },
      });
    } catch (error) {
      return new Response(JSON.stringify({ error: error.message }), { status: 500 });
    }
  }