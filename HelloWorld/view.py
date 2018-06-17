# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import re
import urllib.request


def hello(request):
    res = {}
    res['hello'] = '你好'
    return render(request, 'hello.html', res)


def hellow(request):
    url = 'https://www.52pojie.cn/forum-24-1.html'

    page = urllib.request.urlopen(url).read()
    page = page.decode('gbk')

    #<a href="thread-752240-1-1.html" onclick="atarget(this)" class="s xst">【分享】WOR片带PSD带教程</a>
    zz = r'<a href="(thread-.+?)".+? class="s xst">(.+?)</a>'
    html = re.findall(zz, page, re.S)
    print(html)
    i = 0
    for line in html:
        line = html[i]
        print(line)
        url = 'https://www.52pojie.cn/' + line[0]
        title = line[1]
        res = res + title + " " + url + "\r\n"
        print(title + " " + url)
        i = i + 1

    return HttpResponse(html)