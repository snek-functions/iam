#!/usr/bin/env bash

if [ $# -ne 1 ]; then
  echo "Start as container" 1>&2

  # Test connection with psql and echo result to console.
  # psql "postgres://app_user:changeme@localhost:5432/app_db"
  until psql "postgres://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_DB" -c '\l'; do
      echo >&2 "Postgres is unavailable - sleeping"
      sleep 1
  done

  echo >&2 "Postgres is up - continuing"

  cd $LAMBDA_TASK_ROOT/dist/django

  # Migrate database for deployment.
  # $LAMBDA_TASK_ROOT/venv/bin/python django_iam/manage.py migrate --noinput

  $LAMBDA_TASK_ROOT/venv/bin/python -m django_iam.proxy_handler &
  exec yarn snek-functions server -p $SNEK_FUNCTIONS_PORT -f $LAMBDA_TASK_ROOT/dist
fi
export _HANDLER="$1"

RUNTIME_ENTRYPOINT=/var/runtime/bootstrap
if [ -z "${AWS_LAMBDA_RUNTIME_API}" ]; then
  exec /usr/local/bin/aws-lambda-rie $RUNTIME_ENTRYPOINT
else
  exec $RUNTIME_ENTRYPOINT
fi
