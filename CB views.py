from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . import startldap
import time
from . import otpgenerate
from . import passwordchange
from . import ldap_db
from datetime import datetime



def open_chat(request):

    return render(request,'dupli.html')

def get_user_name(request):
    
    if request.method == 'POST':
        user_input = request.POST.get('message', '')
        step = request.POST.get('step', 'start')
        response_data = {'message': '', 'next_step': ''}

        if step == 'start':

            user_input==request.POST.get('value','')
            
            if user_input == 'reset my citrix password':
                
                response_data['message'] = 'Enter your username'
                response_data['next_step'] = 'username'
            else:
                response_data['message'] = 'Enter valid request'
                response_data['next_step'] = 'start'

            
                
        elif step == 'username':
            ldap_user,ldap_user_mail = startldap.start_server(Search=step)
            user_info = request.POST.get('value', '')
            
            if user_info in ldap_user:
                response_data['message'] = 'User Found...Enter your OTP'
                user_dn_name=ldap_user[user_info]
                request.session['user_info']=user_info
                request.session['userdnname']=user_dn_name
                request.session['usermail']=ldap_user_mail[user_info]
                response_data['next_step'] = 'otp'
                system_otp = otpgenerate.generate_otp(ldap_user_mail[user_info])
                request.session['systemotp']=system_otp
                print(system_otp)
            else:
                response_data['message'] = 'User not found..Enter valid user'
                response_data['next_step'] = 'username'
                
        elif step=='otp':
            try:
                user_info = request.session['user_info']
                system_otp = request.session['systemotp']
                
                print(system_otp)
                    
                user_otp = request.POST.get('value', '')     
                if user_otp == system_otp:
                    response_data['message'] = 'OTP is Valid...Enter your password'
                    response_data['next_step'] = 'password'
                else:
                    response_data['message'] = 'Invalid OTP....Enter OTP again'
                    response_data['next_step'] = 'otp'
            except Exception as e:
                print(e)

        elif step=='password':
            try:      
                new_passowrd = request.POST.get('value', '')     
                request.session['newpassword']=new_passowrd
                response_data['message'] = 'please confirm your password'
                response_data['next_step'] = 'confirm_password'
            except Exception as e:
                print(e)

        elif step=='confirm_password':

            try:  
                new_passowrd=request.session['newpassword'] 
                confirm_passowrd = request.POST.get('value', '')     
                if confirm_passowrd==new_passowrd:
                    response_data['message'] = 'password Matched'
                    time.sleep(2)
                    try:
                        user_dn_name=request.session['userdnname']
                        result=passwordchange.change_password(user_dn_name,new_passowrd)
                        response_data['message'] = "password successfully changed"
                        user_info=request.session['user_info']
                        user_mail=request.session['usermail']
                        response_data['next_step']='start'
                        ldap_db.ldap_reset_details(user_info,user_mail,status='success')

                    except Exception as e:
                        ldap_db.ldap_reset_details(emp_id=user_info,emp_mail=user_mail,status='failed')
                        response_data['message'] = 'Failed'
                        
                else:
                    response_data['message']='password Not Matched..Please Enter password again'
                    response_data['next_step']='confirm_password'

            except Exception as e:
                print(e)
                

        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
