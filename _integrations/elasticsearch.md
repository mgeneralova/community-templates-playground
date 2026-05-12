---
layout: integration
title: "Elasticsearch"
folder_path: "Databases/Elasticsearch"
tags: ["Elasticsearch", "Search", "Analytics", "Database"]
categories: ["Databases"]
status: "stale"
author: "community"
last_updated: "2024-02-15"
description: "Monitor Elasticsearch cluster health, indexing performance, and search metrics with real-time dashboards."
---

## Overview

Monitor your Elasticsearch clusters with comprehensive Zabbix integration. This template provides insights into cluster health, node statistics, shard allocation, and query performance metrics.

## Features

- **Cluster Health Monitoring**: Track red/yellow/green status
- **Node Metrics**: CPU, memory, and disk usage per node
- **Index Statistics**: Document count, indexing rate, search rate
- **JVM Monitoring**: Garbage collection and memory heap metrics
- **Query Performance**: Query latency and throughput
- **Automatic Discovery**: Discover nodes and indices automatically

## Metrics

### Cluster Level
- Cluster status and node count
- Active shards and relocating shards
- Delayed unassigned shards

### Node Level
- JVM heap usage
- Garbage collection time
- Disk usage and I/O operations
- Network throughput

### Index Level
- Document count and size
- Primary shard count
- Search and indexing rates

## Setup Instructions

### Prerequisites

- Elasticsearch 7.0+
- Zabbix 5.4+
- Network connectivity to Elasticsearch HTTP port (default: 9200)

### Installation Steps

1. Download the template from the repository
2. Import into Zabbix Administration > Templates
3. Link template to Elasticsearch hosts
4. Configure macros (see below)

### Macro Configuration

```
{$ELASTICSEARCH_URL} = http://localhost:9200
{$ELASTICSEARCH_USERNAME} = elastic (if auth enabled)
{$ELASTICSEARCH_PASSWORD} = your_password
```

## Key Metrics Table

| Metric | Interval | Alert Threshold |
|--------|----------|------------------|
| Cluster Status | 60s | Red = Critical |
| Heap Usage | 30s | >85% = Warning |
| Disk Usage | 60s | >80% = Warning |
| Query Latency | 30s | >1000ms = Warning |
| Index Refresh Rate | 60s | >10000/min = Info |

## Discovery Rules

### LLD Discovery

- **Node Discovery**: Automatically discovers all Elasticsearch nodes
- **Index Discovery**: Finds indices matching pattern (configurable)
- **Data Stream Discovery**: Discovers data streams if enabled

## Dashboards

Pre-configured dashboards:
- Elasticsearch Overview
- Cluster Health Status
- Node Performance Metrics
- Index Management
- JVM Metrics

## Troubleshooting

### Issue: No data collection

**Solution:**
1. Verify Elasticsearch is running: `curl http://localhost:9200`
2. Check security (check if authentication is required)
3. Verify port 9200 is accessible from Zabbix server
4. Check Zabbix server logs for connection errors

### Issue: High memory usage alerts

**Actions:**
1. Review heap allocation settings
2. Check for memory leaks in custom plugins
3. Monitor GC frequency and duration
4. Consider index lifecycle policies

## Performance Optimization

- Increase update interval for large clusters
- Use discovery filters for specific indices/nodes
- Adjust history retention based on requirements
- Consider dedicated monitoring indices

## Notes

⚠️ **Status**: This template is currently **STALE** and may need updates for the latest Elasticsearch versions. 
Community contributions are welcome!

## Contributing

Want to update or improve this template? See [Contributing Guidelines](../CONTRIBUTING.md)

## See Also

- [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/)
- [Zabbix LLD Discovery](https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery)
