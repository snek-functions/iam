import {spawn} from 'child_process'

spawn('venv/bin/python', ['-m', 'django_iam.proxy_handler'])
