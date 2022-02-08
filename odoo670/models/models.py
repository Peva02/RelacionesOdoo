# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class odoo670(models.Model):
#     _name = 'odoo670.odoo670'
#     _description = 'odoo670.odoo670'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo import models, fields, api

class vehiculos670(models.Model):
	_name = 'odoo670.vehiculos670'
	_description = 'Modelo vehiculos670'

	name = fields.Char('Matricula',required=True)
	marca = fields.Char(string='Marca',required=True)
	precio = fields.Char(string='Precio',required=True)


class coches670(models.Model):
	_name = 'odoo670.coches670'ff
	_description = 'Modelo coches670'

	name = fields.Char('Matricula',required=True)
	marca = fields.Char(string='Marca',required=True)
	precio = fields.Char(string='Precio',required=True)
    
    #supervisor_id=fields.Many2one('odoo670.supervisores670',string='supervisor')

class furgonetas670(models.Model):
	_name = 'odoo670.furgonetas670'
	_description = 'Modelo furgonetas670'

	name = fields.Char('Matricula',required=True)
	marca = fields.Char(string='Marca',required=True)
	precio = fields.Char(string='Precio',required=True)
#-------------------------------------------------------------------------
class clientes670(models.Model):
	_name = 'odoo670.clientes670'
	_description = 'Modelo clientes670'

	name = fields.Char('Nombre',required=True)
	apellidos = fields.Char(string='Apellidos',required=True)

class andalucia670(models.Model):
	_name = 'odoo670.andalucia670'
	_description = 'Modelo andalucia670'

	name = fields.Char('Nombre',required=True)
	apellidos = fields.Char(string='Apellidos',required=True)

class madrid670(models.Model):
	_name = 'odoo670.madrid670'
	_description = 'Modelo madrid670'

	name = fields.Char('Nombre',required=True)
	apellidos = fields.Char(string='Apellidos',required=True)
#-------------------------------------------------------------------------
class departamentos670(models.Model):
	_name = 'odoo670.departamentos670'
	_description = 'Modelo departamentos670'

	name = fields.Char('Nombre',required=True)
	apellidos = fields.Char(string='Apellidos',required=True)
class empleados670(models.Model):
	_name = 'odoo670.empleados670'
	_description = 'Modelo empleados670'

	name = fields.Char('Nombre',required=True)
	apellidos = fields.Char(string='Apellidos',required=True)

class supervisores670(models.Model):
	_name = 'odoo670.supervisores670'
	_description = 'Modelo supervisores670'

	name = fields.Char('Nombre',required=True)
	apellidos = fields.Char(string='Apellidos',required=True)
    #coches_ids = fields.One2many('odoo670.coches670','supervisor_id',string='Alumno tutoria')

