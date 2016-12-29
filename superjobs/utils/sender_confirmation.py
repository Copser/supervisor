# utils/sender_confirmation.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from twilio.rest import TwilioRestClient
from django_twilio.utils import discover_twilio_credentials



my_user = User.objects.get(pk=USER_ID)

account_id, auth_token = discover_twilio_credentials(my_user)

twilio_client = TwilioRestClient(account_id, auth_token)
