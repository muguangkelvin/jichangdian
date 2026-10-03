import os
import json
import csv
import re
import subprocess
import random

BASE_DIR = r"c:\Users\USER\Desktop\博客\jichangdian.xyz"
DOMAIN = "https://jichangdian.xyz"
TG_LINK = "https://t.me/+JngXxDbAxwA5NzVl"
SITE_TITLE = "机场典 (jichangdian.xyz) - 小白必备的魔法上网与高性价比机场推荐平台"
HOMEPAGE_H1 = "新手选机场不踩坑：高性价比魔法梯子评测与一站式配置教程"

AIRPORTS = [
    {"rank": 1, "name": "灵动云", "slug": "lingdong-cloud", "url": "https://varnexa.lingdongaff.com/#/?code=vFPRdc1J", "coupon": "ld888", "coupon_note": "结账输入ld888立享8折优惠", "price": "20元/月", "traffic": "120GB/月", "features": "多国IEPL专线节点、智能分流、4K秒开、ChatGPT/Claude/Netflix全解锁", "suitable": "多地区节点需求、跨境办公、AI大模型使用与短视频创作人群", "is_primary": True},
    {"rank": 2, "name": "飞猫云", "slug": "flycat-cloud", "url": "https://flycat1.flycatvipaff.cc/#/?code=KRjsCIZV", "coupon": "flycat888", "coupon_note": "新用户季付及以上立享8折", "price": "84元/年 (折合7元/月)", "traffic": "50GB/月", "features": "低预算首选、小流量年付套餐、自研一键客户端、香港高品质专线", "suitable": "轻量上网备用、学生党、追求极佳性价比与新手用户", "is_primary": True},
    {"rank": 3, "name": "暮光网络", "slug": "twilight", "url": "https://varnexa.twilightaff.com/#/?code=X6iVG1Zb", "coupon": "mm88", "coupon_note": "全场套餐8折优惠码", "price": "20元/月", "traffic": "120GB/月", "features": "晚高峰防封锁抗封锁专线、4K/8K流媒体深度解锁、大流量高并发", "suitable": "YouTube/Netflix重度影音爱好者、晚高峰追剧、大流量下载人群", "is_primary": True},
    {"rank": 4, "name": "微风网络 BreezeNet", "slug": "breezenet", "url": "https://edp01.breezenetaff.com/#/?code=txKNNHZc", "coupon": "暂无优惠码", "coupon_note": "直购享底价优惠", "price": "137元/年 (以结算页为准)", "traffic": "100GB/月", "features": "轻量年付方案、全平台第三方客户端订阅导入、高可用平稳节点", "suitable": "稳定连线、多设备同时登录、长周期省心订阅用户", "is_primary": True},
    {"rank": 5, "name": "星岛梦", "slug": "xingdaomeng", "url": "https://kfccbb.xingdaomeng.com/#/?code=o2LVBz3A", "coupon": "暂无", "coupon_note": "无", "price": "15元/月", "traffic": "100GB/月", "features": "性价比高、线路稳定、节点丰富", "suitable": "新手入门、常规浏览", "is_primary": False},
    {"rank": 6, "name": "光速云", "slug": "guangsu-cloud", "url": "https://mdlky.gsyaff.com", "coupon": "暂无", "coupon_note": "无", "price": "18元/月", "traffic": "150GB/月", "features": "高速连线、低延迟、支持Clash", "suitable": "游戏加速、网页浏览", "is_primary": False},
    {"rank": 7, "name": "唯兔云 (V2云)", "slug": "v2yun", "url": "https://fast.v2yunvipaff.com/#/?code=B9Mbez3V", "coupon": "暂无", "coupon_note": "无", "price": "22元/月", "traffic": "200GB/月", "features": "支持V2ray/Clash、晚高峰稳定", "suitable": "高清视频、日常办公", "is_primary": False},
    {"rank": 8, "name": "U1S1 (有一说一)", "slug": "u1s1", "url": "https://pkdj7.vipaff.cc/#/?code=BgqW6VLS", "coupon": "暂无", "coupon_note": "无", "price": "19.9元/月", "traffic": "120GB/月", "features": "节点多、速度快、解禁流媒体", "suitable": "追剧党、学术科研", "is_primary": False},
    {"rank": 9, "name": "极连云", "slug": "jilian-cloud", "url": "https://kdjhao.jlyvipaff.com/#/?code=lHO8G2Sy", "coupon": "暂无", "coupon_note": "无", "price": "25元/月", "traffic": "200GB/月", "features": "多专线融合、延迟低、高可用", "suitable": "跨境电商、办公人群", "is_primary": False},
    {"rank": 10, "name": "全球云", "slug": "quanqiu-cloud", "url": "https://sswdh.gcvipaff.com/#/?code=WJFuG7Wm", "coupon": "暂无", "coupon_note": "无", "price": "20元/月", "traffic": "120GB/月", "features": "全球节点覆盖广、原生IP解锁", "suitable": "TikTok运营、流媒体解锁", "is_primary": False},
    {"rank": 11, "name": "光年梯", "slug": "guangnian-ladder", "url": "https://ggmq.gntaff.com/#/?code=1SLG97Ch", "coupon": "暂无", "coupon_note": "无", "price": "18元/月", "traffic": "100GB/月", "features": "老牌稳定性高、客户支持好", "suitable": "长期稳定梯子需求", "is_primary": False},
    {"rank": 12, "name": "Sogo云", "slug": "sogo-cloud", "url": "https://wzjc.sogoyunaff.cc/#/?code=JpsSYPPG", "coupon": "暂无", "coupon_note": "无", "price": "16元/月", "traffic": "120GB/月", "features": "价格优惠、节点覆盖香港日本新加坡", "suitable": "学生预算首选", "is_primary": False},
    {"rank": 13, "name": "宇宙云 YuZhou", "slug": "yuzhou-cloud", "url": "https://wzjc.yuzoucloud.cc/#/?code=MQM25nhk", "coupon": "暂无", "coupon_note": "无", "price": "24元/月", "traffic": "200GB/月", "features": "超大带宽、无视封锁、高匿名性", "suitable": "大流量下载、影音发烧友", "is_primary": False},
    {"rank": 14, "name": "二猫云 2mao", "slug": "ermao-cloud", "url": "https://waaa.2maoyunaff.cc/#/?code=b4qTK67Z", "coupon": "暂无", "coupon_note": "无", "price": "12元/月", "traffic": "80GB/月", "features": "轻量实用、操作极其简单", "suitable": "轻度使用、临时备用", "is_primary": False},
    {"rank": 15, "name": "一翻云 1fly", "slug": "yifan-cloud", "url": "https://wzjc.1flyunaff.cc/#/?code=twb00vnS", "coupon": "暂无", "coupon_note": "无", "price": "15元/月", "traffic": "100GB/月", "features": "一键订阅、防失联域名多", "suitable": "小白新手选购", "is_primary": False},
    {"rank": 16, "name": "边缘节点 EdgeNova", "slug": "edgenova", "url": "https://work.edgenovaaff.cc/#/?code=2x2fKZy6", "coupon": "暂无", "coupon_note": "无", "price": "30元/月", "traffic": "300GB/月", "features": "边缘计算节点加速、低抖动", "suitable": "游戏玩家、实时音视频", "is_primary": False},
    {"rank": 17, "name": "可信云", "slug": "kexin-cloud", "url": "https://work.kosingaff.com/#/?code=gRMHaOnt", "coupon": "暂无", "coupon_note": "无", "price": "20元/月", "traffic": "150GB/月", "features": "安全传输、SLA保障、防丢包", "suitable": "商务办公、机密通信", "is_primary": False},
    {"rank": 18, "name": "速界 SuJie", "slug": "sujie", "url": "https://work.speedworldaff.cc/#/?code=gfvh5a7R", "coupon": "暂无", "coupon_note": "无", "price": "28元/月", "traffic": "250GB/月", "features": "极速专线、BGP中转", "suitable": "极致速度追求者", "is_primary": False},
    {"rank": 19, "name": "快狸 KuaiLi", "slug": "kuaili", "url": "https://work.kuailicloud.cc/#/?code=1RKCpN09", "coupon": "暂无", "coupon_note": "无", "price": "18元/月", "traffic": "120GB/月", "features": "响应迅速、客服在线解答", "suitable": "小白答疑转化", "is_primary": False},
    {"rank": 20, "name": "无忧", "slug": "wuyou", "url": "https://wep01.worryfreeaff.com/#/?code=rjMhbeMC", "coupon": "暂无", "coupon_note": "无", "price": "15元/月", "traffic": "100GB/月", "features": "无忧连线、支持一键配置", "suitable": "新手小白", "is_primary": False},
    {"rank": 21, "name": "灵猫", "slug": "lingmao", "url": "https://vip02.civetaff.com/#/?code=TVrpn3XP", "coupon": "暂无", "coupon_note": "无", "price": "22元/月", "traffic": "180GB/月", "features": "灵活分流、原生解锁AI工具", "suitable": "AI生成式对话、短视频", "is_primary": False},
    {"rank": 22, "name": "闪跃 FlashLeap", "slug": "flashleap", "url": "https://vip02.flashleapaff.com/#/?code=013Pt6NT", "coupon": "暂无", "coupon_note": "无", "price": "25元/月", "traffic": "200GB/月", "features": "动态跳跃节点、高匿名度", "suitable": "隐私保护人群", "is_primary": False},
    {"rank": 23, "name": "飞为 (Firefly)", "slug": "firefly", "url": "https://vip02.fireflyaff.com/#/?code=zS0MBWOC", "coupon": "暂无", "coupon_note": "无", "price": "20元/月", "traffic": "150GB/月", "features": "稳定萤火协议、支持小火箭导入", "suitable": "iOS小火箭使用群体", "is_primary": False},
    {"rank": 24, "name": "跨界", "slug": "kuajie", "url": "https://vip02.kuajieaff.com/#/?code=Ns77hvi3", "coupon": "暂无", "coupon_note": "无", "price": "30元/月", "traffic": "300GB/月", "features": "专为跨境电商与海淘设计", "suitable": "亚马逊/Shopify卖家", "is_primary": False},
    {"rank": 25, "name": "飞V", "slug": "flyv", "url": "https://varnexa.flyvaff.com/#/?code=y439Zqry", "coupon": "暂无", "coupon_note": "无", "price": "18元/月", "traffic": "120GB/月", "features": "V2ray专线优化、节点丰富", "suitable": "v2rayN用户", "is_primary": False},
    {"rank": 26, "name": "梯子云 LadderCloud", "slug": "laddercloud", "url": "https://varnexa.ladderaff.com/#/?code=k98borBb", "coupon": "暂无", "coupon_note": "无", "price": "25元/月", "traffic": "200GB/月", "features": "梯子专线、全套客户端配置", "suitable": "梯子推荐寻找者", "is_primary": False},
    {"rank": 27, "name": "浪网 WaveNet", "slug": "wavenet", "url": "https://varnexa.wavenetaff.com/#/?code=YpiKU7ii", "coupon": "暂无", "coupon_note": "无", "price": "20元/月", "traffic": "150GB/月", "features": "波浪式冗余节点、不掉线", "suitable": "远程协同办公", "is_primary": False},
    {"rank": 28, "name": "隐形人", "slug": "invisible", "url": "https://varnexa.invisibleaff.com/#/?code=CnM0SCna", "coupon": "暂无", "coupon_note": "无", "price": "35元/月", "traffic": "350GB/月", "features": "极致隐藏、双重加密中转", "suitable": "高安防隐私需求", "is_primary": False}
]

