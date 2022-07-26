import folio
import uuid


def create_user(first_name, last_name, barcode, email):
    payload = {
        'active': True,
        'personal': {
            'firstName': first_name,
            'preferredContactTypeId': '002',
            'lastName': last_name,
            'email': email
        },
        'barcode': barcode,
        'patronGroup': '3684a786-6671-4268-8ed0-9db82ebca60b',
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

