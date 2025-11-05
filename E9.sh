#!/usr/bin/env bash
# Name: Jamie Knowles
# Student Number: C00307559
# Date: 05/11/25
# Purpose: Use a Bash loop with Python to compute SHA256 for a small word list

for word in admin test guest; do
  python3 -c "import hashlib,sys; w=sys.argv[1].encode(); print(sys.argv[1]+' ->', hashlib.sha256(w).hexdigest())" "$word"
done
