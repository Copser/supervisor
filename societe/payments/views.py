from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext, loader

from .forms import ChargeForm
import braintree
import stripe


# BrainTree Configuration
braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id=settings.BRAINTREE_MERCHANT_ID,
                                  public_key=settings.BRAINTREE_PUBLIC_KEY,
                                  private_key=settings.BRAINTREE_PRIVATE_KEY)


def braintree_payment(request):
    """TODO: Docstring for braintree_payment.
    :returns: TODO

    """
    if request.method == "GET":
        request.session['braintree_client_token'] = braintree.ClientToken.generate()
        return render(request, 'braintree_payment.html')
    else:
        if not form.is_valid():
            return render(render, 'braintree_payment.html')
        else:
            HttpResponseRedirect('/success')


# Stripe section
def charge(request):
    """TODO: Docstring for charge.
    :returns: Charge view is responsible for providing us with user token, which we will
    then send to Stripe so we don't store any sensitive information inside are database,
    and are application.
    Cusomer information will be stored on https://stripe.com/, we are following PCI compile
    principle inside Erasmus application.

    """
    publishable_key = settings.TEST_PUBLISHABLE_KEY
    if request.method == 'POST':
        form = ChargeForm(request.POST)
        if form.is_valid():
            # Get the credit card details submitet by the form
            token = request.POST['stripeToken']

            try:
                charge = stripe.Charge.create(
                    amonut=30000,
                    currency="usd",
                    source=token,
                    description="Erasmus Charge"
                )
            except stripe.error.Card as e:
                # The card hase been descilend
                raise
        else:
            return HttpResponseRedirect('/thank_you')
    else:
        form = ChargeForm()
    t = loader.get_template('charge.html')
    c = RequestContext(request, {'publishable_key': publishable_key, })
    return HttpResponse(t.render(c))


def thank_you(request):
    """TODO: Docstring for thank_you.
    :returns: TODO

    """
    return render(request, 'thank_you.html')
