"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from search.views import search
from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()
from wolf.models import Entry,Link,Category
from django.views.generic.dates import ArchiveIndexView
from django.views.generic.dates import YearArchiveView
from django.views.generic.dates import MonthArchiveView
from django.views.generic.dates import DayArchiveView
from django.views.generic.dates import DateDetailView
from tagging.models import Tag
from django.views.generic.list import ListView
from wolf.views import category_detail

entry_info_dict = {
'queryset': Entry.objects.all(),
'date_field': 'pub_date',
}
link_info_dict = {
'queryset': Link.objects.all(),
'date_field': 'pub_date',
}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^search/$', search),
    url(r'^weblog/$', ArchiveIndexView.as_view(model=Entry, date_field="pub_date")),
    url(r'^weblog/(?P<year>\d{4})/$', YearArchiveView.as_view(model=Entry,date_field="pub_date")),
    url(r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/$',MonthArchiveView.as_view(model=Entry,date_field="pub_date")),
    url(r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',DayArchiveView.as_view(model=Entry,date_field="pub_date")),
    url(r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',DateDetailView.as_view(model=Entry,date_field="pub_date")),

    url(r'^weblog/$', ArchiveIndexView.as_view(model=Link, date_field="pub_date")),
    url(r'^weblog/(?P<year>\d{4})/$', YearArchiveView.as_view(model=Link,date_field="pub_date")),
    url(r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/$',MonthArchiveView.as_view(model=Link,date_field="pub_date")),
    url(r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',DayArchiveView.as_view(model=Link,date_field="pub_date")),
    url(r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',DateDetailView.as_view(model=Link,date_field="pub_date")),
    url(r'', include('django.contrib.flatpages.urls')),

    url(r'^categories/$',ListView.as_view(queryset=Category.objects.all())),
    url(r'^categories/(?P<slug>[-\w]+)/$',category_detail),
    url(r'^tags/$',ListView.as_view(queryset=Tag.objects.all())),
]
