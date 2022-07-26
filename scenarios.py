import inventory
import circulation
import users


def create_user_and_items(number_of_items):
    material_type_id = '1a54b431-2e4f-452d-9cae-9cee66c9a892'
    permanent_loan_type = '2b94c631-fca9-4892-a730-03ee529ffe27'
    service_point_id = '7c5abc9f-f3d7-4856-b8d7-6712462ca007'
    instance_type_id = 'a2c91e87-6bab-44d6-8adb-1fd02481fc4f'
    source_id = 'f32d531e-df79-46b3-8932-cdd35f7a2264'
    permanent_location_id = 'fcd64ce1-6995-48f0-840e-89ffa2288371'

    user = users.create_user('FolioClientFirst', 'FolioClientLast', 'ak2', 'folioclient@epam.com')
    instance = inventory.create_instance('test1432', instance_type_id)
    holdings_record = inventory.create_holdings_record(instance['id'], source_id, permanent_location_id)

    holdings_record_id = holdings_record['id']

    for i in range(1, number_of_items + 1):
        print('Creating item #%d' % i)

        item_barcode = '10000%d' % i

        inventory.create_item({
            'status': {
                'name': 'Available'
            },
            'holdingsRecordId': holdings_record_id,
            'barcode': item_barcode,
            'materialType': {
                'id': material_type_id
            },
            'permanentLoanType': {
                'id': permanent_loan_type
            }
        })


def create_user_and_create_loans(user_barcode, title, item_barcode_prefix, number_of_loans):
    material_type_id = '1a54b431-2e4f-452d-9cae-9cee66c9a892'
    permanent_loan_type = '2b94c631-fca9-4892-a730-03ee529ffe27'
    service_point_id = '7c5abc9f-f3d7-4856-b8d7-6712462ca007'
    instance_type_id = 'a2c91e87-6bab-44d6-8adb-1fd02481fc4f'
    source_id = 'f32d531e-df79-46b3-8932-cdd35f7a2264'
    permanent_location_id = 'fcd64ce1-6995-48f0-840e-89ffa2288371'

    user = users.create_user('FolioClientFirst', 'FolioClientLast', user_barcode,
                             'folioclient%s@epam.com' % user_barcode)

    instance = inventory.create_instance(title, instance_type_id)
    holdings_record = inventory.create_holdings_record(instance['id'], source_id, permanent_location_id)

    holdings_record_id = holdings_record['id']

    for i in range(1, number_of_loans + 1):
        print('Creating loan #%d' % i)

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
                'id': permanent_loan_type
            }
        })

        circulation.check_out(item['barcode'], user['barcode'], service_point_id)


# def create_loans(user_barcode, item_barcode_prefix, number_of_loans):
#     material_type_id = '1a54b431-2e4f-452d-9cae-9cee66c9a892'
#     permanent_loan_type = '2b94c631-fca9-4892-a730-03ee529ffe27'
#     service_point_id = '7c5abc9f-f3d7-4856-b8d7-6712462ca007'
#     instance_type_id = 'a2c91e87-6bab-44d6-8adb-1fd02481fc4f'
#     source_id = 'f32d531e-df79-46b3-8932-cdd35f7a2264'
#     permanent_location_id = 'fcd64ce1-6995-48f0-840e-89ffa2288371'
#
#     user = users.create_user('FolioClientFirst', 'FolioClientLast', user_barcode,
#                              'folioclient%s@epam.com' % user_barcode)
#
#     instance = inventory.create_instance(title, instance_type_id)
#     holdings_record = inventory.create_holdings_record(instance['id'], source_id, permanent_location_id)
#
#     holdings_record_id = holdings_record['id']
#
#     for i in range(1, number_of_loans + 1):
#         print('Creating loan #%d' % i)
#
#         item_barcode = '%s%d' % (item_barcode_prefix, i)
#
#         item = inventory.create_item({
#             'status': {
#                 'name': 'Available'
#             },
#             'holdingsRecordId': holdings_record_id,
#             'barcode': item_barcode,
#             'materialType': {
#                 'id': material_type_id
#             },
#             'permanentLoanType': {
#                 'id': permanent_loan_type
#             }
#         })
#
#         circulation.check_out(item['barcode'], user['barcode'], service_point_id)
