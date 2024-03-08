#!/bin/bash

TYPE=$1
RUN_ID=$2
INPUTS=$3

cp vars.yml ${TYPE}_vars_temp_${RUN_ID}.yml

for key in Client Environment type Source_Backup_AppDB Source_Backup_EngDB Bypass_Backup
do
  if [[ -n "${INPUTS[$key]}" ]]; then
    echo "${TYPE}_${key}: '${INPUTS[$key]}'" >> ${TYPE}_vars_temp_${RUN_ID}.yml
  fi
done
