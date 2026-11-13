from odoo import fields, models


class Phong(models.Model):
    _name = 'phong'
    _description = 'Phòng ban'

    name = fields.Char(string='Tên phòng', required=True)
    depid = fields.Integer(string='Mã phòng', required=True)


class NhanVien(models.Model):
    _name = 'nhanvien'
    _description = 'Nhân viên'

    name = fields.Char(string='Họ và tên', required=True)
    empid = fields.Integer(string='Mã nhân viên', required=True)
    gender = fields.Selection(
        [('Nam', 'Nam'), ('Nữ', 'Nữ')],
        string='Giới tính',
    )
    phone = fields.Char(string='Điện thoại')
