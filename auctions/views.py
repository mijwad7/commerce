from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, Listing, ListingForm, Bid, BidForm, Comment, CommentForm

def index(request):
    active_listings = Listing.objects.filter(isActive=True)
    return render(request, "auctions/index.html", {
        "listings": active_listings,
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
    

@login_required
def create(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = Listing(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['category'],
                starting_bid=form.cleaned_data['starting_bid'],
                image=form.cleaned_data['image'],
                owner=request.user
            )
            listing.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = ListingForm()

    return render(request, 'auctions/create.html', {'form': form})

def listing(request, id):
    listing = Listing.objects.get(pk=id)
    comments =  Comment.objects.filter(item=listing)
    highest_bid = Bid.objects.filter(item=listing).order_by('-bid_amount').first()
    bids = Bid.objects.filter(item=listing).count()
    if request.method == "POST":
        form = BidForm(request.POST)
        if form.is_valid():
            bid_amount = form.cleaned_data['bid_amount']
            if bid_amount >= listing.starting_bid:
                if highest_bid is None or bid_amount > highest_bid.bid_amount:
                    bid = Bid(
                        bid_amount=bid_amount,
                        bidder=request.user,
                        item=listing
                        )
                    bid.save()
                    return HttpResponseRedirect(reverse("listing", args=[id]))
                else:
                    form.add_error('bid_amount', 'Your bid must be higher than the current highest bid.')
            else:
                form.add_error('bid_amount', 'Your bid must be at least as large as the starting bid.')
    else:
        form = BidForm()

    return render(request, 'auctions/listing.html', {
        "listing": listing,
        "form": form,
        "highest_bid": highest_bid,
        "bids": bids,
        "comments": comments
    })

    
def watchlist(request, id):
    listing = Listing.objects.get(pk=id)
    user = request.user
    if request.method == "POST":
            if listing not in user.watchlist.all():
                user.watchlist.add(listing)
                return HttpResponseRedirect(reverse("listing", args=[id]))
            else:
                user.watchlist.remove(listing)
                return HttpResponseRedirect(reverse("listing", args=[id]))
    else:
        return render(request, 'auctions/listing.html', {
            "listing": listing,
            "user": user
            })
            
def view_watchlist(request):
    user = request.user
    listings = user.watchlist.all()
    return render(request, "auctions/watchlist.html", {
        "listings": listings
    })

def categories(request):
    categories = Listing.category_choices
    return render(request, "auctions/categories.html", {
        "categories": categories
    })

def category(request, category):
    listings = Listing.objects.filter(category=category)
    return render(request, "auctions/category.html", {
        "listings": listings,
        "category": category
        })

def close_auction(request, id):
    user = request.user
    listing = Listing.objects.get(pk=id)
    if user == listing.owner:
        if request.method == "POST":
            listing.isActive = False
            listing.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/listing.html", {
                "listing": listing,
                })
    else:
        return render(request, "auctions/listing.html", {
                "listing": listing
                })
        

def comment (request, id):
    listing = Listing.objects.get(pk=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                commenter=request.user,
                comment=form.cleaned_data['comment'],
                item=listing
            )
            comment.save()
            return HttpResponseRedirect(reverse("listing", args=[id]))
    else:
        return render(request, "auctions/listing.html", {
                "listing": listing,
                })

def add_comment(request, id):
    listing = Listing.objects.get(pk=id)
    form = CommentForm()     
    return render(request, 'auctions/add_comment.html', {
        "listing": listing,
        "comment_form": form
        })