from django.contrib import admin

from .models import Tweet


class TweetModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')

    # form = TweetModelForm
    class Meta:
        model = Tweet


admin.site.register(Tweet, TweetModelAdmin)
