from django.contrib import admin

# Register your models here.

from .models import Author, Quote

#admin.site.register(Author)

class QuoteInline(admin.StackedInline):
    model = Quote
    extra = 3


class AuthorAdmin(admin.ModelAdmin):
	list_display = ('author_name', 'author_bio')
	list_filter = ['author_name']
	fieldsets = [(None,               {'fields': ['author_name', 'author_bio']}),]
	inlines = [QuoteInline]

admin.site.register(Author, AuthorAdmin)