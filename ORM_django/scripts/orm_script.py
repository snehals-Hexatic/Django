from Core.models import Restaurant,Rating, sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User

def run():
    # restaurant = Restaurant()
    # restaurant.name = 'My Italian Restaurant'
    # restaurant.latitude = 50.2
    # restaurant.longitude = 50.2
    # restaurant.date_opened =timezone.now()
    # restaurant.restaurant_type = Restaurant.TypeChoices.ITALIAN
    
    # restaurant.save()
    
    # restaurant = Restaurant.objects.all()[0]
    # print(restaurant)
    
   
    #  user = User.objects.first()
    #  restaurant = Restaurant.objects.first()
     
    #  rating = Rating(user=user,restaurant=restaurant, rating =5)
     
    #  rating.full_clean()
    # rating.save()


    restaurant = Restaurant.objects.first() 
    print(restaurant.name)
    
    restaurant.name = 'New Restaurant Name'
    restaurant.save(update_fields=['name']) 
    
    print(connection.queries)
