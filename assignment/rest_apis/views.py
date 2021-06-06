from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def validate_numeric_entity(request):

    if request.method == 'POST':
        request2 = request.data
        try:
            if request2['pick_first']:

                x= request2["values"][0]["value"]
                evaluation = eval(request2['constraint'])
                
                if evaluation:
                    data =  {"filled": True,"partially_filled": False,"trigger": '',"parameters": {"ids_stated": request2["values"][0]["value"]}}
                else:
                    data = {"filled": False,"partially_filled": False,"trigger": 'invalid_ids_stated',"parameters":{}}
            else:

                out_arr = []
                for i in request2["values"]:
                    x= i["value"]
                    out = eval(request2['constraint'])
                    if out:
                        out_arr.append(i["value"])
                
                if len(out_arr)>0:
                    if len(out_arr)==len(request2['values']):
                        filled=True
                        partially_filled = False
                        data = {"filled": filled,"partially_filled": partially_filled,"trigger": '',"parameters": {"ids_stated": out_arr}}
                    else:
                        filled=False
                        partially_filled = True            
                        data = {"filled": filled,"partially_filled": partially_filled,"trigger": 'invalid_ids_stated',"parameters": {}}
                else:
                    data = {"filled": False,"partially_filled": False,"trigger": 'invalid_ids_stated',"parameters": {}}
        except Exception as e:
            print(e)
            data = {"filled": False,"partially_filled": False,"trigger": 'invalid_ids_stated',"parameters": {}}

        return Response(data, status=status.HTTP_200_OK)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        data= {'status':False, 'message':'Incorrect method used'}
        return Response(data, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def validate_finite_values_entity(request):
    if request.method=='POST':
        request1 = request.data
        try:
            if request1['pick_first']:
                if request1['values'][0]['value'] in request1['supported_values']:
                    data = {"filled": True,"partially_filled": False,"trigger": '',"parameters": {"ids_stated":request1['values'][0]['value'] }}
                else:
                    data = {"filled": False,"partially_filled": False,"trigger": 'invalid_ids_stated',"parameters": {}}

            else:
                if request1['support_multiple']:
                    out_arr = []
                    for i in request1['values']:
                        if i['value'] in request1['supported_values']:
                            out_arr.append(i['value'])
                            
                    if len(out_arr)>0:
                        if len(out_arr)==len(request1['values']):
                            filled=True
                            partially_filled = False
                            data = {"filled": filled,"partially_filled": partially_filled,"trigger": '',"parameters": {"ids_stated": out_arr}}
                        else:
                            filled=False
                            partially_filled = True
                            out_arr = 'invalid_ids_stated'                    
                            data = {"filled": filled,"partially_filled": partially_filled,"trigger": 'invalid_ids_stated',"parameters": {}}
                    else:
                        data = {"filled": False,"partially_filled": False,"trigger": 'invalid_ids_stated',"parameters": {}}
        except:
            data = {"filled": False,"partially_filled": False,"trigger": 'invalid_ids_stated',"parameters": {}}
        return Response(data, status=status.HTTP_200_OK)

        