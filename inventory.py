import uuid
import folio


def get_items():
    print('Getting items...')
    request = folio.get('inventory/items')
    if request.status_code == 200:
        print("Succeeded to get items. Items in the response: %d. Total records: %d" %
              (len(request.json()['items']), request.json()['totalRecords']))
        return request.json()
    else:
        print('Failed to get items')


def get_item(item_id):
    print('Getting an item %s...' % item_id)
    request = folio.get('inventory/items/%s' % item_id)
    if request.status_code == 200:
        print("Succeeded to get item %s" % item_id)
        return request.json()
    else:
        print('Failed to get items')


def create_item(item):
    print('Creating an item...')
    request = folio.post('inventory/items', item)
    if request.status_code == 201:
        item_id = request.json()['id']
        print("Succeeded to create an item. ID: %s" % item_id)
        return request.json()
    else:
        print('Failed to create an item')
        print(request.text)


def create_instance(title, instanceTypeId):
    instance_id = str(uuid.uuid4())
    payload = {
        'id': instance_id,
        'discoverySuppress': False,
        'staffSuppress': False,
        'previouslyHeld': False,
        'source': 'FOLIO',
        'title': title,
        'instanceTypeId': instanceTypeId,
        'precedingTitles': [],
        'succeedingTitles': [],
        'parentInstances': [],
        'childInstances': [],
        "contributors": []
    }

    print('Creating an instance...')
    request = folio.post('inventory/instances', payload)
    print(request.status_code)
    print(request.text)
    if request.status_code == 201:
        print("Succeeded to create an instance. ID: %s" % instance_id)
        return payload
    else:
        print('Failed to create an instance')


def create_holdings_record(instance_id, sourceId, permanentLocationId):
    payload = {
        'instanceId': instance_id,
        'sourceId': sourceId,
        'permanentLocationId': permanentLocationId,
        'callNumber': 'holdingsCallNumber'
    }

    print('Creating a holdings record...')
    request = folio.post('holdings-storage/holdings', payload)
    if request.status_code == 201:
        holdings_record_id = request.json()['id']
        print("Succeeded to create a holdings record. ID: %s" % holdings_record_id)
        return request.json()
    else:
        print('Failed to create a holdings record')


def get_material_type_id_by_name(name):
    return folio.find_id('material-types', 'name', name, 'mtypes')


def get_loan_type_id_by_name(name):
    return folio.find_id('loan-types', 'name', name, 'loantypes')


def get_service_point_id_by_name(name):
    return folio.find_id('service-points', 'code', name, 'servicepoints')


def get_instance_type_id_by_name(name):
    return folio.find_id('instance-types', 'name', name, 'instanceTypes')


def get_holdings_record_source_id_by_name(name):
    return folio.find_id('holdings-sources', 'name', name, 'holdingsRecordsSources')


def get_location_id_by_name(name):
    return folio.find_id('locations', 'name', name, 'locations')


