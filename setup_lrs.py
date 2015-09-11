import os
import sys
import linecache
from os import system

# Media folder names
agent_profile = 'agent_profile'
activity_profile = 'activity_profile'
activity_state = 'activity_state'
statement_attachments = 'attachment_payloads'

# Add env packages and project to the path
cwd = os.path.dirname(os.path.abspath(__file__))

if not cwd in sys.path:
    sys.path.append(cwd)

env_dir = os.path.join(cwd, '~/py2.7-lrs/lib/python2.7/site-packages')
if not env_dir in sys.path:
    sys.path.append(env_dir)

log_dir = os.path.join(cwd, '../logs')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Add settings module so fab file can see it
os.environ['DJANGO_SETTINGS_MODULE'] = "adl_lrs.settings"
from django.conf import settings
adldir = settings.MEDIA_ROOT

# Create media directories
if not os.path.exists(os.path.join(adldir,activity_profile)):
    os.makedirs(os.path.join(adldir,activity_profile))

if not os.path.exists(os.path.join(adldir,activity_state)):
    os.makedirs(os.path.join(adldir,activity_state))

if not os.path.exists(os.path.join(adldir,agent_profile)):
    os.makedirs(os.path.join(adldir,agent_profile))

if not os.path.exists(os.path.join(adldir,statement_attachments)):
    os.makedirs(os.path.join(adldir,statement_attachments))

# Create cache tables and sync the db
system('./manage.py createcachetable cache_statement_list')
system('./manage.py createcachetable attachment_cache')
system('./manage.py syncdb')
