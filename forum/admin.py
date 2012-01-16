from forum.models import *
from django.contrib import admin

admin.site.register(Forum, ForumAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(ThreadView, ThreadViewAdmin)
admin.site.register(Post, PostAdmin)
