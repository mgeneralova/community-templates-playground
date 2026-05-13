---
layout: integration
title: "AWS CloudWatch"
folder_path: "Cloud/AWS"
tags: ["AWS", "CloudWatch", "Cloud Monitoring"]
categories: ["Cloud", "AWS"]
status: "active"
author: "mgeneralova"
maintainer: "mgeneralova"
last_updated: "2024-05-12"
community_score: 82
discussion_count: 6
open_issues: 2
description: "Monitor AWS CloudWatch metrics via Docker Wrapper with real-time dashboards and alerting."
---

## Overview

The AWS CloudWatch Zabbix template provides comprehensive monitoring of your AWS infrastructure through CloudWatch metrics. This template is designed to work with the AWS CloudWatch Docker Wrapper for seamless integration.

## Features

- **Real-time Metrics Collection**: Automatically collects CloudWatch metrics from your AWS account
- **Custom Dashboards**: Pre-built Zabbix dashboards for common AWS services
- **Alert Integration**: Configurable alerts based on CloudWatch alarm thresholds
- **Multi-Account Support**: Monitor multiple AWS accounts from a single Zabbix instance
- **Cost Optimization**: Helps identify unused resources and optimize spending

## Installation

### Prerequisites

- Zabbix Server 5.0 or higher
- AWS Account with appropriate IAM permissions
- Docker (for the CloudWatch Wrapper)
- Python 3.7+

### Step-by-Step Installation

1. Clone the template repository:
   ```bash
   git clone https://github.com/mgeneralova/community-templates-playground.git
   cd community-templates-playground/Cloud/AWS
   ```

2. Configure your AWS credentials:
   ```bash
   cp .env.example .env
   # Edit .env with your AWS access key and secret
   ```

3. Deploy the Docker container:
   ```bash
   docker-compose up -d
   ```

4. Import the Zabbix template via the admin interface

## Configuration

### AWS IAM Policy

Ensure your AWS IAM user has the following permissions:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "cloudwatch:GetMetricStatistics",
                "cloudwatch:ListMetrics",
                "ec2:DescribeInstances",
                "ec2:DescribeImages"
            ],
            "Resource": "*"
        }
    ]
}
```

### Zabbix Configuration

1. Import the template file
2. Create a Zabbix user macro `{$AWS_ACCOUNT_ID}` with your AWS account ID
3. Configure the CloudWatch API endpoint URL
4. Set up host groups for different AWS regions

## Metrics Included

| Metric | Description |
|--------|-------------|
| CPUUtilization | EC2 instance CPU usage |
| NetworkIn | Incoming network traffic |
| NetworkOut | Outgoing network traffic |
| DiskReadBytes | Disk read operations |
| DiskWriteBytes | Disk write operations |

## Troubleshooting

### Common Issues

**Docker container not connecting to AWS**
- Verify AWS credentials in `.env` file
- Check IAM permissions
- Review container logs: `docker logs cloudwatch-wrapper`

**Metrics not appearing in Zabbix**
- Ensure the CloudWatch wrapper is running
- Check Zabbix server error logs
- Verify network connectivity to AWS API

## Support & Contribution

- **Issues**: [Report issues on GitHub](https://github.com/mgeneralova/community-templates-playground/issues)
- **Discussions**: [Join discussions](https://github.com/mgeneralova/community-templates-playground/discussions)
- **Contribute**: We welcome pull requests and improvements!

## License

This template is licensed under the MIT License. See the repository for details.

## Related Resources

- [AWS CloudWatch Documentation](https://docs.aws.amazon.com/cloudwatch/)
- [Zabbix Official Documentation](https://www.zabbix.com/documentation)
- [AWS CLI Reference](https://docs.aws.amazon.com/cli/)
