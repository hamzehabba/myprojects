import aiohttp
import asyncio
import time


# دریافت قیمت بیتکوین از بایننس به صورت async
async def get_bitcoin_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                price = data['price']
                return float(price)
            else:
                print("Error fetching price from Binance")
                return None


# async def get_bitcoin_price():
#     url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
#     prices = []
#
#     async with aiohttp.ClientSession() as session:
#         for _ in range(5):  # 5 درخواست در هر ثانیه
#             async with session.get(url) as response:
#                 if response.status == 200:
#                     data = await response.json()
#                     price = float(data['price'])
#                     prices.append(price)  # ذخیره قیمت دریافت شده
#                 else:
#                     print(f"Error fetching price from Binance: {response.status}")
#
#                 # خواب کوتاه برای اینکه درخواست‌ها با فاصله کوتاه ارسال شوند (0.2 ثانیه برای 5 درخواست در هر ثانیه)
#                 await asyncio.sleep(0.1)
#
#     return prices  # بازگرداندن لیست قیمت‌ها


# ارسال پیام به تلگرام به صورت async
async def send_to_telegram_async(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {'chat_id': chat_id, 'text': message}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=params) as response:
            if response.status == 200:
                print("پیام با موفقیت ارسال شد")
            else:
                print(f"Error sending message, status code: {response.status}")

from datetime import datetime
def convert_count(hour):
    if 12 <= hour < 14:
        return 5
    elif 14 <= hour < 16:
        return 7
    elif 16 <= hour < 18:
        return 7
    elif 18 <= hour < 20:
        return 9
    elif 20 <= hour < 21:
        return 7
    elif 21 <= hour < 22:
        return 6
    elif 22 <= hour < 23:
        return 7
    elif 23 <= hour < 0:
        return 8
    elif 0 <= hour < 1:
        return 6
    elif 1 <= hour < 2:
        return 7
    elif 2 <= hour < 3:
        return 5
    elif 3 <= hour < 4:
        return 7
    elif 4 <= hour < 5:
        return 5
    elif 5 <= hour < 6:
        return 10
    elif 6 <= hour < 7:
        return 7
    elif 7 <= hour < 9:
        return 9
    elif 9 <= hour < 10:
        return 5
    elif 10 <= hour < 11:
        return 9
    elif 11 <= hour < 12:
        return 8
    else:
        return -1


def append_if_in_range(count, sum3, first_list):
    first_list.append(count)
    if len(first_list) > 100:
        first_list.pop(0)
    if first_list[-1] == 0:
        count = first_list[-2]

        # اگر لیست خالی نیست و count بزرگتر از آخرین عنصر لیست است
        if len(sum3) > 0 and count > max(sum3):
            sum3.clear()  # اگر count بزرگ‌تر بود، لیست را خالی کن
            # اگر لیست خالی نیست و count کوچکتر از کوچکترین عنصر لیست است
        elif len(sum3) > 0 and count < min(sum3):
            sum3.clear()  # اگر count کوچکتر بود، لیست را خالی کن
        sum3.append(count)  # سپس count را به لیست اضافه کن

    # بررسی تعداد تکرارها در sum3
    if len(sum3) == 3:
        return sum3  # اگر عددی 3 بار تکرار شد، لیست را برگردان


