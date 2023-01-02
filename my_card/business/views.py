from django.shortcuts import render, get_object_or_404
from .models import Comment, Projects, Company, Owner_site, Contacts
# from django.views import generic
from django import forms
from django.utils import timezone


def index(request):
    owner_site = Owner_site.objects.all().last()
    contacts_list = owner_site.contacts_set.all()
    context = {
        'owner_site': owner_site,
        'contacts_list': contacts_list,
    }
    return render(request, 'business/index.html', context)


def projects(request):
    owner_site = Owner_site.objects.all().last()
    projects_list = Projects.objects.all()
    context = {
        'projects_list': projects_list,
        'owner_site': owner_site,
    }
    return render(request, 'business/projects.html', context)


def detail(request, pk):
    owner_site = Owner_site.objects.all().last()
    project = get_object_or_404(Projects, pk=pk)
    context = {
        'project': project,
        'owner_site': owner_site,
    }
    return render(request, 'business/project.html', context)


class CommentForm(forms.Form):
    class_field = 'form-control'
    first_name = forms.CharField(min_length=2, widget=forms.TextInput(
        attrs={'placeholder': 'Ваше имя', 'class': class_field}))
    last_name = forms.CharField(min_length=2, widget=forms.TextInput(
        attrs={'placeholder': 'Ваша фамилия', 'class': class_field}))
    company = forms.CharField(min_length=2, widget=forms.TextInput(
        attrs={'placeholder': 'Компания', 'class': class_field}))
    comment = forms.CharField(min_length=4, widget=forms.Textarea(
        attrs={'placeholder': 'Комментарий', 'rows': 6, 'class': class_field}))


def reviews(request):
    owner_site = Owner_site.objects.all().last()
    latest_comments_list = Comment.objects.order_by('-pub_date')[:5]
    context = {
        'latest_comments_list': latest_comments_list,
        'owner_site': owner_site,
    }
    if request.method == 'POST':
        data_form = CommentForm(request.POST)
        if data_form.is_valid():
            company, created = Company.objects.get_or_create(
                name=data_form.cleaned_data['company'], country='Russia')
            owner, created = company.owner_set.get_or_create(
                first_name=data_form.cleaned_data['first_name'], last_name=data_form.cleaned_data['last_name'])
            owner.comment_set.create(
                comment_text=data_form.cleaned_data['comment'], pub_date=timezone.now())
        form = CommentForm()
    else:
        form = CommentForm()
    context['form'] = form
    return render(request, 'business/reviews.html', context)
