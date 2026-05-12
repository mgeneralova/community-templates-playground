---
layout: integration
title: "Nginx Plus"
folder_path: "Web-servers/Nginx_Plus"
tags: ["Nginx", "Web Server", "Monitoring"]
categories: ["Web Servers"]
status: "active"
author: "community"
last_updated: "2024-05-10"
description: "Monitor Nginx Plus load balancer and web server with health checks, connection stats, and performance metrics."
---

## Overview

This Zabbix template provides detailed monitoring of Nginx Plus load balancers and web servers. It collects metrics directly from the Nginx Plus API to provide real-time insights into server performance, connection handling, and upstream health status.

## Key Metrics

- **Active Connections**: Current active client connections
- **Requests**: Total, completed, and per-second request rates
- **Data Transfer**: Bytes sent and received
- **Upstream Health**: Status of backend servers
- **Cache Performance**: Cache hit rates and statistics
- **SSL/TLS Statistics**: Connection and certificate metrics

## Installation

### Prerequisites

- Nginx Plus (commercial edition with API access)
- Zabbix 5.0+
- Network access to Nginx Plus API endpoint

### Setup

1. Access the template in the repository:
   ```bash
   cd Web-servers/Nginx_Plus
   ```

2. Note the Nginx Plus API endpoint (usually `http://localhost:8080/api`)

3. Import the template into Zabbix

4. Configure the host with:
   - IP/hostname of Nginx Plus server
   - API endpoint URL
   - Port (default: 8080)

## API Requirements

Ensure your Nginx Plus API is accessible:

```nginx
http {
    server {
        listen 8080;
        
        location /api/ {
            api write=on;
        }
    }
}
```

## Macros

- `{$NGINX_API_URL}` - Base URL of Nginx Plus API
- `{$NGINX_API_PORT}` - Port of Nginx Plus API (default: 8080)
- `{$UPSTREAM_WARNING_THRESHOLD}` - Connection warning threshold
- `{$UPSTREAM_CRITICAL_THRESHOLD}` - Connection critical threshold

## Upstream Monitoring

Monitor individual upstream servers with automatic discovery of:

- Backend server status (up/down)
- Connection counts per upstream
- Request handling statistics
- Health check results

## Dashboard

The template includes pre-configured dashboards for:

- **Overview Dashboard**: Real-time server metrics
- **Upstream Dashboard**: Backend server health status
- **Performance Dashboard**: Request rates and latency
- **Cache Dashboard**: Cache hit rates and efficiency

## Alerts

Pre-configured alerts for:

- High CPU usage
- High memory usage
- Upstream servers down
- Abnormal request rates
- API connectivity issues

## Performance Tuning

### Optimization Tips

1. **Adjust Update Intervals**: Modify item update frequency based on your needs
2. **Upstream Discovery**: Configure discovery filter for specific upstreams
3. **Data Retention**: Set appropriate history and trend retention periods

## Troubleshooting

**No metrics appearing**
- Verify Nginx Plus API is enabled
- Check firewall rules allow access to API port
- Review Zabbix server logs

**API Connection Refused**
- Ensure Nginx Plus is running: `nginx -s status`
- Verify API configuration in nginx.conf
- Test API manually: `curl http://localhost:8080/api/`

## Version History

- **v2.0** (2024-05-10): Updated for Nginx Plus 3.x
- **v1.5** (2024-03-15): Added caching metrics
- **v1.0** (2023-12-01): Initial release

## Support

- Report issues: [GitHub Issues](https://github.com/mgeneralova/community-templates-playground/issues)
- Documentation: [Repository Wiki](https://github.com/mgeneralova/community-templates-playground/wiki)

## License

MIT License
