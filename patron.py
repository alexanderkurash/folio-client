import uuid
import folio


def create_instance_request(patron_id, instance_id, pickup_location_id):
    print('Creating an instance request (mod-patron, EDS-style)...')
    request = folio.post('patron/account/%s/instance/%s/hold' % (patron_id, instance_id), {
        'requestDate': '2022-08-25T17:47:52.041Z',
        'pickupLocationId': pickup_location_id
    })
    if request.status_code == 201:
        id = request.json()['id']
        print("Succeeded to create an instance request. ID: %s" % id)
        return request.json()
    else:
        print('Failed to create an instance request')
        print(request.text)
