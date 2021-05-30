from django.forms import ModelForm

from .models import Band, Member, Person


class BandModelForm(ModelForm):
    class Meta:
        model = Band
        fields = ['band_name', 'genre', 'est_date', 'about', 'poster']




class MemberModelForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

