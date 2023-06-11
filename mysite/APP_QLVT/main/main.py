
from django.http import HttpResponse
from django.template import Template, Context
from django import forms
from django.shortcuts import render
from APP_QLVT.models import QLVT_Data
from django.db import models
import pandas as pd
import csv




# Lớp dành cho export file dùng để tạo trường dữ liệu để chọn folder chứa file cần xuất.
# folder cho phép chỉ nằm trong C:/Users/Admin như trường hợp ở dưới. Có thể thay đổ đường dẫn ở phía dưới path=''
class FileDownLoad(forms.Form):
    FolderPath = forms.FilePathField(path = "C:/Users/Admin" ,allow_folders = True, allow_files = False)


#Lớp tạo trường dữ liệu để chọn file tải lên dành cho import file
class FileUPLoad(forms.Form):
    FilePath = forms.FileField()


respone = None
record_list_parent = []

#Hàm sau thực hiện khi vừa đăng nhập vào
def main(request): 
    respone = HttpResponse()
    template_string = open("APP_QLVT/staticfiles/main.html", 'r', encoding = "utf-8").read()
    t = Template(template_string)
    respone.content = t.render(Context({'link_logout': '/logout/' ,'up_load_file': FileUPLoad(), 'down_load_file': FileDownLoad()}))
    return respone



# Hàm sau thực hiện lấy bản bản ghi từ csdl QLVT_Data
def main_when_get_Data(request, file = None, file1 = None): 
    respone = HttpResponse()
    template_string = open("APP_QLVT/staticfiles/main.html", 'r', encoding = "utf-8").read()
    t = Template(template_string)

    record_list0 = []
    records0 = QLVT_Data.objects.values('id')
    for record in records0:
        record_list0.append(record.get('id'))

    record_list1 = []
    records1 = QLVT_Data.objects.values('[Tên thiết bị]')
    for record in records1:
        record_list1.append(record.get("[Tên thiết bị]"))

    records2 = QLVT_Data.objects.values('[Số Serial]')
    record_list2 = []
    for record in records2:
        record_list2.append(record.get("[Số Serial]"))
    
    records3 = QLVT_Data.objects.values('[Phân loại]')
    record_list3 = []
    for record in records3:
        record_list3.append(record.get("[Phân loại]"))

    records4 = QLVT_Data.objects.values('[Nhà sản xuất]')
    record_list4 = []
    for record in records4:
        record_list4.append(record.get("[Nhà sản xuất]"))

    records5 = QLVT_Data.objects.values('[Đài Viễn Thông/Điều hành/Vô Tuyến]')
    record_list5 = []
    for record in records5:
        record_list5.append(record.get("[Đài Viễn Thông/Điều hành/Vô Tuyến]"))

    records6 = QLVT_Data.objects.values('[Ngày ĐV QLSDTS gửi yêu cầu SC]')
    record_list6 = []
    for record in records6:
        record_list6.append(record.get("[Ngày ĐV QLSDTS gửi yêu cầu SC]"))

    records7 = QLVT_Data.objects.values('[Ngày CN hoàn thành phân loại kiểm tra tại ĐV QLSDTS]')
    record_list7 = []
    for record in records7:
        record_list7.append(record.get("[Ngày CN hoàn thành phân loại kiểm tra tại ĐV QLSDTS]"))

    records8 = QLVT_Data.objects.values("[Tình trạng tiếp nhận tại ĐV QLSDTS] ")
    record_list8 = []
    for record in records8:
        record_list8.append(record.get("[Tình trạng tiếp nhận tại ĐV QLSDTS] "))

    records9 = QLVT_Data.objects.values('[Ngày CN  gửi kế hoạch vận chuyển]')
    record_list9 = []
    for record in records9:
        record_list9.append(record.get("[Ngày CN  gửi kế hoạch vận chuyển]"))

    records10 = QLVT_Data.objects.values('[Ngày P.KT ĐV QLSDTS gửi phiếu xuất kho]')
    record_list10 = []
    for record in records10:
        record_list10.append(record.get('[Ngày P.KT ĐV QLSDTS gửi phiếu xuất kho]'))

    records11 = QLVT_Data.objects.values('[Ngày giao cho đối tác mang đi SC]')
    record_list11 = []
    for record in records11:
        record_list11.append(record.get("[Ngày giao cho đối tác mang đi SC]"))

    records12 = QLVT_Data.objects.values('[Tình trạng bàn giao đi sửa chữa]')
    record_list12 = []
    for record in records12:
        record_list12.append(record.get("[Tình trạng bàn giao đi sửa chữa]"))

    records13 = QLVT_Data.objects.values('[Ngày CN gửi yêu cầu nhập kho sau SC]')
    record_list13 = []
    for record in records13:
        record_list13.append(record.get("[Ngày CN gửi yêu cầu nhập kho sau SC]"))

    records14 = QLVT_Data.objects.values('[Ngày nhận về từ đối tác sau SC]')
    record_list14 = []
    for record in records14:
        record_list14.append(record.get("[Ngày nhận về từ đối tác sau SC]"))

    records15 = QLVT_Data.objects.values('[Số serial sau SC]')
    record_list15 = []
    for record in records15:
        record_list15.append(record.get("[Số serial sau SC]"))

    records16 = QLVT_Data.objects.values('[Ngày P.KT làm phiếu nhập kho sau SC]')
    record_list16 = []
    for record in records16:
        record_list16.append(record.get("[Ngày P.KT làm phiếu nhập kho sau SC]"))

    records17 = QLVT_Data.objects.values('[Ngày hoàn thành kiểm tra sau SC]')
    record_list17 = []
    for record in records17:
        record_list17.append(record.get("[Ngày hoàn thành kiểm tra sau SC]"))

    records18 = QLVT_Data.objects.values('[Kết quả kiểm tra sau sửa chữa]')
    record_list18 = []
    for record in records18:
        record_list18.append(record.get("[Kết quả kiểm tra sau sửa chữa]"))

    records19 = QLVT_Data.objects.values('[Ngày P.KT gửi phiếu xuất kho trả thiết bị cho ĐV QLSDTS]')
    record_list19 = []
    for record in records19:
        record_list19.append(record.get("[Ngày P.KT gửi phiếu xuất kho trả thiết bị cho ĐV QLSDTS]"))

    records20 = QLVT_Data.objects.values('[Ngày giao tại kho ĐV QLSDTS]')
    record_list20 = []
    for record in records20:
        record_list20.append(record.get("[Ngày giao tại kho ĐV QLSDTS]"))

   
    count = len(QLVT_Data.objects.values('id'))
    for i in range(0, count):
        record_list_parent.append([record_list0[i] ,record_list1[i], record_list2[i], record_list3[i], record_list4[i], record_list5[i], record_list6[i], record_list7[i], record_list8[i], record_list9[i], record_list10[i], record_list11[i], record_list12[i], record_list13[i], record_list14[i], record_list15[i], record_list16[i], record_list17[i], record_list18[i], record_list19[i], record_list20[i]])
    respone.content = t.render(Context({'link_logout': '/logout/' ,"records": show_record_list(record_list_parent), "up_load_file": FileUPLoad() , "down_load_file": FileDownLoad()}))
    return respone


