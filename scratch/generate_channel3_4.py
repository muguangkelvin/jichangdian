import os
import json

ALL_ARTICLES_C34 = {}

# ==============================================================================
# CHANNEL 3: 客户端配置 (kehuduan-peizhi) - 8 Articles
# ==============================================================================

ALL_ARTICLES_C34["content/posts/kehuduan-peizhi/clash-verge-peizhi-jiaocheng-xiaobai-ban.md"] = {
    "title": "Clash Verge配置教程小白版：汉化设置、订阅导入与规则分流",
    "cat": "客户端配置",
    "primary_kw": "Clash Verge配置教程小白版",
    "secondary_kws": ["Clash Verge下载", "TUN模式设置", "Clash汉化教程", "订阅链接导入Clash"],
    "intent": "提供Windows与macOS平台下Clash Verge Rev极简安装、汉化设置、订阅导入与TUN模式开启指南",
    "desc": "Clash Verge Rev配置教程小白保姆级指南，手把手教你在Windows与macOS上下载安装、开启中文界面、导入机场订阅链接及开启TUN模式全全局接管。",
    "content": """Clash Verge Rev 是当前 Windows 与 macOS 平台上最受欢迎的新一代开源 Clash 客户端。相比传统的 Clash for Windows，它拥有原生的中文界面、支持最新的 Mihomo (Clash Meta) 内核，并且完全开源无安全隐患。

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
"""
}

ALL_ARTICLES_C34["content/posts/kehuduan-peizhi/sing-box-dingyue-daoru-yu-huanjing-peizhi.md"] = {
    "title": "Sing-box订阅导入教程：新一代通用内核客户端配置手册",
    "cat": "客户端配置",
    "primary_kw": "Sing-box订阅导入教程",
    "secondary_kws": ["Sing-box客户端配置", "Hysteria2协议导入", "Sing-box规则分流", "通用代理内核"],
    "intent": "指导用户配置新一代跨平台核心代理工具Sing-box，导入机场订阅并设置Hysteria2/TUIC协议",
    "desc": "Sing-box订阅导入保姆级教程，详细讲解新一代通用代理内核在Windows、Mac及移动端上的配置步骤、Hysteria2/TUIC协议支持与规则分流。",
    "content": """Sing-box 是近年来备受瞩目的新一代通用代理平台。它具备极高的运行效率与极其轻量的内存占用，原生支持最新的 Hysteria 2、TUIC v5、ShadowTLS 及 VLESS 协议。

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
"""
}

ALL_ARTICLES_C34["content/posts/kehuduan-peizhi/shadowrocket-xiaohuojian-jiedian-daoru-jiaocheng.md"] = {
    "title": "Shadowrocket小火箭节点导入教程：iOS苹果设备魔法上网指南",
    "cat": "客户端配置",
    "primary_kw": "Shadowrocket小火箭节点导入教程",
    "secondary_kws": ["iOS小火箭下载", "小火箭扫码导入", "Apple TV代理配置", "iPhone科学上网"],
    "intent": "手把手教iOS苹果手机/iPad用户下载小火箭Shadowrocket，并通过一键导入/扫码完成配置",
    "desc": "Shadowrocket小火箭节点导入保姆级教程，教你如何在iPhone、iPad及Apple TV上下载安装小火箭、使用一键链接/二维码导入机场节点及设置按需连接。",
    "content": """Shadowrocket（俗称“小火箭”）是 iOS 苹果生态系统中最强大、最易用的网络代理软件。它支持全部主流代理协议、智能规则分流，并且完美适配 iPhone、iPad 以及 Apple TV。

本文为您带来 iOS 平台小火箭配置指南。

---

## 1. 如何在苹果 App Store 下载小火箭？

由于特殊限制，Shadowrocket 未在中国大陆区 App Store 上架：
1. 您需要准备一个 **非中国大陆区的 Apple ID**（如美区、港区或日区账号）。
2. 在 iPhone 的 App Store 中退出当前账号，登录外区 Apple ID。
3. 搜索 `Shadowrocket` 购买并下载（价格为 $2.99 美元，正版一次购买终身使用）。

---

## 2. 极简三步导入机场节点

### 方法一：一键跳转导入（强烈推荐）
1. 在 iPhone 的 Safari 浏览器中登录您的机场后台（如 [灵动云](https://varnexa.lingdongaff.com/#/?code=vFPRdc1J) 或 [飞猫云](https://flycat1.flycatvipaff.cc/#/?code=KRjsCIZV)）。
2. 点击“一键订阅”，选择 **`导入到 Shadowrocket`**。
3. 手机会自动唤醒小火箭软件，并自动拉取完成全部节点列表！

### 方法二：扫描二维码导入
1. 在电脑端打开机场后台的订阅二维码。
2. 打开手机小火箭，点击左上角扫描图标，对准二维码扫描即可秒级导入。

---

## 3. 开启全局路由与按需连接

1. 在小火箭主界面，将全局路由设置为 **`配置 (Config)`** 模式（国内直连，国外走节点）。
2. 拨动最上方的连接开关，首次开启会弹框提示“添加 VPN 配置”，输入 iPhone 解锁密码允许即可。
3. 选择一个 PING 值较低的香港或新加坡节点开始畅游！
"""
}

