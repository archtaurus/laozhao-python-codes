#!/usr/bin/env python2
# -*- coding:utf-8 -*-
"""老赵的Python代码碎片之一

文件: pycode0x0030.py
功能: 小故事网故事采集程序
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2016.12.09
"""

import os
import sys
import shelve
import urllib
import re
from HTMLParser import HTMLParser
from random import randint

site_url = 'http://www.xigushi.com'
"""网址"""
site_coding = 'gb2312'
"""网站编码"""
index_url_pattern = site_url + '/{}/list_{}_{}.html'
"""索引页面地址模式"""
story_url_pattern = site_url + '{}'
"""故事页面地址模式
http://www.xigushi.com/<类别缩写>/list_<类别编号>_<分页编号>.html"""
stories_per_pege = 20
"""每页故事数量"""
working_path = os.path.abspath(os.path.dirname(__file__))
"""脚本所在路径"""
database_filename = os.path.join(working_path, 'stories.dat')
"""故事数据库文件名"""
story_database = shelve.open(database_filename)
"""故事数据库(shelve文件)
结构：
类别索引：键名：categories
         类型：列表，[abbr1, abbr2, ...]
类别：键名：类别缩写 abbr
      类型：元组，(类别名称(utf-8编码), 类别编号, 已采集数)
条目：键名：类别缩写+顺序号
      类型：元组 (类别名称(utf-8编码), 故事标题(unicode)，故事正文(unicode))"""
story_database['categories'] = story_database.get('categories', [])
"""故事类别索引列表"""

# 正则表达式
count_regex = re.compile(u'页.+?(\d+).+?条')
list_regex = re.compile(
    '<a href="(/\w+/\d+.html)" target=\'_blank\' title=".+?">', re.S | re.I)
pages_regex = re.compile('<a href=\'\d+_(\d+).html\'>\d+</a>', re.S | re.I)
story_regex = re.compile(
    '<div class="by">.+?<h1>(.+?)</h1>.+?</div>(.+?)<div class="page">', re.S | re.I)
"""故事内容正则表达式
original web source sample:
    Sourse sample:
        <div class="by">
            <dl>
                <dt>当前位置...</dt>
                <dd>
                    <h1>令尊</h1>
                    <div class="info">
                        时间:2016-11-21 作者:未知 点击:
                        <script src="...javascript"></script>次</div>
                    <p>　　...轿夫问道：&ldquo;相公，&lsquo;令尊&rsquo;...
                        <br />
                        <br /> 　　轿夫信以为真...&rdquo;...
                        <br />
                        <br /> 　　轿夫真以为他没儿子，很替他难过，...
                    </p>
                    </br>
                    <div class="page">
"""


def add_category(abbr, name, num):
    """添加类别
    Example:
        add_category('thgs', '童话故事', 2)
    """
    if story_database.get(abbr):
        sys.exit('category already exists.')
    else:
        story_database[abbr] = name, num, 0
        _categories = story_database['categories']
        _categories.append(abbr)
        story_database['categories'] = _categories


class _DeHTMLParser(HTMLParser):
    """HTML析构器
    """
    def __init__(self):
        HTMLParser.__init__(self)
        self.__text = []

    def handle_data(self, data):
        text = data.strip()
        if text:
            text = re.sub('\s+', '', text)  # \s == [ \t\r\n\f\v]
            self.__text.append(text)

    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self.__text.append('\n')

    def text(self):
        return ''.join(self.__text).strip()


def html2txt(html_code):
    """将html内容解析为纯文本
    Example:
        html2txt('<p>hello<br/>world</p>') -> 'hello\nworld'
    """
    parser = _DeHTMLParser()
    parser.feed(html_code)
    parser.close()
    return parser.text()


def reget(url, regex, limit=0):
    """读取指定网页依据正则表达式返回搜索结果
    """
    try:
        _page_content = urllib.urlopen(url).read().decode(site_coding, 'ignore')
        """unicode编码的网页内容"""
    except:
        sys.exit(u'网页内容转码失败')
    _result = regex.findall(_page_content)
    if not _result:
        return []
    if limit == 0:
        return _result
    elif limit == 1:
        return _result[0]
    else:
        return _result[:limit]


