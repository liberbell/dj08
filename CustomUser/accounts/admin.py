from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import UserChangeForm, UserCreationForm
from .models import Schools, Students

# Register your models here.
User = get_user_model()

class CustomizeUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ("username", "email", "is_staff")
    fieldsets = (
        ("User information",
            {"fields": ("username", "email", "password", "website", "picture")}
        ),
        ("Permissions", 
            {"fields": ("is_staff", "is_active", "is_superuser")}
        ),
    )

    add_fieldsets = (
        ("User information",
            {"fields": ("username", "email", "password", "confirm_password")}),
    )

@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):

    fields = ("name", "score", "age", "school")
    list_display = ("id", "name", "age", "score", "school")
    list_display_links = ("name",)
    search_fields = ("name", "age")
    list_filter = ("name", "age", "score", "school")
    list_editable = ("age", "score")

@admin.register(Schools)
class SchoolsAdmin(admin.ModelAdmin):
    
    list_display = ("name", "student_count")

    def student_count(self, obj):
        print(type(obj))
        count = obj.students_set.count()
        return count

admin.site.register(User, CustomizeUserAdmin)