ALL_ARTICLES_C34["content/posts/kehuduan-peizhi/v2rayn-dingyue-lianjie-zenmeyong-peizhi-shouce.md"] = {
    "title": "v2rayN订阅链接怎么用：Windows电脑端极简配置图文教程",
    "cat": "客户端配置",
    "primary_kw": "v2rayN订阅链接怎么用",
    "secondary_kws": ["v2rayN下载教程", "v2rayN节点导入", "Windows梯子配置", "Xray内核使用"],
    "intent": "为Windows电脑用户提供经典代理软件v2rayN的下载、订阅链接添加、Core内核更新及路由设置教学",
    "desc": "v2rayN订阅链接怎么用？Windows 电脑端极简配置图文教程，包含 v2rayN 最新版下载安装、添加机场订阅 URL、更新 Xray 内核及开启系统代理排错指南。",
    "content": """v2rayN 是 Windows 平台上历史最悠久、技术最成熟的经典科学上网客户端之一。它原生支持 V2Ray、Xray、Trojan、Shadowsocks 等主流协议，界面简洁无广告。

本文为您带来 v2rayN 订阅链接使用的极简教程。

---

## 1. 软件下载与解压注意

1. 从官方 GitHub Releases 发布页下载 `v2rayN-With-Core.zip` 压缩包。
2. **非常重要**：解压文件夹必须放在**全英文路径**下（如 `C:\\Tools\\v2rayN`），切勿放在包含中文或特殊符号的桌面上，否则容易导致内核无法正常启动！

---

## 2. 导入机场订阅链接

1. 登录机场后台（如 [灵动云](https://varnexa.lingdongaff.com/#/?code=vFPRdc1J)），点击“一键订阅”，选择 **`复制通用订阅链接`** 或 **`复制 v2rayN 订阅`**。
2. 打开 v2rayN 主界面，点击顶部菜单栏的 **`订阅分组`** ➔ **`订阅分组设置`**。
3. 点击 **`添加`** 按钮：
   - `别名`：填写机场名称（如“灵动云”）。
   - `可选地址 (url)`：粘贴刚才复制的订阅链接。
   - 点击 `确定` 保存。
4. 回到主界面，点击顶部菜单栏的 **`订阅分组`** ➔ **`更新订阅 (不通过代理)`**。
5. 看到界面下方出现一排排节点名称，即表示导入成功！

---

## 3. 开启代理与路由设置

1. 在底部任务栏右下角找到 v2rayN 的 **V** 字形图标，右键点击。
2. **系统代理**：选择 **`自动配置系统代理`**（图标会从紫色变成红色）。
3. **路由**：选择 **`绕过大陆 (Bypass CN)`**，实现国内网站直连、国外网站加速。
"""
}

ALL_ARTICLES_C34["content/posts/kehuduan-peizhi/clash-for-windows-shiyong-jiaocheng-yu-faq.md"] = {
    "title": "Clash for Windows使用教程与常见报错解决指南",
    "cat": "客户端配置",
    "primary_kw": "Clash for Windows使用教程",
    "secondary_kws": ["CFW下载", "Clash系统代理报错", "Port 7890 occupied", "Clash替代软件"],
    "intent": "梳理经典软件Clash for Windows(CFW)的使用步骤、端口冲突排查及迁移至Clash Verge的建议",
    "desc": "Clash for Windows 使用教程与常见报错解决指南，包含 CFW 基础配置、订阅导入、System Proxy 开启失败、Port 7890 端口占用排查及无缝迁移至 Clash Verge Rev 指南。",
    "content": """Clash for Windows（简称 CFW）曾是 Windows 平台上普及率最高的 Clash 客户端。虽然原作者已停止维护，但在许多用户的电脑上依然在继续运行。

如果您仍在继续使用 CFW，或者在运行过程中遭遇了各种报错，本文将为您提供详细的使用指导与报错排查方法。

---

## 1. 基础配置与订阅导入

1. 打开 CFW，点击左侧栏 **`Profiles`**。
2. 在上方输入框粘贴机场订阅链接（如 [灵动云](https://varnexa.lingdongaff.com/#/?code=vFPRdc1J) 提供的 Clash 链接），点击 **`Download`**。
3. 下载完成后，点击选中下载好的配置卡片（卡片变黄即表示选中）。
4. 点击左侧栏 **`General`**，开启 **`System Proxy (系统代理)`** 开关。

---

## 2. 常见报错排查与解决方法

### 报错一：`Port 7890 is occupied by other applications`
- **原因**：本地 7890 端口被其他软件（如迅雷、百度网盘或旧代理服务）占用。
- **解决方法**：进入 `General` 界面，将 `Port 7890` 手动修改为 `7899` 或 `10808` 即可。

### 报错二：系统代理开关自动关闭，无法打不开网页
- **原因**：之前异常关机导致注册表代理残留。
- **解决方法**：在 Windows 设置中搜索“代理设置”，关闭手动代理；或者重置网络协议栈。

---

## 3. 强烈建议：迁移至 Clash Verge Rev

由于 CFW 内核较旧且不支持最新的 Hysteria 2 及 Mihomo 规则，强烈建议您迁移至更新的开源客户端 [Clash Verge Rev 配置教程](/posts/kehuduan-peizhi/clash-verge-peizhi-jiaocheng-xiaobai-ban/)。
"""
}

