#!/bin/bash
# Takes in a URL, sends a request to it, displays size of body of response
curl -s "$1" | wc -c
