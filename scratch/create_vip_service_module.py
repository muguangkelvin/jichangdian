import os
import re

BASE_DIR = r"c:\Users\USER\Desktop\博客\jichangdian.xyz"

# 1. Create layouts/partials/vip_service_cta.html
vip_partial_path = os.path.join(BASE_DIR, "layouts", "partials", "vip_service_cta.html")
vip_partial_content = """<section class="vip-service-cta-wrapper">
  <div class="container">
    <div class="vip-service-box">
      <!-- 第一层：标题与说明 -->
      <header class="vip-header">
        <h2 class="vip-title">本站自营VIP服务与一对一答疑支持</h2>
        <p class="vip-subtitle">高质量机场测评、梯子选购对比、客户端配置与一对一新手答疑服务</p>
      </header>

      <!-- 第二层：4个横向服务卡片 -->
      <div class="vip-cards-grid">
        <div class="vip-card">
          <div class="vip-card-icon">🎯</div>
          <h3 class="vip-card-title">机场选择建议</h3>
          <p class="vip-card-desc">根据预算、设备和使用需求帮助筛选合适方案</p>
        </div>

        <div class="vip-card">
          <div class="vip-card-icon">💰</div>
          <h3 class="vip-card-title">套餐选择建议</h3>
          <p class="vip-card-desc">结合流量与使用周期判断套餐，减少不必要支出</p>
        </div>

        <div class="vip-card">
          <div class="vip-card-icon">⚙️</div>
          <h3 class="vip-card-title">客户端配置指导</h3>
          <p class="vip-card-desc">提供 Windows、macOS、Android、iOS 等常见客户端配置指引</p>
        </div>

        <div class="vip-card">
          <div class="vip-card-icon">💬</div>
          <h3 class="vip-card-title">使用问题答疑</h3>
          <p class="vip-card-desc">针对订阅导入、节点选择、连接异常等常见问题提供排查思路</p>
        </div>
      </div>

      <!-- 第三层：用户引导 -->
      <div class="vip-guidance">
        <h4 class="vip-guidance-title">不知道自己应该怎么选？</h4>
        <p class="vip-guidance-desc">从使用设备、预算、流量需求和使用场景出发，帮助你更快找到合适的方案。</p>
      </div>

      <!-- 第四层：CTA 转化按钮 -->
      <div class="vip-cta-actions">
        <a href="/posts/jichang-tuijian/" class="btn btn-primary btn-lg">查看2026机场推荐精选榜 ➔</a>
        <a href="https://t.me/+JngXxDbAxwA5NzVl" target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-lg">
          <span class="tg-icon">✈️</span> 联系客服咨询
        </a>
      </div>
    </div>
  </div>
</section>
"""

with open(vip_partial_path, "w", encoding="utf-8") as f:
    f.write(vip_partial_content)

print("Created layouts/partials/vip_service_cta.html")

# 2. Update layouts/services/single.html
service_single_path = os.path.join(BASE_DIR, "layouts", "services", "single.html")
service_single_content = """{{ define "main" }}
<div class="service-page-container">
  {{ partial "vip_service_cta.html" . }}

  <div class="container section-padding">
    <div class="service-page-wrapper">
      <div class="service-body">
        {{ .Content }}
      </div>
    </div>
  </div>
</div>
{{ end }}
"""

with open(service_single_path, "w", encoding="utf-8") as f:
    f.write(service_single_content)

print("Updated layouts/services/single.html")

# 3. Update layouts/index.html to include partial above footer
index_path = os.path.join(BASE_DIR, "layouts", "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    index_content = f.read()

if "vip_service_cta.html" not in index_content:
    # Insert above section master-post-banner or latest
    index_content = index_content.replace(
        '{{ partial "home_beginner_article.html" . }}',
        '{{ partial "home_beginner_article.html" . }}\n\n{{ partial "vip_service_cta.html" . }}'
    )
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_content)
    print("Inserted vip_service_cta.html into layouts/index.html")

# 4. Append CSS to static/css/style.css
style_css_path = os.path.join(BASE_DIR, "static", "css", "style.css")
vip_css = """
/* VIP Service CTA Section Styling */
.vip-service-cta-wrapper {
  padding: 56px 0;
  background-color: #f8fafc;
  border-top: 1px solid #e2e8f0;
  border-bottom: 1px solid #e2e8f0;
  margin-top: 20px;
}

.vip-service-box {
  max-width: 1200px;
  margin: 0 auto;
  text-align: center;
}

.vip-header {
  margin-bottom: 32px;
}

.vip-title {
  font-size: 1.8rem;
  font-weight: 800;
  color: #0f172a;
  margin-bottom: 10px;
  line-height: 1.35;
}

.vip-subtitle {
  font-size: 0.98rem;
  color: #64748b;
  margin-bottom: 0;
}

.vip-cards-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  margin-bottom: 32px;
}

.vip-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 24px 20px;
  text-align: left;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.02);
  transition: transform 0.2s, box-shadow 0.2s;
}

.vip-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(37, 99, 235, 0.08);
  border-color: #bfdbfe;
}

.vip-card-icon {
  font-size: 1.8rem;
  margin-bottom: 12px;
}

.vip-card-title {
  font-size: 1.05rem;
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 8px;
}

.vip-card-desc {
  font-size: 0.88rem;
  color: #64748b;
  line-height: 1.55;
  margin-bottom: 0;
}

.vip-guidance {
  background: #eff6ff;
  border: 1px solid #bfdbfe;
  border-radius: 10px;
  padding: 18px 24px;
  max-width: 800px;
  margin: 0 auto 28px auto;
  text-align: center;
}

.vip-guidance-title {
  font-size: 1.08rem;
  font-weight: 700;
  color: #1e3a8a;
  margin-bottom: 6px;
}

.vip-guidance-desc {
  font-size: 0.92rem;
  color: #1e40af;
  margin-bottom: 0;
}

.vip-cta-actions {
  display: flex;
  gap: 16px;
  justify-content: center;
  flex-wrap: wrap;
}

@media (max-width: 1024px) {
  .vip-cards-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 640px) {
  .vip-cards-grid {
    grid-template-columns: 1fr;
  }
  .vip-service-cta-wrapper {
    padding: 40px 0;
  }
  .vip-title {
    font-size: 1.45rem;
  }
}
"""

with open(style_css_path, "a", encoding="utf-8") as f:
    f.write("\n" + vip_css)

print("Appended VIP CSS to static/css/style.css")
