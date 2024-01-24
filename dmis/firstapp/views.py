from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage
from module import func

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    mtext = event.message.text
                    if mtext == '最新消息':
                        func.sendNews(event)
    
                    elif mtext == '課程資訊':
                        func.sendCourse(event)
    
                    elif mtext == '招生資訊':
                        func.sendAdmission(event)
    
                    elif mtext == '師資簡介':
                        func.sendTeacher(event)
    
                    elif mtext == '學生專區':
                        func.sendStudent(event)
                    
                    if mtext == '美食推薦':
                        func.sendFood(event)
                        
        return HttpResponse()  
    
    else:
        return HttpResponseBadRequest()