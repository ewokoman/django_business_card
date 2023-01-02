from django.contrib import admin
from django import forms
from .models import Owner, Company, Comment, Projects, Owner_site, Contacts


class ContactsInline(admin.StackedInline):
    model = Contacts
    extra = 2


class Owner_site_prevew(admin.ModelAdmin):
    fields = ['first_name', 'last_name',
              'position', 'company', 'about', 'image']
    list_display = ('first_name', 'last_name', 'position', 'company')
    inlines = [ContactsInline]


class ProjectsModelForm( forms.ModelForm ):
    comment_text = forms.CharField( widget=forms.Textarea )
    class Meta:
        fields = '__all__'
        model = Projects

class Projects_Admin( admin.ModelAdmin ):
    form = ProjectsModelForm



admin.site.register(Owner)
admin.site.register(Company)
admin.site.register(Comment)
admin.site.register(Projects, Projects_Admin)
admin.site.register(Owner_site, Owner_site_prevew)
