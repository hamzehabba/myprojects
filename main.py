# from requests import post, get
# from bs4 import BeautifulSoup
#
# botUrl = "https://www.salamati24.com/fa/profile/241376/%D8%AF%DA%A9%D8%AA%D8%B1-%D9%86%D8%A7%D9%87%DB%8C%D8%AF-%D9%86%DB%8C%DA%A9-%D9%81%D8%B1%D8%AC%D8%A7%D9%85"
#
# # GET COOKIES:
#
#
# def getCookies(var) -> dict:
#     r = get(var)
#     soup = BeautifulSoup(r.text, 'html.parser')
#     return r.cookies, var, soup.find(class_="clinic-booking").find("button", {"type": "button"})['data-link']
#
# # GET DAYS:
#
#
# def getFirstTime(var) -> list:
#     url = "https://www.salamati24.com" + var[2]
#     r = get(url, cookies=var[0])
#     soup = BeautifulSoup(r.text, 'html.parser')
#     # inputList = list(set(soup.find_all("input", class_="radio")) - set(soup.find_all("input", {"disabled" : "disabled"}, class_="radio")))
#     while len(soup.find_all("input", class_="radio")) == 0:
#         r = get(url, cookies=var[0])
#         soup = BeautifulSoup(r.text, 'html.parser')
#     myInput = soup.find("input", class_="radio")
#     try:
#         can = myInput.has_attr('disabled')
#     except:
#         can = True
#     while can:
#         try:
#             myInput = myInput.find_next("input", class_="radio")
#             can = myInput.has_attr('disabled')
#         except:
#             can = True
#     return myInput, myInput, var[1].split("/")[-2], soup.find("input", {"name": "_token"})['value'], var[0], soup.find("input", {"id": "uniq"})['value'], var[1]
#
# # GET THE VISIT:
#
#
# def getVisit(var, information):
#     BBBB = var[0]
#     for i in range(0, len(information)):
#         r = get(f"https://www.salamati24.com/fa/appointment-step02?_token={var[3]}&DoctorAppointmentId={BBBB['id']}&uniq={var[5]}&newtok={var[1]['data-newtok']}&forapp=1&DoctorService=0&DoctorAppointment={BBBB['id']}", cookies=var[4], headers={
#             "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
#             "referer": var[6],
#             "content-type": "multipart/form-data; boundary=----WebKitFormBoundaryxvEBFbUzUVnirlv3",
#             "origin": "https://www.salamati24.com",
#         })
#         if r.status_code == 200:
#             with open(str(information[i]['mobile']) + ".html", "w", encoding="utf-8") as file:
#                 file.write(r.text)
#
#             # file = open(str(information[i]['mobile']) + ".html", "w")
#             # file.write(r.text)
#             print("True:", str(information[i]['mobile']))
#         else:
#             with open(str(information[i]['mobile']) + ".html", "w", encoding="utf-8") as file:
#                 file.write(r.text)
#
#             # file = open(str(information[i]['mobile']) + ".html", "w")
#             # file.write(r.text)
#             print("False:", str(information[i]['mobile']))
#         BBBB = BBBB.find_next("input", class_="radio")
#
# # SEND INFORMATION FOR VISIT:
#
#
# def sendInformation(var, information):
#     data = []
#     for i in range(0, len(information)):
#         data.append({
#             "_token": var[3],
#             "_token": var[3],
#             "doctor_service": 0,
#             "doctor_id": var[2],
#             "doctor_appointment_id": var[0],
#             "doctor_appointment_tok": var[1],
#             "for_who": 1,
#             "forapp": 1,
#             "mobile": information[i]['mobile'],
#             "countryCode": 98,
#             "appointment_for": information[i]['appointment_for'],
#             "birth_dateDay": information[i]['birth_dateDay'],
#             "birth_dateMonth": information[i]['birth_dateMonth'],
#             "birth_dateYear": information[i]['birth_dateYear'],
#             "gender": information[i]['gender'],
#             "payment_method": 0,
#             "visit_price": 0,
#         })
#     for i in range(0, len(data)):
#         r = post("https://www.salamati24.com/fa/new-appointment/"+var[5], data=data[i], headers={
#             "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
#             "referer": f"https://www.salamati24.com/fa/appointment-step02?_token={data[i]['_token']}&DoctorAppointmentId={data[i]['doctor_appointment_id']}&newtok={data[i]['doctor_appointment_tok']}&forapp={data[i]['forapp']}&DoctorService={data[i]['doctor_service']}&DoctorAppointment={data[i]['doctor_appointment_id']}",
#             "content-type": "multipart/form-data; boundary=----WebKitFormBoundaryxvEBFbUzUVnirlv3",
#             "origin": "https://www.salamati24.com",
#             "cookie": "_ga=GA1.1.1325825870.1724517715; _ga_Z43RYYVZSJ=GS1.1.1724908242.7.1.1724908351.60.0.0; XSRF-TOKEN=eyJpdiI6Ilk5Q0EyQjg2YU1DWDZjaFhVdHkxbHc9PSIsInZhbHVlIjoiSHBSbHdwZlFCMmhvSDBYTjJYVGZ2aFp5UCt4MVRDQ2JZRnNGSmlBY2dQTlVDTXhwTG5BbXI0RkdpS0s3NTZoYkJqZ3RmaUt6ZTQ4Ty9ONXhwME9QdE8zS2ZKbHFxVjREMExtT1NDZEVNQk4xKy9IZW9MeFZudzlHSEhqOGEzU1IiLCJtYWMiOiJlMjFhYjE0YzgyNmEyNjE2YTg5ODE4YjIzYjk2MWI4OTJjMGJhODE2NDJhZWNkMjc4NGQzZDBmM2MwYWVlMzliIiwidGFnIjoiIn0%3D; salamati24_session=eyJpdiI6IlhDdUs0KzhZNE9nWlQzTW5vTUk2eHc9PSIsInZhbHVlIjoidlpQRDd2c25rbUxtMHQ3QmVSZk9CYU05Y0VNVnErOGFpTytGZEc1cXIwNm5KWll0WEdDaFdEaHRWdTd1Zi9iR2pTSlA1Sm9rWkpEbkoxR2tscFVDNE42eWFVYis5UWlBY1VXMjF5Yi9valRGdmZVSm1IUkZ2TGdPeHU1M0JXWFMiLCJtYWMiOiJkOWMxYjFmYjlhYmExNjNjZDJiMGJkMDcwMzAzM2QzZGVkMzFkZDhiMGRkNmIzNDhiZDU2MDQ2ZGU3OGZhYjBlIiwidGFnIjoiIn0%3D"
#
#         })
#         if r.status_code == 200:
#             with open(str(information[i]['mobile']) + ".html", "w", encoding="utf-8") as file:
#                 file.write(r.text)
#
#             # file = open(str(data[i]['mobile']) + ".html", "w")
#             # file.write(r.text)
#             print("True:", str(data[i]['mobile']))
#         else:
#             with open(str(information[i]['mobile']) + ".html", "w", encoding="utf-8") as file:
#                 file.write(r.text)
#             # file = open(str(data[i]['mobile']) + ".html", "w")
#             # file.write(r.text)
#             print("False:", str(data[i]['mobile']))
#
#
# # RUN:
# res = getVisit(
#     getFirstTime(
#         getCookies(
#             botUrl
#         )
#     ),
#     [
#         {
#             "mobile": "9112857001",
#             "appointment_for": "زهرا خشنود",
#             "birth_dateDay": 2,
#             "birth_dateMonth": 1,
#             "birth_dateYear": 1400,
#             "gender": 1
#         },
#         {
#             "mobile": "9112857002",
#             "appointment_for": "رضا باقری",
#             "birth_dateDay": 2,
#             "birth_dateMonth": 1,
#             "birth_dateYear": 1400,
#             "gender": 1
#         },
#         {
#             "mobile": "9112857003",
#             "appointment_for": "مریم بابایی",
#             "birth_dateDay": 2,
#             "birth_dateMonth": 1,
#             "birth_dateYear": 1400,
#             "gender": 1
#         },
#         {
#             "mobile": "9112857004",
#             "appointment_for": "زهرا قربانی",
#             "birth_dateDay": 2,
#             "birth_dateMonth": 1,
#             "birth_dateYear": 1400,
#             "gender": 1
#         },
#         {
#             "mobile": "9112857005",
#             "appointment_for": "عباس کرمی",
#             "birth_dateDay": 2,
#             "birth_dateMonth": 1,
#             "birth_dateYear": 1400,
#             "gender": 1
#         },
#         {
#             "mobile": "9112857006",
#             "appointment_for": "لیلا شادمان",
#             "birth_dateDay": 2,
#             "birth_dateMonth": 1,
#             "birth_dateYear": 1400,
#             "gender": 1
#         },
#         {
#             "mobile": "9112857007",
#             "appointment_for": "زینب کاملیان",
#             "birth_dateDay": 2,
#             "birth_dateMonth": 1,
#             "birth_dateYear": 1400,
#             "gender": 1
#         },
#         {
#             "mobile": "9112857008",
#             "appointment_for": "عباس زواری",
#             "birth_dateDay": 2,
#             "birth_dateMonth": 1,
#             "birth_dateYear": 1400,
#             "gender": 1
#         },
#         {
#             "mobile": "9112857009",
#             "appointment_for": "سحر عباس زاده",
#             "birth_dateDay": 2,
#             "birth_dateMonth": 1,
#             "birth_dateYear": 1400,
#             "gender": 1
#         },
#         {
#             "mobile": "9112857000",
#             "appointment_for": "مجید قنادزاده",
#             "birth_dateDay": 2,
#             "birth_dateMonth": 1,
#             "birth_dateYear": 1400,
#             "gender": 1
#         }
#     ]
# )
# # print((res))


