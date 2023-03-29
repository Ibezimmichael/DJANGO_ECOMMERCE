from django.shortcuts import render, redirect

from . import forms
from payment.models import Order, OrderItem

from payment.forms import ShippingForm
from payment.models import ShippingAddress

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login 
from django.contrib.sites.shortcuts import get_current_site
from .token import user_tokenizer_generate

from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from django.contrib import messages
# Create your views here.



def register(request):
    form = forms.CreateUserForm()
    if request.method == 'POST':
        form = forms.CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            

            # Email verification setup (template)

            current_site = get_current_site(request)
            subject = "Account verification email"
            message = render_to_string('account/registration/email-verification.html',{
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': user_tokenizer_generate.make_token(user)
            })

            user.email_user(subject=subject, message=message)



            return redirect('email-verification-sent')

    context = {'form':form}

    return render(request, 'account/registration/register.html', context=context)    


def email_verification(request, uidb64, token):
    unique_id = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=unique_id)

    if user and user_tokenizer_generate.check_token(user, token):
        user.is_active = True
        user.save()

        return redirect('email-verification-success')
    else:
        return redirect('email-verification-failed')


def email_verification_sent(request):

    return render(request, 'account/registration/email-verification-sent.html')
 

def email_verification_success(request):
    return render(request, 'account/registration/email-verification-success.html')


def email_verification_failed(request):
    return render(request, 'account/registration/email-verification-failed.html')



def user_login(request):

    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                login(request, user)

                return redirect("dashboard")


    context = {'form':form}

    return render(request, 'account/login.html', context=context)

# @login_required
# def user_logout(request):
#     logout(request)
#     return redirect('store:index')

@login_required
def user_logout(request):
    try:
        for key in list(request.session.keys()):
            if key == 'session_key':
                continue
            else:
                del request.session[key]
    except KeyError:
        pass
    messages.success(request, "Logout success")

    return redirect("store:index")



@login_required(login_url='login')
def dashboard(request):
    return render(request, 'account/dashboard.html')


@login_required(login_url='login')
def profile_mangement(request):
    user_form = forms.UpdateUserForm(instance=request.user)

    if request.method == 'POST':
        user_form = forms.UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.info(request, "Update success!")
            return redirect('dashboard')
    context = {'user_form':user_form}

    return render(request, 'account/profile-management.html', context=context)

@login_required(login_url='login')
def delete_account(request):
    user = User.objects.get(id=request.user.id)

    if request.method == 'POST':
        user.delete()
        messages.error(request, "Account deleted")
        return redirect('store:index')
    return render(request, 'account/delete-account.html')


@login_required(login_url='login')
def manage_shipping(request):

    try:
        # Account user with shipment information
        shipping = ShippingAddress.objects.get(user=request.user.id)

    except ShippingAddress.DoesNotExist:
        # Account user with no shipment information
        shipping = None

    form = ShippingForm(instance=shipping)

    if request.method == 'POST':
        form = ShippingForm(request.POST, instance=shipping)

        if form.is_valid():
            # Assign the user FK on the object
            shipping_user = form.save(commit=False)
            # Adding the FK itself
            shipping_user.user = request.user
            shipping_user.save()
            messages.info(request, "Update success!")

            return redirect('dashboard')

    context = {'form':form}
    return render(request, 'account/manage-shipping.html', context=context)


@login_required(login_url='login')
def track_orders(request):

    try:

        orders = OrderItem.objects.filter(user=request.user)

        context = {'orders':orders}

        return render(request, 'account/track-orders.html', context=context)

    except:

        return render(request, 'account/track-orders.html')
