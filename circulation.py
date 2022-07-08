import folio


def check_out(item_barcode, user_barcode, service_point_id):
    print('Checking out an item %s...')
    request = folio.post('circulation/check-out-by-barcode', {'itemBarcode': item_barcode,
                                                              'userBarcode': user_barcode,
                                                              'servicePointId': service_point_id})
    if request.status_code == 201:
        loan_id = request.json()['id']
        print("Succeeded to check out an item. Loan ID: %s" % loan_id)
        return request.json()
    else:
        print('Failed to check out an item')