import asyncio
import aiohttp
import aiofiles

from bs4 import BeautifulSoup

botUrl = "https://www.salamati24.com/fa/profile/241376/%D8%AF%DA%A9%D8%AA%D8%B1-%D9%86%D8%A7%D9%87%DB%8C%D8%AF-%D9%86%DB%8C%DA%A9-%D9%81%D8%B1%D8%AC%D8%A7%D9%85"

# GET COOKIES:
async def getCookies(session, var) -> dict:
    async with session.get(var) as r:
        soup = BeautifulSoup(await r.text(), 'html.parser')
        return r.cookies, var, soup.find(class_="clinic-booking").find("button", {"type": "button"})['data-link']

# GET DAYS:
async def getFirstTime(session, var) -> list:
    url = "https://www.salamati24.com" + var[2]
    async with session.get(url, cookies=var[0]) as r:
        soup = BeautifulSoup(await r.text(), 'html.parser')
        while len(soup.find_all("input", class_="radio")) == 0:
            async with session.get(url, cookies=var[0]) as r:
                soup = BeautifulSoup(await r.text(), 'html.parser')
        myInput = soup.find("input", class_="radio")
        try:
            can = myInput.has_attr('disabled')
        except:
            can = True
        while can:
            try:
                myInput = myInput.find_next("input", class_="radio")
                can = myInput.has_attr('disabled')
            except:
                can = True
        return myInput, myInput, var[1].split("/")[-2], soup.find("input", {"name": "_token"})['value'], var[0], soup.find("input", {"id": "uniq"})['value'], var[1]