# حلقه اصلی برای به‌روزرسانی قیمت بیت‌کوین و بررسی پیام‌های تلگرام
async def main():
    bot_token = '7390882203:AAFap8oDw5Ole-dfmX46jZe6oN8Z6zzxmPo'
    chat_id = '@bitcoin_sadtaie2'
    notification_chat_id = '@getmessage2'
    updowntakibit= '@updownbtcust'
    message_count = 1
    down_count = 0
    up_count = 0
    # final_count = 4
    previous_price = None
    threshold = 40
    messages = []
    messages2=[]
    up_down_for_another_chanel = []
    massage_hour = []

    final_count = 4

    first_list = []
    sum3=[]
    while True:
        current_time = datetime.now()
        current_hour = current_time.hour
        count_with_hour = convert_count(current_hour)
        try:
            current_price = await get_bitcoin_price()
            # for current_price in current_prices:
            if current_price is None:
                await asyncio.sleep(5)
                continue

                # بررسی تغییرات قیمت
            if previous_price is not None:
                price_difference = current_price - previous_price
                if abs(price_difference) >= threshold:
                    if current_price > previous_price:
                        message = f" {message_count} : BTC-price: {current_price} - UP"
                    else:
                        message = f"{message_count} : BTC-price: {current_price} - DOWN"
                    await send_to_telegram_async(bot_token, chat_id, message)
                    message_count += 1

                    message = message.split()
                    messages.append(message)
                    messages2.append(message)
                elif abs(price_difference) > threshold + 3 or abs(price_difference) < threshold:
                    continue

            previous_price = current_price


            # count_with_hour = 4
            if len(messages2) > count_with_hour:
                messages2.pop(0)
            if len(messages2) >= count_with_hour:

                # f = len(messages2) - count_with_hour
                # b = messages2[f:]
                for p in messages2:
                    massage_hour.append(p[-1])

                bi = all('UP' == i for i in massage_hour) or all(
                    'DOWN' == i for i in massage_hour)
                if bi and len(massage_hour) >= count_with_hour:
                    taki_message = f"{massage_hour[0]} : {len(massage_hour)}"
                    await send_to_telegram_async(bot_token, updowntakibit, taki_message)
                else:
                    massage_hour = []
            # مقایسه پیام آخر با پنجمین پیام قبل و ارسال پیام به کانال دوم
            if len(messages) > 5:
                messages.pop(0)
            if len(messages) == 5:
                last_message = messages[-1]
                fifth_last_message = messages[-5]
                last_message_count = last_message[0]
                fifth_last_message_count = fifth_last_message[0]
                up_down = last_message[-1]

                if "UP" in last_message and "UP" in fifth_last_message:
                    similar_message = f"btcusdt (up) number : {last_message_count} - {fifth_last_message_count} "
                    await send_to_telegram_async(bot_token, chat_id, similar_message)
                    up_down_for_another_chanel.append(up_down)
                    down_count += 1
                    if down_count > 2:
                        sum_number = f"number : {down_count}"
                        await send_to_telegram_async(bot_token, chat_id, sum_number)


                elif "DOWN" in last_message and "DOWN" in fifth_last_message:
                    similar_message = f"btcusdt (down) number : {last_message_count} - {fifth_last_message_count} "
                    await send_to_telegram_async(bot_token, chat_id, similar_message)
                    up_down_for_another_chanel.append(up_down)
                    down_count += 1
                    if down_count > 2:
                        sum_number = f"number : {down_count}"
                        await send_to_telegram_async(bot_token, chat_id, sum_number)


                elif ("UP" in last_message and "DOWN" in fifth_last_message) or (
                        "DOWN" in last_message and "UP" in fifth_last_message):
                    down_count = 0
                    up_count = 0
                    up_down_for_another_chanel = []

                if down_count == final_count:
                    final_message = f"number : 1-4 : {up_down_for_another_chanel}"
                    await send_to_telegram_async(bot_token, notification_chat_id, final_message)

                elif down_count > final_count:
                    final_message = f'number: {down_count} : {up_down_for_another_chanel}'
                    await send_to_telegram_async(bot_token, notification_chat_id, final_message)

                send_sum_3_number=append_if_in_range(down_count,sum3,first_list)
                if send_sum_3_number:
                    sum3_number = f'سه بار: {sum3[0]} اتفاق افتاد'
                    await send_to_telegram_async(bot_token, notification_chat_id, sum3_number)

            await asyncio.sleep(0.2)  # تاخیر کوتاه بین هر حلقه

        except Exception as e:
            print(f"خطا رخ داد: {e}")
            await asyncio.sleep(5)


# اجرای main به صورت async
if __name__ == "__main__":
    asyncio.run(main())

