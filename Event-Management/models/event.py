# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re  # For email validation

class Event(models.Model):
    _name = 'event.management'
    _description = 'Event Management'

    name = fields.Char(string="Event Name", required=True)
    date_start = fields.Datetime(string="Start Date", required=True)
    date_end = fields.Datetime(string="End Date", required=True)
    location = fields.Char(string="Location")
    description = fields.Text(string="Description")
    ticket_ids = fields.One2many('event.ticket', 'event_id', string="Tickets")
    participant_ids = fields.One2many('event.participant', 'event_id', string="Participants")

    @api.constrains('date_start', 'date_end')
    def _check_dates(self):
        for record in self:
            if record.date_end < record.date_start:
                raise ValidationError("End Date must be greater than Start Date.")

    def action_view_participants(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Participants',
            'res_model': 'event.participant',
            'view_mode': 'tree,form',
            'domain': [('event_id', '=', self.id)],
            'context': {'default_event_id': self.id},
        }
