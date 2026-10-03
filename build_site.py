import os
import json
import csv
import re
import subprocess
import sys

BASE_DIR = r"c:\Users\USER\Desktop\博客\jichangdian.xyz"

# 1. Primary Data Definitions
DOMAIN = "https://jichangdian.xyz"
TG_LINK = "https://t.me/+JngXxDbAxwA5NzVl"
SITE_TITLE = "机场典 (jichangdian.xyz) - 小白必备的魔法上网与高性价比机场推荐平台"
HOMEPAGE_H1 = "新手选机场不踩坑：高性价比魔法梯子评测与一站式配置教程"

AIRPORTS = [
    {
        "rank": 1,
        "name": "灵动云",
        "slug": "lingdong-cloud",
        "url": "https://varnexa.lingdongaff.com/#/?code=vFPRdc1J",
        "coupon": "ld888",
        "coupon_note": "结账输入ld888立享8折优惠",
        "price": "20元/月",
        "traffic": "120GB/月",
        "features": "多国IEPL专线节点、智能分流、4K秒开、ChatGPT/Claude/Netflix全解锁",
        "suitable": "多地区节点需求、跨境办公、AI大模型使用与短视频创作人群",
        "is_primary": True
    },
    {
        "rank": 2,
        "name": "飞猫云",
        "slug": "flycat-cloud",
        "url": "https://flycat1.flycatvipaff.cc/#/?code=KRjsCIZV",
        "coupon": "flycat888",
        "coupon_note": "新用户季付及以上立享8折",
        "price": "84元/年 (折合7元/月)",
        "traffic": "50GB/月",
        "features": "低预算首选、小流量年付套餐、自研一键客户端、香港高品质专线",
        "suitable": "轻量上网备用、学生党、追求极佳性价比与新手用户",
        "is_primary": True
    },
    {
        "rank": 3,
        "name": "暮光网络",
        "slug": "twilight",
        "url": "https://varnexa.twilightaff.com/#/?code=X6iVG1Zb",
        "coupon": "mm88",
        "coupon_note": "全场套餐8折优惠码",
        "price": "20元/月",
        "traffic": "120GB/月",
        "features": "晚高峰防封锁抗封锁专线、4K/8K流媒体深度解锁、大流量高并发",
        "suitable": "YouTube/Netflix重度影音爱好者、晚高峰追剧、大流量下载人群",
        "is_primary": True
    },
    {
        "rank": 4,
        "name": "微风网络 BreezeNet",
        "slug": "breezenet",
        "url": "https://edp01.breezenetaff.com/#/?code=txKNNHZc",
        "coupon": "暂无优惠码",
        "coupon_note": "直购享底价优惠",
        "price": "137元/年 (以结算页为准)",
        "traffic": "100GB/月",
        "features": "轻量年付方案、全平台第三方客户端订阅导入、高可用平稳节点",
        "suitable": "稳定连线、多设备同时登录、长周期省心订阅用户",
        "is_primary": True
    },
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

print(f"Loaded {len(AIRPORTS)} airports.")
