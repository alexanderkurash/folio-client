import uuid
import folio


def create_instance_request(patron_id, instance_id, pickup_location_id):
    print('Creating an instance request (mod-patron, EDS-style)...')
    request = folio.post('patron/account/%s/instance/%s/hold' % (patron_id, instance_id), {
        'requestDate': '2022-08-25T17:47:52.041Z',
        'pickupLocationId': pickup_location_id
    })
    if request.status_code == 201:
        requestId = request.json()['requestId']
        print("Succeeded to create an instance request. ID: %s" % requestId)
        return request.json()
    else:
        print('Failed to create an instance request')
        print(request.text)


def cancel_instance_request(request, user):
    print('Cancelling instance request (mod-patron, EDS-style)...')
    cancel_request_body = {
        'holdId': request['requestId'],
        'cancellationReasonId': '4ca6a58e-f8ed-4f7a-89ee-7a3e0f20a659',
        'canceledByUserId': user['id'],
        'cancellationAdditionalInformation': 'Info',
        'pickupLocationId': request['pickupLocationId'],
        "canceledDate": "2022-09-22T10:16:30Z",
        'requestDate': request['requestDate']}
    print('Cancelling request. Body: %s' % cancel_request_body)
    cancelled_request = folio.post('patron/account/%s/hold/%s/cancel' % (user['id'], request['requestId']),
                                   cancel_request_body)
    if cancelled_request.status_code == 200:
        requestId = cancelled_request.json()['requestId']
        print("Succeeded to cancel an instance request. ID: %s" % requestId)
        return cancelled_request.json()
    else:
        print('Failed to cancel an instance request')
        print(cancelled_request)
