# coding=utf-8
from django.contrib import admin
from questions.models import Callback


class CallbackAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'name', 'phone', 'email')

    fieldsets = (
        (None, {
            'fields': ('created_at', 'name', 'phone', 'email')
        }),
    )

    readonly_fields = ('created_at',)


admin.site.register(Callback, CallbackAdmin)
