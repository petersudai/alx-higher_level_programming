#!/bin/bash
# script that takes in a URL, sends a GET request to the URL
curl -s - /tmp/body "$1" && cat /tmp/body
