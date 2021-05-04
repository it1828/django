from django.shortcuts import render
from django.views.generic import DetailView
from kapela.models import Band, Member

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

