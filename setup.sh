#!/bin/bash
# Installation script for M141 PostgreSQL setup

echo "M141 PostgreSQL Setup - Security Enhanced"
echo "========================================"

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is available
if ! docker compose version &> /dev/null; then
    echo "❌ Docker Compose is not available. Please install Docker Compose."
    exit 1
fi

echo "✅ Docker and Docker Compose are available"

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "📝 Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Please edit .env file and set secure passwords before starting containers!"
else
    echo "✅ .env file already exists"
fi

# Validate docker-compose configuration
echo "🔧 Validating Docker Compose configuration..."
cd docker
if docker compose config > /dev/null 2>&1; then
    echo "✅ Docker Compose configuration is valid"
else
    echo "❌ Docker Compose configuration has errors"
    exit 1
fi

echo ""
echo "✅ Setup completed successfully!"
echo ""
echo "Next steps:"
echo "1. Edit .env file and set secure passwords"
echo "2. Run: cd docker && docker compose up -d"
echo "3. Access pgAdmin at: http://localhost:8081"
echo "4. Connect to PostgreSQL at: localhost:5432"
echo ""
echo "Security notes:"
echo "- Services are bound to localhost only"
echo "- Use strong passwords in .env file"
echo "- Regularly update Docker images"
echo "- Monitor container logs for security events"