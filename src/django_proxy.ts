import { spawn } from 'child_process'

const proxy = await spawn('venv/bin/python', ['-m', 'django_iam.proxy_handler'])