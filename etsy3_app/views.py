from django.shortcuts import render, render_to_response

# Create your views here.
from etsy3_app.models import Shop
from django.views.decorators.csrf import csrf_exempt
import json

def index2(request):

    return render(request, 'index2.html')

def index(request):

    return render(request, 'index.html')

@csrf_exempt
def show_shop(request):
    shop_array=[]
    if request.method == 'POST':
        data = json.loads(request.body)
        print data
        for listing in data['searchResults']:


            new_listing = Shop.objects.create(
                title=listing['title'],
                description=listing['description'],
                price=listing['price'],
                listing_id=listing['listing_id'],

            )
            listing_info = {
                'title': new_listing.title,
                'description':new_listing.description,
                'price':new_listing.price,
                'id':new_listing.listing_id,
            }
            shop_array.append(listing_info)
        # return render_to_response('shop_template.html', {'shop_array':shop_array})
        return render(request, 'shop_template.html', {'shop_array': shop_array})

@csrf_exempt
def show_faves(request):
    shop_array=[]
    if request.method == 'POST':
        data = json.loads(request.body)

        for listing in data['searchResults']:


            new_listing = Shop.objects.create(
                title=listing['title'],
                # description=listing['description'],
                # price=listing['price'],
                # listing_id=listing['listing_id'],

            )
            listing_info = {
                'title': new_listing.title,
                # 'description':new_listing.description,
                # 'price':new_listing.price,
                # 'id': new_listing.listing_id,
            }
            print listing_info
            shop_array.append(listing_info)
        # return render_to_response('shop_template.html', {'shop_array':shop_array})
        return render(request,'show_faves.html', {'shop_array':shop_array})
