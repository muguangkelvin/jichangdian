import os

css_addition = """
.home-guide-article-wrapper {
  margin-top: 20px;
  margin-bottom: 20px;
}

.home-guide-article-card {
  background-color: rgb(255, 255, 255);
  border-radius: 14px;
  padding: 35px;
  border: 1px solid rgb(226, 232, 240);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
}

.guide-header {
  background-color: rgb(240, 247, 255);
  border-radius: 12px;
  padding: 28px;
  margin-bottom: 30px;
  border: 1px solid rgb(219, 234, 254);
}

.guide-header-badge {
  display: inline-block;
  background-color: rgb(37, 99, 235);
  color: rgb(255, 255, 255);
  font-size: 0.85rem;
  font-weight: 700;
  padding: 4px 14px;
  border-radius: 20px;
  margin-bottom: 12px;
}

.guide-main-title {
  font-size: 1.65rem;
  font-weight: 800;
  color: rgb(15, 23, 42);
  margin-bottom: 16px;
  line-height: 1.4;
}

.guide-intro-text p {
  margin-bottom: 12px;
  color: rgb(51, 65, 85);
  font-size: 0.96rem;
  line-height: 1.75;
}

.guide-section {
  margin-top: 32px;
  padding-top: 24px;
  border-top: 1px solid rgb(241, 245, 249);
}

.guide-section-title {
  font-size: 1.3rem;
  font-weight: 800;
  color: rgb(30, 41, 59);
  margin-bottom: 16px;
}

.guide-flow-grid {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 10px;
  background-color: rgb(248, 250, 252);
  padding: 16px;
  border-radius: 10px;
  margin: 18px 0;
  border: 1px solid rgb(226, 232, 240);
}

.flow-step {
  display: flex;
  align-items: center;
  gap: 8px;
  background-color: rgb(255, 255, 255);
  padding: 8px 14px;
  border-radius: 6px;
  font-weight: 700;
  font-size: 0.88rem;
  color: rgb(30, 41, 59);
  border: 1px solid rgb(203, 213, 225);
}

.flow-step span {
  background-color: rgb(37, 99, 235);
  color: rgb(255, 255, 255);
  border-radius: 50px;
  width: 20px;
  height: 20px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
}

.flow-arrow {
  color: rgb(148, 163, 184);
  font-weight: 800;
}

.highlight-callout {
  background-color: rgb(254, 252, 232);
  border-left: 4px solid rgb(234, 179, 8);
  padding: 14px 18px;
  border-radius: 6px;
  font-weight: 700;
  color: rgb(133, 77, 14);
  margin: 16px 0;
}

.parallel-cards-2col {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
  margin: 20px 0;
}

.parallel-cards-3col {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 20px;
  margin: 20px 0;
}

.parallel-card {
  background-color: rgb(248, 250, 252);
  border-radius: 10px;
  padding: 20px;
  border: 1px solid rgb(226, 232, 240);
}

.parallel-card h4 {
  font-size: 1.08rem;
  color: rgb(30, 41, 59);
  margin-bottom: 10px;
  font-weight: 700;
}

.parallel-card p {
  font-size: 0.9rem;
  color: rgb(71, 85, 105);
  margin-bottom: 8px;
}

.sub-note {
  font-size: 0.85rem;
  color: rgb(100, 116, 139);
  font-style: italic;
}

.check-grid-5 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 12px;
  margin: 18px 0;
}

.check-item {
  background-color: rgb(240, 253, 244);
  border: 1px solid rgb(187, 247, 208);
  border-radius: 8px;
  padding: 12px;
  text-align: center;
  font-size: 0.85rem;
  font-weight: 700;
  color: rgb(22, 101, 52);
}

.check-item span {
  display: block;
  font-size: 0.75rem;
  color: rgb(22, 163, 74);
  margin-bottom: 4px;
}

.pitfalls-grid-5 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 18px;
  margin: 20px 0;
}

.pitfall-card {
  background-color: rgb(254, 242, 242);
  border: 1px solid rgb(254, 202, 202);
  border-radius: 10px;
  padding: 18px;
  position: relative;
}

.pitfall-badge {
  display: inline-block;
  background-color: rgb(220, 38, 38);
  color: rgb(255, 255, 255);
  font-size: 0.75rem;
  font-weight: 800;
  padding: 2px 10px;
  border-radius: 10px;
  margin-bottom: 8px;
}

.pitfall-card h4 {
  font-size: 1rem;
  color: rgb(153, 27, 27);
  margin-bottom: 8px;
  font-weight: 700;
}

.pitfall-card p {
  font-size: 0.88rem;
  color: rgb(127, 29, 29);
  margin-bottom: 6px;
}

.pitfall-sub {
  font-size: 0.82rem;
  color: rgb(185, 28, 28);
}

.platform-card {
  text-align: center;
}

.platform-icon {
  font-size: 2rem;
  margin-bottom: 10px;
}

.mini-steps {
  background-color: rgb(255, 255, 255);
  border: 1px dashed rgb(59, 130, 246);
  padding: 8px;
  border-radius: 6px;
  font-size: 0.82rem;
  font-weight: 700;
  color: rgb(29, 78, 216);
  margin: 10px 0;
}

.contrast-cards {
  margin: 18px 0;
}

.contrast-card {
  border-radius: 10px;
  padding: 18px;
  border: 1px solid rgb(226, 232, 240);
}

.card-a {
  background-color: rgb(241, 245, 249);
}

.card-b {
  background-color: rgb(240, 253, 244);
  border-color: rgb(187, 247, 208);
}

.contrast-tag {
  display: inline-block;
  font-size: 0.78rem;
  font-weight: 800;
  padding: 3px 10px;
  border-radius: 12px;
  background-color: rgb(100, 116, 139);
  color: rgb(255, 255, 255);
  margin-bottom: 10px;
}

.tag-good {
  background-color: rgb(22, 163, 74);
}

.questions-grid-3 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 16px;
  margin: 20px 0;
}

.q-card {
  background-color: rgb(239, 246, 255);
  border: 1px solid rgb(191, 219, 254);
  border-radius: 10px;
  padding: 18px;
  text-align: center;
}

.q-num {
  font-size: 0.8rem;
  font-weight: 800;
  color: rgb(29, 78, 216);
  margin-bottom: 6px;
}

.q-card p {
  font-size: 0.95rem;
  font-weight: 700;
  color: rgb(30, 58, 138);
}

.faq-accordion-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 16px;
  margin: 20px 0;
}

.faq-item-card {
  background-color: rgb(248, 250, 252);
  border-radius: 10px;
  padding: 18px;
  border: 1px solid rgb(226, 232, 240);
}

.faq-item-card h4 {
  font-size: 0.98rem;
  color: rgb(30, 41, 59);
  margin-bottom: 8px;
  font-weight: 700;
}

.faq-item-card p {
  font-size: 0.88rem;
  color: rgb(71, 85, 105);
}

.guide-footer-callout {
  background-color: rgb(30, 41, 59);
  color: rgb(255, 255, 255);
  border-radius: 12px;
  padding: 30px;
  margin-top: 35px;
}

.guide-footer-callout h3 {
  font-size: 1.35rem;
  margin-bottom: 16px;
  color: rgb(248, 250, 252);
}

.guide-footer-callout p {
  font-size: 0.92rem;
  color: rgb(203, 213, 225);
  margin-bottom: 10px;
  line-height: 1.7;
}

.final-motto {
  font-weight: 700;
  color: rgb(253, 224, 71);
  margin-top: 15px;
  font-size: 1rem;
}
"""

forbidden_symbols = ['!', '！', '@', '#', '￥', '%', '……', '&', '*']
found = [sym for sym in forbidden_symbols if sym in css_addition]
print("Forbidden symbols in CSS addition:", found)

if not found:
    css_path = r"c:\Users\USER\Desktop\博客\jichangdian.xyz\static\css\style.css"
    with open(css_path, "a", encoding="utf-8") as f:
        f.write("\n" + css_addition)
    print("Successfully appended clean CSS to static/css/style.css with EXACT 0 forbidden symbols!")
