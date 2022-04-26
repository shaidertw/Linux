#!/bin/bash

Height=$1
Weight=$2

if [ $3 -ne 0 ]
then
    char=$4
else
    char=' '
fi

for (( i = 1; i <= $Height; i++ )); do
  for (( j = 1; j <= $Weight; j++ )); do
    if (( 1 == i || $Height == i || 1 == j || $Weight == j )); then
      echo -n $4
    else
      echo -n "$char"
    fi
  done
  echo
done
