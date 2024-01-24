from django.conf import settings

from linebot import LineBotApi
from linebot.models import *


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def sendNews(event):
    try:
        message = TemplateSendMessage(
            alt_text = '最新消息',
            template = ButtonsTemplate(
                thumbnail_image_url='https://techexpo.moe.edu.tw/search/images/upload/schools/68/b/2021090903235101_1.jpg',
                title='最新消息',
                text='最新消息來了!\n德明資管系又有新花招!!\n你絕對不能錯過!!!',
                actions=[
                    URITemplateAction(
                        label='一般公告',
                        uri='http://localhost/DMIS_IM/pages/navbar-sublist/News-List/gene.php'
                    ),
                    URITemplateAction(
                        label='招生公告',
                        uri='http://localhost/DMIS_IM/pages/navbar-sublist/News-List/stud.php'
                    ),
                    URITemplateAction(
                        label='徵才資訊',
                        uri='http://localhost/DMIS_IM/pages/navbar-sublist/News-List/invite.php'
                    ),
                    URITemplateAction(
                        label='榮譽榜',
                        uri='http://localhost/DMIS_IM/pages/navbar-sublist/News-List/glory.php'
                    ),
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))   

def sendCourse(event):
    try:
        message = TemplateSendMessage(
            alt_text = '課程資訊',
            template = ButtonsTemplate(
                thumbnail_image_url='https://techexpo.moe.edu.tw/search/images/upload/schools/68/b/2021090903235101_1.jpg',
                title='課程資訊',
                text='準備好了嗎？\n資管系的課程規劃就像歷險般刺激\n讓你一窺資訊科技的奧秘！',
                actions=[
                    URITemplateAction(
                        label='一般規劃',
                        uri='http://localhost/DMIS_IM/pages/navbar-sublist/Course-List/course_planning.php'
                    ),
                    URITemplateAction(
                        label='修業規定',
                        uri='http://localhost/DMIS_IM/pages/navbar-sublist/Course-List/course_guidelines.php'
                    ),
                    URITemplateAction(
                        label='課程地圖',
                        uri='http://localhost/DMIS_IM/pages/navbar-sublist/Course-List/map.php'
                    ),
                    URITemplateAction(
                        label='課程基準表',
                        uri='http://localhost/DMIS_IM/pages/navbar-sublist/Course-List/course_standards.php'
                    ),
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))  

def sendAdmission(event):
    try:
        message = TemplateSendMessage(
            alt_text = '招生資訊',
            template = CarouselTemplate(
                columns = [
                    CarouselColumn(
                        thumbnail_image_url='https://misweb.takming.edu.tw/var/file/31/1031/msys_1031_5305355_93804.png',
                        title='大學部',
                        text='這裡不只有程式碼\n還有夢想的擁抱',
                        actions=[
                            URITemplateAction(
                                label='大學部',
                                uri='http://localhost/DMIS_IM/pages/navbar-sublist/Admissions-List/undergraduate.php'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://media.gq.com.tw/photos/65a1197131c13dcbb074eec0/16:9/w_2560%2Cc_limit/1452604857',
                        title='AI加值智慧製造專班',
                        text='歡迎來到 AI 加值智慧製造專班~',
                        actions=[
                            URITemplateAction(
                                label='AI加值智慧製造專班',
                                uri='http://localhost/DMIS_IM/pages/navbar-sublist/Admissions-List/masterDegree.php'
                            ),
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://www.cio.com.tw/wp-content/uploads/AI-ISO%E6%A8%99%E6%BA%96156496.jpg',
                        title='AI跨領域技優專班',
                        text='快來挑戰自己\n成為 AI 技術的先驅！',
                        actions=[
                            URITemplateAction(
                                label='AI跨領域技優專班',
                                uri='http://localhost/DMIS_IM/pages/navbar-sublist/Admissions-List/aiDegree.php'
                            ),
                        ]
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))  
        
def sendTeacher(event):
    try:
        message = TemplateSendMessage(
            alt_text = '師資簡介',
            template = ButtonsTemplate(
                thumbnail_image_url='https://www.hindustantimes.com/ht-img/img/2023/09/02/1600x900/teachers_day_1693652054152_1693652065719.jpg',
                title='師資簡介',
                text='我們的導師們不只是教學高手\n更是資訊科技的嚮導',
                actions=[
                    URITemplateAction(
                        label='專任教師',
                        uri='http://localhost/DMIS_IM/pages/navbar-sublist/Faculty-List/full_time_teachers.php'
                    ),
                    URITemplateAction(
                        label='兼任教師',
                        uri='http://localhost/DMIS_IM/pages/navbar-sublist/Faculty-List/part_time_teachers.php'
                    ),
                    URITemplateAction(
                        label='退休教師',
                        uri='http://localhost/DMIS_IM/pages/navbar-sublist/Faculty-List/retired_teachers.php'
                    )
                ]
            )
        )
           
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！')) 
        
def sendStudent(event):
    try:
        message = TemplateSendMessage(
            alt_text = '學生專區',
            template = ButtonsTemplate(
                thumbnail_image_url='https://wpvip.edutopia.org/wp-content/uploads/2022/10/shutterstock_1958383675-crop.jpg',
                title='學生專區',
                text='這裡是你的學習遊樂場\n滿滿的資訊、活動和歡笑等著你！',
                actions=[
                    URITemplateAction(
                        label='就學貸款',
                        uri='http://localhost/DMIS_IM/pages/navbar-sublist/Student-List/loans.php'
                    ),
                    URITemplateAction(
                        label='獎助學金',
                        uri='http://localhost/DMIS_IM/pages/navbar-sublist/Student-List/scholarships.php'
                    ),
                    URITemplateAction(
                        label='畢業門檻',
                        uri='http://localhost/DMIS_IM/pages/navbar-sublist/Student-List/graduation.php'
                    ),
                    URITemplateAction(
                        label='考證資訊',
                        uri='http://localhost/DMIS_IM/pages/navbar-sublist/Student-List/certification.php'
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))  

def sendFood(event):
    try:
        message = TextSendMessage(
            text='這裡有口袋名單必備的好味道！',
            quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(label="恩家食堂",text="恩家食堂")
                    ),
                QuickReplyButton(
                    action=MessageAction(label="泛美台式自助餐",text="泛美台式自助餐")
                    ),
                QuickReplyButton(
                    action=MessageAction(label="佳佳義大利麵",text="佳佳義大利麵")
                    ),
                QuickReplyButton(
                    action=MessageAction(label="三顧茅廬-內湖文湖店",text="三顧茅廬-內湖文湖店")
                    ),
                QuickReplyButton(
                    action=MessageAction(label="豬窩窩咖啡廚房",text="豬窩窩咖啡廚房")
                    ),
                QuickReplyButton(
                    action=MessageAction(label="285小老闆",text="285小老闆")
                    ),
                QuickReplyButton(
                    action=MessageAction(label="有人知影快炒",text="有人知影快炒")
                    ),
                QuickReplyButton(
                    action=MessageAction(label="包子&ME嘉義火雞肉飯",text="包子&ME嘉義火雞肉飯")
                    ),
                QuickReplyButton(
                    action=MessageAction(label="來佳海南雞飯",text="來佳海南雞飯")
                    ),
                QuickReplyButton(
                    action=MessageAction(label="日久阿囉哈早餐",text="日久阿囉哈早餐")
                    ),
                ]
            )
        )

        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))   

def sendres1(event):
    try:
        message = LocationSendMessage(
            title = '恩家食堂',
            address = '114台北市內湖區環山路一段92號',
            latitude = 25.08677517190767,
            longitude = 121.56746663832266 
        )

        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))   

def sendres2(event):
    try:
        message = LocationSendMessage(
            title = '泛美台式自助餐',
            address = '114台北市內湖區文湖街71號',
            latitude = 25.086837104168257, 
            longitude = 121.56399425313309
        )

        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))   

