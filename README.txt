一、作业要求及完成情况
【x】  1. 官网首页动态轮播图
【x】  2. 类似京东商品组合搜索
【 】  3. 瀑布流图片                               # 未完成
【x】  4. 动态加载图片
【x】  5. 基于Admin后台管理页面处理，前端显示


二、验证
主页: http://127.0.0.1:8000/
搜索页：http://127.0.0.1:8000/search/teacher-0-0-0.html


三、文件夹说明
│  .gitignore
│  db.sqlite3
│  manage.py
│  README.docx                       # 验证过程
│  
├─edu_app
│  │  admin.py
│  │  apps.py
│  │  models.py
│  │  tests.py
│  │  views.py
│  │  __init__.py
│  │  
│  ├─migrations
│  │  │  __init__.py
│  │  │  
│  │  └─__pycache__
│  │          __init__.cpython-36.pyc
│  │          
│  ├─templatetags
│  │  │  searchbox.py                                   # 组合搜索使用了simple_tag
│  │  │  
│  │  └─__pycache__
│  │          searchbox.cpython-36.pyc
│  │          
│          
├─edu_website
│  │  settings.py
│  │  urls.py
│  │  wsgi.py
│  │  __init__.py
│  │  
│          
├─repository
│  │  admin.py
│  │  apps.py
│  │  models.py                                         # 另起了一个repository的app进行统一数据库存储
│  │  tests.py
│  │  views.py
│  │  __init__.py
│  │  
│          
├─static
│  │  jquery-3.3.1.js
│  │  
│  ├─css
│  │  │  grid.css
│  │  │  reset.css
│  │  │  style.css
│  │  │  
│  │  └─ie
│  │          ie6.css
│  │          
│  ├─media
│  │  ├─avatars                                   # 头像
│  │  │      1.jpg
│  │  │      2.jpeg
│  │  │      3.jpg
│  │  │      4.jpg
│  │  │      default.jpg
│  │  │      
│  │  └─imgs                                         # 轮播图
│  │          1.jpg
│  │          2.jpg
│  │          3.jpg
│  │          4.jpg
│  │          5.jpg
│  │          6.jpg
│  │          7.jpg
│  │          
│  └─plugins
│      └─bootstrap-3.3.7-dist
│          ├─css
│          │      bootstrap-theme.css
│          │      bootstrap-theme.css.map
│          │      bootstrap-theme.min.css
│          │      bootstrap-theme.min.css.map
│          │      bootstrap.css
│          │      bootstrap.css.map
│          │      bootstrap.min.css
│          │      bootstrap.min.css.map
│          │      
│          ├─fonts
│          │      glyphicons-halflings-regular.eot
│          │      glyphicons-halflings-regular.svg
│          │      glyphicons-halflings-regular.ttf
│          │      glyphicons-halflings-regular.woff
│          │      glyphicons-halflings-regular.woff2
│          │      
│          └─js
│                  bootstrap.js
│                  bootstrap.min.js
│                  npm.js
│                  
└─templates
    ├─edu_pages
    │      edu_search.html                              # 搜索页
    │      index.html                                    # 主页
    │      
    ├─include
    │      search.html
    │      轮播图.html
    │      
    └─layout
            layout_index.html
            