#Hàm ghi dữ liệu lên trang html
#Show các cột
def show_item_record(record):
    context = ""
    for item in record:
        context += "<td style = 'margin-left: 4px'  class = 'p-4' style = 'font-size: smaller'>{}</td>".format(item)
    return context

#Show các hàng
def show_record_list(list_record):
    context = ""
    id = 1
    for record in list_record:
        context += '''<tr class = 'row-4' style = 'border: 2px solid; padding: 10px;' onmouseover = 'mouseoverRecord(this)' onmouseout = 'mouseoutRecord(this)' onclick = "select_record(['{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'])">{}</tr>'''.format(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],show_item_record(record))
    return context





# Tìm kiếm bản ghi
def search_records(request):
    record_find_list = []
    if request.method == "POST":
        field_to_find = request.POST['field-to-find']
        key_to_find = request.POST['key-to-find']

        # Xử lí tìm kiếm
        records = QLVT_Data.objects.filter(['[{}]'.format(field_to_find), key_to_find]).values()
        for record in records:
                record_find_list.append(list(record.values()))
    
    return render(request, "main.html", {'link_logout': '/logout/' ,"record_find_list": show_record_list(record_find_list), "up_load_file": FileUPLoad(), "down_load_file": FileDownLoad() })
    

        

# Cập nhật bản ghi
def update_record(request):
    if request.method == "POST":
        var0 = request.POST['id0']
        if var0 == '':
            return main_when_get_Data(request, file = FileUPLoad())
        else:
            var1 = request.POST['id1']
            var2 = request.POST['id2']
            var3 = request.POST['id3']
            var4 = request.POST['id4']
            var5 = request.POST['id5']
            date1 = request.POST['id6']
            date2 = request.POST['id7']
            var6 = request.POST['id8']
            date3 = request.POST['id9']
            date4 = request.POST['id10']
            date14 = request.POST['id11']
            var8 = request.POST['id12']
            date15 = request.POST['id13']
            date16 = request.POST['id14']
            var9 = request.POST['id15']
            date17 = request.POST['id16']
            date18 = request.POST['id17']
            var10 = request.POST['id18']
            date21 = request.POST['id19']
            date23 = request.POST['id20']
            qlvt_data = QLVT_Data.objects.get(id = var0)
            qlvt_data.var1 = var1
            qlvt_data.var2 = var2
            qlvt_data.var3 = var3
            qlvt_data.var4 = var4
            qlvt_data.var5 = var5
            qlvt_data.date1 = date1
            qlvt_data.date2 = date2
            qlvt_data.var6 = var6
            qlvt_data.date3 = date3
            qlvt_data.date4 = date4
            qlvt_data.date14 = date14
            qlvt_data.var8 = var8
            qlvt_data.date15 = date15
            qlvt_data.date16 = date16
            qlvt_data.var9 = var9
            qlvt_data.date17 = date17
            qlvt_data.date18 = date18
            qlvt_data.var10 = var10
            qlvt_data.date21 = date21
            qlvt_data.date23 = date23
            qlvt_data.save()
            return main_when_get_Data(request, file = FileUPLoad(), file1 = FileDownLoad())
    else:
        return HttpResponse("<p>Lỗi không lấy được dữ liệu</p>")


