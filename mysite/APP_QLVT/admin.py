from django.contrib import admin
from .models import QLVT_Data
# Register your models here.


# class PostAdmin(admin.ModelAdmin):
#     list_display = ["[Tên thiết bị]", "[Nhà sản xuất]"]
#     list_filter = ['[Tên thiết bị]']
#     search_fields = ['[Tên thiết bị]']

# admin.site.register(QLVT_Data, PostAdmin)

admin.site.register(QLVT_Data)