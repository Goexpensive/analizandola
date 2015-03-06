from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from transactions.models import Transaction
from mercadopago.mercadopago import *
import json


class TransactionView(View):
	model = Transaction
	template_name = 'lista_de_pruebas.html'

	def get(self, request, **kwargs):
	    mp = MP("2393090223886468", "eXxJNpUGgoxbmD84QJbvmNVuI2TKlNQ9")
	    paymentInfo = mp.get_payment_info (request.GET["id"])
	    
	    if paymentInfo["status"] == 200:
	    	json_data = json.dumps(paymentInfo)
	    	HttpResponse(json_data,content_type='application/json')
	    	return HttpResponse(json_data,content_type='application/json')
	    else:
	        paymentInfo['status'] = self.post(request)
	        json_data = json.dumps(paymentInfo)
	        return HttpResponse(json_data,content_type='application/json')
	#Guardar los datos en el modelo.     
	def post(self, request, **kwargs):
			paymentInfo = 'Es un post'
			return paymentInfo
	#Obtener los datos necesarios de la transacción.
	def get_resource_data()
		pass

