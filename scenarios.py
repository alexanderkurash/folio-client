import inventory
import circulation
import users
import patron


def create_instance_with_multiple_items(number_of_loans, title, item_barcode_prefix, material_type_name,
                                        permanent_loan_type_name, instance_type_name, holdings_record_source_name,
                                        location_name):

    material_type_id = inventory.get_material_type_id_by_name(material_type_name)
    if material_type_id is not None:
        print('Material type ID: %s' % material_type_id)
    else:
        print('Failed to find material type %s' % material_type_name)
        return

    permanent_loan_type_id = inventory.get_loan_type_id_by_name(permanent_loan_type_name)
    if permanent_loan_type_id is not None:
        print('Permanent loan type ID: %s' % permanent_loan_type_id)
    else:
        print('Failed to find loan type %s' % permanent_loan_type_name)
        return

    instance_type_id = inventory.get_instance_type_id_by_name(instance_type_name)
    if instance_type_id is not None:
        print('Instance type ID: %s' % instance_type_id)
    else:
        print('Failed to find instance type %s' % instance_type_name)
        return

    source_id = inventory.get_holdings_record_source_id_by_name(holdings_record_source_name)
    if source_id is not None:
        print('Holdings record source ID: %s' % source_id)
    else:
        print('Failed to find holdings record source %s' % holdings_record_source_name)
        return

    permanent_location_id = inventory.get_location_id_by_name(location_name)
    if permanent_location_id is not None:
        print('Permanent location ID: %s' % permanent_location_id)
    else:
        print('Failed to find location %s' % location_name)
        return

    instance = inventory.create_instance(title, instance_type_id)
    holdings_record = inventory.create_holdings_record(instance['id'], source_id, permanent_location_id)
    holdings_record_id = holdings_record['id']

    items = []
    for i in range(1, number_of_loans + 1):
        print('Creating item #%d' % i)

        item_barcode = '%s%d' % (item_barcode_prefix, i)

        item = inventory.create_item({
            'status': {
                'name': 'Available'
            },
            'holdingsRecordId': holdings_record_id,
            'barcode': item_barcode,
            'materialType': {
                'id': material_type_id
            },
            'permanentLoanType': {
                'id': permanent_loan_type_id
            },
            'effectiveShelvingOrder': '%s-callnum' % item_barcode,
            'effectiveCallNumberComponents': {
                'callNumber': '%s-callnum' % item_barcode,
                'prefix': 'pre',
                'suffix': 'suf'
            },
            'itemLevelCallNumber': '%s-callnum' % item_barcode,
            'itemLevelCallNumberPrefix': 'pre',
            'itemLevelCallNumberSuffix': 'suf',
        })
        items.append(item)

    return {
        'instance': instance,
        'holdings_record': holdings_record,
        'items': items
    }


def create_instance_and_holding_record_with_no_items(title, instance_type_name, holdings_record_source_name,
                                                     location_name):

    instance_type_id = inventory.get_instance_type_id_by_name(instance_type_name)
    source_id = inventory.get_holdings_record_source_id_by_name(holdings_record_source_name)
    permanent_location_id = inventory.get_location_id_by_name(location_name)

    instance = inventory.create_instance(title, instance_type_id)
    holdings_record = inventory.create_holdings_record(instance['id'], source_id, permanent_location_id)
    holdings_record_id = holdings_record['id']
    return holdings_record_id


def create_user_and_create_loans(number_of_loans, user_barcode, patron_group, title, item_barcode_prefix,
                                 material_type_name, permanent_loan_type_name, service_point_name, instance_type_name,
                                 holdings_record_source_name, location_name):

    inv = create_instance_with_multiple_items(number_of_loans, title, item_barcode_prefix, material_type_name,
                                              permanent_loan_type_name, instance_type_name,
                                              holdings_record_source_name, location_name)

    check_out_service_point_id = inventory.get_service_point_id_by_name(service_point_name)
    if check_out_service_point_id is not None:
        print('Check out service point ID: %s' % check_out_service_point_id)
    else:
        print('Failed to find service point %s' % service_point_name)
        return

    user = users.get_or_create_user_by_barcode(user_barcode, '%s-fn' % user_barcode, '%s-ln' % user_barcode,
                                               '%s@epam.com' % user_barcode, patron_group)
    if user is not None:
        print('Found user %s, ID: %s' % (user_barcode, user['id']))
    else:
        print('Failed to find or create user')
        return

    for item in inv['items']:
        circulation.check_out(item['barcode'], user['barcode'], check_out_service_point_id)


def create_instance_request(user_barcode, patron_group, instance_id, pickup_location_name):
    user = users.get_or_create_user_by_barcode(user_barcode,
                                               '%s-firstname' % user_barcode,
                                               '%s-lastname' % user_barcode,
                                               '%s@epam.com' % user_barcode,
                                               patron_group)

    pickup_location_id = inventory.get_service_point_id_by_name(pickup_location_name)
    request_creation_result = patron.create_instance_request(user['id'], instance_id, pickup_location_id)
    print(request_creation_result)
    return request_creation_result


def create_and_cancel_instance_request(user_barcode, patron_group, instance_id, pickup_location_name):
    user = users.get_or_create_user_by_barcode(user_barcode,
                                               '%s-firstname' % user_barcode,
                                               '%s-lastname' % user_barcode,
                                               '%s@epam.com' % user_barcode,
                                               patron_group)
    pickup_location_id = inventory.get_service_point_id_by_name(pickup_location_name)
    request = patron.create_instance_request(user['id'], instance_id, pickup_location_id)
    print(request)

    cancelled_request = patron.cancel_instance_request(request, user)
    print(cancelled_request)


def create_multiple_ilrs(number_of_requests, user_barcode, patron_group, title, item_barcode_prefix,
                         material_type_name, permanent_loan_type_name, pickup_location_name, instance_type_name,
                         holdings_record_source_name, location_name):

    inv = create_instance_with_multiple_items(number_of_requests, title, item_barcode_prefix, material_type_name,
                                              permanent_loan_type_name, instance_type_name,
                                              holdings_record_source_name, location_name)

    pickup_location_id = inventory.get_service_point_id_by_name(pickup_location_name)

    user = users.get_or_create_user_by_barcode(user_barcode, '%s-fn' % user_barcode, '%s-ln' % user_barcode,
                                               '%s@epam.com' % user_barcode, patron_group)

    for item in inv['items']:
        print('Creating request for item %s' % item['barcode'])
        instance = inv['instance']
        holdings_record = inv['holdings_record']
        circulation.create_ilr(user['id'], 'Page', instance['id'], holdings_record['id'], item['id'], 'Hold Shelf',
                               pickup_location_id)


def exp():
    print(inventory.get_material_type_id_by_name('book'))
    print(users.get_patron_group_id_by_name('Staff'))
