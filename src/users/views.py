from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import CustomLoginForm, CustomRegisterForm
from django.views.generic import TemplateView
from django.shortcuts import render, redirect

class LoginAndRegisterView(TemplateView):
    template_name = 'login_registration.html'
    login_form_class = CustomLoginForm
    register_form_class = CustomRegisterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = self.login_form_class()
        context['register_form'] = self.register_form_class()
        return context

    def post(self, request, *args, **kwargs):
        login_form = self.login_form_class(request, data=request.POST)
        register_form = self.register_form_class(request.POST)
        
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
        
        if register_form.is_valid():
            # Perform registration logic
            user = register_form.save(commit=False)
            user.set_password(register_form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('home')  
        
        # If neither form is valid, re-render the template with the errors
        return render(request, self.template_name, {
            'login_form': login_form,
            'register_form': register_form
        })







