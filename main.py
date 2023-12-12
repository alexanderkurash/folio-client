import folio
import scenarios

# folio.login()
folio.login_with_expiry()

test_id = '1050'

# for Snapshot
# scenarios.create_user_and_create_loans(number_of_loans=100,
#                                        user_barcode='fcu-%s' % test_id,
#                                        patron_group='staff',
#                                        title='FC %s' % test_id,
#                                        item_barcode_prefix='fci-%s-' % test_id,
#                                        material_type_name='video recording',
#                                        permanent_loan_type_name='Can circulate',
#                                        service_point_name='cd1',
#                                        instance_type_name='text',
#                                        holdings_record_source_name='FOLIO',
#                                        location_name='Main Library')

# scenarios.create_instance_and_holding_record_with_no_items(title='FC %d' % test_num,
#                                                            instance_type_name='text',
#                                                            holdings_record_source_name='FOLIO',
#                                                            location_name='Main Library')

# for BugFest
scenarios.create_user_and_create_loans(number_of_loans=100,
                                       user_barcode='fcu-%s' % test_id,
                                       patron_group='staff',
                                       title='FC-AK test title %s' % test_id,
                                       item_barcode_prefix='fci-%s-' % test_id,
                                       material_type_name='video recording',
                                       permanent_loan_type_name='Can circulate',
                                       service_point_name='aksp1',
                                       instance_type_name='text',
                                       holdings_record_source_name='FOLIO',
                                       location_name='ak-loc')

# scenarios.create_multiple_ilrs(number_of_requests=500,
#                                user_barcode='fcu-%s' % test_id,
#                                patron_group='staff',
#                                title='FC-AK test title %s' % test_id,
#                                item_barcode_prefix='fci-%s-' % test_id,
#                                material_type_name='video recording',
#                                permanent_loan_type_name='Can circulate',
#                                pickup_location_name='aksp1',
#                                instance_type_name='text',
#                                holdings_record_source_name='FOLIO',
#                                location_name='ak-loc')

# scenarios.create_instance_request('fcu-1', 'staff', '')


# scenarios.exp()

# scenarios.create_and_cancel_instance_request(user_barcode='fcu-%d' % test_num,
#                                              patron_group='staff',
#                                              instance_id='14842f25-3a63-4e9d-b501-51776963552e',
#                                              pickup_location_name='cd1')

