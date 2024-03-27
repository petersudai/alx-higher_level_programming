#!/bin/bash
# script that takes URL, sends request to URL
curl -s "$1" | wc -c
