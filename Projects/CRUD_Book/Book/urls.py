from django.urls import path
from .import views
urlpatterns = [
    path('viewAll/',views.read_book,name='viewAll'),
    path('addBook/',views.add_book,name='addBook'),
    path('deleteBook/<int:book_id>',views.delete_book,name='deleteBook'),
    path('update/<int:book_id>',views.update,name="update"),
    path('updateRecord/<int:book_id>',views.updateRecord,name="updateRecord"),
]