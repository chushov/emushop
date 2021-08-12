from django.contrib import admin

from .models import *


admin.site.register(Genre)
admin.site.register(Member)
admin.site.register(MediaType)
admin.site.register(ImageGallery)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Notification)