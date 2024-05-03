from django.contrib import admin
from  .models import home,renter





class homemodel(admin.ModelAdmin):
    list_display=('location','phone_owner','numberof_home')
class rentemodel(admin.ModelAdmin):
    list_display=('your_contact','home_number','user_name')


admin.site.register(home,homemodel)
admin.site.register(renter,rentemodel)

# Register your models here.
