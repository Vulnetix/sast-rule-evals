#!/usr/bin/env bash
# Fake vulnerable script for SAST evaluation - DO NOT USE IN PRODUCTION
# This file demonstrates VNX-BASH-003: missing set -euo pipefail

# TRIGGERS VNX-BASH-003: no set -e, -u, or -o pipefail

DATADIR="/var/data"
rm -rf $DATADIR/*   # if $DATADIR is unset, this becomes "rm -rf /*"
cp /etc/config .    # failure silently ignored without set -e
