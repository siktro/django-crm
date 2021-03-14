from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import Lead, Agent
from .forms import LeadForm, LeadModalForm, CustonUserCreationForm

# Handling webrequests and sending responses

class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustonUserCreationForm

    def get_success_url(self):
        return reverse('login')


class LandingPageView(generic.TemplateView):
    template_name = 'landing.html'


class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'  # object_list by default


def landing_page(request):
    return render(request, 'landing.html')

# simple function based view


def lead_list(request):
    # return HttpResponse('hello world!')
    # return render(request, 'second_page.html', {}) # for templates in 'global' folder
    # context allow to use own data to build dynamic templates
    # context = {
    #     'name': 'Joe',
    #     'age': 42
    # }
    leads = Lead.objects.all()
    context = {
        'leads': leads
    }
    return render(request, 'leads/lead_list.html', context)


class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'  # object_list by default


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        'lead': lead
    }
    return render(request, 'leads/lead_detail.html', context)


class LeadCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModalForm

    def get_success_url(self):
        return reverse('leads:lead-list')

# function with ModelForm


def lead_create(request):
    form = LeadModalForm()
    if request.method == 'POST':
        form = LeadModalForm(request.POST)
        if form.is_valid():
            form.save()  # automaticly creates new Lead in DB
            return redirect('/leads/')

    context = {
        'form': form
    }

    return render(request, 'leads/lead_create.html', context)


class LeadUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'leads/lead_update.html'
    queryset = Lead.objects.all()
    form_class = LeadModalForm

    def get_success_url(self):
        return reverse('leads:lead-list')

def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModalForm(instance=lead)
    if request.method == 'POST':
        form = LeadModalForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/leads/')

    context = {
        'lead': lead,
        'form': form
    }
    return render(request, 'leads/lead_update.html', context)


class LeadDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead-list')


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads/')


# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     if request.method == 'POST':
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             Lead.objects.update(**form.cleaned_data)
#             return redirect('/leads/')

#     context = {
#         'lead': lead,
#         'form': form
#     }
#     return render(request, 'leads/lead_update.html', context)


# function with MANUAL form
# def lead_create(request):
#     form = LeadForm()
#     if request.method == 'POST':
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             agent = Agent.objects.first()
#             Lead.objects.create(agent=agent, **form.cleaned_data)
#             return redirect('/leads/')

#     context = {
#         'form': form
#     }

#     return render(request, 'leads/lead_create.html', context)
