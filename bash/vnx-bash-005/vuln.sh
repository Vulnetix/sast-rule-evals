#!/usr/bin/env bash
# Fake vulnerable script for SAST evaluation - DO NOT USE IN PRODUCTION
# This file demonstrates VNX-BASH-005: hardcoded secret in shell variable

set -euo pipefail

# TRIGGERS VNX-BASH-005: hardcoded password
PASSWORD='SuperSecret123!'

# TRIGGERS VNX-BASH-005: hardcoded API token
API_KEY='sk-prod-abc123xyz789secrettoken'

# TRIGGERS VNX-BASH-005: hardcoded database password
DB_PASSWORD="myH4rdcodedP@ss"

# Use the credentials (bad practice demonstrated)
curl -u "admin:$PASSWORD" https://api.example.com/data
