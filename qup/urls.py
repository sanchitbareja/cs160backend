from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Django admin site
from django.contrib import admin
admin.autodiscover()

# API
from tastypie.api import Api
from api.api import UserResource, BusinessResource, CouponResource, QueueResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(BusinessResource())
v1_api.register(CouponResource())
v1_api.register(QueueResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # v1 API
    url(r'^api/', include(v1_api.urls)),
)  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

