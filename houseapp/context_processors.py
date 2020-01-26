from houseapp.models import Membership


def add_variable_to_context(request):
    name = 'House Name'

    print(request.user)
    try:
        if request.user.is_authenticated:
            name = Membership.objects.get(person=request.user).house
            housemates = Membership.objects.get(
                person=request.user).house.members.all()
    except Exception:
        name = ''
        housemates = ['']

    return {
        'housename': name,
        'housemates': housemates
    }
