老赵的Python代码碎片
===================

以下代码是老赵日常学习Python时所写，在Python2.7.12下测试通过。在Python3环境可能需要稍作修改才能运行，另外还有一点不足之处——这些代码没有任何逻辑顺序可言！

代码可能使用到的第三方的库：[PIL](http://pythonware.com/products/pil/), [pygame](http://www.pygame.org/), [numpy](http://www.numpy.org/), [QRcode](https://pypi.python.org/pypi/qrcode), [pyzbar](https://pypi.python.org/pypi/pyzbar), [requests](http://cn.python-requests.org/zh_CN/latest/), [bs4](https://www.crummy.com/software/BeautifulSoup/)。

    送给正在努力学习Python的同学们！

源码目录 CODE LIST
-----------------

- [pycode0x0000.py : Hello, Python!](src/pycode0x0000.py)
- [pycode0x0001.py : 数字1、2、3、4能组成多少个无重复数字的三位数？](src/pycode0x0001.py)
- [pycode0x0002.py : 斐波拉契数列生成器](src/pycode0x0002.py)
- [pycode0x0003.py : 用字符c画边长为n的正方形和菱形](src/pycode0x0003.py)
- [pycode0x0004.py : 三个玩家玩斗地主，洗牌、发牌、理牌、留3张底牌 ...](src/pycode0x0004.py)
- [pycode0x0005.py : 求小于1000的整数中3或5的整倍数的和](src/pycode0x0005.py)
- [pycode0x0006.py : 求前一百个自然数的“和的平方”与它们的“平方的和”的“差”](src/pycode0x0006.py)
- [pycode0x0007.py : 把2的1000次方的数值各位上的数字加在一起是多少？](src/pycode0x0007.py)
- [pycode0x0008.py : 小学时代无聊时玩过的一个游戏(random.choice)](src/pycode0x0008.py)
- [pycode0x0009.py : 已知10个半径，求圆面积的和，要求保留3位小数(派和四舍五入)](src/pycode0x0009.py)
- [pycode0x000A.py : 求出两个三位数的乘积中最大的回文数(分片、max、生成器推导式)](src/pycode0x000A.py)
- [pycode0x000B.py : 公元年份的干支纪年](src/pycode0x000B.py)
- [pycode0x000C.py : 求24点算式](src/pycode0x000C.py)
- [pycode0x000D.py : 求Python之禅中字符的出现频率(百分率，不区分大小写字母)](src/pycode0x000D.py)
- [pycode0x000E.py : 谁是罪犯？](src/pycode0x000E.py)
- [pycode0x000F.py : Pygame摄像头捕获演示程序](src/pycode0x000F.py)
- [pycode0x0010.py : 打印输出Pygame事件对象的信息](src/pycode0x0010.py)
- [pycode0x0011.py : 和电脑玩Blackjack](src/pycode0x0011.py)
- [pycode0x0012.py : 自定义my_sorted函数排序一个列表](src/pycode0x0012.py)
- [pycode0x0013.py : 将base64字符串转为文件对象](src/pycode0x0013.py)
- [pycode0x0014.py : 皇后问题 N-queens puzzle solver](src/pycode0x0014.py)
- [pycode0x0015.py : 将整数转成英语形式](src/pycode0x0015.py)
- [pycode0x0016.py : 一个WSGI接口WEB服务器](src/pycode0x0016.py)
- [pycode0x0017.py : 和电脑玩石头剪刀布](src/pycode0x0017.py)
- [pycode0x0018.py : 用乌龟(Turtle)画方块套方块、圈圈套圈圈](src/pycode0x0018.py)
- [pycode0x0019.py : 读心术（人类版）](src/pycode0x0019.py)
- [pycode0x001A.py : 读心术（电脑版）](src/pycode0x001A.py)
- [pycode0x001B-server.py : socket通讯小例子（服务器端）](src/pycode0x001B-server.py)
- [pycode0x001B-clien.py : socket通讯小例子（客户端）](src/pycode0x001B-clien.py)
- [pycode0x001C.py : Pygame方向键控制运动方向演示程序](src/pycode0x001C.py)
- [pycode0x001D.py : 打印字符串在内存里的二进制形式](src/pycode0x001D.py)
- [pycode0x001E.py : numpy.array demo](src/pycode0x001E.py)
- [pycode0x001F.py : 用matplotlib画正弦余弦曲线](src/pycode0x001F.py)
- [pycode0x0020.py : 用matplotlib画动态随机折线](src/pycode0x0020.py)
- [pycode0x0021.py : 用matplotlib画动态正弦曲线](src/pycode0x0021.py)
- [pycode0x0022.py : 用matplotlib画动态水面雨滴效果](src/pycode0x0022.py)
- [pycode0x0023.py : 命令行二维码图片生成程序](src/pycode0x0023.py)
- [pycode0x0024.py : 命令行读取图片中二维码程序](src/pycode0x0024.py)
- [pycode0x0025.py : 生成Github随机用户头像](src/pycode0x0025.py)
- [pycode0x0026.py : 用matplotlib画双曲面](src/pycode0x0026.py)
- [pycode0x0027.py : 从zlib压缩的二进制文件中读取100万以内的质数数据](src/pycode0x0027.py)
- [pycode0x0028.py : 模拟打字机输出字符串](src/pycode0x0028.py)
- [pycode0x0029.py : 下载某网站整站视频的脚本](src/pycode0x0029.py)
- [pycode0x002A.py : 两个简单的质数生成器](src/pycode0x002A.py)
- [pycode0x002B.py : 用pygame和HTTPServer将摄像头图像串流到http页面上](src/pycode0x002B.py)

联系老赵 CONTACT
---------------

- QQ群： 200929675
- 官方网站： [http://pythonchallenge.club](http://pythonchallenge.club)
- 个人网站： [http://nixoahz.com](http://nixoahz.com)
- 优酷频道： [http://i.youku.com/imzhao](http://i.youku.com/imzhao)
- 老赵QQ: 7176466
- 老赵邮箱： [pythonchallenge@qq.com](mailto:pythonchallenge@qq.com)
- 新浪微博： [@老赵爱编程](http://www.weibo.com/archtaurus)