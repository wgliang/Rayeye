import urllib
for i in range(50):
	# 设置验证码抓取地址，这里以知乎为例
    url = 'http://www.zhihu.com/captcha.gif?r=1449192615046'
    print "download", i
    file("./pic/%04d.gif" % i, "wb").write(urllib.urlopen(url).read())