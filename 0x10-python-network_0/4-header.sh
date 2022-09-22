#!/bin/bash
#Take in URL, add header variable, displays "Hello School!"
curl -sH "X-School-User-Id: 98" "$1"

