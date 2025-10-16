from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Post

@receiver(post_save, sender=Post)
def update_post_count(sender, instance, created, **kwargs):
    if created:
      
        print("Signal Triggered for:", instance.user.email)

        count = Post.objects.count()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "posts",
            {
                "type": "post_created",
                "count": count,
                "email": instance.user.email
            }
        )
