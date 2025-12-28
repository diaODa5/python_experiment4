from django.contrib import admin

# Register your models here.
from django.contrib import admin
# 导入你刚才写的模型
from .models import BlogPost

# 注册模型
admin.site.register(BlogPost)