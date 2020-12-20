from django.urls import path

from client_front.view.api.auth.auth_api_view import client_auth_api_view
from client_front.view.index_view import IndexView
from client_front.view.auth_view import AuthView, client_logout
from client_front.view.schema_create_view import SchemaCreateView
from client_front.view.schema_data_sets_download_view import do_download_dataset_file_view
from client_front.view.schema_data_sets_generate_view import do_generate_dataset_file_view
from client_front.view.schema_data_sets_view import DataSetsView
from client_front.view.schema_delete_view import do_remove_schema
from client_front.view.schema_edit_view import SchemaEditView, create_column_for_scheme, remove_column_in_scheme


app_name = 'client_front'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('schema/', SchemaCreateView.as_view(), name='schema_new'),
    path('schema/<int:schema_pk>/edit', SchemaEditView.as_view(), name='schema_edit'),
    path('schema/<int:schema_pk>/remove', do_remove_schema, name='schema_remove'),
    path('schema/<int:schema_pk>/column_new', create_column_for_scheme, name='schema_new_column'),
    path('schema/<int:schema_pk>/column_remove', remove_column_in_scheme, name='schema_remove_column'),
    path('schema/<int:schema_pk>/data-sets', DataSetsView.as_view(), name='schema_data_sets'),
    path('schema/<int:schema_pk>/data-sets/generate', do_generate_dataset_file_view, name='schema_data_sets_generate'),
    path('schema/<int:schema_pk>/data-sets/<int:data_pk>/download', do_download_dataset_file_view,
         name='data_sets_download'),

    # Auth url
    path('auth', AuthView.as_view(), name='client_auth'),
    path('auth/logout', client_logout, name='client_logout'),

    # Url for api
    path('api/v1/auth/', client_auth_api_view, name='client_auth_api'),
]
