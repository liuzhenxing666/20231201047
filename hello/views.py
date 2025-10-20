from django.http import Http404, HttpResponse
import os

# Create your views here.
def index(request):
    # 直接读取并返回HTML文件内容
    html_file_path = os.path.join(os.path.dirname(__file__), 'index.html')
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    return HttpResponse(html_content)

# The texts are much longer in reality, but have
# been shortened here to save space
texts = ["Text 1", "Text 2", "Text 3"]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")