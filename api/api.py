# tastypie imports
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.http import HttpForbidden

# misc
from django.db.models import Q
from users.models import User
from business.models import Business
from coupon.models import Coupon
from queue.models import Queue
import datetime

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'users'
        # Add it here.
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()

        allowed_methods = ['get']
        filtering = {
            "first_name": ("exact")
        }
        excludes = ['password','is_active','is_admin','is_superuser']

    def dehydrate(self, bundle):
        """
        Return a list of clubs formatted according to what the developer expects
        """

        return bundle

    def alter_list_data_to_serialize(self, request, data):
        # rename "objects" to "response"
        data['response'] = {"users":data['objects']}
        del(data['objects'])
        return data

    def determine_format(self, request):
        return 'application/json'

class BusinessResource(ModelResource):
    class Meta:
        queryset = Business.objects.all()
        resource_name = 'businesses'
        # Add it here.
        # authentication = BasicAuthentication()
        authorization = DjangoAuthorization()
        always_return_data = False
        allowed_methods = ['get']
        filtering = {
            'lat' : ALL,
            'lng': ALL,
            'organization_type': ('exact',),
            'organization_subtype': ('exact', 'startswith'),
        }

    def dehydrate(self, bundle):
        """
        Return a list of businesses formatted according to what the developer expects
        """

        return bundle

    def alter_list_data_to_serialize(self, request, data):
        # rename "objects" to "response"
        data['response'] = {"businesses":data['objects']}
        del(data['objects'])
        return data

    def determine_format(self, request):
        return 'application/json'

class CouponResource(ModelResource):
    business = fields.OneToOneField(BusinessResource, 'business', full=True)
    class Meta:
        queryset = Coupon.objects.all()
        resource_name = 'coupons'
        # Add it here.
        # authentication = BasicAuthentication()
        authorization = DjangoAuthorization()
        always_return_data = False
        allowed_methods = ['get','post']
        filtering = {
            'start': ALL,
            'end': ALL,
            'business': ALL
        }

    def dehydrate(self, bundle):
        """
        Return a list of businesses formatted according to what the developer expects
        """

        return bundle

    def obj_create(self, bundle, **kwargs):
        """
        Posts a new coupon
        """
        business = Business.objects.get(id=bundle.data["business"])
        message = bundle.data['message']
        new_coupon = Coupon(message=message, business=business)
        new_coupon.save()
        bundle.obj = new_coupon
        return bundle
        
    def alter_list_data_to_serialize(self, request, data):
        # rename "objects" to "response"
        data['response'] = {"coupons":data['objects']}
        del(data['objects'])
        return data

    def determine_format(self, request):
        return 'application/json'

class QueueResource(ModelResource):
    user = fields.OneToOneField(UserResource, 'user', full=True)
    business = fields.OneToOneField(BusinessResource, 'business', full=True)
    class Meta:
        queryset = Queue.objects.all()
        resource_name = 'queues'
        # Add it here.
        # authentication = BasicAuthentication()
        authorization = DjangoAuthorization()
        always_return_data = False
        allowed_methods = ['get','post','delete']
        filtering = {
            "user": ALL,
            "business": ALL,
        }

    def dehydrate(self, bundle):
        """
        Return a list of businesses formatted according to what the developer expects
        """

        return bundle

    def obj_create(self, bundle, **kwargs):
        """
        Posts a new business
        """
        user = User.objects.get(id=bundle.data['user'])
        business = Business.objects.get(id=bundle.data['business'])
        new_queue_entry = Queue(user=user, business=business)
        new_queue_entry.save()
        bundle.obj = new_queue_entry
        return bundle
        
    def alter_list_data_to_serialize(self, request, data):
        # rename "objects" to "response"
        data['response'] = {"queues":data['objects']}
        del(data['objects'])
        return data

    def determine_format(self, request):
        return 'application/json'