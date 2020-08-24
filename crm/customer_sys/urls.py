from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="app"),

    # Customer Routes
    path('newcontact/', views.newContact, name="newContact"),
    path('createcustomer/', views.createCustomer, name="createCustomer"),
    path('customer/<int:cust_id>', views.customerPage, name="customerPage"),
    path('editcustomer/<int:cust_id>', views.customerEdit, name="customerEdit"),
    path('deletecustomer/<int:cust_id>/', views.customerDelete, name="customerDelete"),

    # Note Routes
    path('addnote/', views.addNote, name="addNote"),
    path('deletenote/<int:note_id>/<int:cust_id>', views.deleteNote, name="deleteNote"),

    # Party Routes
    path('newparty/', views.newParty, name="newParty"),
    path('createparty/', views.createParty, name="createParty"),
    path('party/<int:party_id>', views.partyPage, name="partyPage"),
    path('editparty/<int:party_id>', views.partyEdit, name="partyEdit"),
    path('deleteparty/<int:party_id>/', views.deleteParty, name="deleteParty"),
]