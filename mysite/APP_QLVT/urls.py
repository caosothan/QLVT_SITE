

from django.urls import path
from .main.main import main , main_when_get_Data, search_records, update_record, add_record, delete_record, import_file, export_file
from tkinter.filedialog import askdirectory

app_name = "APP_QLVT"
urlpatterns = [
    path("action/", main), 
    path("action/action-get-data/", main_when_get_Data),
    path("action/find/", search_records),
    path("action/update/", update_record),
    path("action/add/", add_record),
    path("action/delete/", delete_record),
    path("action/import-file/", import_file),
    path("action/export-file/", export_file), 
 






]


