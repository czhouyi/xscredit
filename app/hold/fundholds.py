#encoding=utf8
import urllib.request, re

url = 'http://fund.eastmoney.com/%s.html'
p1 = re.compile(r'<li class="mc"><a href="http://quote.eastmoney.com/(.*?).html">.*?</a>')
p2 = re.compile(r'<li class="cc"><span class="ping">(.*?)%</span>')

def crawle_hold(code):
	html = str(urllib.request.urlopen(url % code).read())
	codes = p1.findall(html)
	rates = p2.findall(html)
	return list(zip(codes, rates))

if __name__=='__main__':
	print(crawle_hold('000697'))
