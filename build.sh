#!/usr/bin/env bash
# exit on error
set -o errexit

# Create .env file with all required variables
cat << EOF > .env
GOOGLE_API_KEY=${GOOGLE_API_KEY}
DATABASE_NAME=${DATABASE_NAME}
DATABASE_USER=${DATABASE_USER}
DATABASE_PASSWORD=${DATABASE_PASSWORD}
DATABASE_HOST=${DATABASE_HOST}
SECRET_KEY=${SECRET_KEY}
EMAIL_HOST_USER=${EMAIL_HOST_USER}
EMAIL_HOST_PASSWORD=${EMAIL_HOST_PASSWORD}
REDIS_URL=${REDIS_URL}
EOF

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
