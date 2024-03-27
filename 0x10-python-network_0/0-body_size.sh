#!/bin/bash
# script that takes URL, sends request to URL
# displays size of body of the response
curl -sI "$1" | wc -c
