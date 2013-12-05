#API Reference for qUP
This is the `/v1/` API documentation for the resolution mobile API. All requests are RESTful and all request & response bodies are `json` formatted.

*	[Login User/Get Users](#getusers)
*	[Get Businesses](#getbusinesses)
*	[Get Coupons](#getcoupons)
*	[Post Coupons](#postcoupons)
*	[Get Queues](#getqueues)

** By default, all requests have an application/json content type. **

** By default, all request can be filtered by 'limit' eg. /api/v1/xxxx?limit=100 **

** For all get request, params refer to /api/v1/xxxx?param1=abc&param2=abc2 **

##<a id="getusers"></a>Login User
This is basically checking is a user exists. /api/v1/users requires basic authentication so we will use that. For more information on how to construct the Basic Authentication authorization header: [wiki](http://en.wikipedia.org/wiki/Basic_access_authentication)

	HTTP Method: GET
	Requires Authentication: Yes - Basic Authentication
	URL: /api/v1/users/
	Content Type: application/json
	
**Example Request Header:**

	Content-Type: application/json
	Authorization: Basic c2FuY2hpdDpyb290 -- this corresponds to sanchit:root
	Accept: */*
	
**Example Response Body:** it basically returns a list of users. This doesn't matter for us. I think the more important thing is that the return Response Status Code is 200.

	{
    	"meta": {
        	"limit": 20,
        	"next": null,
        	"offset": 0,
        	"previous": null,
        	"total_count": 1
    	},
    	"response": {
        	"users": [{
            	"email": "sanchitbareja@gmail.com",
            	"first_name": "",
            	"id": 1,
            	"is_business": false,
            	"is_premium": false,
            	"last_login": "2013-12-05T03:52:05.606896",
            	"last_name": "",
            	"resource_uri": "/api/v1/users/1/",
            	"username": "sanchit"
        	}]
    	}
	}

	
##<a id="getbusinesses"></a>Get Businesses

Returns a list of businesses.

**Filtering options:**

* lat (ALL type of filterings allow eg. lat__lt, lat__gt) - [field lookups](https://docs.djangoproject.com/en/dev/ref/models/querysets/#field-lookups)
* lng (ALL type of filterings allow eg. lng__lt, lng__gt) - [field lookups](https://docs.djangoproject.com/en/dev/ref/models/querysets/#field-lookups)
* type  (needs to be exact e.g. "Cafe") - (see below for the list of types)

**List of Types**

* Cafe
* Restaurant
	
**Example Request Body**	

	Request Url: http://127.0.0.1:8000/api/v1/businesses/
	Request Method: GET
	Status Code: 200
	Params: {
    	"lat__gt": "37",
    	"lng__gt": "-123",
    	"lat__lt": "38",
    	"lng__lt": "-122",
    	"organization_type": "Cafe"
	}
	
**Example Response Body**

	{
    	"meta": {
    	    "limit": 20,
       		"next": null,
        	"offset": 0,
        	"previous": null,
        	"total_count": 1
    	},
    	"response": {
        	"businesses": [{
            	"avg_wait_time": "2.0",
            	"id": 3,
            	"lat": "37.8781000000",
            	"lng": "-122.2692600000",
            	"name": "Philz Coffee",
            	"organization_type": "Cafe",
            	"resource_uri": "/api/v1/businesses/3/"
        	}]
    	}
	}

##<a id="getcoupons"></a>Get Coupons

Returns a list of Coupons

**Filtering options**

* start
* end (this will probably be most commonly used. ALL filters allowed as above eg. end__lt)
* business (specify the business id e.g. 1)

**Example Request Body**

	Request Url: http://127.0.0.1:8000/api/v1/coupons/
	Request Method: GET
	Status Code: 200
	Params: {
	    "business": "1",
    	"end__lt": "2013-12-06T06:00:00"
	}

**Example Response Body**

	{
    	"meta": {
    	    "limit": 20,
        	"next": null,
        	"offset": 0,
        	"previous": null,
        	"total_count": 1
    	},
    	"response": {
        	"coupons": [{
            	"business": {
                	"avg_wait_time": "5.0",
                	"id": 1,
                	"lat": "37.8703400000",
                	"lng": "-122.2668900000",
                	"name": "Sliver",
                	"organization_type": "Restaurant",
                	"resource_uri": "/api/v1/businesses/1/"
            	},
            	"end": "2013-12-06T05:06:39",
            	"id": 3,
            	"message": "Buy 5 get 1 free",
            	"resource_uri": "/api/v1/coupons/3/",
            	"start": "2013-12-05T05:06:39"
        	}]
    	}
	}
	
##<a id="postcoupons"></a>Post Coupon

**Example Request Body**

Look at this article to see how to make a post request: [Article](http://django-tastypie.readthedocs.org/en/latest/interacting.html#creating-a-new-resource-post)

Currently, I've forced the start time to be the time we decide to add the coupon and end time to be 1 day later. Can't be specified - I believe this is easier for now unless we want to change it. In any case, I feel it's just more work on the frontend

	Specify data to be : {"business":1,"message":"50% all items"}
	Request Url: http://127.0.0.1:8000/api/v1/coupons/
	Request Method: POST

**Example Response Header**

	Status Code: 201
	Location: http://127.0.0.1:8000/api/v1/coupons/4/
	Date: Thu, 05 Dec 2013 05:25:23 GMT
	Vary: Accept
	Server: WSGIServer/0.1 Python/2.7.5
	X-Frame-Options: SAMEORIGIN
	Content-Type: text/html; charset=utf-8

##<a id="getqueues"></a>Get Queues

**Filtering options**
* user (ALL filters allowed as above e.g. user=1)
* business (ALL filters allowed as above e.g. business=1)

**Example Request Body**

	Request Url: http://127.0.0.1:8000/api/v1/queues/
	Request Method: GET
	Status Code: 200
	Params: {
	    "user": "1"
	}

**Example Response Body**

	{
    	"meta": {
        	"limit": 20,
        	"next": null,
        	"offset": 0,
        	"previous": null,
        	"total_count": 3
    	},
    	"response": {
        	"queues": [{
            	"business": {
                	"avg_wait_time": "5.0",
                	"id": 1,
                	"lat": "37.8703400000",
                	"lng": "-122.2668900000",
                	"name": "Sliver",
                	"organization_type": "Restaurant",
                	"resource_uri": "/api/v1/businesses/1/"
            	},
            	"id": 2,
            	"resource_uri": "/api/v1/queues/2/",
            	"time_entered_in_queue": "2013-12-05T05:36:16.979565",
            	"user": {
                	"email": "sanchitbareja@gmail.com",
                	"first_name": "",
                	"id": 1,
                	"is_business": false,
                	"is_premium": false,
                	"last_login": "2013-12-05T03:52:05.606896",
                	"last_name": "",
                	"resource_uri": "/api/v1/users/1/",
                	"username": "sanchit"
            	}
        	}, {
            	"business": {
                	"avg_wait_time": "10.0",
                	"id": 2,
                	"lat": "37.8800100000",
                	"lng": "-122.2695000000",
                	"name": "Cheeseboard",
                	"organization_type": "Restaurant",
                	"resource_uri": "/api/v1/businesses/2/"
            	},
            	"id": 3,
            	"resource_uri": "/api/v1/queues/3/",
            	"time_entered_in_queue": "2013-12-05T05:36:24.224587",
            	"user": {
                	"email": "sanchitbareja@gmail.com",
                	"first_name": "",
                	"id": 1,
               		"is_business": false,
                	"is_premium": false,
                	"last_login": "2013-12-05T03:52:05.606896",
                	"last_name": "",
                	"resource_uri": "/api/v1/users/1/",
                	"username": "sanchit"
            	}
        	}, {
            	"business": {
                	"avg_wait_time": "2.0",
                	"id": 3,
                	"lat": "37.8781000000",
                	"lng": "-122.2692600000",
                	"name": "Philz Coffee",
                	"organization_type": "Cafe",
                	"resource_uri": "/api/v1/businesses/3/"
            	},
            	"id": 4,
            	"resource_uri": "/api/v1/queues/4/",
            	"time_entered_in_queue": "2013-12-05T05:36:30.602893",
            	"user": {
                	"email": "sanchitbareja@gmail.com",
                	"first_name": "",
                	"id": 1,
                	"is_business": false,
                	"is_premium": false,
                	"last_login": "2013-12-05T03:52:05.606896",
                	"last_name": "",
                	"resource_uri": "/api/v1/users/1/",
                	"username": "sanchit"
            	}
        	}]
    	}
	}
	
##<a id="postqueues"></a>Post Queue

**Example Request Body**

Look at this article to see how to make a post request: [Article](http://django-tastypie.readthedocs.org/en/latest/interacting.html#creating-a-new-resource-post)

Currently, you only need to specify the user and business id

	Specify data to be : {"business":1,"user":1}
	Request Url: http://127.0.0.1:8000/api/v1/queues/
	Request Method: POST

**Example Response Header**

	Status Code: 201
	Location: http://127.0.0.1:8000/api/v1/queues/5/
	Date: Thu, 05 Dec 2013 06:01:27 GMT
	Vary: Accept
	Server: WSGIServer/0.1 Python/2.7.5
	X-Frame-Options: SAMEORIGIN
	Content-Type: text/html; charset=utf-8