# Xóa bản ghi
def delete_record(request):
    if request.method == "POST":
        var0 = request.POST['id0']
        if id == '':
            return main_when_get_Data(request)
        else:
            record = QLVT_Data.objects.get(id = var0)
            record.delete()
            return main_when_get_Data(request, file = FileUPLoad(), file1 = FileDownLoad())
    else:
        return HttpResponse("<p>Lỗi không lấy được dữ liệu</p>")

# Thêm bản ghi
def add_record(request):
    if request.method == "POST":
        var0 = request.POST['id0']
        var1 = request.POST['id1']
        var2 = request.POST['id2']
        var3 = request.POST['id3']
        var4 = request.POST['id4']
        var5 = request.POST['id5']
        date1 = request.POST['id6']
        date2 = request.POST['id7']
        var6 = request.POST['id8']
        date3 = request.POST['id9']
        date4 = request.POST['id10']
        date14 = request.POST['id11']
        var8 = request.POST['id12']
        date15 = request.POST['id13']
        date16 = request.POST['id14']
        var9 = request.POST['id15']
        date17 = request.POST['id16']
        date18 = request.POST['id17']
        var10 = request.POST['id18']
        date21 = request.POST['id19']
        date23 = request.POST['id20']
        qlvt = QLVT_Data(var0, var1, var2, var3, var4, var5, date1, date2, var6, date3, date4, date14, var8, date15, date16, var9, date17, date18, var10, date21, date23)
        qlvt.save()
        return main_when_get_Data(request, file = FileUPLoad(), file1 = FileDownLoad())



    else:
        return HttpResponse("<p>Lỗi không lấy được dữ liệu</p>")




# Nhập file
def import_file(request):
    f = ''
    if request.method == 'POST':
        
        file = FileUPLoad(request.POST, request.FILES)
        if file.is_valid():
            f = request.FILES['FilePath']
            handle_uploadfile(f)
            if f == '':
                return main_when_get_Data(request, file = FileUPLoad(), file1 = FileDownLoad())
            else:
          
                reader = list(pd.read_excel(io = 'static/uploads/'+ f.name, header = 0).values)
                for i in range(0, len(reader)):
                    if len(reader[i]) < 20:
                        for j in range(0, 20 - len(reader[i])):
                            reader[i].append("") 
                    elif len(reader[i]) > 33:
                        for j in range(20, len(reader[i])):
                            del(reader[i][j])

                count = len(QLVT_Data.objects.values('id'))
                qlvt = None
                for i in range(0, len(reader)):
                    qlvt = QLVT_Data(str(count+i+1), reader[i][0], reader[i][1], reader[i][2], reader[i][3], reader[i][4], reader[i][5], reader[i][6], reader[i][7], reader[i][8], reader[i][9], reader[i][10], reader[i][11], reader[i][12], reader[i][13], reader[i][14], reader[i][15], reader[i][16], reader[i][17], reader[i][18], reader[i][19])
                    qlvt.save()
                return render(request, "main.html", {'link_logout': '/logout/', "up_load_file": FileUPLoad(), "down_load_file": FileDownLoad(), "message_import_file_successfully": "Nhập file thành công"})
            
        else:
            return HttpResponse("<h1>Upload file không hợp lệ</h1>")

    else:
        return HttpResponse("<h1>Lỗi lấy đường dẫn file</h1>")