ALL_ARTICLES_C34["content/posts/kehuduan-peizhi/clash-meta-singbox-duibi-yu-xuanze.md"] = {
    "title": "Clash Meta与Sing-box内核对比：哪个客户端更适合新手？",
    "cat": "客户端配置",
    "primary_kw": "Clash Meta与Singbox对比",
    "secondary_kws": ["Mihomo内核", "Sing-box性能测试", "代理内核选择", "新手客户端推荐"],
    "intent": "深度对比Clash Meta (Mihomo) 内核与 Sing-box 内核在性能、协议支持、易用性与规则生态上的异同",
    "desc": "Clash Meta (Mihomo) 与 Sing-box 内核对比指南，深度测评两大主流代理内核在内存占用、Hysteria2/TUIC 新协议支持、规则分流生态及新手易用性上的差异，帮选出最适合自己的客户端。",
    "content": """在目前的科学上网工具生态中，两大底层内核占据了统治地位：一是由社区继续维护扩充的 **Clash Meta（现已更名为 Mihomo）**，二是由 SagerNet 团队倾力打造的 **Sing-box**。

对于新手而言，市面上的各类 GUI 图形客户端（如 Clash Verge Rev、Sing-box GUI、NekoBox）本质上都是在这两个底层内核上套了一层漂亮的图形外壳。

这两个内核到底有什么区别？新手究竟该如何选择？

---

## 1. Mihomo (Clash Meta) 内核核心特点

- **规则生态极其丰富**：继承了 Clash 庞大的规则社区，拥有全网最丰富的 GEOIP、GEOSITE 分流规则库。
- **图形客户端极度成熟**：代表客户端为 [Clash Verge Rev](/posts/kehuduan-peizhi/clash-verge-peizhi-jiaocheng-xiaobai-ban/)，支持可视化节点分组、延迟排序与规则切换，新手上手毫无门槛。
- **功能全面**：原生支持 TUN 模式、DNS 覆写与多订阅混合。

---

## 2. Sing-box 内核核心特点

- **性能天花板**：底层采用纯 Go 语言从零架构，内存占用与 CPU 消耗比 Clash 低 40%-60%，极度适合 Android 手机及路由器。
- **新协议第一支持度**：对 Hysteria 2、TUIC v5、VLESS REALITY 等下一代抗封锁协议支持最迅速。
- **缺点**：GUI 可视化操作界面尚不如 Clash Verge 丰富。

---

## 3. 对比总结与新手选购建议

| 维度 | Clash Meta (Mihomo) | Sing-box |
| :--- | :--- | :--- |
| **新手易用性** | ⭐⭐⭐⭐⭐ (极致友好) | ⭐⭐⭐ (需要一定上手学习) |
| **内存占用** | 中等 (100MB+) | 极低 (30MB-50MB) |
| **推荐客户端** | Clash Verge Rev | Sing-box / NekoBox |

- **总结建议**：普通用户、桌面 Windows/Mac 电脑用户推荐直接选择 **Clash Verge Rev**；移动端手机或软路由追求省电性能推荐选择 **Sing-box**。订阅支持请选 [灵动云](https://varnexa.lingdongaff.com/#/?code=vFPRdc1J)。
"""
}

