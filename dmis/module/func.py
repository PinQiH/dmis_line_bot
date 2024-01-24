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