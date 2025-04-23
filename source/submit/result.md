---
title: 文章投稿结果
layout: page
---

<style>
  .result-box {
    max-width: 800px;
    margin: 2rem auto;
    padding: 2rem;
    border-radius: 8px;
  }
  .success { background: #e8f5e9; border: 1px solid #4caf50; }
  .error { background: #ffebee; border: 1px solid #f44336; }
  .issue-link { word-break: break-all; }
</style>

<div id="result-container"></div>

<script>
  function renderResult() {
    const container = document.getElementById('result-container');
    const result = JSON.parse(sessionStorage.getItem('submissionResult') || '{}');

    if (!result.status) {
      container.innerHTML = `<p>没有找到提交记录</p>`;
      return;
    }

    const isSuccess = result.status === 'success';
    const html = `
      <div class="result-box ${isSuccess ? 'success' : 'error'}">
        <h2>${isSuccess ? '✅ 投稿成功' : '❌ 提交失败'}</h2>
        ${isSuccess ? `
          <p>文章已成功提交至 GitHub Issue</p>
          <p>Issue 地址：
            <a href="${result.data.html_url}" class="issue-link" target="_blank">
              ${result.data.html_url}
            </a>
          </p>
        ` : `
          <p>错误信息：${result.data.error || '未知错误'}</p>
        `}
        <p><a href="/submit">返回投稿页</a></p>
      </div>
    `;

    container.innerHTML = html;
    sessionStorage.removeItem('submissionResult'); // 清除存储
  }

  // 页面加载时渲染
  renderResult();
</script>
