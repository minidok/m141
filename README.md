# m141 - PostgreSQL Container Setup (Security Enhanced)

This project sets up PostgreSQL and pgAdmin4 containers with enhanced security configurations.

## Security Features

- **Environment Variables**: Sensitive data is stored in environment variables instead of hard-coded values
- **Pinned Image Versions**: Using specific image versions to avoid security vulnerabilities from latest tags
- **Network Security**: Services bound to localhost only, preventing external access
- **Resource Limits**: CPU and memory limits to prevent resource exhaustion attacks
- **Health Checks**: Built-in health checks for container reliability
- **Non-root Users**: Containers run with non-root users where possible
- **Security Options**: Enhanced security options like `no-new-privileges`
- **SSL/TLS Support**: Database connections configured to prefer encrypted connections

## Setup Instructions

1. **Copy environment configuration:**
   ```bash
   cp .env.example .env
   ```

2. **Update passwords in .env file:**
   Edit `.env` file and set strong passwords for:
   - `POSTGRES_PASSWORD`
   - `PGADMIN_DEFAULT_PASSWORD`

3. **Start the containers:**
   ```bash
   cd docker
   docker-compose up -d
   ```

4. **Access services:**
   - PostgreSQL: `localhost:5432`
   - pgAdmin: `http://localhost:8081`

## Security Considerations

- **Password Security**: Use strong, unique passwords in the `.env` file
- **Network Access**: Services are bound to localhost only. For external access, configure properly secured reverse proxy
- **SSL/TLS**: For production, enable SSL/TLS encryption for database connections
- **Backup Security**: Ensure database backups are encrypted and stored securely
- **Regular Updates**: Regularly update Docker images to get security patches

## Database Connection

The Python application supports two configuration modes:
- `postgresql_test`: For local development (connects to localhost)
- `postgresql_container`: For containerized applications (connects to db service)

Set `DOCKER_ENV=true` environment variable when running inside containers.

## Monitoring

Check container health:
```bash
docker-compose ps
docker-compose logs db
docker-compose logs pgadmin
```