from django.db import models

# Create your models here.

class QLVT_Data(models.Model):
    var1 = models.TextField(name = "[Tên thiết bị]")
    var2 = models.TextField(name = "[Số Serial]")
    var3 = models.TextField(name = "[Phân loại]")
    var4 = models.TextField(name = "[Nhà sản xuất]")
    var5 = models.TextField(name = "[Đài Viễn Thông/Điều hành/Vô Tuyến]")
    date1  =models.TextField(name = "[Ngày ĐV QLSDTS gửi yêu cầu SC]")
    date2 = models.TextField(name = "[Ngày CN hoàn thành phân loại kiểm tra tại ĐV QLSDTS]")
    var6 = models.TextField(name = "[Tình trạng tiếp nhận tại ĐV QLSDTS] ")
    date3 = models.TextField(name = "[Ngày CN  gửi kế hoạch vận chuyển]")
    date4 = models.TextField(name = "[Ngày P.KT ĐV QLSDTS gửi phiếu xuất kho]")
    date14 = models.TextField(name = "[Ngày giao cho đối tác mang đi SC]")
    var8 = models.TextField(name = "[Tình trạng bàn giao đi sửa chữa]")
    date15 = models.TextField(name = "[Ngày CN gửi yêu cầu nhập kho sau SC]")
    date16 = models.TextField(name = "[Ngày nhận về từ đối tác sau SC]")
    var9 = models.TextField(name = "[Số serial sau SC]")
    date17 = models.TextField(name = "[Ngày P.KT làm phiếu nhập kho sau SC]")
    date18 = models.TextField(name = "[Ngày hoàn thành kiểm tra sau SC]")
    var10 = models.TextField(name = "[Kết quả kiểm tra sau sửa chữa]")
    date21 = models.TextField(name = "[Ngày P.KT gửi phiếu xuất kho trả thiết bị cho ĐV QLSDTS]")
    date23 = models.TextField(name = "[Ngày giao tại kho ĐV QLSDTS]")


