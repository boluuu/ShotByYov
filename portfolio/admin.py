from django.contrib import admin
from .models import Portfolio, Category, Contact
# Register your models here.
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('description', )
    search_fields = ['category']

admin.site.register(Portfolio, PortfolioAdmin)

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)

class ContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contact, CategoryAdmin)