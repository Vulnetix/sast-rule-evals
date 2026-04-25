#!/usr/bin/env bash
# Fake vulnerable script for SAST evaluation - DO NOT USE IN PRODUCTION
# This file demonstrates VNX-BASH-004: unquoted variable in [ ] test

set -euo pipefail

username="$1"
role="$2"

# TRIGGERS VNX-BASH-004: unquoted $username in test - subject to word splitting
if [ $username = "admin" ]; then
    echo "Admin access"
fi

# TRIGGERS VNX-BASH-004: unquoted variable may cause unexpected glob expansion
if [ $role == "superuser" ]; then
    echo "Super user"
fi

# Safe alternatives:
# if [ "$username" = "admin" ]; then
# if [[ $username == "admin" ]]; then
