from houseapp.models import Membership


def add_variable_to_context(request):
    name = 'House Name'

    try:
        if request.user.is_authenticated:
            name = Membership.objects.get(person=request.user).house
    except Exception:
        name = 'No House'

    return {
        'housename': name
    }
