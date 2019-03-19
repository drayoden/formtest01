from django.views.generic import TemplateView
from pages.forms import HomeForm
from django.shortcuts import render, redirect

class HomeView(TemplateView):
    template_name = 'pages/index.html'

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            msg = form.cleaned_data['msg']
            form = HomeForm()
            # return redirect('home:home') / not sure what this means yet

        args = {'form': form, 'name': name, 'email': email, 'msg': msg}
        return render(request, self.template_name, args)
