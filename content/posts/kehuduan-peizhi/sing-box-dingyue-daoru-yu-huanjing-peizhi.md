---
title: "Sing-box订阅导入教程：新一代通用内核客户端配置手册"
date: 2026-10-02
categories: ["客户端配置"]
tags: ["Sing-box客户端配置", "Hysteria2协议导入", "Sing-box规则分流", "通用代理内核"]
primary_keyword: "Sing-box订阅导入教程"
secondary_keywords: ["Sing-box客户端配置", "Hysteria2协议导入", "Sing-box规则分流", "通用代理内核"]
search_intent: "指导用户配置新一代跨平台核心代理工具Sing-box，导入机场订阅并设置Hysteria2/TUIC协议"
description: "Sing-box订阅导入保姆级教程，详细讲解新一代通用代理内核在Windows、Mac及移动端上的配置步骤、Hysteria2/TUIC协议支持与规则分流。"
keywords: ["Sing-box订阅导入教程", "Sing-box客户端配置", "Hysteria2协议导入", "Sing-box规则分流", "通用代理内核"]
---

Sing-box 是近年来备受瞩目的新一代通用代理平台。它具备极高的运行效率与极其轻量的内存占用，原生支持最新的 Hysteria 2、TUIC v5、ShadowTLS 及 VLESS 协议。

本文为您带来 Sing-box 客户端在各平台下的订阅导入配置手册。

---

## 1. 为什么越来越多用户选择 Sing-box？

- **极致性能与省电**：底层采用 Go 语言全新编写，内存占用仅为传统客户端的三分之一，特别适合移动端手机。
- **下一代协议原生支持**：对 Hysteria 2 协议支持极佳，在弱网、高丢包环境下依然能跑满带宽。
- **跨平台统一配置**：支持 iOS、Android、Windows 及 macOS。

---

## 2. 导入 Sing-box 订阅步骤

1. **获取 Sing-box 专属订阅**：登录机场用户后台（如 [灵动云](https://varnexa.lingdongaff.com/#/?code=vFPRdc1J)），在“一键订阅”下拉菜单中选择 **`复制 Sing-box 订阅链接`**。
2. **在客户端添加 Profiles**：
   - 打开 Sing-box 客户端，进入 `Profiles / 订阅` 选项卡。
   - 点击右上角加号 `+`，选择 `Create from URL`。
   - 填写名称（如“灵动云 Sing-box”），在 URL 框内粘贴订阅地址，点击保存。
3. **启用配置并开始连接**：在主界面选择刚才导入的 Profile，点击 `Enable` 开启代理。

---

## 3. Sing-box 与 Clash 内核选择对比

如果您不确定该选择 Sing-box 还是 Clash，可阅读 [Clash Meta 与 Sing-box 深度对比](/posts/kehuduan-peizhi/clash-meta-singbox-duibi-yu-xuanze/)。简单而言：追求极简可视化推荐 Clash Verge；追求极致速度与新协议推荐 Sing-box。
