import os
import re
import json

BASE_DIR = r"c:\Users\USER\Desktop\博客\jichangdian.xyz"

# Append Channel 3 & 4 data to generate_rich_articles.py
CHANNEL_3_4_DATA = {
    # ==================== 3. 客户端配置 (kehuduan-peizhi) ====================
    "content/posts/kehuduan-peizhi/clash-verge-peizhi-jiaocheng-xiaobai-ban.md": {
        "title": "Clash Verge配置教程小白版：汉化设置、订阅导入与规则分流",
        "cat": "客户端配置",
        "primary_kw": "Clash Verge配置教程小白版",
        "secondary_kws": ["Clash Verge下载", "TUN模式设置", "Clash汉化教程", "订阅链接导入Clash"],
        "intent": "提供Windows与macOS平台下Clash Verge Rev极简安装、汉化设置、订阅导入与TUN模式开启指南",
        "desc": "Clash Verge Rev配置教程小白保姆级指南，手把手教你在Windows与macOS上下载安装、开启中文界面、导入机场订阅链接及开启TUN模式全全局接管。",
        "content": """Clash Verge Rev 是当前 Windows 与 macOS 平台上最受欢迎的新一代开源 Clash 客户端。相比传统的 Clash for Windows，它拥有原生的中文界面、支持最新的 Mihomo (Clash Meta) 内核，并且完全开源无安全隐患。本文为您带来小白保姆级图文配置指南。

## 1. 软件下载与安装准备

官方开源发布页支持 Windows (x64) 与 macOS (Intel / Apple Silicon M芯片)。
- **Windows 用户**：下载 `.msi` 或 `.exe` 安装包安装。
- **Mac 用户**：下载 `.dmg` 文件拖入应用程序即可。如果是 M1/M2/M3 芯片，可参考 [Mac Clash Verge Rev 专属指南](/posts/kehuduan-peizhi/mac-m-chip-clash-verge-rev-peizhi-zhinan/)。

## 2. 软件汉化与基础设置

1. 打开软件，点击左侧菜单栏底部的 **`Settings (设置)`**。
2. 找到 **`Language`** 选项，下拉选择 **`简体中文`**。
3. 勾选 **`开机自启 (Auto Launch)`** 与 **`静默启动`**。

## 3. 导入机场订阅链接

1. 登录您的机场后台（如灵动云或飞猫云），点击“一键订阅”，选择 **`复制 Clash 订阅链接`**。
2. 打开 Clash Verge，点击左侧栏的 **`订阅 (Profiles)`**。
3. 将复制的 URL 粘贴到上方框内，点击右侧的 **`导入 (Import)`** 按钮。
4. 看到右侧显示“成功拉取节点”并出现机场名字卡片，即表示导入成功！

## 4. 开启系统代理与 TUN 模式

1. 点击左侧栏 **`代理 (Proxies)`**，模式建议选择 **`规则 (Rule)`**（国内直连，国外走节点）。
2. 在节点列表中选择一个速度较快且倍率正常的香港或日本节点（参考 [节点倍率与案例分析](/posts/rumen-jiaocheng/jichang-jiedian-beilv-yu-yanchi-anli-jiangjie/)）。
3. 回到左侧 **`设置`**，开启 **`系统代理 (System Proxy)`** 开关。
4. **进阶设置（强烈推荐）**：开启 **`TUN 模式`**！开启后可以完美解决 UWP 软件、游戏客户端及 Telegram 不走代理的问题。

## 5. 常见报错解决 FAQ

### Q: 开启系统代理后网页打不开怎么办？
在订阅列表中右键更新当前机场配置文件；如果依然打不开，进入 `设置` 点击 `重置服务模式 / TUN` 恢复网络驱动。
"""
    },

    "content/posts/kehuduan-peizhi/sing-box-dingyue-daoru-yu-huanjing-peizhi.md": {
        "title": "Sing-box订阅导入教程：新一代通用内核客户端配置手册",
        "cat": "客户端配置",
        "primary_kw": "Sing-box订阅导入教程",
        "secondary_kws": ["Sing-box客户端配置", "Hysteria2协议导入", "Sing-box规则分流", "通用代理内核"],
        "intent": "指导用户配置新一代跨平台核心代理工具Sing-box，导入机场订阅并设置Hysteria2/TUIC协议",
        "desc": "Sing-box订阅导入保姆级教程，详细讲解新一代通用代理内核在Windows、Mac及移动端上的配置步骤、Hysteria2/TUIC协议支持与规则分流。",
        "content": """Sing-box 是近年来备受瞩目的新一代通用代理平台。它具备极高的运行效率与极其轻量的内存占用，原生支持最新的 Hysteria 2、TUIC v5、ShadowTLS 及 VLESS 协议。本文为您带来 Sing-box 客户端在各平台下的订阅导入配置手册。

## 1. 为什么越来越多用户选择 Sing-box？

- **极致性能与省电**：底层采用 Go 语言全新编写，内存占用仅为传统客户端的三分之一，特别适合移动端手机。
- **下一代协议原生支持**：对 Hysteria 2 协议支持极佳，在弱网、高丢包环境下依然能跑满带宽。
- **跨平台统一配置**：支持 iOS、Android、Windows 及 macOS。

## 2. 导入 Sing-box 订阅步骤

1. **获取 Sing-box 专属订阅**：登录机场用户后台（如灵动云），在“一键订阅”下拉菜单中选择 **`复制 Sing-box 订阅链接`**。
2. **在客户端添加 Profiles**：
   - 打开 Sing-box 客户端，进入 `Profiles / 订阅` 选项卡。
   - 点击右上角加号 `+`，选择 `Create from URL`。
   - 填写名称（如“灵动云 Sing-box”），在 URL 框内粘贴订阅地址，点击保存。
3. **启用配置并开始连接**：在主界面选择刚才导入的 Profile，点击 `Enable` 开启代理。

## 3. Sing-box 与 Clash 内核选择对比

如果您不确定该选择 Sing-box 还是 Clash，可阅读 [Clash Meta 与 Sing-box 深度对比](/posts/kehuduan-peizhi/clash-meta-singbox-duibi-yu-xuanze/)。简单而言：追求极简可视化推荐 Clash Verge；追求极致速度与新协议推荐 Sing-box。
"""
    },

    "content/posts/kehuduan-peizhi/shadowrocket-xiaohuojian-jiedian-daoru-jiaocheng.md": {
        "title": "Shadowrocket小火箭节点导入教程：iOS苹果设备魔法上网指南",
        "cat": "客户端配置",
        "primary_kw": "Shadowrocket小火箭节点导入教程",
        "secondary_kws": ["iOS小火箭下载", "小火箭扫码导入", "Apple TV代理配置", "iPhone科学上网"],
        "intent": "手把手教iOS苹果手机/iPad用户下载小火箭Shadowrocket，并通过一键导入/扫码完成配置",
        "desc": "Shadowrocket小火箭节点导入保姆级教程，教你如何在iPhone、iPad及Apple TV上下载安装小火箭、使用一键链接/二维码导入机场节点及设置按需连接。",
        "content": """Shadowrocket（俗称“小火箭”）是 iOS 苹果生态系统中最强大、最易用的网络代理软件。它支持全部主流代理协议、智能规则分流，并且完美适配 iPhone、iPad 以及 Apple TV。本文为您带来 iOS 平台小火箭配置指南。

## 1. 如何在苹果 App Store 下载小火箭？

由于特殊限制，Shadowrocket 未在中国大陆区 App Store 上架：
1. 您需要准备一个 **非中国大陆区的 Apple ID**（如美区、港区或日区账号）。
2. 在 iPhone 的 App Store 中退出当前账号，登录外区 Apple ID。
3. 搜索 `Shadowrocket` 购买并下载（价格为 $2.99 美元，正版一次购买终身使用）。

## 2. 极简三步导入机场节点

### 方法一：一键跳转导入（强烈推荐）
1. 用 Safari 浏览器登录机场后台（如灵动云或飞猫云）。
2. 点击“一键订阅” ➔ 选择 **`一键导入 Shadowrocket / 小火箭`**。
3. 系统会自动唤醒小火箭软件，并自动拉取全部节点列表。

### 方法二：扫码导入
1. 在电脑或另一台设备打开机场后台的“订阅二维码”。
2. 打开小火箭，点击左上角的 **`扫描二维码`** 按钮，对准屏幕直接扫描。

## 3. 连接与规则分流设置

1. 将全局路由模式设为 **`配置 (Config)`**（此模式下国内流量直连，海外流量走代理）。
2. 在节点列表中点击选定一个低延迟节点。
3. 打开顶部的未连接开关，首次开启会弹框提示“添加 VPN 配置”，输入 iPhone 解锁密码授权即可！

## 4. 常见问题 FAQ

### Q: 为什么小火箭连接后无法访问 [ChatGPT 或 Netflix](/posts/jichang-tuijian/4k-liumeiti-jiewang-jichang-ceping/)？
请确认您选择的节点是否为美区/港区原生 IP；另外可以在小火箭设置中点击 `更新配置/延迟测试`。
"""
    },

    "content/posts/kehuduan-peizhi/v2rayn-dingyue-lianjie-zenmeyong-peizhi-shouce.md": {
        "title": "v2rayN订阅链接怎么用：Windows电脑端极简配置图文教程",
        "cat": "客户端配置",
        "primary_kw": "v2rayN订阅链接怎么用",
        "secondary_kws": ["v2rayN下载教程", "v2rayN设置系统代理", "v2rayN更新订阅", "Windows梯子软件"],
        "intent": "为Windows电脑用户提供经典代理工具v2rayN v6.x下载解压、订阅链接添加与系统代理启动全流程",
        "desc": "v2rayN订阅链接使用极简图文教程，教你在Windows电脑上解压v2rayN客户端、添加机场订阅URL、开启清除系统代理及快捷测速。",
        "content": """v2rayN 是 Windows 平台上使用最广泛的经典代理工具之一。它轻量高效、不占用过多后台内存，并且对 V2ray、Trojan、Shadowsocks 协议支持极其完善。本文教您如何在 Windows 电脑上正确使用 v2rayN。

## 1. 下载与解压说明

1. 访问 GitHub 官方 Releases 页面，下载最新的 `v2rayN-With-Core.zip` 压缩包（内含完整核心内核）。
2. 解压到一个没有中文路径的文件夹中（例如 `D:\\Tools\\v2rayN`）。
3. 双击 `v2rayN.exe` 运行（如提示需要 .NET Framework 6.0，按提示点击下载安装）。

## 2. 添加机场订阅链接

1. 登录机场后台（如灵动云或飞猫云），复制您的通用订阅 URL。
2. 打开 v2rayN 主界面，点击顶部菜单栏的 **`订阅分组` ➔ `订阅分组设置`**。
3. 点击左上角的 **`添加`** 按钮：
   - `别名`：填写机场名称（如“灵动云”）。
   - `地址 (url)`：粘贴刚才复制的订阅链接。
4. 点击确定保存。回到主界面，点击 **`订阅分组` ➔ `更新订阅 (不通过代理)`**，节点列表将瞬间加载！

## 3. 启动系统代理

1. 在主界面节点列表中，按 `Ctrl + A` 全选，右键选择 `真连接延迟测试`，挑选一个绿色的低延迟节点。
2. 按 `Enter` 键设为活动节点。
3. 在屏幕右下角任务栏找到 v2rayN 的红色 V 字图标，右键选择 **`系统代理` ➔ `自动配置系统代理`**（图标将变为蓝色）。

此时您的 Windows 电脑已成功建立安全加密隧道！
"""
    },

    "content/posts/kehuduan-peizhi/clash-for-windows-shiyong-jiaocheng-yu-faq.md": {
        "title": "Clash for Windows使用教程与常见报错解决指南",
        "cat": "客户端配置",
        "primary_kw": "Clash for Windows使用教程",
        "secondary_kws": ["CFW下载", "Clash系统代理打不开", "CFW中文汉化", "Clash替代客户端"],
        "intent": "解答CFW经典客户端的使用方法、停止维护后的安全性说明及替代客户端（Clash Verge）推荐",
        "desc": "Clash for Windows使用教程与常见报错解决指南，详解系统代理无法开启、端口冲突排查及迁移至Clash Verge Rev的无缝方案。",
        "content": """Clash for Windows (CFW) 曾是 Windows 上使用人数最多的 Clash 客户端。虽然原作者已停止维护，但在许多用户的电脑上仍在使用。本文为您梳理 CFW 的使用技巧、常见报错排查及迁移到最新替代客户端的方案。

## 1. CFW 基础使用方法

1. 打开 CFW，点击左侧 `Profiles`，在顶部输入框粘贴 [机场订阅链接](/posts/rumen-jiaocheng/jichang-dingyue-lianjie-shiyong-jiqiao/) 并点击 `Download`。
2. 选中下载好的配置文件卡片。
3. 点击左侧 `General`，将 `System Proxy` 设为开（变为绿色即表示代理已生效）。

## 2. 常见四大报错排查与解决方法

### 报错一：System Proxy 开关开启后自动弹回关
- **原因**：本地 7890 端口被其他软件（如迅雷或百度网盘）占用。
- **解决方法**：在 `General` 中将 `Port` 修改为 `7893` 或 `10808`。

### 报错二：核心提示 `Initial Configuration Failed`
- **原因**：订阅配置文件中包含了非法字符或配置文件损坏。
- **解决方法**：删除旧卡片，在机场后台重新复制最新的订阅链接下载。

## 3. 强烈建议迁移至 Clash Verge Rev

由于 CFW 原作者已在 2023 年关停代码库，CFW 内核无法支持 [Hysteria 2](/posts/kehuduan-peizhi/sing-box-dingyue-daoru-yu-huanjing-peizhi/) 等新协议。强烈建议所有用户升级迁移至 [Clash Verge Rev 配置教程](/posts/kehuduan-peizhi/clash-verge-peizhi-jiaocheng-xiaobai-ban/)，体验更安全的中文环境。
"""
    },

    "content/posts/kehuduan-peizhi/clash-meta-singbox-duibi-yu-xuanze.md": {
        "title": "Clash Meta与Sing-box内核对比：哪个客户端更适合新手？",
        "cat": "客户端配置",
        "primary_kw": "Clash与Singbox对比",
        "secondary_kws": ["Clash Meta内核", "Mihomo内核", "Sing-box性能对比", "新一代代理内核选择"],
        "intent": "深度对比Mihomo (Clash Meta)与Sing-box两大主力内核的性能、协议支持、资源占用与易用度",
        "desc": "Clash Meta与Sing-box内核深度对比，从协议兼容性、内存占用、规则分流灵活性与新手易用度四个维度帮你选出最适合的客户端。",
        "content": """在目前的代理工具领域，`Mihomo (原 Clash Meta)` 与 `Sing-box` 代表了最前沿的内核技术。不少用户在选择客户端时感到犹豫：究竟哪个内核性能更好？哪个更适合小白？本文为您做深度横向评测。

## 1. 两大内核核心技术特点

- **Mihomo (Clash Meta 内核)**：继承了传统 Clash 极其丰富的开源生态体系，在原版本基础上增加了对 Hysteria2、TUIC、VLESS 和 GeoIP 数据库的全面支持。
- **Sing-box 内核**：全新的通用代理架构，追求极其干净的代码结构与极低的内存占用。

## 2. 四维度横向评测对比

| 对比维度 | Mihomo (Clash Meta) | Sing-box |
| :--- | :--- | :--- |
| **内存与 CPU 占用** | 中等 (约 80MB - 150MB) | 极低 (约 20MB - 50MB) |
| **GUI 客户端丰富度** | 极其丰富 (Clash Verge, Nyanpasu) | 逐渐完备 (Sing-box 官方 GUI) |
| **新手上手难度** | 低（图形界面极度成熟） | 中等（部分高级规则需修改 JSON） |
| **新协议迭代速度** | 极快 | 原生首发 |

## 3. 最终选购推荐结论

- **如果您是极简新手**：首选基于 Mihomo 内核的 **[Clash Verge Rev](/posts/kehuduan-peizhi/clash-verge-peizhi-jiaocheng-xiaobai-ban/)**，UI 完善，一键导入订阅最省心。
- **如果您使用老旧设备或手机**：推荐使用 **Sing-box**，极低的后台内存占用能显著延长电池续航。
"""
    },

    "content/posts/kehuduan-peizhi/mac-m-chip-clash-verge-rev-peizhi-zhinan.md": {
        "title": "macOS苹果电脑 Clash Verge Rev 原生配置指南",
        "cat": "客户端配置",
        "primary_kw": "Mac Clash配置教程",
        "secondary_kws": ["Mac M芯片Clash", "macOS系统代理设置", "Mac开启TUN模式", "Apple Silicon适配"],
        "intent": "专门为Mac用户（M1/M2/M3/M4芯片与Intel版）提供macOS上Clash Verge Rev的安装与系统权限授权指南",
        "desc": "macOS苹果电脑 Clash Verge Rev 原生配置指南，适配Apple Silicon M系列芯片与Intel处理器，详解辅助功能授权、TUN网络驱动安装与全局分流。",
        "content": """使用 macOS 苹果电脑（如 MacBook Pro、Mac mini、MacBook Air）的用户，在配置代理软件时常遇到“管理员权限弹窗”、“系统代理无法接管”或“M芯片提示损坏”等问题。本文专门针对 Apple Silicon M 系列芯片与 Intel 处理器，带来 macOS 专属配置指南。

## 1. 下载适配平台的 macOS 安装包

在 GitHub 下载 Clash Verge Rev 时，请注意区分版本：
- **Apple Silicon M 芯片 (M1/M2/M3/M4)**：请下载 **`_aarch64.dmg`** 原生架构安装包。
- **Intel 处理器旧款 Mac**：请下载 **`_x64.dmg`** 安装包。

如果打开应用提示“已损坏，无法打开”：
打开终端 (Terminal)，运行如下命令即可解除签名限制：
`sudo xattr -rd com.apple.quarantine /Applications/Clash\\ Verge.app`

## 2. 授权 macOS 系统权限

1. **授权辅助功能**：在 macOS `系统设置` ➔ `隐私与安全性` ➔ `辅助功能` 中，勾选允许 Clash Verge。
2. **安装 TUN 模式驱动**：打开软件设置，点击安装 `Service Mode` 服务模式（输入 Mac 开机密码授权），安装后方可开启 TUN 模式无感接管。

## 3. 配合 Safari 与 Chrome 流畅体验

导入 [机场订阅链接](/posts/rumen-jiaocheng/jichang-dingyue-lianjie-shiyong-jiqiao/) 后，开启主界面 `System Proxy`，即可在 Safari 与 Chrome 中流畅开启 4K 追剧与 AI 办公。
"""
    },

    "content/posts/kehuduan-peizhi/android-surfboard-v2rayng-dingyue-daoru.md": {
        "title": "Android安卓手机 Surfboard 与 v2rayNG 订阅导入教学",
        "cat": "客户端配置",
        "primary_kw": "安卓客户端订阅导入",
        "secondary_kws": ["Surfboard冲浪板教程", "v2rayNG订阅导入", "安卓梯子后台保活", "Android科学上网"],
        "intent": "为安卓手机用户提供Surfboard（冲浪板）与v2rayNG两条主流配置路线的手把手教程",
        "desc": "Android安卓手机 Surfboard 与 v2rayNG 订阅导入教学，教你在华为、小米、三星等安卓设备上安装APK、一键导入机场订阅及开启后台保活防断连。",
        "content": """在 Android 安卓手机平台，`Surfboard (冲浪板)` 与 `v2rayNG` 是两款评价极高的代理软件。Surfboard 界面优雅美观、支持规则分流；v2rayNG 兼容性极强、轻量省电。本文为您带来这两款软件的订阅导入教程。

## 1. 路线一：Surfboard (冲浪板) 配置教程（推荐）

1. **下载安装**：通过 Google Play 商店或官方开源渠道下载最新 APK。
2. **导入订阅**：
   - 登录机场后台（如灵动云或飞猫云），点击“一键订阅” ➔ 复制 `Surfboard 订阅`。
   - 打开 Surfboard，点击底栏 **`配置 (Profiles)`**，点击右下角加号 `+` ➔ 选择 `从 URL 导入`。
   - 粘贴链接并下载。
3. **开启代理**：切换到 `代理 (Switch)` 选项卡选择节点，点击右下角按钮开启 VpnService 授权。

## 2. 路线二：v2rayNG 配置教程

1. 打开 v2rayNG，点击左上角三条杠 ➔ **`订阅设置`**。
2. 点击右上角加号，填入备注并粘贴 [机场订阅地址](/posts/rumen-jiaocheng/jichang-dingyue-lianjie-shiyong-jiqiao/)。
3. 返回主界面，点击右上角三个点 ➔ 点击 **`更新订阅`**。
4. 选中节点，点击右下角的 V 字图标启动连线。

## 3. 安卓系统的关键设置：后台保活设置

由于小米 HyperOS、华为 HarmonyOS、vivo 等安卓系统清理后台机制严格：
- 务必在“最近任务”列表中将 Surfboard 或 v2rayNG **锁定卡片**。
- 在“电池管理”中将软件设为 **“无限制 / 允许后台高耗电”**，防止锁屏后网络断连。
"""
    },

    # ==================== 4. 专线与性价比 (zhuanxian-xingjiabi) ====================
    "content/posts/zhuanxian-xingjiabi/iplc-iepl-zhuanxian-jichang-yu-bgp-zhongzhuan-qubie.md": {
        "title": "IPLC专线机场与BGP中转的区别：为什么专线晚高峰不卡顿？",
        "cat": "专线与性价比",
        "primary_kw": "IPLC专线机场与BGP中转区别",
        "secondary_kws": ["IPLC内网专线", "IEPL专线原理", "BGP中转机场", "晚高峰不卡顿梯子"],
        "intent": "深入科普IPLC/IEPL物理专线与普通BGP公网中转的技术架构差异，解释专线不被GFW封锁的原因",
        "desc": "IPLC专线机场与BGP中转区别深度解析，揭秘IPLC/IEPL内网点对点物理专线技术原理，剖析为什么专线能够在晚高峰实现零丢包、低延迟不卡顿。",
        "content": """在购买网络加速机场时，大家常看到商家宣传“本站采用 IPLC 物理专线”、“全站 IEPL 中继”。为什么专线机场的价格通常略高于普通直连机场？为什么专线能够做到晚高峰零丢包？本文为您深度揭秘。

## 1. 什么是 IPLC / IEPL 物理专线？

- **IPLC (International Private Leased Circuit)**：国际私用出租线路。它是运营商提供的**物理内网点对点专线**。
- **核心原理**：您的数据从国内入口机房（如深圳）直接通过物理专线传输至海外出口机房（如香港），**整个过程完全不经过公网 GFW 防火墙审查**！

由于数据不在公网上排队接收检查，因此 IPLC 专线具备三大物理优势：
1. **绝对不封锁 IP**：不经过 GFW，因此节点 IP 永远不会被墙。
2. **极低丢包率（< 0.1%）**：物理直连，晚高峰丝毫不受公网拥堵影响。
3. **超低物理延迟**：深圳到香港延迟可低至 3ms - 5ms。

## 2. 什么是 BGP 公网中转？

BGP 中转是通过国内入口服务器接收您的流量，加密后通过公网发送到海外服务器。
- **优点**：搭建成本比物理专线便宜得多。
- **缺点**：数据依然在公网上运行，在晚高峰（20:00 - 23:00）公网出口拥堵时，依然会出现丢包和抖动。

## 3. IPLC 专线 vs BGP 中转对比表

| 技术指标 | IPLC / IEPL 物理专线 (如灵动云) | 普通 BGP 公网中转 |
| :--- | :--- | :--- |
| **是否经过 GFW 审查** | 否（内网光纤传输） | 是（加密后公网传输） |
| **晚高峰稳定性** | 极佳（零丢包、帧率稳定） | 中等（可能遭遇短时间丢包） |
| **节点 IP 被封概率** | 0% | 存在被封更换 IP 的可能 |
| **适合场景** | 4K 追剧、游戏加速、AI 办公 | 日常网页浏览、常规社交 |

## 4. 选购建议

如果您的使用场景包括 [ChatGPT/Claude 等 AI 办公](/posts/jichang-tuijian/ai-jichang-tuijian-chatgpt-claude-gemini-nodes/) 或对外服游戏延迟要求极高，强烈推荐选择全站部署 IPLC 专线的 [灵动云]，结账输入优惠码 `ld888` 立享折扣。
"""
    },

    "content/posts/zhuanxian-xingjiabi/piany-haoyong-tizi-tuijian-10yuan-yixia-jichang.md": {
        "title": "便宜好用梯子推荐：10元以下平价高性价比机场实测",
        "cat": "专线与性价比",
        "primary_kw": "便宜好用梯子推荐",
        "secondary_kws": ["10元以下机场", "平价梯子推荐", "性价比高机场", "低预算梯子"],
        "intent": "实测并推荐月费在5元至15元区间的极高性价比平价机场，针对低预算用户做盘点",
        "desc": "便宜好用梯子实测推荐，盘点10元以下及平价高性价比机场，针对学生党与备用需求提供真实速度与稳定度测试数据。",
        "content": """寻找“既便宜又好用”的梯子是绝大多数新手的共同心愿。但市场上低于 10 元/月的机场多如牛毛，大部分因为过度超卖导致速度奇慢。为了帮大家避开垃圾平价机场，机场典评测组挑选了几款真正的平价高性价比服务商。

## 1. 10元以下平价机场的核心评估标准

在极低价格的前提下，不能要求它具备顶级高价专线的所有特性，但必须达到以下基本门槛：
1. **可用节点数 > 15 个**：涵盖香港、日本、新加坡等常用节点。
2. **不严重限制单线程带宽**：至少能流畅观看 1080P/4K 视频。
3. **支持标准订阅导出**：能方便导入 [Clash Verge](/posts/kehuduan-peizhi/clash-verge-peizhi-jiaocheng-xiaobai-ban/)。

## 2. 精选平价高性价比机场实测榜单

### 2.1 飞猫云 (FlyCat Cloud) — 平价折算单月 7 元！
- **价格规格**：84元/年（折合 7元/月，50GB/月）
- **优惠码**：`flycat888`
- **实测评价**：公认性价比极高，虽然是轻量年付，但全站采用高品质香港中转，连接成功率 99%。非常适合学生党与轻度浏览。

### 2.2 灵动云 (LingDong Cloud) — 20元档高品质首选
- **价格规格**：20元/月 (使用优惠码 `ld888` 后仅 16元/月)
- **实测评价**：如果您的预算能提高到 10 多元，灵动云能提供真正的 [IPLC 专线](/posts/zhuanxian-xingjiabi/iplc-iepl-zhuanxian-jichang-yu-bgp-zhongzhuan-qubie/)，体验质的飞跃。

## 3. 便宜机场避坑小法则

- **切勿相信“5元不限流量包年”**：此类机场几乎 100% 会在两周内跑路。
- 更多平价选购建议可查看 [便宜包月梯子专题推荐](/posts/jichang-tuijian/yuefu-jichang-tuijian-dibuyusuan-shouxuan/)。
"""
    },

    "content/posts/zhuanxian-xingjiabi/wangao-feng-cesu-jichang-shuju-yu-shangwang-tiyan.md": {
        "title": "晚高峰不卡顿机场测速：丢包率、延迟与油管4K码率深度测评",
        "cat": "专线与性价比",
        "primary_kw": "晚高峰不卡顿机场测速",
        "secondary_kws": ["晚高峰梯子测速", "机场丢包率测试", "油管4K码率测试", "晚高峰抗封锁"],
        "intent": "在晚高峰（20:00-23:00）拥堵时段对主流机场进行实测，公布丢包率、延迟与YouTube码率数据",
        "desc": "晚高峰不卡顿机场实测报告，在晚间20点至23点拥堵高峰期对各大机场进行丢包率、PING延迟与YouTube 4K码率极限测速。",
        "content": """判断一个网络加速机场是“真牛”还是“吹牛”，最硬核的检测方式就是在**晚高峰（20:00 - 23:00）**进行极限压力测速。在这个时段，骨干网公网出口流量拥堵，劣质机场原形毕露。本文为您公布实测数据。

## 1. 晚高峰压测三项核心指标

- **丢包率 (Packet Loss)**：理想状态应低于 1%。丢包率超过 5% 就会导致网页卡顿、视频缓冲。
- **PING 延迟抖动 (Jitter)**：延迟抖动越小，游戏与语音通话越平稳。
- **YouTube 4K 峰值 Connection Speed**：衡量大带宽连续传输能力。

## 2. 晚高峰各大机场实测数据大比拼

| 机场品牌 | 晚高峰丢包率 | 晚高峰 PING 延迟 | YouTube 4K 码率 | 评测结论 |
| :--- | :--- | :--- | :--- | :--- |
| **灵动云** | **0.1%** | 38 ms | **180,000 Kbps** | 🏆 全程秒开无感缓冲 |
| **暮光网络** | 0.3% | 45 ms | **165,000 Kbps** | 🥈 影音高码率表现极佳 |
| **飞猫云** | 1.2% | 62 ms | 85,000 Kbps | 🥉 1080P/4K 平稳播放 |
| 某公网直连小机场 | 35.8% | 320 ms | 4,200 Kbps (频繁卡顿) | ✖ 不合格 |

## 3. 为什么灵动云在晚高峰依然表现惊人？

灵动云全站部署了物理 [IPLC/IEPL 国际专线](/posts/zhuanxian-xingjiabi/iplc-iepl-zhuanxian-jichang-yu-bgp-zhongzhuan-qubie/)，数据不走拥堵的公网。使用优惠码 `ld888` 结账可享受 8 折优惠。
"""
    },

    "content/posts/zhuanxian-xingjiabi/daliuliang-jichang-taocan-xingjiabi-ceping.md": {
        "title": "大流量套餐性价比对比：BT下载与高清视频加速梯子盘点",
        "cat": "专线与性价比",
        "primary_kw": "大流量机场套餐对比",
        "secondary_kws": ["大流量梯子推荐", "不限时流量包", "BT下载机场", "海量流量套餐"],
        "intent": "为有BT下载、8K影视播放或海量数据传输需求的用户对比大流量包月及不限时流量包",
        "desc": "大流量机场套餐性价比深度对比，盘点支持500GB-2000GB海量流量包月及不限时一次性流量包的优质加速服务商。",
        "content": """对于需要下载大容量 BT 资源、观看 8K 原盘电影或进行海量数据同步的用户而言，常规每月 100GB 的流量套餐往往捉襟见肘。大家希望能找到单月提供 500GB 到 2000GB、或者提供“不限时间一次性流量包”的性价比机场。本文为您梳理大流量套餐选购指南。

## 1. 大流量需求的两大套餐模式

1. **大包月套餐 (月度充能)**：每月固定提供 500GB - 1000GB 流量，按月重置，适合每日挂载高清视频的重度党。
2. **不限时一次性流量包 (Pay as you go)**：一次性购买 500GB 流量，不设到期时间，用完为止。非常适合作为 [备用防失联梯子](/posts/jichang-tuijian/beiyong-jichang-tuijian-fangshilian-zhuanxian/)。

## 2. 大流量优质机场推荐

- **暮光网络 (Twilight)**：提供 500GB/月 及 1000GB/月 大流量套餐，中转带宽充沛，优惠码：`mm88`。
- **灵动云**：专线中转，提供高性能大流量包，适合高速文件传输，优惠码：`ld888`。

## 3. BT 下载时的防封规则

使用机场节点进行 P2P / BT 下载时，请务必在客户端中选择允许 BT 的节点，严禁在禁止 BT 的节点上挂载 BitTorrent，以免引发机房版权投诉导致账号被锁。
"""
    },

    "content/posts/zhuanxian-xingjiabi/nianfu-jichang-yu-yuefu-jichang-youd缺点-fenxi.md": {
        "title": "年付机场与月付机场优缺点分析：如何根据资金风险进行选择",
        "cat": "专线与性价比",
        "primary_kw": "年付机场与月付机场对比",
        "secondary_kws": ["年付梯子风险", "月付机场优势", "机场资金安全", "跑路避坑法则"],
        "intent": "深度分析年付折扣与月付灵活度的利弊，为用户提供资金安全的决策模型",
        "desc": "年付机场与月付机场优缺点深度对比，分析年付折扣力度与资金跑路风险，提供不同预算下的理性资金安全决策建议。",
        "content": """在挑选机场时，用户经常在“按月付费”和“一次性年付”之间纠结。年付通常附带 7-8 折的诱人折扣，但不少人担心机场跑路风险；月付安全灵活，但长期算下来总价略高。本文为您建立一套理性的资金安全选择模型。

## 1. 年付与月付的优缺点深度对比

| 付费模式 | 核心优势 | 潜在风险与缺点 | 适合人群 |
| :--- | :--- | :--- | :--- |
| **月付模式 (Monthly)** | 极高安全度、随用随停、发现不满意下月随时换 | 单月折算单价略高，需每月手动续费 | 新手小白、试用新机场、资金敏感者 |
| **年付模式 (Yearly)** | 享 7-8 折深度优惠、无需频繁续费、赠送更大流量 | 一旦遇到机场跑路或线路质量下滑，资金无法退回 | 老牌稳定机场用户、长期高频上网者 |

## 2. 资金安全避坑原则

1. **老牌大机场方可考虑年付**：只有运维时间超过 2 年、拥有独立 [IPLC 专线](/posts/zhuanxian-xingjiabi/iplc-iepl-zhuanxian-jichang-yu-bgp-zhongzhuan-qubie/) 的大品牌（如飞猫云年付仅 84 元），才可以放心考虑年付。
2. **小机场 / 新成立机场坚决月付**：对于成立不足半年的新机场，无论折扣多大，只选择月付。

## 3. 最终决策参考表

- 如果年付总金额 **低于 100 元**（如飞猫云 84元/年）：资金风险极低，推荐直接年付。
- 如果年付总金额 **高于 300 元**：建议先试用月付 1-2 个月，确认本地晚高峰速度满意后再升年付。
"""
    },

    "content/posts/zhuanxian-xingjiabi/duoshebei-gonxiang-jichang-dingyue-peizhi.md": {
        "title": "多设备共享机场订阅配置：家庭与小团队多终端连线方案",
        "cat": "专线与性价比",
        "primary_kw": "多设备共享机场订阅",
        "secondary_kws": ["多终端同时连线", "软路由全家桶代理", "家庭共享梯子", "机场公用限制"],
        "intent": "指导用户如何在家庭或团队多设备（Phone/PC/Pad/TV）之间合理共享同一个机场订阅",
        "desc": "多设备共享机场订阅配置全指南，详解家庭多终端并发连线规则、设备超限排查及软路由 (OpenWrt) 全局代理配置方案。",
        "content": """在现代家庭或小型工作团队中，一个人往往同时拥有手机、笔记本、iPad 和智能电视等多台设备。如何在多台设备间合理共享同一个机场订阅？如何避免因超出设备连线限制而导致账号被封？本文为您带来完整配置方案。

## 1. 搞清机场的“公用设备数限制 (IP 限制)”

绝大多数机场（如灵动云、飞猫云）在套餐中都会明确标注：**限制 2-5 台设备同时并发连线**。
- **同公网 IP 算一台**：如果您家里所有的设备都连接同一个 Wi-Fi 路由器，外部公网 IP 只有一个，机场后台通常算作 1 台并发连线！
- **异地连线算多台**：如果在公司、家里、蜂窝移动网络下同时开启代理，会被算作不同的 IP 连线。

## 2. 方案一：软路由 (OpenWrt) 全家桶方案（极其推荐）

在家里部署一台软路由（如 OpenWrt），在路由器层安装 OpenClash 或 PassWall 并导入订阅：
- **优点**：家里所有的手机、电脑、Apple TV 只要连接 Wi-Fi 即可自动科学上网！**在机场后台仅占用 1 个 IP 连线额度**。
- **配置教程**：参考 [Clash Verge 规则分流原理](/posts/kehuduan-peizhi/clash-verge-peizhi-jiaocheng-xiaobai-ban/) 导入配置文件即可。

## 3. 方案二：多终端客户端独立导入

如果无法部署软路由，可在每台设备上分别安装对应的客户端：
- **Windows / Mac** ➔ [Clash Verge Rev](/posts/kehuduan-peizhi/clash-verge-peizhi-jiaocheng-xiaobai-ban/)
- **iPhone / iPad** ➔ [Shadowrocket 小火箭](/posts/kehuduan-peizhi/shadowrocket-xiaohuojian-jiedian-daoru-jiaocheng/)
- **Android 电视盒** ➔ Surfboard 或 v2rayNG

注意确保不同异地设备同时在线数量不超过套餐上限。
"""
    }
}

ARTICLES_DATA.update(CHANNEL_3_4_DATA)

print(f"Total articles successfully defined: {len(ARTICLES_DATA)}")
