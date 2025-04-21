urlpatterns += i18n_patterns(
    path('prefixed/', view, name='prefixed'),
    path('prefixed.xml', view, name='prefixed_xml'),
    re_path(_(r'^users/$'), view, name='users'),
    re_path(_(r'^account/'), include('i18n.patterns.urls.namespace', namespace='account')),
)