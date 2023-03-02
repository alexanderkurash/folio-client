import folio
import scenarios

folio.login()

test_num = 1

# for Snapshot
# scenarios.create_user_and_create_loans(number_of_loans=0,
#                                        user_barcode='fcu-%d' % test_num,
#                                        patron_group='staff',
#                                        title='FC %d' % test_num,
#                                        item_barcode_prefix='fci-%d-' % test_num,
#                                        material_type_name='video recording',
#                                        permanent_loan_type_name='Can circulate',
#                                        service_point_name='cd1',
#                                        instance_type_name='text',
#                                        holdings_record_source_name='FOLIO',
#                                        location_name='Main Library')
# scenarios.create_user_and_create_loans(number_of_loans=1,
#                                        user_barcode='fcu-%d' % test_num,
#                                        patron_group='staff',
#                                        title='FC %d' % test_num,
#                                        item_barcode_prefix='fci-%d-' % test_num,
#                                        material_type_name='video recording',
#                                        permanent_loan_type_name='Can circulate',
#                                        service_point_name='cd1',
#                                        instance_type_name='text',
#                                        holdings_record_source_name='FOLIO',
#                                        location_name='testloc')

# scenarios.create_instance_and_holding_record_with_no_items(title='FC %d' % test_num,
#                                                            instance_type_name='text',
#                                                            holdings_record_source_name='FOLIO',
#                                                            location_name='Main Library')

# for MG BugFest
# scenarios.create_user_and_create_loans(number_of_loans=3,
#                                        user_barcode='1000000001',
#                                        patron_group='ak-test',
#                                        title='FC %d' % test_num,
#                                        item_barcode_prefix='fc-%d-' % test_num,
#                                        material_type_name='video recording',
#                                        permanent_loan_type_name='Can circulate',
#                                        service_point_name='aksp1',
#                                        instance_type_name='text',
#                                        holdings_record_source_name='FOLIO',
#                                        location_name='ak-loc')

# for Lotus BugFest
# scenarios.create_user_and_create_loans(number_of_loans=1,
#                                        user_barcode='1000000001',
#                                        patron_group='ak-test',
#                                        title='Title 1569 %d' % test_num,
#                                        item_barcode_prefix='1569-%d-' % test_num,
#                                        material_type_name='video recording',
#                                        permanent_loan_type_name='Can circulate',
#                                        service_point_name='ak-sp',
#                                        instance_type_name='text',
#                                        holdings_record_source_name='FOLIO',
#                                        location_name='ak-loc')

# for Nolana BugFest
# scenarios.create_user_and_create_loans(number_of_loans=1,
#                                        user_barcode='1000000002',
#                                        patron_group='ak-test',
#                                        title='Title 1655 %d' % test_num,
#                                        item_barcode_prefix='1655-%d-' % test_num,
#                                        material_type_name='video recording',
#                                        permanent_loan_type_name='Can circulate',
#                                        service_point_name='aksp1',
#                                        instance_type_name='text',
#                                        holdings_record_source_name='FOLIO',
#                                        location_name='ak-loc')

# scenarios.exp()

scenarios.create_and_cancel_instance_request(user_barcode='fcu-%d' % test_num,
                                             patron_group='staff',
                                             instance_id='14842f25-3a63-4e9d-b501-51776963552e',
                                             pickup_location_name='cd1')

