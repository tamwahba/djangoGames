from django.contrib import admin
from django.db import models
from knights.models import UserProfile, Sprite
from django.forms import CheckboxSelectMultiple

#class SpriteInline(admin.TabularInline):
#    model = Sprite
#    extra = 1


class UserProfileAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple}}


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Sprite)
