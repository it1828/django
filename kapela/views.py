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

class BandCreateView(CreateView):
    model = Band
    fields = ['band_name', 'genre', 'est_date', 'about', 'poster']
    template_name = 'kapela/band_bootstrap_form.html'

    def get_success_url(self):
        return reverse('band_detail', kwargs={'pk': self.object.pk})



class BandUpdateView(UpdateView):
    model = Band
    form_class = BandModelForm
    template_name = 'kapela/band_bootstrap_form.html'

    def get_success_url(self):
        return reverse('band_detail', kwargs={'pk': self.object.pk})


class BandDeleteView(DeleteView):
    model = Band
    success_url = reverse_lazy('index')



class MemberCreateView(CreateView):
    model = Member
    fields = '__all__'
    template_name = 'kapela/member_bootstrap_form.html'

    def get_success_url(self):
        return reverse('member_detail', kwargs={'pk': self.object.pk})



class MemberUpdateView(UpdateView):
    model = Member
    form_class = MemberModelForm
    template_name = 'kapela/member_bootstrap_form.html'

    def get_success_url(self):
        return reverse('member_detail', kwargs={'pk': self.object.pk})


class MemberDeleteView(DeleteView):
    model = Member
    success_url = reverse_lazy('index')



class PersonCreateView(CreateView):
    model = Person
    fields = '__all__'
    template_name = 'kapela/person_bootstrap_form.html'

    success_url = reverse_lazy('index')