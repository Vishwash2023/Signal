from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import User


@receiver(post_save, sender=User)    
def task_hendlar(sender , instance, **kwargs):
    print("fetched____________________________________________________________________________________________")
    
    

