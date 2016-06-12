from django.contrib import admin
from search.models import SearchKeyword
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
# Register your models here.
class SearchKeywordInline(admin.StackedInline):
    model = SearchKeyword
class FlatPageAdminWithKeywords(FlatPageAdmin):
    inlines = [SearchKeywordInline]
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdminWithKeywords)