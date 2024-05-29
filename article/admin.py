from django.contrib import admin

from .models import Article



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=['title','author','create_date']

    list_display_links=['title','create_date']

    search_fields=['author']

    list_filter=['create_date']
    class Meta:
        model=Article