#!/bin/bash
distanceBetween ()  {
  #remember, param 1 is $1
  #there is not logic for absolute value in bash
  if [ "$(($1+$2))" -lt "0"]
    then
    returnVal="$(('$(($1+$2))' * -1))"
  else
    returnVal="$(($1+$2))"
  fi
  return returnVal
}