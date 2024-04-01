from django.contrib import admin
from .models import Signup, Login

class SignupAdmin(admin.ModelAdmin):
    list_display = ("username", "emailaddress", "password", "confirm_password")

admin.site.register(Signup, SignupAdmin)

class LoginAdmin(admin.ModelAdmin):
    list_display = ("get_username", "get_password")

    def get_username(self, obj):
        return obj.username

    def get_password(self, obj):
        return obj.password

    get_username.short_description = 'Username'
    get_password.short_description = 'Password'

admin.site.register(Login, LoginAdmin)


