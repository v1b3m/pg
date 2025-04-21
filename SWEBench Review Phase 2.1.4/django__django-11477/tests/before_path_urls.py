    path('users/<id>/', views.empty_view, name='user-with-id'),
    path('included_urls/', include('urlpatterns.included_urls')),
    re_path(r'^regex/(?P<pk>[0-9]+)/$', views.empty_view, name='regex'),
    path('', include('urlpatterns.more_urls')),
    path('<lang>/<path:url>/', views.empty_view, name='lang-and-path'),
]