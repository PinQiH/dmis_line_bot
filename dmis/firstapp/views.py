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
                    
                    elif mtext == '美食推薦':
                        func.sendFood(event)
                    
                    elif mtext == '恩家食堂':
                        func.sendres1(event)
                    
                    elif mtext == '泛美台式自助餐':
                        func.sendres2(event)

                    elif mtext == '佳佳義大利麵':
                        func.sendres3(event)

                    elif mtext == '三顧茅廬-內湖文湖店':
                        func.sendres4(event)

                    elif mtext == '豬窩窩咖啡廚房':
                        func.sendres5(event)

                    elif mtext == '285小老闆':
                        func.sendres6(event)

                    elif mtext == '有人知影快炒':
                        func.sendres7(event)

                    elif mtext == '包子&ME嘉義火雞肉飯':
                        func.sendres8(event)

                    elif mtext == '來佳海南雞飯':
                        func.sendres9(event)

                    elif mtext == '日久阿囉哈早餐':
                        func.sendres0(event)
                        
        return HttpResponse()  
    
    else:
        return HttpResponseBadRequest()