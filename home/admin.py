from django.contrib import admin

from .models import About, Contact, Portfolio, Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_detail', 'slug', 'status', 'created']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_detail', 'status', 'created']


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'subject', 'status', 'created']