# GET THE VISIT:
async def getVisit(session, var, information):
    BBBB = var[0]
    tasks = []
    for info in information:
        url = f"https://www.salamati24.com/fa/appointment-step02?_token={var[3]}&DoctorAppointmentId={BBBB['id']}&uniq={var[5]}&newtok={var[1]['data-newtok']}&forapp=1&DoctorService=0&DoctorAppointment={BBBB['id']}"
        task = asyncio.create_task(fetchVisit(session, url, var, info))
        tasks.append(task)
        BBBB = BBBB.find_next("input", class_="radio")
    await asyncio.gather(*tasks)

# Helper function to fetch each visit
async def fetchVisit(session, url, var, info):
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "referer": var[6],
        "content-type": "multipart/form-data; boundary=----WebKitFormBoundaryxvEBFbUzUVnirlv3",
        "origin": "https://www.salamati24.com",
    }
    async with session.get(url, cookies=var[4], headers=headers) as r:
        filename = f"{info['mobile']}.html"
        async with aiofiles.open(filename, 'w', encoding='utf-8') as file:
            await file.write(await r.text())
        print(f"{'True' if r.status == 200 else 'False'}: {info['mobile']}")

# SEND INFORMATION FOR VISIT:
async def sendInformation(session, var, information):
    data = []
    for info in information:
        data.append({
            "_token": var[3],
            "doctor_service": 0,
            "doctor_id": var[2],
            "doctor_appointment_id": var[0],
            "doctor_appointment_tok": var[1],
            "for_who": 1,
            "forapp": 1,
            "mobile": info['mobile'],
            "countryCode": 98,
            "appointment_for": info['appointment_for'],
            "birth_dateDay": info['birth_dateDay'],
            "birth_dateMonth": info['birth_dateMonth'],
            "birth_dateYear": info['birth_dateYear'],
            "gender": info['gender'],
            "payment_method": 0,
            "visit_price": 0,
        })
    tasks = [asyncio.create_task(postAppointment(session, var[5], d)) for d in data]
    await asyncio.gather(*tasks)

