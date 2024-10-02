# dify-mermaid-flask-service
为AI带路党Pro视频<a href="https://www.bilibili.com/video/BV1PntFeqEe9" target="_blank">Dify实战教程:搭建AI自动生成流程图、序列图、甘特图等图表agent</a>准备

## 使用指南

1. 拷贝mermain-flask-service到dify的docker目录中
2. 修改docker-compose.yaml文件，在services字段下新增一个mermaid-flask-service子级，具体配置如下。
```yaml
  mermaid-flask-service:
    build: ./mermaid-flask-service
    container_name: mermaid-flask-service
    restart: always
    volumes:
      - ./mermaid-flask-service/data:/app/data
    ports:
      - 5002:5002
    networks:
      - ssrf_proxy_network
      - default
```
3. 执行docker compose up
4. 在dify中导入mermaid作图工具.yml和mermaid_agent.yml
   - 把mermaid作图工具创建出来的工作流发布为工具
   - 在mermaid_agent.yml中引用该工具