import folio
import datetime


def check_out(item_barcode, user_barcode, service_point_id):
    print('Checking out the item %s to the user %s...' % (item_barcode, user_barcode))
    request = folio.post('circulation/check-out-by-barcode', {'itemBarcode': item_barcode,
                                                              'userBarcode': user_barcode,
                                                              'servicePointId': service_point_id})
    if request.status_code == 201:
        loan_id = request.json()['id']
        print("Succeeded to check out an item. Loan ID: %s" % loan_id)
        return request.json()
    else:
        print('Failed to check out an item')
        print(request.text)


def get_requests(query):
    request = folio.get('request-storage/requests?query=(requestType=="Page") '
                        'sortby searchIndex.shelvingOrder requester.barcode/sort.descending')
    if request.status_code == 200:
        print(request.json()['totalCount'])


def create_ilr(requester_id, request_type, instance_id, holdings_record_id, item_id, fulfilment_preference,
               pickup_service_point_id):

    request = folio.post('circulation/requests', {
        'requestLevel': 'Item',
        'instanceId': instance_id,
        'holdingsRecordId': holdings_record_id,
        'itemId': item_id,
        'requesterId': requester_id,
        'requestType': request_type,
        'requestDate': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.000Z'),
        'fulfilmentPreference': fulfilment_preference,
        'pickupServicePointId': pickup_service_point_id,
    })
    if request.status_code == 201:
        request_id = request.json()['id']
        print("Succeeded to create a request. Request ID: %s" % request_id)
        return request.json()
    else:
        print('Failed to create a request')
        print(request.text)

