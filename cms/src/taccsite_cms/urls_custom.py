from django.urls import path, re_path, include

custom_urls = [

    path('example_app/', include('apps.example_app.urls', namespace='example_app')),

    # DJANGO
    # To allow CMS user to change or reset password
    # TODO: Make CMS-only Portal Use TAPIs Auth & Do Not Do This
    path('accounts/', include('django.contrib.auth.urls')),

]
