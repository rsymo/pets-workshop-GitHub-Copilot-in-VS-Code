#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "Usage: $0 <tag-name> <message>" >&2
  exit 1
fi

tag="$1"; msg="$2"

git tag -a "$tag" -m "$msg"
echo "Created tag $tag"
