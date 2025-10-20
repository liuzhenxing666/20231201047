"""刘振兴_20231201047_项目 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def student_info(request):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>学生信息 - 医疗项目</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #f5f5f5;
            }
            .container {
                max-width: 600px;
                margin: 0 auto;
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #2c3e50;
                text-align: center;
                border-bottom: 2px solid #3498db;
                padding-bottom: 10px;
            }
            .info-item {
                margin: 15px 0;
                padding: 10px;
                background-color: #f8f9fa;
                border-left: 4px solid #3498db;
            }
            .label {
                font-weight: bold;
                color: #2c3e50;
            }
            .value {
                color: #34495e;
            }
            .timestamp {
                text-align: center;
                color: #7f8c8d;
                font-size: 14px;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>学生信息</h1>
            <div class="info-item">
                <span class="label">姓名：</span>
                <span class="value">刘振兴</span>
            </div>
            <div class="info-item">
                <span class="label">学号：</span>
                <span class="value">20231201047</span>
            </div>
            <div class="info-item">
                <span class="label">班级：</span>
                <span class="value">23医信</span>
            </div>
            <div class="info-item">
                <span class="label">项目：</span>
                <span class="value">医疗管理系统</span>
            </div>
            <div class="timestamp">
                页面生成时间：<span id="current-time"></span>
            </div>
        </div>
        <script>
            document.getElementById('current-time').textContent = new Date().toLocaleString('zh-CN');
        </script>
    </body>
    </html>
    """
    return HttpResponse(html_content)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', student_info, name='student_info'),
    path('hello/', include('hello.urls')),
]