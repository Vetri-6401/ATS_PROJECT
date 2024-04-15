from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


def open_chat(request):

    return render(request,'index.html')

def get_user_input_view(request):
    if request.method == 'POST':
        msg = request.POST.get('msg', '')
        response_data = {f'{msg}': 'Response from server'}
        return HttpResponse(response_data)
    else:
        # Handle other HTTP methods, such as GET
        return JsonResponse({'error': 'Method not allowed'}, status=405)
