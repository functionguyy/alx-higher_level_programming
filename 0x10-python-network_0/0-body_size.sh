#!/usr/bin/env bash

if [ "$#" -eq "1" ]
then
	body_size=$(curl -s -w '%{size_download}' -o /dev/null "$1")
else
	echo "Usage: $(basename "$0") <IP addr>:<port>"
	exit 1
fi

echo "$body_size"
