from kapela.models import Band, Member

def bands(request):
    return {'bands': Band.objects.all()}

def members(request):
    return {'members': Member.objects.all()}