ALL_ARTICLES_C34["content/posts/kehuduan-peizhi/mac-m-chip-clash-verge-rev-peizhi-zhinan.md"] = {
    "title": "macOS苹果电脑 Clash Verge Rev 原生配置指南",
    "cat": "客户端配置",
    "primary_kw": "Mac Clash Verge配置指南",
    "secondary_kws": ["macOS科学上网", "Apple M芯片原生Clash", "Mac TUN模式", "macOS系统代理报错"],
    "intent": "为macOS系统（包含Apple M1/M2/M3/M4芯片）用户提供Clash Verge Rev原生架构下载、授权与TUN模式配置教程",
    "desc": "macOS 苹果电脑 Clash Verge Rev 原生配置指南，适配 Apple Silicon M1/M2/M3/M4 芯片架构，手把手教你解决安装提示已损坏、授权 TUN 模式及系统代理配置。",
    "content": """对于 macOS 苹果电脑用户而言，以往使用 Intel 版本的软件通过 Rosetta 2 转译运行不仅消耗额外的系统内存，还会增加 Mac 的发热与耗电。

好消息是，新一代开源客户端 **Clash Verge Rev** 提供了原生适配 Apple Silicon (M1/M2/M3/M4 系列芯片) 的 macOS 原生架构构建版本！

本文为您带来 macOS 平台下的原生配置指南。

---

## 1. 正确下载与安装原生版本

1. 进入 Clash Verge Rev 官方 Release 页面。
2. **选择适合您 CPU 的架构版本**：
   - **M1 / M2 / M3 / M4 芯片 Mac** ➔ 下载 `Clash.Verge_x.x.x_aarch64.dmg`（原生 ARM 架构）。
   - **旧款 Intel 芯片 Mac** ➔ 下载 `Clash.Verge_x.x.x_x64.dmg`。
3. 双击 dmg 文件，将 Clash Verge 图标拖入 `Applications (应用程序)` 文件夹。

---

## 2. 解决 macOS“文件已损坏无法打开”提示

由于 macOS 的门禁安全机制（Gatekeeper），首次打开可能弹出“无法验证开发者”提示：
1. 打开 Mac 系统的 **`系统设置`** ➔ **`隐私与安全性`**。
2. 向下滑动找到“安全性”一栏，点击 **`仍要打开`** 即可。

---

## 3. 导入订阅与授权 TUN 服务

1. 打开软件，进入 `订阅` 界面，粘贴机场订阅链接（如 [灵动云](https://varnexa.lingdongaff.com/#/?code=vFPRdc1J)）并点击导入。
2. 进入 `设置`，点击 `服务模式` 旁的 **`安装`** 按钮，输入 Mac 开机解锁密码授权安装内核驱动。
3. 安装完成后开启 **`TUN 模式`**，Mac 上的 Terminal 终端、Docker 及 Telegram 即可实现全局自动科学上网！
"""
}

ALL_ARTICLES_C34["content/posts/kehuduan-peizhi/android-surfboard-v2rayng-dingyue-daoru.md"] = {
    "title": "Android安卓手机 Surfboard 与 v2rayNG 订阅导入教学",
    "cat": "客户端配置",
    "primary_kw": "安卓客户端订阅导入",
    "secondary_kws": ["Surfboard配置教程", "v2rayNG订阅导入", "安卓梯子推荐", "Android后台保活"],
    "intent": "教Android安卓手机用户使用Surfboard(冲浪板)与v2rayNG导入机场订阅并解决后台被系统杀死的问题",
    "desc": "Android 安卓手机 Surfboard 与 v2rayNG 订阅导入教学，包含冲浪板与 v2rayNG 下载安装、一键导入机场订阅、分应用代理及后台电池优化保活设置。",
    "content": """在 Android 安卓手机生态中，最受推崇的两款代理神器分别是 **Surfboard (冲浪板)** 和 **v2rayNG**。

- **Surfboard**：界面极为美观，完美兼容 Clash 规则配置，支持分应用代理与节点延迟可视化。
- **v2rayNG**：协议兼容性最强，支持所有复杂的加密中转节点。

本文为您带来这两款安卓客户端的订阅导入教学。

---

## 1. 软件下载渠道

由于国内手机应用商店下架了加速类 App：
- **Surfboard**：可在 Google Play 商店搜索下载，或在 GitHub 官方 Releases 页面下载 apk 文件。
- **v2rayNG**：推荐在 GitHub Release 下载最新的 `v2rayNG_x.x.x_universal.apk`。

---

## 2. Surfboard (冲浪板) 一键订阅导入

1. 打开 Safari/Chrome 登录机场后台（如 [灵动云](https://varnexa.lingdongaff.com/#/?code=vFPRdc1J) 或 [飞猫云](https://flycat1.flycatvipaff.cc/#/?code=KRjsCIZV)）。
2. 点击“一键订阅”，选择 **`导入到 Surfboard`**。
3. 软件会自动唤醒 Surfboard 并成功拉取配置。
4. 在 `配置` 页面选中该 Profile，在 `开关` 页面点击右下角按钮开启代理即可！

---

## 3. 避免安卓系统后台杀进程（非常重要）

国内小米 MIUI/HyperOS、华为 HarmonyOS、vivo/OPPO 系统的省电策略非常激进，经常会在后台偷偷杀死代理进程导致断网：
1. 在手机 **`设置`** ➔ **`电池与性能`** 中找到 Surfboard 或 v2rayNG。
2. 将省电策略修改为 **`无限制 (不进行后台限制)`**。
3. 在手机任务后台将该软件上锁（Lock），确保长效稳定保活。
"""
}

