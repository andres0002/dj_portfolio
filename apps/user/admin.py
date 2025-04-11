# django
from django.contrib import admin
# third
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# own
from apps.user.models import User, Skill, File

# Register your models here.

class UserResource(resources.ModelResource):
    class Meta:
        model = User

class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('user_id', 'speciality')
    readonly_fields = ('create_date', 'update_date')
    list_display = ('user_id', 'phone', 'mobile_phone', 'direction', 'page')
    list_filter = ('speciality', 'create_date', 'update_date')
    class_resource = UserResource

class SkillResource(resources.ModelResource):
    class Meta:
        model = Skill

class SkillAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('title', 'slug', 'description', 'content', 'create_date', 'update_date')
    readonly_fields = ('create_date', 'update_date')
    list_display = ('title', 'slug', 'create_date', 'update_date')
    list_filter = ('create_date', 'update_date')
    class_resource = SkillResource

class FileResource(resources.ModelResource):
    class Meta:
        model = File

class FileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('title', 'slug', 'create_date', 'update_date')
    readonly_fields = ('create_date', 'update_date')
    list_display = ('title', 'slug', 'create_date', 'update_date')
    list_filter = ('create_date', 'update_date')
    class_resource = FileResource

admin.site.register(User, UserAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(File, FileAdmin)