# Xuất file
def export_file(request):
    folderpath = None
    record_list = []
    if request.method == "POST":
        folderpath = FileDownLoad(request.POST, request.FILES)
        if folderpath.is_valid():
            field = request.POST['field']
            key = request.POST['key']
            name_file = request.POST['name_file']
            type_file = request.POST['type_file']
            folder = request.POST['FolderPath']
            
            records = QLVT_Data.objects.filter(['[{}]'.format(field), key]).values()
            for record in records:
                record_list.append(list(record.values()))
            if type_file == "xlsx":
                df = pd.DataFrame(record_list, columns = ["id", "Tên thiết bị", "Số Serial", "Phân loại", "Nhà sản xuất", "Đài Viễn Thông/Điều hành/Vô Tuyến", "Ngày ĐV QLSDTS gửi yêu cầu SC", "Ngày CN hoàn thành phân loại kiểm tra tại ĐV QLSDTS", "Tình trạng tiếp nhận tại ĐV QLSDTS", "Ngày CN  gửi kế hoạch vận chuyển", "Ngày P.KT ĐV QLSDTS gửi phiếu xuất kho", "Ngày giao cho đối tác mang đi SC", "Tình trạng bàn giao đi sửa chữa", "Ngày CN gửi yêu cầu nhập kho sau SC", "Ngày nhận về từ đối tác sau SC", "Số serial sau SC", "Ngày P.KT làm phiếu nhập kho sau SC", "Ngày hoàn thành kiểm tra sau SC", "Kết quả kiểm tra sau sửa chữa", "Ngày P.KT gửi phiếu xuất kho trả thiết bị cho ĐV QLSDTS", "Ngày giao tại kho ĐV QLSDTS"])
                with pd.ExcelWriter(folder + '/' + name_file + '.' + type_file, mode = "w") as writer:
                    df.to_excel(writer, sheet_name = "Sheet1") 
            elif type_file == "csv":
                with open(folder + '/' + name_file + '.' + type_file, mode = "w", encoding = "utf-8" , newline = "") as file:
                        writer = csv.writer(file)
                        writer.writerow(["id", "Tên thiết bị", "Số Serial", "Phân loại", "Nhà sản xuất", "Đài Viễn Thông/Điều hành/Vô Tuyến", "Ngày ĐV QLSDTS gửi yêu cầu SC", "Ngày CN hoàn thành phân loại kiểm tra tại ĐV QLSDTS", "Tình trạng tiếp nhận tại ĐV QLSDTS", "Ngày CN  gửi kế hoạch vận chuyển", "Ngày P.KT ĐV QLSDTS gửi phiếu xuất kho", "Ngày giao cho đối tác mang đi SC", "Tình trạng bàn giao đi sửa chữa", "Ngày CN gửi yêu cầu nhập kho sau SC", "Ngày nhận về từ đối tác sau SC", "Số serial sau SC", "Ngày P.KT làm phiếu nhập kho sau SC", "Ngày hoàn thành kiểm tra sau SC", "Kết quả kiểm tra sau sửa chữa", "Ngày P.KT gửi phiếu xuất kho trả thiết bị cho ĐV QLSDTS", "Ngày giao tại kho ĐV QLSDTS"])
                        writer.writerows(record_list)
                file.close()


            return render(request, "main.html", {'link_logout': '/logout/' , "up_load_file": FileUPLoad(), "down_load_file": FileDownLoad(), "message_export_file_successfully": "Xuất file thành công"})
        else:
            return HttpResponse("<h1>Lỗi xuất file</h1>")
            

    else:
        return render(request, "main.html", {'link_logout': '/logout/' ,"up_load_file": FileUPLoad(), "down_load_file": FileDownLoad()})

# Upload file lên đường dẫn static/uploads/ trước khi tải dữ liệu lên
def handle_uploadfile(f):
    with open('static/uploads/' + f.name, 'wb+') as file:
        for chunk in f.chunks():
            file.write(chunk)


    
    

