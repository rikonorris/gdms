from django.contrib import admin

from django.contrib.auth.admin import GroupAdmin

from . import models


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">account_balance</i>'
    list_display = ('dept_no', 'dept_name')


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DeptEmp)
class DeptEmpAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">people_outline</i>'
    list_display = ('employee', 'department', 'from_date', 'to_date')
    list_select_related = True
    raw_id_fields = ('employee', )
    list_filter = ('department', )


@admin.register(models.DeptManager)
class DeptManagerAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">assignment_ind</i>'
    list_display = ('employee', 'department', 'from_date', 'to_date')
    raw_id_fields = ('employee', )
    list_filter = ('department', )



@admin.register(models.Title)
class TitleAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">reorder</i>'
    list_display = ('employee', 'from_date', 'to_date', 'title')
    raw_id_fields = ('employee', )
    list_filter = ('title', )


@admin.register(models.ProxyGroup)
class ProxyGroupAdmin(GroupAdmin):
    pass
