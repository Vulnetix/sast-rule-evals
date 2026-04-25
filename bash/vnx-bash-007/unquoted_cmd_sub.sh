#!/bin/bash
# vnx-bash-007 eval target

# TRIGGERS: unquoted command substitution subject to word splitting and glob expansion
TARGET_DIR=$(pwd)
mkdir -p $TARGET_DIR/output

# TRIGGERS: unquoted $(hostname) - if hostname has spaces, this breaks
HOST=$(hostname)
echo "Deploying to: " $HOST

# TRIGGERS: unquoted $(date) used as argument
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
cp config.json /tmp/backup_$TIMESTAMP.json

# TRIGGERS: unquoted $() in if test
if [ $(whoami) = "root" ]; then
    echo "Running as root"
fi

# Safe alternative: always quote command substitutions
# mkdir -p "$TARGET_DIR/output"
# HOST="$(hostname)"
# echo "Deploying to: $HOST"
