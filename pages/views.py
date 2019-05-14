from django.views.generic import TemplateView
from pages.forms import HomeForm
from django.shortcuts import render, redirect

class HomeView(TemplateView):
    template_name = 'pages/index.html'

    def get(self, request):
        form = HomeForm()
        contact_joy = False
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = HomeForm(request.POST)
        contact_joy = False
        if form.is_valid():

            contact_joy = True

            # save form data to db
            form.save()

            # data needed for modal...
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            msg = form.cleaned_data['msg']

            # reinitialize form...
            form = HomeForm()  # does not prevent refresh submit, modal works
            # return redirect('/') # works, but breaks the modal
            # return redirect('formtest:views') # not sure what this means yet
            # return redirect(self.template_name)
            # return HttpResponseRedirect(self.template_name)

        args = {'form': form, 'name': name, 'email': email, 'msg': msg, 'cjoy': contact_joy}
        return render(request, self.template_name, args)