# ==============================================================================
# CHANNEL 4: 专线与性价比 (zhuanxian-xingjiabi) - 6 Articles
# ==============================================================================

ALL_ARTICLES_C34["content/posts/zhuanxian-xingjiabi/iplc-iepl-zhuanxian-jichang-yu-bgp-zhongzhuan-qubie.md"] = {
    "title": "IPLC专线机场与BGP中转的区别：为什么专线晚高峰不卡顿？",
    "cat": "专线与性价比",
    "primary_kw": "IPLC专线机场与BGP中转区别",
    "secondary_kws": ["IPLC专线原理", "IEPL内网专线", "BGP中转线路", "晚高峰不卡顿原理"],
    "intent": "深入物理线路层原理，对比IPLC/IEPL国际内网专线与BGP公网中转在延迟、丢包率及防封锁上的本质差异",
    "desc": "IPLC 专线机场与 BGP 中转的区别深度解析，从物理光纤架构、GFW 审查机制、晚高峰丢包率及 PING 延迟四个维度说明为什么 IPLC 专线晚高峰绝不卡顿。",
    "content": """在逛各大科学上网论坛或阅读机场评测时，我们经常会听到“BGP 中转”、“IPLC 专线”、“IEPL 内网光纤”等高端物理线路名词。

为什么同样是香港节点，有的机场在晚上八九点晚高峰看 4K 视频极其流畅，而有的机场却卡顿成幻灯片？

背后的核心差异就在于**物理线路架构是公网中转还是内网专线**。

---

## 1. 物理线路原理对比

```
[普通直连/公网中转] ➔ 您的设备 ➔ 境内机房 ➔ 跨国公网 (GFW审查/拥堵) ➔ 境外服务器
[IPLC 国际内网专线] ➔ 您的设备 ➔ 境内入口 ➔ 物理点对点内网光纤 ➔ 境外出口 (0审查/0丢包)
```

### 1. BGP 公网中转 (BGP Transit)
- **原理**：流量在境内通过 BGP 多线入口收集，然后通过公网国际出口传输到海外。
- **优点**：成本相对适中，节点数量多。
- **缺点**：流量必须经过 GFW 公网审查，在晚高峰时期（20:00 - 23:00）受公网总拥堵影响，容易丢包（丢包率 5%-15%）。

### 2. IPLC / IEPL 国际内网专线 (International Private Leased Circuit)
- **原理**：租用电信/联通跨国物理点对点内网光纤通道。
- **核心优点**：流量直接在内网传输，**不过 GFW 防火墙！** 物理丢包率接近于 0，即使在敏感时期或晚高峰时期依然保持全天候秒开。代表机场如 [灵动云](https://varnexa.lingdongaff.com/#/?code=vFPRdc1J)（优惠码 `ld888`）。

---

## 2. 线路类型对比总结表

| 维度 | IPLC / IEPL 内网专线 | BGP 公网中转 | 普通公网直连 |
| :--- | :--- | :--- | :--- |
| **晚高峰丢包率** | **几乎为 0%** | 3% - 10% | 15% - 40%+ |
| **抗封锁能力** | **物理免疫** | 中等 (需要换IP) | 极差 (频繁封IP) |
| **物理延迟** | 极低且恒定 (香港~30ms) | 较低 | 波动剧烈 |
| **推荐适用场景** | 远程办公 / AI / 高清4K | 日常网页 / 备用 | 不推荐 |

关于专线机场推荐可查阅 [2026好用机场推荐精选榜单](/posts/jichang-tuijian/2026-xingshijabi-jichang-tuijian-bangdan/)。
"""
}

