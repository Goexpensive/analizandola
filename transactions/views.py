from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from transactions.models import Transaction
from mercadopago.mercadopago import *


class TransactionView(View):
	model = Transaction
	template_name = 'lista_de_pruebas.html'

	def get(self, request, **kwargs):
	    mp = MP("client_id", "client_secret")
	    paymentInfo = mp.get_payment_info (request.GET["id"])
	    
	    if paymentInfo["status"] == 200:
	    	return render(request, self.template_name, {'Status': paymentInfo['status'],'Response': paymentInfo['response']})
	    else:
	        return render(request, self.template_name, {'Status': paymentInfo['status'],'Response': paymentInfo['response']})

