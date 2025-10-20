# Hello App - Django项目

这是一个独立的Django项目，包含一个名为"hello"的应用。

## 项目结构

```
hello_app_project/
├── manage.py          # Django项目管理脚本
├── db.sqlite3         # SQLite数据库文件
├── requirements.txt   # Python依赖包
├── mysite/            # Django项目配置
│   ├── __init__.py
│   ├── settings.py    # 项目设置
│   ├── urls.py        # 主URL路由配置
│   └── wsgi.py        # WSGI配置
└── hello/             # Hello应用
    ├── __init__.py
    ├── admin.py       # 管理后台
    ├── apps.py        # 应用配置
    ├── migrations/    # 数据库迁移
    ├── models.py      # 数据模型
    ├── tests.py       # 测试文件
    ├── urls.py        # 应用URL路由
    └── views.py       # 视图函数
```

## 功能特性

- **响应式设计** - 适配各种设备屏幕
- **美观界面** - 渐变背景和现代化卡片设计
- **完整导航** - 首页、关于、联系页面之间的导航
- **学生信息展示** - 显示个人信息（姓名、学号、班级）
- **动态时间显示** - 实时显示页面生成时间

## 安装和运行

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 运行开发服务器
```bash
python manage.py runserver
```

### 3. 访问应用
- **Hello应用首页**: http://localhost:8000/hello/
- **关于页面**: http://localhost:8000/hello/about/
- **联系页面**: http://localhost:8000/hello/contact/
- **原项目首页**: http://localhost:8000/

## 技术栈

- **后端**: Django 4.2.8
- **数据库**: SQLite3
- **前端**: HTML5, CSS3, JavaScript
- **模板引擎**: Django模板系统

## 开发者信息

- **姓名**: 刘振兴
- **学号**: 20231201047
- **班级**: 23医信

## 许可证

本项目使用MIT许可证。