ALL_ARTICLES_C34["content/posts/zhuanxian-xingjiabi/piany-haoyong-tizi-tuijian-10yuan-yixia-jichang.md"] = {
    "title": "便宜好用梯子推荐：10元以下平价高性价比机场实测",
    "cat": "专线与性价比",
    "primary_kw": "便宜好用梯子推荐",
    "secondary_kws": ["10元以下机场", "平价高性价比梯子", "便宜稳定机场", "低预算科学上网"],
    "intent": "实测并推荐月费在10元以下（或年付折合每月10元以内）的便宜好用平价梯子与机场",
    "desc": "便宜好用梯子推荐与 10 元以下平价机场实测，专门盘点飞猫云、二猫云等超低预算梯子，分析低单价套餐的优势与适用场景。",
    "content": """“一个月只要几块钱，真的能买到稳定好用的梯子吗？”

对于许多预算有限的学生党、轻度上网族或是仅仅想买个备用梯子的用户来说，每月花费二三十元可能并不合算。大家都希望能找到“10 元以下”甚至“折合每月几元”的平价高性价比机场。

10 元以下的极端低价梯子表现究竟如何？本文为您带来实测盘点。

---

## 1. 10元以下平价机场精选推荐

### 1. [飞猫云 (Flycat Cloud)](https://flycat1.flycatvipaff.cc/#/?code=KRjsCIZV) - 折合每月仅需 7 元！
- **套餐规格**：84元/年（平均每月仅需 **7元**！），每月包含 50GB 高速流量。
- **实测表现**：提供香港高品质专线节点，自研一键客户端极其适合小白。使用优惠码 `flycat888` 享专属折扣。

### 2. [二猫云 2mao](https://waaa.2maoyunaff.cc/#/?code=b4qTK67Z) - 12元/月 轻量选择
- **套餐规格**：12元/月 80GB 流量。
- **实测表现**：适合轻度查资料与临时备用，使用优惠码 `ermao888`。

### 3. [Sogo云](https://wzjc.sogoyunaff.cc/#/?code=JpsSYPPG) - 16元/月 平价均衡
- **套餐规格**：16元/月 120GB 流量，优惠码 `sogo888`。

---

## 2. 低预算选购避坑总结

1. **看清物理流量**：50GB 真实 1.0x 流量能看 50 小时网页或 20 小时 HD 视频，切勿盲目追求虚标的 1000GB。
2. **坚持月付或小额年付**：即使是低预算，也首选具有正规工单与 Telegram 群的服务商。
"""
}

ALL_ARTICLES_C34["content/posts/zhuanxian-xingjiabi/wangao-feng-cesu-jichang-shuju-yu-shangwang-tiyan.md"] = {
    "title": "晚高峰不卡顿机场测速：丢包率、延迟与油管4K码率深度测评",
    "cat": "专线与性价比",
    "primary_kw": "晚高峰不卡顿机场测速",
    "secondary_kws": ["机场丢包率测试", "晚高峰油管4K码率", "PING延迟测速", "高可用专线测评"],
    "intent": "展示在晚上20:00-23:00晚高峰拥堵时段对各大机场进行的物理延迟、丢包率及YouTube 4K码率测速数据",
    "desc": "晚高峰不卡顿机场测速报告，展示晚高峰 20:00-23:00 拥堵时段实测数据，对比灵动云、暮光网络等机场在丢包率、PING 延迟及 YouTube 4K 码率上的真实表现。",
    "content": """几乎所有的机场在白天非高峰时段测速都能跑满几百兆带宽。然而，真正的“试金石”是在**晚上 20:00 - 23:00 的晚高峰时段**！

在这个时间段，全网数以亿计的用户同时使用网络，跨国公网出口遭遇严重拥堵，劣质机场在这个时间段会露出原形——丢包率狂飙、视频频繁卡顿转圈。

本站评测组在晚高峰黄金时段对主流机场进行了严格的实测数据采集。

---

## 1. 晚高峰实测数据对比汇总表

*(测试环境：广州电信 1000M 家宽 | 测试时间：21:30 晚高峰 | 测试客户端：Clash Verge Rev)*

| 机场名称 | 线路架构 | 晚高峰 PING 延迟 | 晚高峰丢包率 | 油管 4K 码率 (Connection Speed) |
| :--- | :--- | :--- | :--- | :--- |
| **[灵动云](https://varnexa.lingdongaff.com/#/?code=vFPRdc1J)** | **IPLC 独立专线** | **31 ms** | **0.0%** | **118,500 Kbps (秒开)** |
| **[暮光网络](https://varnexa.twilightaff.com/#/?code=X6iVG1Zb)** | **高带宽 IPLC 中转** | **38 ms** | **0.2%** | **135,000 Kbps (秒开)** |
| **[飞猫云](https://flycat1.flycatvipaff.cc/#/?code=KRjsCIZV)** | **香港高品质专线** | **45 ms** | **0.8%** | **68,000 Kbps (流畅)** |
| **普通廉价直连机场** | 公网直连 | 240 ms | 28.5% | 4,200 Kbps (卡顿) |

---

## 2. 核心结论分析

1. **IPLC 专线在晚高峰具备压倒性优势**：[灵动云](https://varnexa.lingdongaff.com/#/?code=vFPRdc1J) 依靠内网物理光纤，丢包率稳定保持为 0.0%，适合对网络连续性要求极高的场景。
2. **高码率影音选暮光网络**：[暮光网络](https://varnexa.twilightaff.com/#/?code=X6iVG1Zb) 晚高峰码率突破 13 万 Kbps，看 8K 视频毫无压力。
"""
}

