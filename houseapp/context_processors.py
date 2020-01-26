from houseapp.models import Membership


def add_variable_to_context(request):
    return {
        'housename': Membership.objects.get(person=request.user).house
    }