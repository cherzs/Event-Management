from odoo import models, fields

class Participant(models.Model):
    _name = 'event.participant'
    _description = 'Event Participant'

    name = fields.Char(string="Participant Name", required=True)
    email = fields.Char(string="Email", required=True)
    event_id = fields.Many2one('event.management', string="Event", required=True)
    feedback = fields.Text(string="Feedback")