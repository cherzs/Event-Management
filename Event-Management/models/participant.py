from odoo import models, fields
from odoo.exceptions import ValidationError
import re 

class Participant(models.Model):
    _name = 'event.participant'
    _description = 'Event Participant'

    name = fields.Char(string="Participant Name", required=True)
    email = fields.Char(string="Email", required=True)
    event_id = fields.Many2one('event.management', string="Event", required=True)
    feedback = fields.Text(string="Feedback")

    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if not re.match(r"[^@]+@[^@]+\.[^@]+", record.email):
                raise ValidationError("Invalid email format for participant: %s" % record.name)