# Helper function to post each appointment
async def postAppointment(session, uniq, data):
    url = f"https://www.salamati24.com/fa/new-appointment/{uniq}"
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "referer": f"https://www.salamati24.com/fa/appointment-step02?_token={data['_token']}&DoctorAppointmentId={data['doctor_appointment_id']}&newtok={data['doctor_appointment_tok']}&forapp={data['forapp']}&DoctorService={data['doctor_service']}&DoctorAppointment={data['doctor_appointment_id']}",
        "content-type": "multipart/form-data; boundary=----WebKitFormBoundaryxvEBFbUzUVnirlv3",
        "origin": "https://www.salamati24.com",
    }
    async with session.post(url, data=data, headers=headers) as r:
        filename = f"{data['mobile']}.html"
        async with aiofiles.open(filename, 'w', encoding='utf-8') as file:
            await file.write(await r.text())
        print(f"{'True' if r.status == 200 else 'False'}: {data['mobile']}")

# Main entry point
async def main():
    async with aiohttp.ClientSession() as session:
        cookies_data = await getCookies(session, botUrl)
        first_time_data = await getFirstTime(session, cookies_data)
        await getVisit(session, first_time_data, [
            {
                "mobile": "9112857001",
                "appointment_for": "زهرا خشنود",
                "birth_dateDay": 2,
                "birth_dateMonth": 1,
                "birth_dateYear": 1400,
                "gender": 1
            },
            {
                "mobile": "9112857002",
                "appointment_for": "رضا باقری",
                "birth_dateDay": 2,
                "birth_dateMonth": 1,
                "birth_dateYear": 1400,
                "gender": 1
            },
            {
                "mobile": "9112857003",
                "appointment_for": "مریم بابایی",
                "birth_dateDay": 2,
                "birth_dateMonth": 1,
                "birth_dateYear": 1400,
                "gender": 1
            },
            {
                "mobile": "9112857004",
                "appointment_for": "زهرا قربانی",
                "birth_dateDay": 2,
                "birth_dateMonth": 1,
                "birth_dateYear": 1400,
                "gender": 1
            },
            {
                "mobile": "9112857005",
                "appointment_for": "عباس کرمی",
                "birth_dateDay": 2,
                "birth_dateMonth": 1,
                "birth_dateYear": 1400,
                "gender": 1
            },
            {
                "mobile": "9112857006",
                "appointment_for": "لیلا شادمان",
                "birth_dateDay": 2,
                "birth_dateMonth": 1,
                "birth_dateYear": 1400,
                "gender": 1
            },
            {
                "mobile": "9112857007",
                "appointment_for": "زینب کاملیان",
                "birth_dateDay": 2,
                "birth_dateMonth": 1,
                "birth_dateYear": 1400,
                "gender": 1
            },
            {
                "mobile": "9112857008",
                "appointment_for": "عباس زواری",
                "birth_dateDay": 2,
                "birth_dateMonth": 1,
                "birth_dateYear": 1400,
                "gender": 1
            },
            {
                "mobile": "9112857009",
                "appointment_for": "سحر عباس زاده",
                "birth_dateDay": 2,
                "birth_dateMonth": 1,
                "birth_dateYear": 1400,
                "gender": 1
            },
            {
                "mobile": "9112857000",
                "appointment_for": "مجید قنادزاده",
                "birth_dateDay": 2,
                "birth_dateMonth": 1,
                "birth_dateYear": 1400,
                "gender": 1
            }
            # Add more entries as needed
        ])

# Run the program
asyncio.run(main())
