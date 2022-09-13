from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, state_choices, bedroom_choices
from django.shortcuts import get_object_or_404

from .models import Listing

def index(req):

   listings = Listing.objects.order_by('-list_date').filter(is_published=True)
   paginator = Paginator(listings, 6)
   page = req.GET.get('page')
   paged_listings = paginator.get_page(page)

   context = { 
        'listings': paged_listings,
   }

   return render(req, 'listings/listings.html', context)

def listing(req, listing_id):

   listing = get_object_or_404(Listing, pk=listing_id)

   context = {
      'listing': listing,
   }
   return render(req, 'listings/listing.html', context)

def search(req):

   context = { 
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices
   }

   return render(req, 'listings/search.html', context)