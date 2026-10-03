---
title: "Clash Verge配置教程小白版：汉化设置、订阅导入与规则分流"
date: 2026-10-02
categories: ["客户端配置"]
tags: ["Clash Verge下载", "TUN模式设置", "Clash汉化教程", "订阅链接导入Clash"]
primary_keyword: "Clash Verge配置教程小白版"
secondary_keywords: ["Clash Verge下载", "TUN模式设置", "Clash汉化教程", "订阅链接导入Clash"]
search_intent: "提供Windows与macOS平台下Clash Verge Rev极简安装、汉化设置、订阅导入与TUN模式开启指南"
description: "Clash Verge Rev配置教程小白保姆级指南，手把手教你在Windows与macOS上下载安装、开启中文界面、导入机场订阅链接及开启TUN模式全全局接管。"
keywords: ["Clash Verge配置教程小白版", "Clash Verge下载", "TUN模式设置", "Clash汉化教程", "订阅链接导入Clash"]
---

Clash Verge Rev 是当前 Windows 与 macOS 平台上最受欢迎的新一代开源 Clash 客户端。相比传统的 Clash for Windows，它拥有原生的中文界面、支持最新的 Mihomo (Clash Meta) 内核，并且完全开源无安全隐患。

本文为您带来小白保姆级图文配置指南。

---

## 1. 软件下载与安装准备

官方开源发布页支持 Windows (x64) 与 macOS (Intel / Apple Silicon M芯片)。
- **Windows 用户**：下载 `.msi` 或 `.exe` 安装包安装。
- **Mac 用户**：下载 `.dmg` 文件拖入应用程序即可。如果是 M1/M2/M3 芯片，可参考 [Mac Clash Verge Rev 专属指南](/posts/kehuduan-peizhi/mac-m-chip-clash-verge-rev-peizhi-zhinan/)。

---

## 2. 软件汉化与基础设置

1. 打开软件，点击左侧菜单栏底部的 **`Settings (设置)`**。
2. 找到 **`Language`** 选项，下拉选择 **`简体中文`**。
3. 勾选 **`开机自启 (Auto Launch)`** 与 **`静默启动`**。

---

## 3. 导入机场订阅链接

1. 登录您的机场后台（如 [灵动云](https://varnexa.lingdongaff.com/#/?code=vFPRdc1J) 或 [飞猫云](https://flycat1.flycatvipaff.cc/#/?code=KRjsCIZV)），点击“一键订阅”，选择 **`复制 Clash 订阅链接`**。
2. 打开 Clash Verge，点击左侧栏的 **`订阅 (Profiles)`**。
3. 将复制的 URL 粘贴到上方框内，点击右侧的 **`导入 (Import)`** 按钮。
4. 看到右侧显示“成功拉取节点”并出现机场名字卡片，即表示导入成功！

---

## 4. 开启系统代理与 TUN 模式

1. 点击左侧栏 **`代理 (Proxies)`**，模式建议选择 **`规则 (Rule)`**（国内直连，国外走节点）。
2. 在节点列表中选择一个速度较快且倍率正常的香港或日本节点（参考 [节点倍率与案例分析](/posts/rumen-jiaocheng/jichang-jiedian-beilv-yu-yanchi-anli-jiangjie/)）。
3. 回到左侧 **`设置`**，开启 **`系统代理 (System Proxy)`** 开关。
4. **进阶设置（强烈推荐）**：开启 **`TUN 模式`**！开启后可以完美解决 UWP 软件、游戏客户端及 Telegram 不走代理的问题。

---

## 5. 常见报错解决 FAQ

### Q: 开启系统代理后网页打不开怎么办？
在订阅列表中右键更新当前机场配置文件；如果依然打不开，进入 `设置` 点击 `重置服务模式 / TUN` 恢复网络驱动。
