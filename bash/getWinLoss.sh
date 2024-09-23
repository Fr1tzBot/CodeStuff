#!/bin/bash
curl --silent "https://www.thebluealliance.com/team/$1" | grep "Team $1 was" | head -1 | xargs | sed "s/.*<strong>//" | sed "s/<\/strong>.*//"

