# Dify Backend API

## Usage

1. 定义终端窗口环境变量
   ```bash
   echo "export UID=$(id -u)" >> ~/.zshrc
   echo "export GID=$(id -g)" >> ~/.zshrc
   source ~/.zshrc
   ```
2. 修改目录所有者
   ```bash
   cd ../docker
   sudo chown -R (id -u):(id -g) ./volumes
   ```
2. Start the docker-compose stack
   The backend require some middleware, including PostgreSQL, Redis, and Weaviate, which can be started together using `docker-compose`.
   必须先修改目录所有者，再启动容器，否则会出现权限问题导致容器无法启动。
   ```bash
   cd ../docker
   docker-compose -f docker-compose.middleware.yaml up -d
   cd ../api
   ```
2. Copy `.env.example` to `.env`
3. Generate a `SECRET_KEY` in the `.env` file.

   ```bash
   openssl rand -base64 42
   ```
4. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
5. Run migrate

   Before the first launch, migrate the database to the latest version.

   ```bash
   flask db upgrade
   ```
6. Start backend:
   ```bash
   flask run --host 0.0.0.0 --port=5001 --debug
   ```
7. Setup your application by visiting http://localhost:5001/console/api/setup or other apis...

8. If you need to debug local async processing, you can run `celery -A app.celery worker`, celery can do dataset importing and other async tasks.

10. 如需使用国内OpenAI代理，在Worker、API添加如下环境变量即可。
   ```yaml
   OPENAI_API_BASE=https://azure-gpt-proxy.gz.cvte.cn/v1
   ```