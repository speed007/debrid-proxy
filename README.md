# Debrid Proxy Manager 🚀

*A secure, high-performance proxy service for Real-Debrid API with caching and rate limiting*

![Docker](https://img.shields.io/badge/Docker-✓-blue?logo=docker)
![Redis](https://img.shields.io/badge/Redis-✓-red?logo=redis)
![Prometheus](https://img.shields.io/badge/Monitoring-✓-orange?logo=prometheus)

## Features ✨

- 🔒 **Secure API Gateway** for Real-Debrid
- ⚡ **Redis Caching** (Up to 10x faster responses)
- 🚦 **Smart Rate Limiting** (30 reqs/minute)
- 📊 **Built-in Metrics** (Prometheus/Grafana)
- 🐳 **Docker-Optimized** (Multi-stage build)

## Quick Start ▶️

```bash
# Clone and deploy
git clone https://github.com/yourusername/debrid-proxy.git
cd debrid-proxy
cp .env.sample .env  # Edit with your credentials
docker-compose up -d

Access Endpoints:

http://localhost:8000 - Proxy service

http://localhost:9090 - Prometheus metrics

http://localhost:3000 - Grafana (if enabled)

Configuration ⚙️
Environment Variables
Variable	Required	Default	Description
RD_API_KEY	Yes	-	Real-Debrid API token
ENCRYPTION_KEY	Yes	-	Fernet key (32-byte base64)
CACHE_TTL	No	3600	Redis cache TTL (seconds)
RATE_LIMIT	No	30/60	Requests per minute
Generate encryption key:

openssl rand -base64 32 >> .env

Architecture 📐

Copy
graph TD
    A[Client] --> B[Debrid Proxy]
    B --> C[Redis Cache]
    B --> D[Real-Debrid API]
    B --> E[Prometheus Metrics]


Monitoring 📈
Pre-configured dashboards track:

API response times

Cache hit/miss ratios

Rate limit usage

Error rates


Troubleshooting 🛠️
Common Issues:

bash
Copy
# Verify services
docker-compose ps

# Check logs
docker-compose logs -f app

# Test API endpoint
curl http://localhost:8000/health