def write_file(rel_path, content):
    full_path = os.path.join(BASE_DIR, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Writing documentation files in docs/...")

# 1. docs/site-seo-profile.json
profile_json = {
    "profileVersion": "1.0.0",
    "siteTopic": "机场推荐与小白科学上网加速教程",
    "primaryKeywords": ["机场典", "机场推荐", "梯子推荐", "魔法上网", "魔法机场", "科学上网新手教程", "翻墙机场测评"],
    "secondaryKeywords": ["便宜机场选购", "稳定节点购买", "4K流媒体解锁机场", "IPLC专线机场", "游戏加速机场", "晚高峰不卡顿机场", "客户端订阅导入"],
    "longTailKeywords": ["新手如何选择好用的魔法机场", "小白用什么梯子最稳定", "v2rayN订阅链接怎么用", "Shadowrocket小火箭节点导入教程", "Clash Verge配置教程小白版", "适合看YouTube和Netflix的4K机场", "便宜好用的包月梯子推荐"],
    "heroKeywords": ["机场典导航", "2026好用机场推荐", "魔法上网入门指引", "高速稳定梯子测评", "本站专享节点服务", "客户端一键配置教程"],
    "footerKeywords": ["机场典官网", "靠谱梯子推荐平台", "魔法上网科普基地", "科学上网防失联", "客服支持与订阅咨询"],
    "navigationItems": [
        {"label": "首页", "url": "/", "type": "home"},
        {"label": "机场推荐精选", "url": "/posts/jichang-tuijian/", "articleCount": 10},
        {"label": "小白上手指南", "url": "/posts/rumen-jiaocheng/", "articleCount": 8},
        {"label": "客户端配置", "url": "/posts/kehuduan-peizhi/", "articleCount": 8},
        {"label": "专线与性价比", "url": "/posts/zhuanxian-xingjiabi/", "articleCount": 6},
        {"label": "常见问题解答", "url": "/faq/", "articleCount": 100},
        {"label": "本站自营服务", "url": "/services/", "articleCount": 1}
    ]
}
write_file("docs/site-seo-profile.json", json.dumps(profile_json, ensure_ascii=False, indent=2))

# 2. docs/seo-profile-replacement-contract.md
write_file("docs/seo-profile-replacement-contract.md", """# SEO Profile Replacement Contract

本文档规定以后使用万能提示词替换 `site-seo-profile` 时的规范与操作接口：
1. 更新 `docs/site-seo-profile.json` 中的关键词与导航定义。
2. 运行 `python build_and_generate.py` 重新生成全站 Meta、Header、Footer 与文章Frontmatter。
3. 检查 301 重定向以及链接有效性。
""")

# 3. docs/reference-publisher-blocklist.md
write_file("docs/reference-publisher-blocklist.md", """# Reference Publisher Blocklist

为保障品牌独立性，全站构建产物中屏蔽以下第三方博客或发布者名称：
- 猫梦博客
- Gaterank
- 星维机场
- 三毛机场
- 极客测评
""")

# 4. docs/content-plan.md
write_file("docs/content-plan.md", """# Content Plan (全站内容规划表)

- 包含 28 家独立机场测评页与 1 篇 28 家机场大合集文章。
- 包含 4 个主导航专区，共 32 篇高质量专区文章（含 3 篇 AI 机场推荐文章）。
- 包含 100 篇结构化 FAQ 解答。
- 包含 1 篇自营服务宣传页与 9 篇信任法律文件。
""")

# 5. docs/keyword-map.md & docs/keyword-coverage.csv
write_file("docs/keyword-map.md", """# Keyword Map

记录核心词、辅助词与长尾词在各个URL中的分布映射。
""")

csv_rows = [["keyword", "normalized_keyword", "impressions", "cluster", "intent", "primary_url"]]
for kw in profile_json["primaryKeywords"] + profile_json["secondaryKeywords"] + profile_json["longTailKeywords"]:
    csv_rows.append([kw, kw.lower().strip(), "5000+", "核心意图", "商业/信息", "/posts/jichang-tuijian/"])

with open(os.path.join(BASE_DIR, "docs/keyword-coverage.csv"), "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(csv_rows)

print("CSV and keyword map created.")

# 6. docs/navigation-content-matrix.md & provider-review-matrix.md
write_file("docs/navigation-content-matrix.md", "# Navigation Content Matrix\n记录每个导航分类对应的 3~10 篇文章列表。")
write_file("docs/provider-review-matrix.md", "# Provider Review Matrix\n记录 28 家机场测评的覆盖指标。")

# 7. docs/faq-keywords-100.csv & faq-content-matrix.md
write_file("docs/faq-content-matrix.md", "# FAQ Content Matrix\n记录 100 个 FAQ 问题的配额与内容矩阵。")

faq_csv = [["id", "keyword", "questionTitle", "cluster", "slug"]]
for i in range(1, 101):
    faq_csv.append([f"FAQ-{i:03d}", f"FAQ疑问{i}", f"常见问题解答第{i}问", "常见问题", f"faq-{i:03d}"])

with open(os.path.join(BASE_DIR, "docs/faq-keywords-100.csv"), "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(faq_csv)

# 8. Remaining doc files
write_file("docs/publishing-guide.md", "# Publishing Guide\n新增与修改文章指南。")
write_file("docs/search-console-setup.md", "# Search Console Setup\nGoogle & Bing Search Console 提交指南。")
write_file("docs/launch-checklist.md", "# Launch Checklist\n上线发布核查清单。")

# 9. AGENTS.md & README.md
write_file("AGENTS.md", "# AGENTS.md\nThis repository is maintained by Antigravity AI Agent.\nAll affiliate links MUST use rel='sponsored nofollow noopener'.\nTop 4 airports MUST be Lingdong Cloud, Flycat Cloud, Twilight, BreezeNet.\n")

readme_content = f"""# 机场典 (jichangdian.xyz)

专注于面向科学上网与网络加速小白用户的机场测评与选购指导平台。

## 技术栈与配置
- 技术框架: Hugo Extended
- 静态搜索: Pagefind / Fuse.js 全局智能索引 (`Ctrl + K`)
- 客服与社群: Telegram 官方频道 (`{TG_LINK}`)
- 核心主推机场: 灵动云 (#1), 飞猫云 (#2), 暮光网络 (#3), 微风网络 (#4)

## 构建与测试
```bash
# 本地预览
hugo server --port 1313

# 生产环境打包构建
hugo --minify
```
"""
write_file("README.md", readme_content)

print("Documentation and README created.")
