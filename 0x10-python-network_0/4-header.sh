#!/bin/bash
#Take in URL, add header variable, displays "Hello School!"
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" "$1"
