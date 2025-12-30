from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('email', 'is_staff', 'is_active')
    fieldsets = [
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ["is_staff",
                                    "is_active", 
                                    "groups",
                                    "user_permissions",
                                    ]}),
    ]
    add_fieldsets = [
        (
            None, 
            {
                "classes": ("wide",),
                "fields": ("email", "password1",
                           "password2", "is_staff",
                        "is_active", "groups",
                        "user_permissions",
                ),
            },
        ),
    ]
    search_fields = ("email",)
    ordering = ("email",)

admin.site.register(CustomUser, UserAdmin)