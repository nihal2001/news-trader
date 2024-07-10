#!/bin/bash

# Check for a specific file that indicates the scraper has completed
if [ -f /shared/scraper_done.txt ]; then
  exit 0
else
  exit 1
fi
