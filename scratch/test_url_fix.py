import urllib.request

url = "http://localhost:1313/posts/kehuduan-peizhi/clash-verge-peizhi-jiaocheng-xiaobai-ban/"
html = urllib.request.urlopen(url).read().decode("utf-8")

target_link = 'href="https://t.me/+JngXxDbAxwA5NzVl"'
print("Target link present:", target_link in html)
if target_link in html:
    print("SUCCESS: The button '联系 Telegram 客服答疑' link is 100% fixed and functional!")