def fetch_story(url):
    """抓取指定页面的故事内容
    内容由gb2312转码为unicode，html内容解析为纯文本
    Example:
        fetch_story(url) -> title(unicode), story(unicode)
    """
    _title, _story = reget(url, story_regex, 1)
    pages = reget(url, pages_regex)
    if pages:
        for i in range(2, int(pages[-1]) + 1):
            _url = url.replace('.html', '_{}.html'.format(i))
            _t, _s = reget(_url, story_regex, 1)
            _story += _s
    _story = _story.replace('&lsquo;', u'‘').replace('&rsquo;', u'’')
    _story = _story.replace('&ldquo;', u'“').replace('&rdquo;', u'”')
    _story = _story.replace('&mdash;', u'—')
    return _title.strip(), html2txt(_story.strip())


def get_category_info(_abbr):
    """从数据库获取类别信息
    get_category_info(_abbr) -> _abbr, _name, _num, _fetched, _total
    """
    if _abbr in story_database:
        _name, _num, _fetched = story_database[_abbr]
        _url = index_url_pattern.format(_abbr, _num, 1)
        _total = int(reget(_url, count_regex, 1))  # 网站该类故事总数
        return _abbr, _name, _num, _fetched, _total
    else:
        raise KeyError('category "{}" not exists.'.format(_abbr))


def fetch_stories(abbr, limit=0):
    """按类别抓取故事
    Example:
        fetch_stories('thgs')  # 抓取童话故事
    """
    _abbr, _name, _num, _fetched, _total = get_category_info(abbr)
    _limit = min(_fetched + limit, _total) if limit else _total
    while _fetched < _limit:
        _page_num = _fetched // stories_per_pege + 1
        _url = index_url_pattern.format(_abbr, _num, _page_num)
        _story_urls = reget(_url, list_regex, stories_per_pege)
        if _page_num == _limit // stories_per_pege + 1:
            _story_urls = _story_urls[_fetched % stories_per_pege:_limit % stories_per_pege]
        elif _fetched % stories_per_pege:
            _story_urls = _story_urls[_fetched % stories_per_pege:]
        for _url in _story_urls:
            _story_id = '{}-{}'.format(_abbr, _fetched)  # 类别缩写 - 顺序号
            _title, _story = fetch_story(story_url_pattern.format(_url))
            _fetched += 1
            story_database[_story_id] = (_name, _title, _story)
            story_database[_abbr] = [_name, _num, _fetched]
            print u'类别：', _name
            print u'标签：', _story_id
            print u'标题：', _title
            print u'正文：', _story[:15], '...', _story[-15:]
            print '-' * 79
    print '"{}"({})中已经有 {} 个故事了。'.format(_name, _abbr, _fetched)
    if _fetched == _total:
        print '太好了！所有的"{}"都下载好了。'.format(_name)


def tell_a_story(abbr, n=None):
    """从类别中选讲一个故事, n==None时随机选择
    """
    _abbr, _name, _num, _fetched, _total = get_category_info(abbr)
    if not _fetched:
        n = -1
    elif not n:
        n = randint(0, _fetched - 1)
    if not _fetched:
        print ('提示："{}"中还没有下载故事，网站有 {} 个故事可以下载。'.format(_name, _total))
    elif _total > _fetched:
        print '提示："{}"中有 {} 个新故事还没有下载。'.format(_name, _total - _fetched)
    if 0 <= n < _fetched:
        _, _title, _story = story_database[abbr + '-' + str(n)]
        _story = (u'我们来讲一个故事吧，故事的名字叫《{}》。\n{}'.format(_title, _story))
        print _story
    else:
        sys.exit(u'故事序号 {} 不存在，只有 {} 个故事。'.format(n, _fetched))


# 测试代码
if __name__ == '__main__':
    # add_category('thgs', '童话故事', 2)
    # add_category('ymgs', '幽默故事', 3)
    # print story_database['categories']
    # print story_database['thgs']
    # print story_database['ymgs']
    # print html2txt('<div><p>hello, <br/>world!</p></div>')
    # print int(reget('http://www.xigushi.com/thgs/', count_regex, 1))
    # for _url in reget('http://www.xigushi.com/thgs/', list_regex, stories_per_pege):
    #     print story_url_pattern.format(_url)
    # print reget('http://www.xigushi.com/thgs/13609.html', pages_regex)[-1]
    # title, story = reget('http://www.xigushi.com/thgs/13609.html', story_regex, 1)
    # print title
    # print story
    # title, story = fetch_story('http://www.xigushi.com/thgs/13609.html')
    # print title
    # print story
    # print get_category_info('thgs')
    # fetch_stories('thgs', 10)
    # print len(story_database)
    # tell_a_story('thgs', 100)
    for abbr in ['thgs', 'ymgs']:
        fetch_stories(abbr)
    tell_a_story('thgs')
    story_database.close()
