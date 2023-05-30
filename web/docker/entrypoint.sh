#!/bin/bash

set -e

export CONSOLE_URL=${CONSOLE_URL}
export APP_URL=${APP_URL}
export NODE_ENV=${DEPLOY_ENV}
export REPORT_URL=${REPORT_URL}
export NEXT_PUBLIC_DEPLOY_ENV=${DEPLOY_ENV}
export NEXT_PUBLIC_EDITION=${EDITION}
export NEXT_PUBLIC_API_PREFIX=${CONSOLE_URL}/console/api
export NEXT_PUBLIC_PUBLIC_API_PREFIX=${APP_URL}/api

/usr/local/bin/pm2 -v
/usr/local/bin/pm2-runtime start /app/web/pm2.json
