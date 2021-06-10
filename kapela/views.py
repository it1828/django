from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from kapela.forms import BandModelForm, MemberModelForm
from kapela.models import Band, Member, Person


def index(request):
    num_bands = Band.objects.all().count()
    bands = Band.objects.order_by('band_name')
    members = Member.objects.order_by('person_name')
    context = {
        'num_bands': num_bands,
        'bands': bands,
        'members': members
    }
    return render(request, 'index.html', context=context)


class BandDetailView(DetailView):
    model = Band
    context_object_name = 'band_detail'
    template_name = 'band/detail.html'

class MemberDetailView(DetailView):
    model = Member
    context_object_name = 'member_detail'
    template_name = 'member/member.html'

class BandCreateView(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
    model = Band
    fields = ['band_name', 'genre', 'est_date', 'about', 'poster']
    template_name = 'kapela/band_bootstrap_form.html'
    permission_required = 'kapela.add_band'


    def get_success_url(self):
        return reverse('band_detail', kwargs={'pk': self.object.pk})



class BandUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Band
    form_class = BandModelForm
    template_name = 'kapela/band_bootstrap_form.html'
    permission_required = 'kapela.change_band'

    def get_success_url(self):
        return reverse('band_detail', kwargs={'pk': self.object.pk})


class BandDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Band
    success_url = reverse_lazy('index')
    permission_required = 'kapela.delete_band'



class MemberCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Member
    fields = '__all__'
    template_name = 'kapela/member_bootstrap_form.html'
    permission_required = 'kapela.add_member'

    def get_success_url(self):
        return reverse('member_detail', kwargs={'pk': self.object.pk})



class MemberUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Member
    form_class = MemberModelForm
    template_name = 'kapela/member_bootstrap_form.html'
    permission_required = 'kapela.change_member'

    def get_success_url(self):
        return reverse('member_detail', kwargs={'pk': self.object.pk})


class MemberDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Member
    success_url = reverse_lazy('index')
    permission_required = 'kapela.delete_member'



class PersonCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Person
    fields = '__all__'
    template_name = 'kapela/person_bootstrap_form.html'
    permission_required = 'kapela.add_person'

    success_url = reverse_lazy('index')