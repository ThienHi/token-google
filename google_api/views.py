from rest_framework import generics
from rest_framework.response import Response
from django.conf import settings
from django.shortcuts import redirect
import google.oauth2.credentials
import google_auth_oauthlib.flow
import requests
from datetime import timedelta
import datetime

# Client configuration for an OAuth 2.0 web server application
# (cf. https://developers.google.com/identity/protocols/OAuth2WebServer)
CLIENT_CONFIG = {'web': {
    'client_id': settings.GOOGLE_CLIENT_ID,
    # 'project_id': settings.GOOGLE_PROJECT_ID,
    'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
    'token_uri': 'https://www.googleapis.com/oauth2/v3/token',
    'auth_provider_x509_cert_url': 'https://www.googleapis.com/oauth2/v1/certs',
    'client_secret': settings.GOOGLE_CLIENT_SECRET,
    'redirect_uris': settings.GOOGLE_REDIRECT_URIS,
    'javascript_origins': settings.GOOGLE_JAVASCRIPT_ORIGINS
    }}

# This scope will allow the application to manage your calendars
SCOPES = [
    # 'https://www.googleapis.com/auth/userinfo.profile',
    # 'https://www.googleapis.com/auth/fitness.activity.read',
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
    # 'https://www.googleapis.com/auth/fitness.activity.write',
    # 'https://www.googleapis.com/auth/fitness.location.read',
    # 'https://www.googleapis.com/auth/fitness.location.write',
    # 'https://www.googleapis.com/auth/fitness.body.read',
    # 'https://www.googleapis.com/auth/fitness.body.write',
    # 'https://www.googleapis.com/auth/fitness.nutrition.read',
    # 'https://www.googleapis.com/auth/fitness.nutrition.write',
    # 'https://www.googleapis.com/auth/fitness.blood_pressure.read',
    # 'https://www.googleapis.com/auth/fitness.blood_pressure.write',
    # 'https://www.googleapis.com/auth/fitness.blood_glucose.read',
    # 'https://www.googleapis.com/auth/fitness.blood_glucose.write',
    # 'https://www.googleapis.com/auth/fitness.oxygen_saturation.read',
    # 'https://www.googleapis.com/auth/fitness.oxygen_saturation.write',
    # 'https://www.googleapis.com/auth/fitness.body_temperature.read',
    # 'https://www.googleapis.com/auth/fitness.body_temperature.write',
    # 'https://www.googleapis.com/auth/fitness.reproductive_health.read',
    # 'https://www.googleapis.com/auth/fitness.reproductive_health.write'
]

flow = google_auth_oauthlib.flow.Flow.from_client_config(
    client_config=CLIENT_CONFIG,
    scopes=SCOPES
)

class GetAccount(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):

        flow.redirect_uri = 'https://herbalife-dev.vracex.com'
        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true')

        return Response(authorization_url)


class AuthAccount(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        print('======================================')
        code = request.data.get('code')
        flow.redirect_uri = 'https://herbalife-dev.vracex.com'
        print(code)
        # code = input('Enter the authorization code: ')
        a = flow.fetch_token(code=code)
        print(a)
        print("++++++++++++++++++++++++++++")
        session = flow.authorized_session()
        print(session)
        print("++++++++++++++++++++++++++++")
        res = session.get('https://www.googleapis.com/oauth2/v2/userinfo')
        r = res.json()
        print(r)


        return Response(r)

class Activity(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        td = timedelta(milliseconds=1628006100000)
        print(str(td))
        s = 1628006100000 /1000
        dt = datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S')
        
        # dt = datetime.datetime.strptime(str(td), "%Y-%m-%d %H:%M:%S")
        # dt = datetime.datetime.fromtimestamp(td)

        return Response(dt)