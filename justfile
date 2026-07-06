# Default recipe to show available commands
default:
    @just --list

# Start the development environment
dev:
    @uv run fastapi dev --port 8080 --reload

# Start all services in the background
up:
    @docker compose up -d

# Stop and remove containers, networks, and images
down:
    @docker compose down
