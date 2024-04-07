from django.contrib import admin

from .models import Flat, Сomplaint, Owner


class OwnerInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ('owner', 'flat')


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address',)
    readonly_fields = ('created_at',)
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
    )
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)
    inlines = [OwnerInline]


@admin.register(Сomplaint)
class СomplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    search_fields = ('name', 'pure_phone',)
    list_display = (
        'name',
        'phonenumber',
        'pure_phone',
    )
    raw_id_fields = ('flats',)
