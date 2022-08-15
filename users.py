import folio
import uuid


def create_user(barcode, first_name, last_name, email, patron_group_name):
    group_id = get_patron_group_id_by_name(patron_group_name)
    if group_id is not None:
        print('Patron group ID: %s', group_id)
    else:
        print('Failed to find patron group')
        return

    payload = {
        'active': True,
        'personal': {
            'firstName': first_name,
            'preferredContactTypeId': '002',
            'lastName': last_name,
            'email': email
        },
        'barcode': barcode,
        'patronGroup': group_id,
        'id': str(uuid.uuid4()),
        'departments': []
    }

    print('Creating a user...')
    request = folio.post('users', payload)
    if request.status_code == 201:
        user_id = request.json()['id']
        print("Succeeded to create a user. ID: %s" % user_id)
        return request.json()
    else:
        print('Failed to create a user')
        print(request.text)


def get_or_create_user_by_barcode(barcode, first_name, last_name, email, patron_group_name):
    response = folio.get("users?query=barcode==%s" % barcode)
    if response.status_code == 200:
        users = response.json()['users']
        if len(users) == 1:
            return users[0]

    return create_user(barcode, first_name, last_name, email, patron_group_name)


def get_patron_group_id_by_name(group):
    return folio.find_id('groups', 'group', group, 'usergroups')

