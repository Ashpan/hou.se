from houseapp.models import Membership


def add_variable_to_context(request):
    name = 'House Name'

    print(request.user)

    if request.user.is_authenticated:
        name = Membership.objects.get(person=request.user).house

    return {
        'housename': name
    }