from django.conf.urls import patterns, include, url
from django.contrib import admin
from transactions.views import TransactionView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'analizandola.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^transaction/$', TransactionView.as_view(), name='transaction')
)
