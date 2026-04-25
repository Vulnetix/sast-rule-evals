#!/bin/bash
# vnx-bash-006 eval target

# TRIGGERS: global IFS reassignment affects all subsequent word splitting
IFS=","

# This reads comma-separated input but the IFS change affects all other operations below
read -r field1 field2 field3

echo "Fields: $field1, $field2, $field3"

# Because IFS is now "," globally, command output and variable expansions
# that should be space-separated are now split on commas instead.
files=$(ls /tmp)
for f in $files; do
    echo "Processing: $f"
done

# Safe alternative: limit the scope of IFS change
# IFS="," read -r field1 field2 field3 <<< "$input_line"
# Or use a subshell: (IFS=","; read -r field1 field2 field3)