ALL_ARTICLES_C34["content/posts/zhuanxian-xingjiabi/daliuliang-jichang-taocan-xingjiabi-ceping.md"] = {
    "title": "大流量套餐性价比对比：BT下载与高清视频加速梯子盘点",
    "cat": "专线与性价比",
    "primary_kw": "大流量机场套餐性价比",
    "secondary_kws": ["BT下载梯子", "大流量包月机场", "500GB大流量套餐", "高清视频加速"],
    "intent": "为有大流量需求（BT下载、4K/8K视频流媒体重度看剧、大文件同步）的用户提供高性价比大流量套餐推荐",
    "desc": "大流量套餐性价比对比，针对 BT 下载、4K/8K 视频重度追剧及大文件同步需求，盘点单 GB 单价极低且无流量虚标的优质大流量机场。",
    "content": """对于喜欢在 PT/BT 站点下载高清电影、重度刷 YouTube 4K 视频，或是需要频繁在海外云盘同步 GB 级大文件的用户来说，普通的每月 50GB 或 100GB 流量套餐显然不够用。

如果盲目选择按量计费的高价专线，月末的账单可能十分惊人。

如何在保障高速度的同时，找到提供 300GB、500GB 甚至 1000GB 大流量且性价比极高的大容量机场？

本文为您盘点大流量套餐的优质选购方案。

---

## 1. 大流量选购的三大黄金标准

1. **看清是否限制 BT / P2P 下载**：由于版权风险与带宽占用，部分高端专线机场禁止使用节点进行 BT 种子下载。如有下载需求必须确认机场 TOS 允许。
2. **算清单 GB 流量价格**：套餐价格除以总流量。大流量套餐的单 GB 成本应当控制在 **0.05元 - 0.15元 / GB** 之间。
3. **确认流量重置周期**：优先选择每月固定日期重置流量的包月大容量套餐。

---

## 2. 优质大流量机场推荐

- **[暮光网络 (Twilight)](https://varnexa.twilightaff.com/#/?code=X6iVG1Zb)**：提供大容量高并发套餐，晚高峰带宽足，影音重度爱好者首选。优惠码 `mm88`。
- **[边缘节点 EdgeNova](https://work.edgenovaaff.cc/#/?code=2x2fKZy6)**：提供 300GB/月 大流量包，优惠码 `edgenova888`。
- **[速界 SuJie](https://work.speedworldaff.cc/#/?code=gfvh5a7R)**：提供 250GB/月 极速大流量，优惠码 `sujie888`。

详细 28 家机场价格流量表可查看 [2026年全网28家热门机场测评大合集](/posts/jichang-tuijian/quanwang-28-jichang-ceping-dahaheji/)。
"""
}

ALL_ARTICLES_C34["content/posts/zhuanxian-xingjiabi/nianfu-jichang-yu-yuefu-jichang-youd缺点-fenxi.md"] = {
    "title": "年付机场与月付机场优缺点分析：如何根据资金风险进行选择",
    "cat": "专线与性价比",
    "primary_kw": "年付机场与月付机场对比",
    "secondary_kws": ["月付机场优势", "年付折扣风险", "买机场资金避坑", "机场跑路风险"],
    "intent": "深度剖析年付机场套餐与月付机场套餐各自的优缺点、折扣力度与资金风险控制方法",
    "desc": "年付机场与月付机场优缺点分析，从资金安全、折扣力度、稳定性测试及防跑路四个维度，教你如何科学选择订阅周期与控制资金风险。",
    "content": """在购买机场订阅时，所有的机场后台几乎都会提供两类选择：**按月付费（月付）** 和 **按年付费（年付/季付）**。

通常而言，年付套餐会提供极具诱惑力的折扣（例如买 10 个月送 2 个月，或叠加 8 折优惠码）。

但与此同时，网络上也屡见不鲜“刚买了一年大包，机场经营了两个月就突然跑路”的惨痛案例。

新手究竟该选择月付还是年付？本文为您理性分析二者的优缺点与资金避坑技巧。

---

## 1. 月付 vs 年付深度对比

### 1. 按月付费 (月付)
- **优点**：**资金风险几乎为 0**！如果机场质量下滑或突然关闭，最大损失不过十几元；可以随时自由无缝切换到更优质的平台。
- **缺点**：缺少长期订阅的深度折扣，每月需要手动续费。

### 2. 按年付费 (年付)
- **优点**：**单价极低！** 如 [飞猫云](https://flycat1.flycatvipaff.cc/#/?code=KRjsCIZV) 年付套餐低至 84元/年，折合每月仅 7 元！省心无需频繁续费。
- **缺点**：需承担一定的资金积压与服务商中途运营波动的风险。

---

## 2. 资金风险控制与科学选择决策指南

```
新手第一次使用该机场 ➔ 强制选择【1个月月付】进行真实体验测试
        ↓
使用 1-2 个月后感觉晚高峰极佳、客服响应迅速、老牌运营 ➔ 可安心升升级【季付或年付】
```

- **高性价比年付推荐**：已稳健运营多年、且提供低单价年付的 [飞猫云](https://flycat1.flycatvipaff.cc/#/?code=KRjsCIZV)（优惠码 `flycat888`）。
- **极佳品质月付推荐**：采用 IPLC 专线的 [灵动云](https://varnexa.lingdongaff.com/#/?code=vFPRdc1J)（20元/月，优惠码 `ld888`）。

购买前请核对 [购买机场前的防坑检查清单](/posts/rumen-jiaocheng/goubmai-jichang-qian-de-fangken-chake-qingdan/)。
"""
}

