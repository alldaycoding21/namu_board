from django.contrib import admin
from .models import Post
# Register your models here.

# 관리자 페이지에서 게시글 관리
admin.site.register(Post)