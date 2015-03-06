from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.models import User
from transactions.models import Transaction
from user_profiles.models import UserProfile
from mercadopago.mercadopago import *
import dateutil.parser
import json


class TransactionView(View):
	model = Transaction
	template_name = 'lista_de_pruebas.html'

	def get(self, request, **kwargs):
	    data = self.get_resource_data(self.request)
	    json_data = self.post(data=data)

	    return HttpResponse(json_data,content_type='application/json')
	    
	
	def post(self, **kwargs):
			tx = Transaction()
			data = kwargs.get('data')
			userP = UserProfile.objects.get(user_external_reference=data['user_id'])
			data['user_id'] = userP.user
			field_names = [name for name in tx._meta.get_all_field_names() if name in data]

			for name in field_names:
				setattr(tx, name, data[name])
			tx.save()	

			return tx

	def get_resource_data(self,request):
		
		mp = MP("2393090223886468", "eXxJNpUGgoxbmD84QJbvmNVuI2TKlNQ9")
		paymentInfo = mp.get_payment_info (request.GET["id"])
		data = paymentInfo
	    
		if paymentInfo["status"] == 200:
			data = {'date_created'       : dateutil.parser.parse(paymentInfo["response"]["collection"]["date_created"]),	
					'last_modified_date' : dateutil.parser.parse(paymentInfo["response"]["collection"]["last_modified"]),
					'user_id'            : paymentInfo["response"]["collection"]["collector"]["id"],
					'buyer'              : paymentInfo["response"]["collection"]["payer"]["id"],
					'transaction_id'     : paymentInfo["response"]["collection"]["id"],
					'status'             : paymentInfo["response"]["collection"]["status"],
					'status_detail'      : paymentInfo["response"]["collection"]["status_detail"],
					'transaction_type'   : paymentInfo["response"]["collection"]["operation_type"],
					'marketplace'        : paymentInfo["response"]["collection"]["marketplace"],
					'amount'             : paymentInfo["response"]["collection"]["transaction_amount"],
					}

		return data


