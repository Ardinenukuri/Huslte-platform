#!/usr/bin/env bash
# exit on error
set -o errexit

# Create .env file with all required variables
cat << EOF > .env
GOOGLE_API_KEY=${GOOGLE_API_KEY}
SECRET_KEY=${SECRET_KEY}
EMAIL_HOST_USER=${EMAIL_HOST_USER}
EMAIL_HOST_PASSWORD=${EMAIL_HOST_PASSWORD}
REDIS_URL=${REDIS_URL}
EOF

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Creating media directory..."
mkdir -p media/certificates

echo "Applying migrations..."
python manage.py migrate

echo "Build completed successfully!"