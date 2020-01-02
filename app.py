from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, ImageSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('ZA8ys3+b/PVTYr9Fj+HWiXwC3+kFppcKWIblYvfmmFmJB4rgUzGqC4QsMRuQDGUPA4YM6Y8PxcHKZPOjQ7O7oKUi6XUXuGoQTeneopq5TvYkKEJlsjGL7vA6k1aNLtpsivInblmkk2rJkt+c2ewsuAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0d445d4a1013320bf7322bdd4904250c')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    msg = event.message.text
    reply = '我不懂你說什麼 (磨下巴'

    


    if msg in ['碰', 'bang', 'Bang', 'ㄅㄧㄤˋ']:
        sticker_message = StickerSendMessage(
            package_id='11537',
            sticker_id='52002757'
        )

        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return

    if msg in ['裝死']:
        image_message = ImageSendMessage(
        original_content_url='https://line-bot-2020.herokuapp.com/image/ori_dead.jpg',
        preview_image_url='https://line-bot-2020.herokuapp.com/image/pre_dead.jpg'
        )

        line_bot_api.reply_message(
        event.reply_token,
        image_message)
        return

    if msg in ['hi', 'Hi', '你好', '哈囉']:
        reply = '你好'
    elif msg == '握手':
        reply = '地板好滑呀'
    elif msg == '換手':
        reply = '(抓癢'
    elif msg == '坐下':
        reply = '?'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply))


if __name__ == "__main__":
    app.run()