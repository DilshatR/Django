from django.contrib import admin
from fdc_corp.models import Languages, Pages, News, MainMenu, FooterMenu, Slider


class Filter(admin.ModelAdmin):
    list_display = ["id","title","lang_id","active"]
    list_filter = ["lang_id","active"]
class PageFilter(admin.ModelAdmin):
    list_display = ["id","page_name","active"]
    list_filter = ["lang_id","active"]

admin.site.register(Languages)
admin.site.register(Pages, PageFilter)
admin.site.register(News, Filter)
admin.site.register(MainMenu, Filter)
admin.site.register(FooterMenu, Filter)
admin.site.register(Slider, Filter)
