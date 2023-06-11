# Generated by Django 4.2.1 on 2023-06-08 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QLVT_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('[Tên thiết bị]', models.TextField()),
                ('[Số Serial]', models.TextField()),
                ('[Phân loại]', models.TextField()),
                ('[Nhà sản xuất]', models.TextField()),
                ('[Đài Viễn Thông/Điều hành/Vô Tuyến]', models.TextField()),
                ('[Ngày ĐV QLSDTS gửi yêu cầu SC]', models.TextField()),
                ('[Ngày CN hoàn thành phân loại kiểm tra tại ĐV QLSDTS]', models.TextField()),
                ('[Tình trạng tiếp nhận tại ĐV QLSDTS] ', models.TextField()),
                ('[Ngày CN  gửi kế hoạch vận chuyển]', models.TextField()),
                ('[Ngày P.KT ĐV QLSDTS gửi phiếu xuất kho]', models.TextField()),
                ('[Ngày giao cho đối tác mang đi SC]', models.TextField()),
                ('[Tình trạng bàn giao đi sửa chữa]', models.TextField()),
                ('[Ngày CN gửi yêu cầu nhập kho sau SC]', models.TextField()),
                ('[Ngày nhận về từ đối tác sau SC]', models.TextField()),
                ('[Số serial sau SC]', models.TextField()),
                ('[Ngày P.KT làm phiếu nhập kho sau SC]', models.TextField()),
                ('[Ngày hoàn thành kiểm tra sau SC]', models.TextField()),
                ('[Kết quả kiểm tra sau sửa chữa]', models.TextField()),
                ('[Ngày P.KT gửi phiếu xuất kho trả thiết bị cho ĐV QLSDTS]', models.TextField()),
                ('[Ngày giao tại kho ĐV QLSDTS]', models.TextField()),
            ],
        ),
    ]