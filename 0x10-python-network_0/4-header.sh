#!/bin/bash
#Take in URL, add header variable, displays "Hello School!"
curl -s "$1" -X GET -H "X-School-User-Id: 98"
