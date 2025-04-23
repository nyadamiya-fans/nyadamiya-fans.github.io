---
title: 文章投稿
layout: page
---

<style>
  :root {
    --btn-bg-color:rgb(60, 96, 134);
    --btn-hover-bg-color: rgb(76, 122, 172);
    --border-radius: 8px;
    --box-shadow: 0 3px 8px 6px rgba(7,17,27,0.06);
  }

  /* 表单容器 */
  .submit-container {
    max-width: 800px;
    margin: 2rem auto;
    padding: 2rem;
    border-radius: var(--border-radius);
    box-shadow: var(--box-shadow);
  }

  /* 表单标题 */
  .submit-title {
    font-size: 1.5rem;
    margin-bottom: 1.5rem;
    border-bottom: 2px solid;
    padding-bottom: 0.5rem;
  }

  /* 表单输入组 */
  .form-group {
    margin-bottom: 1.5rem;
  }

  .form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 500;
  }

  /* 输入框样式 */
  .form-control {
    width: 100%;
    padding: 0.8rem;
    border-radius: calc(var(--border-radius) - 2px);
    transition: all 0.3s ease;
  }

  .form-control:focus {
    border-color: var(--btn-bg-color);
    box-shadow: 0 0 0 3px rgba(0,107,220,0.1);
    outline: none;
  }

  /* 提交按钮 */
  .submit-btn {
    display: inline-block;
    padding: 0.8rem 2rem;
    background: var(--btn-bg-color);
    color: #fff;
    border: none;
    border-radius: calc(var(--border-radius) - 2px);
    cursor: pointer;
    transition: all 0.3s ease;
    font-weight: 500;
  }

  .submit-btn:hover {
    background: var(--btn-hover-bg-color);
    transform: translateY(-1px);
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }

  /* 响应式调整 */
  @media (max-width: 767px) {
    .submit-container {
      margin: 1rem;
      padding: 1.5rem;
    }
    .submit-title {
      font-size: 1.3rem;
    }
  }
</style>

<div class="submit-container">
  <h2 class="submit-title">📝 文章投稿</h2>
  <form id="submit-form">
    <div class="form-group">
      <label for="title">文章标题 *（必填）</label>
      <input
        type="text"
        id="title"
        class="form-control"
        placeholder="请输入文章标题 *（必填）（50字以内）"
        maxlength="50"
        required
      >
    </div>
    <div class="form-group">
      <label for="author">作者 *（必填）</label>
      <input
        type="text"
        id="author"
        class="form-control"
        placeholder="请输入作者名称 *（必填）（20字以内）"
        maxlength="20"
        required
      >
    </div>
    <div class="form-group">
      <label for="categories">文章分类</label>
      <input
        type="text"
        id="categories"
        class="form-control"
        placeholder="请输入文章分类（10字以内）"
        maxlength="10"
      >
    </div>
    <div class="form-group">
      <label for="tags">文章标签</label>
      <input
        type="text"
        id="tags"
        class="form-control"
        placeholder="标签1, 标签2, 标签3, ..."
        maxlength="50"
      >
    </div>
    <div class="form-group">
      <label for="content">文章内容 *（必填）</label>
      <textarea
        id="content"
        class="form-control"
        rows="12"
        placeholder="请输入正文内容 *（必填）（支持 Markdown 格式）..."
        required
      ></textarea>
    </div>
    <div style="text-align: right;">
      <button type="submit" class="submit-btn">
        <i class="iconfont icon-send"></i>提交投稿
      </button>
    </div>
  </form>
</div>

<script>
  document.getElementById('submit-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const title = document.getElementById('title').value;
    const author = document.getElementById('author').value;
    const categories = document.getElementById('categories').value;
    const tags = document.getElementById('tags').value;
    const content = document.getElementById('content').value;

    const issue_body = `---\ntitle: "${title}"\nauthor: "${author}"\ntags: [${tags}]\ncategories: ${categories}\n---\n\n${content}`

  try {
    const response = await fetch('/create-issue', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title, issue_body })
    });

    const result = await response.json();

    // 存储结果到 sessionStorage 并跳转
    sessionStorage.setItem('submissionResult', JSON.stringify({
      status: response.ok ? 'success' : 'error',
      data: result
    }));

    window.location.href = '/submit/result'; // 跳转到结果页

  } catch (error) {
    sessionStorage.setItem('submissionResult', JSON.stringify({
      status: 'error',
      data: { error: '网络请求失败' }
    }));
    window.location.href = '/submit/result';
  }
  });
</script>
