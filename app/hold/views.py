from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.core.urlresolvers import reverse
from app.hold.models import Stock, Fund, Hold
from app.hold.fundholds import crawle_hold


def index(request):
    ctx = dict(user=request.user, funds=Fund.objects.all(), stocker=stocker())
    return render(request, 'hold/index.html', ctx)


def detail(request, fund_id):
	funds = Fund.objects.all()
	fund = Fund.objects.get(pk=fund_id)
	holds = Hold.objects.filter(fund__id=fund_id)
	ctx = dict(user=request.user, funds=funds, fund=fund, holds=holds)
	return render(request, 'hold/detail.html', ctx)


def get_hold(request, fund_id):
	fund = Fund.objects.get(pk=fund_id)
	hls = crawle_hold(fund.code)
	holds = Hold.objects.filter(fund__id=fund_id)
	holds.delete()
	for hl in hls:
		hold = Hold()
		hold.fund = fund
		hold.stock = Stock.objects.get(code=hl[0])
		hold.rate = hl[1]
		hold.save()
	return redirect(reverse('detail', args=[fund_id]))


def stocker():
	holds = Hold.objects.all()
	rl = {}
	for hold in holds:
		k = (hold.stock.name, hold.stock.code)
		v = round(float(hold.fund.amount*hold.rate)/100.0, 2)
		if rl.get(k):
			rl[k] = round(rl[k] + v, 2)
		else:
			rl[k] = v
	l = sorted(rl.items(), key = lambda rl : rl[1], reverse=True)
	return map(lambda x : [x[0][0], x[0][1], x[1]], l)
