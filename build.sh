#!/bin/bash
# Install Node.js and npm
curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
apt-get install -y nodejs && \
npm install -g npm@latest

# Install Python dependencies using pip
pip install -r requirements.txt

npm install -g rimraf && \

# Collect static files and build Tailwind CSS
python manage.py collectstatic --noinput
python manage.py tailwind build