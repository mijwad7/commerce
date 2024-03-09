from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms

class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1000)
    starting_bid = models.FloatField()
    isActive = models.BooleanField(default=True)
    watchlist = models.ManyToManyField(User, blank=True, related_name="watchlist")
    image = models.URLField(blank=True)
    category_choices = [
        ('EL','Electronics'),
        ('SP','Sports'),
        ('HO','Home'),
        ('TV','TV'),
        ('PC','PC'),
        ('CA','Cars'),
        ('SH','Shoes'),
        ('AC','Accessories'),
        ('FS', 'Fashion'),
        ('TY', 'Toys'),
        ('OT','Other')
    ]
    category = models.CharField(choices=category_choices, max_length=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="user")
    @property
    def highest_bid(self):
        highest_bid = Bid.get_highest_bid(self)
        return highest_bid


class ListingForm(forms.Form):
    title = forms.CharField(max_length=64, label='Title')
    description = forms.CharField(max_length=1000, label='Description')
    starting_bid = forms.FloatField(label='Starting Bid')
    image = forms.URLField(label='Image', required=False)
    category = forms.ChoiceField(choices=Listing.category_choices, label='Category')

class Bid(models.Model):
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="item")
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidder")
    bid_amount = models.FloatField()
    @classmethod
    def get_highest_bid(cls, listing):
        highest_bid = cls.objects.filter(item=listing).order_by('-bid_amount').first()
        return highest_bid
    

class BidForm(forms.Form):
    bid_amount = forms.FloatField(label='Bid Amount')

class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="comment_user")
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comment_item")
    comment = models.CharField(max_length=1000)

class CommentForm(forms.Form):
    comment = forms.CharField(max_length=1000, label='Comment')





      
                
