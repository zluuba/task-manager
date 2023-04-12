from django.shortcuts import render
from django.views import View


class IndexView(View):

    def get(self, request, *args, **kwargs):
        # users = User.objects.all()[:15]
        # return render(request, 'users/index.html', context={
        #     'users': users,
        # })
        return render(request, 'users/index.html')


class UserFormCreateView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'users/user_create.html')

    def post(self, request, *args, **kwargs):
        return render(request, 'users/user_create.html')


class UserFormUpdateView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'users/user_update.html')

    def post(self, request, *args, **kwargs):
        return render(request, 'users/user_update.html')


class UserFormDeleteView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'users/user_delete.html')

    def post(self, request, *args, **kwargs):
        return render(request, 'users/user_delete.html')
