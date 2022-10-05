from django.contrib import admin
from .models import Contact, Address, PhoneNumber, Email, SocialMedia, Note

class AddressInline(admin.TabularInline):
    model = Address.contacts.through
    extra = 0
    verbose_name_plural = 'Addresses'

class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber
    extra = 0

class EmailInline(admin.TabularInline):
    model = Email
    extra = 0

class SocialMediaInline(admin.TabularInline):
    model = SocialMedia
    extra = 0
    verbose_name_plural = 'Social Media Accounts'

class NoteInline(admin.TabularInline):
    model = Note
    extra = 0

class ContactAdmin(admin.ModelAdmin):
    inlines = [
        PhoneNumberInline,
        EmailInline,
        SocialMediaInline,
        AddressInline,
        NoteInline
    ]
    search_fields = ('name',)

admin.site.register(Contact, ContactAdmin)
admin.site.register(Address)
admin.site.register(PhoneNumber)
admin.site.register(Email)
admin.site.register(SocialMedia)
admin.site.register(Note)