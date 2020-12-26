# Homemgmt Pigpio + BME280 v0.1
This is a POC of Pigpio + BME280 home management service.
Code is written in Python 3 + Django is used as a framework.
Served via HTTPS using UWSGI + nginx.

Database initialize:

pi@rasp2:~/homemgmt $ ./manage.py migrate --run-syncdb
Operations to perform:
  Synchronize unmigrated apps: homemgmt, livesync, messages, staticfiles
  Apply all migrations: admin, auth, contenttypes, sessions, sites
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK
  Applying sites.0001_initial... OK
  Applying sites.0002_alter_domain_unique... OK
pi@rasp2:~/homemgmt $ ./manage.py createsuperuser
Username (leave blank to use 'pi'): admin
Email address: git@blaze.pl
Password:
Password (again):
Superuser created successfully.
