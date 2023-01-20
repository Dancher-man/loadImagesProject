from django.contrib import admin

from source.models import Persons, Images


class PurchaseInline(admin.TabularInline):
    model = Persons.persons_name.through
    extra = 0


@admin.register(Images)
class ImagesViewAdmin(admin.ModelAdmin):
    list_display = ('geolocation', 'photo', 'description', 'created_at', 'get_persons')
    list_display_links = ('geolocation',)
    list_filter = ('geolocation', 'description', 'created_at')
    search_fields = ('geolocation', 'description', 'created_at')
    save_on_top = True
    save_as = True
    inlines = (PurchaseInline, )

    def get_persons(self, obj):
        return "\n".join([person.name for person in obj.persons_names.all()])


@admin.register(Persons)
class PersonsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    save_on_top = True
    save_as = True
