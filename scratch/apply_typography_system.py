import os
import re

BASE_DIR = r"c:\Users\USER\Desktop\博客\jichangdian.xyz"

# 1. Update static/css/style.css with Unified Typography & Spacing System
style_css_path = os.path.join(BASE_DIR, "static", "css", "style.css")

unified_css = """
/* ==========================================================================
   UNIFIED ARTICLE TYPOGRAPHY & VERTICAL RHYTHM SPACING SYSTEM
   ========================================================================== */

/* Top Margin & Container Gap Fixes */
.single-article {
  max-width: 1000px;
  margin: 0 auto;
}

.article-container {
  padding-top: 24px;
  padding-bottom: 40px;
}

.article-header {
  margin-bottom: 24px;
  border-bottom: 1px solid var(--border-color);
  padding-bottom: 20px;
}

.article-title {
  font-size: 1.85rem;
  font-weight: 800;
  line-height: 1.35;
  color: var(--text-main);
  margin-bottom: 12px;
}

.article-meta {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  font-size: 0.88rem;
  color: var(--text-muted);
}

/* Home Guide Article Section Wrapper Fix (Eliminate redundant top space) */
.home-guide-article-wrapper {
  margin-top: 10px;
  margin-bottom: 25px;
  padding-top: 0 !important;
  padding-bottom: 0 !important;
}

.home-guide-article-card {
  background: #ffffff;
  border-radius: 14px;
  padding: 36px 40px;
  border: 1px solid var(--border-color);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
}

/* Reading Width Scoping (Prose max-width 900px centered) */
.article-body,
.guide-intro-text,
.guide-section {
  max-width: 900px;
  margin-left: auto;
  margin-right: auto;
}

/* Paragraph Spacing & Line Height */
.article-body p,
.guide-intro-text p,
.guide-section p,
.home-guide-article-card p {
  font-size: 1rem;
  line-height: 1.8;
  margin-top: 0;
  margin-bottom: 16px;
  color: #334155;
}

.article-body p:last-child,
.guide-section p:last-child {
  margin-bottom: 0;
}

/* Headings Visual Hierarchy & Spacing */
.article-body h2,
.guide-section-title,
.home-guide-article-card h2 {
  font-size: 1.45rem;
  font-weight: 800;
  line-height: 1.4;
  color: #0f172a;
  margin-top: 34px;
  margin-bottom: 14px;
  padding-top: 12px;
}

.article-body h3,
.home-guide-article-card h3 {
  font-size: 1.25rem;
  font-weight: 700;
  line-height: 1.45;
  color: #1e293b;
  margin-top: 28px;
  margin-bottom: 12px;
}

.article-body h4,
.home-guide-article-card h4 {
  font-size: 1.1rem;
  font-weight: 700;
  line-height: 1.5;
  color: #334155;
  margin-top: 22px;
  margin-bottom: 10px;
}

/* First element after heading spacing tightener */
.article-body h2 + p,
.article-body h3 + p,
.article-body h4 + p,
.guide-section-title + p,
.guide-section-title + div {
  margin-top: 0;
}

/* Real List Styling (ul, ol, li) */
.article-body ul,
.article-body ol,
.guide-section ul,
.guide-section ol,
.home-guide-article-card ul,
.home-guide-article-card ol {
  margin-top: 10px;
  margin-bottom: 18px;
  padding-left: 1.6em;
}

.article-body li,
.guide-section li,
.home-guide-article-card li {
  font-size: 0.98rem;
  line-height: 1.75;
  margin-bottom: 8px;
  color: #334155;
}

.article-body li:last-child,
.home-guide-article-card li:last-child {
  margin-bottom: 0;
}

/* Article Flow Steps (Replacing arrow text walls with clean responsive cards) */
.article-steps-flow,
.guide-flow-grid {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
  list-style: none;
  padding: 16px 20px;
  margin: 20px 0 24px 0;
  background-color: #f8fafc;
  border-radius: 10px;
  border: 1px solid #e2e8f0;
}

.article-steps-flow li,
.flow-step {
  display: flex;
  align-items: center;
  gap: 8px;
  background: #ffffff;
  padding: 8px 16px;
  border-radius: 6px;
  font-size: 0.9rem;
  font-weight: 700;
  color: #1e293b;
  border: 1px solid #cbd5e1;
  box-shadow: 0 1px 2px rgba(0,0,0,0.03);
}

.flow-step span,
.article-steps-flow li::before {
  background: #2563eb;
  color: #ffffff;
  border-radius: 50%;
  width: 22px;
  height: 22px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 0.78rem;
  font-weight: 800;
}

/* Callout Blocks & Blockquotes */
.highlight-callout,
.article-body blockquote {
  background-color: #fefce8;
  border-left: 4px solid #eab308;
  padding: 16px 20px;
  border-radius: 6px;
  font-weight: 700;
  color: #854d0e;
  margin: 22px 0;
  line-height: 1.75;
}

.article-body blockquote p {
  margin-bottom: 0;
  color: #854d0e;
}

/* Responsive Grids for Cards & Tables (Can expand beyond 900px reading width) */
.parallel-cards-2col {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  margin: 22px 0;
}

.parallel-cards-3col {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 20px;
  margin: 22px 0;
}

.parallel-card {
  background: #f8fafc;
  border-radius: 10px;
  padding: 22px;
  border: 1px solid #e2e8f0;
}

.parallel-card h4 {
  margin-top: 0;
  margin-bottom: 10px;
  color: #1e293b;
}

.check-grid-5 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 12px;
  margin: 20px 0;
}

.check-item {
  background: #f0fdf4;
  border: 1px solid #bbf7d0;
  border-radius: 8px;
  padding: 14px 10px;
  text-align: center;
  font-size: 0.88rem;
  font-weight: 700;
  color: #166534;
}

.pitfalls-grid-5 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 18px;
  margin: 22px 0;
}

.pitfall-card {
  background: #fef2f2;
  border: 1px solid #fecaca;
  border-radius: 10px;
  padding: 20px;
}

.pitfall-badge {
  display: inline-block;
  background: #dc2626;
  color: #ffffff;
  font-size: 0.75rem;
  font-weight: 800;
  padding: 2px 10px;
  border-radius: 10px;
  margin-bottom: 10px;
}

.pitfall-card h4 {
  margin-top: 0;
  color: #991b1b;
}

.questions-grid-3 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 16px;
  margin: 20px 0;
}

.q-card {
  background: #eff6ff;
  border: 1px solid #bfdbfe;
  border-radius: 10px;
  padding: 18px;
  text-align: center;
}

.q-num {
  font-size: 0.8rem;
  font-weight: 800;
  color: #1d4ed8;
  margin-bottom: 6px;
}

.q-card p {
  margin-bottom: 0;
  font-weight: 700;
  color: #1e3a8a;
}

.faq-accordion-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 18px;
  margin: 22px 0;
}

.faq-item-card {
  background: #f8fafc;
  border-radius: 10px;
  padding: 20px;
  border: 1px solid #e2e8f0;
}

.faq-item-card h4 {
  margin-top: 0;
  margin-bottom: 8px;
  color: #0f172a;
}

.faq-item-card p {
  margin-bottom: 0;
}

.guide-footer-callout {
  background: #1e293b;
  color: #ffffff;
  border-radius: 12px;
  padding: 32px;
  margin-top: 36px;
}

.guide-footer-callout h3 {
  color: #f8fafc;
  margin-top: 0;
  margin-bottom: 16px;
}

.guide-footer-callout p {
  color: #cbd5e1;
  margin-bottom: 12px;
}

.final-motto {
  font-weight: 700;
  color: #fde047;
  margin-top: 16px;
  margin-bottom: 0 !important;
}

/* Mobile Responsiveness for Article Reading Area */
@media (max-width: 768px) {
  .home-guide-article-card {
    padding: 22px 18px;
  }
  
  .article-title {
    font-size: 1.45rem;
  }
  
  .article-body h2,
  .guide-section-title,
  .home-guide-article-card h2 {
    font-size: 1.25rem;
    margin-top: 26px;
    margin-bottom: 12px;
  }

  .article-body h3,
  .home-guide-article-card h3 {
    font-size: 1.12rem;
    margin-top: 22px;
    margin-bottom: 10px;
  }

  .article-body p,
  .guide-intro-text p,
  .guide-section p,
  .home-guide-article-card p {
    font-size: 0.95rem;
    line-height: 1.75;
    margin-bottom: 14px;
  }
  
  .article-steps-flow,
  .guide-flow-grid {
    flex-direction: column;
    align-items: stretch;
  }
  
  .flow-arrow {
    display: none;
  }
}
"""

with open(style_css_path, "a", encoding="utf-8") as f:
    f.write("\n" + unified_css)

print("Appended unified CSS system to static/css/style.css")
