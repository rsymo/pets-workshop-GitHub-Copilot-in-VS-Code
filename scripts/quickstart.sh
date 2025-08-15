#!/bin/bash
set -e

# Create and activate Python virtual environment
if [ ! -d "venv" ]; then
  python3 -m venv venv
fi
source venv/bin/activate

# Install backend dependencies
pip install -r server/requirements.txt


# Start backend (in background)
cd server
nohup flask --app app run --host 0.0.0.0 --port 5100 &
BACKEND_PID=$!
echo "Backend started with PID $BACKEND_PID on port 5100"
cd ..

# Start frontend
cd client
npm install
npm run dev
