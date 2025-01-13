#!/bin/bash

printenv | awk -F= '/^[^=]+=/ {print $1}'

# printenv: Lists all environment variables.
# |: Sends that list to awk.
# -F=: Tells awk to split each line at the = sign.
# /^[^=]+=/: Matches lines that have something before the = (i.e., valid variable names).
# {print $1}: Prints just the part before the = (the variable name).