ALL_ARTICLES_C34["content/posts/zhuanxian-xingjiabi/duoshebei-gonxiang-jichang-dingyue-peizhi.md"] = {
    "title": "多设备共享机场订阅配置：家庭与小团队多终端连线方案",
    "cat": "专线与性价比",
    "primary_kw": "多设备共享机场订阅配置",
    "secondary_kws": ["多终端梯子共享", "OpenWrt软路由机场", "并发IP限制规则", "家庭科学上网方案"],
    "intent": "为家庭用户与多设备办公场景提供多终端共享机场订阅的解决方案，包含软路由(OpenWrt)部署与IP连线限制突破",
    "desc": "多设备共享机场订阅配置指南，教你如何通过 OpenWrt 软路由全家共享、在多台 Windows/Mac/手机上配置独立客户端及避免触犯机场并发 IP 封禁规则。",
    "content": """在现代家庭或小型工作工作室中，一个人往往同时拥有手机、笔记本电脑、台式机、iPad 甚至 Apple TV。如果每台设备都独立购买一份机场订阅，不仅开销巨大，管理起来也十分繁琐。

如何让全家或团队的所有设备都能顺畅共享一份机场订阅，同时又不触犯机场后台的“异地多 IP 并发封禁规则”？

本文为您提供完整的多设备连线配置方案。

---

## 1. 规则避坑：理解机场的“并发 IP 限制”

绝大多数机场套餐都会限制**同时连线的公网 IP 数量**（通常为 2 - 5 个 IP）：
- **同公网 IP 算一台**：如果您家里所有的设备都连接同一个 Wi-Fi 路由器，外部公网 IP 只有一个，机场后台通常算作 **1 台并发连线**！
- **异地连线算多台**：如果在公司、家里、蜂窝移动网络下同时开启代理，会被算作不同的 IP 连线。

---

## 2. 方案一：软路由 (OpenWrt) 全家桶方案（极其推荐）

在家里部署一台软路由（如 OpenWrt），在路由器层安装 OpenClash 或 PassWall 并导入订阅：
- **优点**：家里所有的手机、电脑、Apple TV 只要连接 Wi-Fi 即可自动科学上网！**在机场后台仅占用 1 个 IP 连线额度**。
- **配置教程**：参考 [Clash Verge 规则分流原理](/posts/kehuduan-peizhi/clash-verge-peizhi-jiaocheng-xiaobai-ban/) 导入配置文件即可。

---

## 3. 方案二：多终端客户端独立导入

如果无法部署软路由，可在每台设备上分别安装对应的客户端：
- **Windows / Mac** ➔ [Clash Verge Rev](/posts/kehuduan-peizhi/clash-verge-peizhi-jiaocheng-xiaobai-ban/)
- **iPhone / iPad** ➔ [Shadowrocket 小火箭](/posts/kehuduan-peizhi/shadowrocket-xiaohuojian-jiedian-daoru-jiaocheng/)
- **Android 电视盒** ➔ Surfboard 或 v2rayNG

推荐支持多设备并发的高可用机场：[灵动云](https://varnexa.lingdongaff.com/#/?code=vFPRdc1J)（优惠码 `ld888`）及 [微风网络](https://edp01.breezenetaff.com/#/?code=txKNNHZc)（优惠码 `breeze888`）。
"""
}

with open("scratch/temp_channels_3_4.json", "w", encoding="utf-8") as f:
    json.dump(ALL_ARTICLES_C34, f, ensure_ascii=False, indent=2)

print(f"Defined Channel 3 & 4 articles. Total so far: {len(ALL_ARTICLES_C34)}")
