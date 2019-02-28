from django.shortcuts import render, redirect
from django.views.generic import View
from .form import Form_demo
import asana
# Create your views here.


class Index(View):

    def get(self, request):
        form = Form_demo()
        return render(request, template_name='form_app/index.html', context={'form': form})

    def post(self, request):
        form = Form_demo(request.POST)
        if form.is_valid():
            client = asana.Client.access_token('0/e53079d9dab14077f642629b927a9ece')
            client.tasks.create_in_workspace( workspace='1111813369839902', projects='1111842186512584',
                                              name=form.cleaned_data['company'],
                                              notes=form.__str__())
            return redirect()