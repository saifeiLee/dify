FROM langgenius/base:1.0.0-bullseye-slim

LABEL maintainer='luowei@cvte.com'

ENV DEPLOY_ENV 'PRODUCTION'
ENV EDITION 'SELF_HOSTED'
#ENV NEXT_PUBLIC_API_PREFIX 'https://dify.cvte.com/console/api'
#ENV NEXT_PUBLIC_PUBLIC_API_PREFIX 'https://dify.cvte.com/api'
ENV FEEDBACK_URL 'https://wxwork.jiandaoyun.com/app/611b7026c316d20009b413c5/entry/6474518948ada60008be4cf7?embed=true'
ENV REPORT_URL 'https://grafana.cvte.com/d/ef91266f-b375-448c-9461-5ffa1bfb4884/dify-abstract?orgId=1&kiosk&var-channel=All&var-loan_no=&theme=light&refresh=1h'
#ENV CONSOLE_URL 'https://dify.cvte.com'
#ENV API_URL 'https://dify.cvte.com'
ENV NODE_OPTIONS --max-old-space-size=8096

EXPOSE 3000
WORKDIR /app/web
COPY package.json /app/web/package.json
RUN npm install
RUN rm -rf .next

COPY . /app/web/
RUN npm run build

COPY docker/pm2.json /app/web/pm2.json
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ARG COMMIT_SHA
ENV COMMIT_SHA ${COMMIT_SHA}
ENTRYPOINT ["/entrypoint.sh"]
