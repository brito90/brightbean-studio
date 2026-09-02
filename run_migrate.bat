@echo off
vercel env run production -- python manage.py migrate --settings=config.settings.production
