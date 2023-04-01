from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json
import requests
from django.http import JsonResponse

def get_address(request, address):
    # Código para procesar la solicitud y devolver una respuesta    
    return HttpResponse(get_contract_abi())

def get_user(request, user):
    # Código para procesar la solicitud y devolver una respuesta


    return HttpResponse("El usuario es: " + user)





#def my_view(request):
#    url = 'https://api.etherscan.io/api?module=contract&action=getabi&address=0xcbb011006eadd48a241eca39181be7834b93dd0b&apikey=NPBZKN6D9KNB29PF7YN4HJFEH7QRB5T4ZF'
#    response = requests.get(url)
#    data = json.loads(response.content)
#
#    if data['status'] == '1':
#        # Do something when status is true
#        return JsonResponse({'message': 'Verified Contract'})
#
#    elif data['status'] == '0':
#        # Do something when status is false
#        return JsonResponse({'message': 'Not Verified Contract'})
#
#    else:
#        # Handle other status values
#        return JsonResponse({'message': 'Unknown API status'})


def get_contract_abi():
    # Replace with your API key
    api_key = 'NPBZKN6D9KNB29PF7YN4HJFEH7QRB5T4ZF'

    # Replace with the contract address you want to get the ABI for
    contract_address = '0xe11271c1ff2c95e5b4cf41fc487c162a13dce01b'

    # Make a GET request to the API endpoint
    url = f'https://api.etherscan.io/api?module=contract&action=getsourcecode&address={contract_address}&apikey={api_key}'
    response = requests.get(url)

    # Parse the JSON response
    data = json.loads(response.content)

    # Check the API status
    if data['status'] == '1':
        # Get the ABI from the API response
        abi = data['result'][0]['SourceCode']
        print('Verified')
        # Return the ABI as a JSON response
        return JsonResponse({'abi': abi})

    else:
        # Handle the case where the API status is not 1
        print('Not Verified')
        return JsonResponse({'message': 'Unable to get contract ABI'})
