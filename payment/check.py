from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
from django.shortcuts import redirect,render,HttpResponse


def gateway(username,user_email):

    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id='ayons64be25828679a', sslc_store_pass='ayons64be25828679a@ssl')

    mypayment.set_urls(success_url='aimaker.com/success', fail_url='aimaker.com/failed', cancel_url='aimaker.com/cancel', ipn_url='aimaker.com/payment_notification')

    mypayment.set_product_integration(total_amount=Decimal(1800.0), currency='BDT', product_category='chatbot', product_name='demo-product', num_of_item=1, shipping_method='NO', product_profile='None')

    mypayment.set_customer_info(name=username, email=user_email, address1='demo address', address2='demo address 2', city='Dhaka', postcode='1207', country='Bangladesh', phone='01711111111')

    # mypayment.set_shipping_info(shipping_to='demo customer', address='demo address', city='Dhaka', postcode='1209', country='Bangladesh')
    # If you want to post some additional values

    # mypayment.set_additional_values(value_a='cusotmer@email.com', value_b='portalcustomerid', value_c='1234', value_d='uuid')

    response_data = mypayment.init_payment()

    # print(response_data['GatewayPageURL'])
    # print(response_data['status'])

    return response_data