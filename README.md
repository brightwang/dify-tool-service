# 说明
本仓库为B站：AI带路党Pro相关Dify实战教程配套参考

### dify-mermaid-flask-service
为AI带路党Pro视频<a href="https://www.bilibili.com/video/BV1PntFeqEe9" target="_blank">Dify实战教程:搭建AI自动生成流程图、序列图、甘特图等图表agent</a>准备

#### 使用指南

1. 拷贝mermaid-flask-service到dify的docker目录中
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
   - 把mermaid作图工具创建出来的工作流发布为工具mermaid_service，并描述设置为"save mermain content and get svg url"
   - 在mermaid_agent中引用该工具mermaid_service

### dify-markmap-flask-service
为AI带路党Pro视频<a href="https://www.bilibili.com/video/BV1hMpGeiEaF" target="_blank">Dify实战: 手把手教你使用Dify搭建AI自动生成思维导图的应用</a>准备

#### 使用指南

1. 拷贝markmap-flask-service到dify的docker目录中
2. 修改docker-compose.yaml文件，在services字段下新增一个markmap-flask-service子级，具体配置如下。
```yaml
  markmap-flask-service:
    build: ./markmap-flask-service
    container_name: markmap-flask-service
    restart: always
    volumes:
      - ./markmap-flask-service/data:/app/data
    ports:
      - 5003:5003
    networks:
      - ssrf_proxy_network
      - default
```
3. 执行docker compose up
4. 在dify中导入markmap思维导图工具.yml和markmap_agent.yml
   - 把markmap思维导图工具创建出来的工作流发布为工具save_markmap，并将工具描述改为"save markmap content and get url"
   - 在markmap_agent删除旧工具，并重新引用工具save_markmap

### dify-marp-flask-service
为AI带路党Pro视频<a href="https://www.bilibili.com/video/BV12ZnRe5ERh" target="_blank">Dify实战: 手把手教你用 Dify 和 Marp 搭建AI自动生成 PPT 应用</a>准备

#### 使用指南

1. 拷贝marp-flask-service到dify的docker目录中
2. 修改docker-compose.yaml文件，在services字段下新增一个marp-flask-service子级，具体配置如下。
```yaml
  marp-flask-service:
    build: ./marp-flask-service
    container_name: marp-flask-service
    restart: always
    volumes:
      - ./marp-flask-service/data:/app/data
    ports:
      - 5004:5004
  marp:
    image: marpteam/marp-cli:latest
    container_name: marp
    restart: always
    volumes:
      - ./marp-flask-service/data:/home/marp/app
    ports:
      - 5005:8080
    environment:
      - LANG=${LANG}
    command: -s .
    networks:
      - ssrf_proxy_network
      - default
```
3. 执行docker compose up
4. 在dify中导入marp的PPT工具.yml和marp_agent.yml
   - 把marp的PPT工具创建出来的工作流发布为工具,名字设置为save_marp_content，工具描述为"保存marp ppt内容，并获得ppt链接"
   - 在marp_agent.yml创建出的agent里删除旧工具，重新添加引用save_marp_content工具

### dify-quiz-flask-service 

视频<a href="https://www.bilibili.com/video/BV12ZnRe5ERh" target="_blank">让AI给你出试卷-Dify实战：搭建自动生成试卷的Agent</a>相关代码

1. 拷贝quiz-flask-service到dify的docker目录中
2. 修改docker-compose.yaml文件，在services字段下新增一个marp-flask-service子级，具体配置如下。
```yaml
  quiz-flask-service:
    build: ./quiz-flask-service
    container_name: quiz-flask-service
    restart: always
    volumes:
      - ./quiz-flask-service/data:/app/data
    ports:
      - 5006:5006
```
3. 执行docker compose up
4. 在dify中导入创建试卷工作流.yml和保存试卷agent.yml
   - 把创建试卷工作流.yml创建出来的工作流发布为工具,名字设置为save_quiz_and_get_url，工具描述为"保存试卷并获取试卷url"
   - 在保存试卷agent.yml创建出的agent里删除旧工具，重新添加引用save_quiz_and_get_url工具
""
