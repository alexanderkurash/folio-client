import folio
import scenarios

folio.login()

# for Snapshot
scenarios.create_user_and_create_loans(number_of_loans=2,
                                       user_barcode='10001',
                                       patron_group='staff',
                                       title='title 1575 1',
                                       item_barcode_prefix='1575-1-',
                                       material_type_name='video recording',
                                       permanent_loan_type_name='Can circulate',
                                       service_point_name='cd1',
                                       instance_type_name='text',
                                       holdings_record_source_name='FOLIO',
                                       location_name='Main Library')

# for MG BugFest
# scenarios.create_user_and_create_loans(number_of_loans=2,
#                                        user_barcode='1000000001',
#                                        patron_group='ak-test',
#                                        title='title 1576 3',
#                                        item_barcode_prefix='1576-3-',
#                                        material_type_name='video recording',
#                                        permanent_loan_type_name='Can circulate',
#                                        service_point_name='ak-sp',
#                                        instance_type_name='text',
#                                        holdings_record_source_name='FOLIO',
#                                        location_name='ak-loc')

# scenarios.exp()

