#!/usr/bin/env bash
# Fake vulnerable script for SAST evaluation - DO NOT USE IN PRODUCTION
# This file demonstrates VNX-BASH-002: curl/wget piped to shell

# TRIGGERS VNX-BASH-002: curl output piped directly to bash
curl -fsSL https://example.com/install.sh | bash

# TRIGGERS VNX-BASH-002: wget with pipe to sh
wget -qO- https://example.com/setup.sh | sh

# TRIGGERS VNX-BASH-002: curl with -k (insecure) piped to bash
curl -k https://example.com/bootstrap.sh | bash

# Safe alternative: download, verify, then execute
# curl -fsSL https://example.com/install.sh -o /tmp/install.sh
# sha256sum -c /tmp/install.sh.sha256
# bash /tmp/install.sh