def sendres3(event):
    try:
        message = LocationSendMessage(
            title = '佳佳義大利麵',
            address = '114台北市內湖區文湖街67號',
            latitude = 25.08697507097801, 
            longitude = 121.56350791874331, 
        )

        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))   

def sendres4(event):
    try:
        message = LocationSendMessage(
            title = '三顧茅廬-內湖文湖店',
            address = '114台北市內湖區文湖街73號',
            latitude = 25.086784337198793, 
            longitude = 121.56278679097369, 
        )

        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))   

def sendres5(event):
    try:
        message = LocationSendMessage(
            title = '豬窩窩咖啡廚房',
            address = '114台北市內湖區文湖街65號',
            latitude = 25.086928037550397, 
            longitude = 121.56368589546129 
        )

        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))   

def sendres6(event):
    try:
        message = LocationSendMessage(
            title = '285小老闆',
            address = '114台北市內湖區內湖路一段285巷68弄7號',
            latitude = 25.08575307190445, 
            longitude = 121.56719097271251
        )

        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))   

def sendres7(event):
    try:
        message = LocationSendMessage(
            title = '無人知影快炒',
            address = '114台北市內湖區內湖路一段285巷65弄7號',
            latitude = 25.084667908600657, 
            longitude = 121.56723573832254
        )

        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))   

def sendres8(event):
    try:
        message = LocationSendMessage(
            title = '包子&ME 嘉義火雞肉飯',
            address = '114台北市內湖區內湖路一段285巷59弄19號',
            latitude = 25.08388428159525, 
            longitude = 121.56784787462804
        )

        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))   

def sendres9(event):
    try:
        message = LocationSendMessage(
            title = '來佳海南雞飯',
            address = '114台北市內湖區內湖路一段285巷8弄3號',
            latitude = 25.082821409431073, 
            longitude = 121.5663164033996
        )

        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))   

def sendres0(event):
    try:
        message = LocationSendMessage(
            title = '日久阿囉哈早餐',
            address = '114台北市內湖區內湖路一段285巷65弄1號',
            latitude = 25.084709300866436, 
            longitude = 121.56701226352028
        )

        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))   
