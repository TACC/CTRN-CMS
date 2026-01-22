from django.urls import path, include

custom_urls = [

    path('example_app/', include('apps.example_app.urls', namespace='example_app')),

    # To support `taggit_autosuggest` (from `djangocms-blog`)
    re_path(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),

]
