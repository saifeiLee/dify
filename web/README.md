# Dify Frontend
This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

[API routes](https://nextjs.org/docs/api-routes/introduction) can be accessed on [http://localhost:3000/api/hello](http://localhost:3000/api/hello). This endpoint can be edited in `pages/api/hello.ts`.

The `pages/api` directory is mapped to `/api/*`. Files in this directory are treated as [API routes](https://nextjs.org/docs/api-routes/introduction) instead of React pages.

This project uses [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) to automatically optimize and load Inter, a custom Google Font.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.

## 环境变量配置
1. 自定义添加如下环境变量。
   ```yaml
    # 问题需求反馈链接
    FEEDBACK_URL=https://wxwork.jiandaoyun.com/app/611b7026c316d20009b413c5/entry/6474518948ada60008be4cf7?embed=true
    
    # 运营报表地址
    REPORT_URL=https://grafana.cvte.com/d/ef91266f-b375-448c-9461-5ffa1bfb4884/dify-abstract?orgId=1&kiosk&var-channel=All&var-loan_no=&theme=light&refresh=1h
    
    # Console API base URL
    CONSOLE_URL=http://dify.cvte.cn:5001
    
    # Service API base URL
    API_URL=http://dify.cvte.cn:5001
    ```