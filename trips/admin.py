# في ملف trips/admin.py
from django.contrib import admin
from .models import Trip,UserInput,Category
# from .models import Booking
# from .models import UserInput


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'date', 'capacity')
    search_fields = ('title', 'description')
    list_filter = ('date',)
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']  


admin.site.register(UserInput)
# class UserInputAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'phone', 'formatted_date')  # تأكد من إضافة الخاصية هنا

# admin.site.register(UserInput, UserInputAdmin)
#     # def formatted_date(self, obj):
    #     return obj.trip_dateTime.strftime("%Y-%m-%d %H:%M")
    # formatted_date.short_description = 'تاريخ الرحلة'
