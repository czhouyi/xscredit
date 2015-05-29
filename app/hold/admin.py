from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from app.hold.models import Stock, Fund, Hold

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
	list_display = ("code", "name",)
	search_fields = ("code", "name",)
	class Media:
		pass

@admin.register(Fund)
class FundAdmin(admin.ModelAdmin):
	list_display = ("code", "name", "rate", "amount",)
	search_fields = ("code", "name",)
	class Media:
		pass

@admin.register(Hold)
class HoldAdmin(admin.ModelAdmin):
	list_display = ("stock", "scode", "fund", "fcode", "rate",)
	search_fields = ("stock__code", "stock__name", "fund__name", "fund__code",)
	class Media:
		pass

