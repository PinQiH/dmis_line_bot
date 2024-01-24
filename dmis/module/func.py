from django.conf import settings

from linebot import LineBotApi
from linebot.models import TemplateSendMessage, TextSendMessage, ButtonsTemplate, MessageTemplateAction, URITemplateAction, PostbackTemplateAction


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def sendNews(event):
    try:
        message = TemplateSendMessage(
            alt_text = '最新消息',
            template = ButtonsTemplate(
                thumbnail_image_url='https://techexpo.moe.edu.tw/search/images/upload/schools/68/b/2021090903235101_1.jpg',
                title='最新消息',
                text='最新消息來了!\n德明資管系又有新花招了!!\n你絕對不能錯過!!!',
                actions=[
                    MessageTemplateAction(
                        label='最新消息',
                        text='@最新消息'
                    ),
                    URITemplateAction(
                        label='連結網頁',
                        uri='http://localhost/DMIS_IM/#'
                    ),
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))   

def sendCourse(event):
    try:
        message = ImageSendMessage(
            original_content_url = "https://imgur.com/TcSD7FL.png",
            preview_image_url = "https://imgur.com/TcSD7FL.png"
           )
        
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))  

def sendAdmission(event):
    try:
        message = StickerSendMessage(
             package_id='11539',
             sticker_id='52114124'         
             )
        
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))  
        
def sendTeacher(event):
    try:
        message = [
            TextSendMessage(
                text='嚕喵毛，換毛季是打掃季！',
            ),
            ImageSendMessage(
                original_content_url = "https://imgur.com/TcSD7FL.png",
                preview_image_url = "https://imgur.com/TcSD7FL.png"
            ),
            StickerSendMessage(
                 package_id='11539',
                 sticker_id='52114124'         
            )
            
        ]
           
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！')) 
        
def sendStudent(event):
    try:
        message = LocationSendMessage(
            title = '台北教育大學',
            address = '台北市大安區和平東路二段134號',
            latitude = 25.024163 ,#緯度
            longitude = 121.544888 #經度

           )
        
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))  

def sendFood(event):
    try:
        message = TextSendMessage(
            text='嚕喵毛，今天要打掃哪裡呢？',
            quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(label="客廳",text="客廳")
                    ),
                QuickReplyButton(
                    action=MessageAction(label="房間",text="房間")
                    ),
                QuickReplyButton(
                    action=MessageAction(label="廚房",text="廚房")
                    ),
                QuickReplyButton(
                    action=MessageAction(label="廁所",text="廁所")
                    ),
                QuickReplyButton(
                    action=MessageAction(label="不想打掃",text="不想打掃")
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))   