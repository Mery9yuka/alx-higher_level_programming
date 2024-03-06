#!/bin/bash
# script that takes in a URL & sends a request to it
#then displays the size of the body of the response
curl -s "$1" | wc -c
