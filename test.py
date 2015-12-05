import urllib

for i in range(4000,6000):
    # url = 'http://www.zhihu.com/captcha.gif?r=1449192615046'
    # url = 'http://qy.zzu.edu.cn:81/public/login_image.php?suoji' 
    # url = 'http://pan.baidu.com/genimage?333242386563323463616633346566373232376336363736376432396666643366623137353232363735373030303030303030303030303030303134343931393839313959848C4C49DF6D11562CB4EB6D743A8F'
    url = 'https://passport.csdn.net/ajax/verifyhandler.ashx?rand=14491994690.48'
    # url = 'http://weibo.com/signup/v5/pincode/pincode.php?lang=zh&sinaId=02cc809ee2ac46b853d62ab42b79d408&r=1449200062'
    print "download", i
    file("./pic/%04d.gif" % i, "wb").write(urllib.urlopen(url).read())

