#!/usr/bin/env bash
# Fake vulnerable script for SAST evaluation - DO NOT USE IN PRODUCTION
# This file demonstrates VNX-BASH-001: eval with user-controlled input

set -euo pipefail

user_input="$1"

# TRIGGERS VNX-BASH-001: eval with variable - allows arbitrary code execution
eval "$user_input"

# TRIGGERS VNX-BASH-001: eval with command substitution
cmd=$(cat /tmp/cmd.txt)
eval $cmd

# Safe: eval with a static string
eval "echo hello"
