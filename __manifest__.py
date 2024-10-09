# -*- coding: utf-8 -*-
{
    'name': "Event Management System",
    'summary': "Manage and track events, participants, and feedback.",
    'description': "A module to create, manage, and track events, including ticketing, attendance, and feedback collection.",
    'author': "Your Name",
    'website': "https://www.yourwebsite.com",
    'license': "AGPL-3",
    'category': 'Events',
    'version': '17.0.1.0',
    'depends': ['base', 'mail'],  # Add other dependencies as needed
    'data': [
        'security/ir.model.access.csv',
        'views/event_views.xml',
        'views/participant_views.xml',
    ],
    'installable': True,
    'application': True,
}
