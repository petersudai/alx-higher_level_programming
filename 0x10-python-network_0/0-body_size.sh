#!/bin/bash
# script that takes URL, sends request to URL
# displays size of body of the response
curl -s "$1" | wc -c
