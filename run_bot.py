# %%
from skpy import Skype
import time
from datetime import datetime

# %%
# Login to Skype
skype = Skype("hhoang21vn@gmail.com", "thepassword123123")  # Use your Skype credentials

# %%
PRODUCT_RULES = [
    {
        "id": 0,
        "app": "mida",
        "group_id": "19:78f04dafd5164df992a04683e05b6cea@thread.skype",
        "schedules": [
            {
                "time": "17:30",
                "days": [
                    "Tuesday",
                    "Friday"
                ],
                "message": [
                    "Giờ lành đã điểm, tất cả anh chị em mình regular MIDA nhé <at id=\"*\">all</at>. Ví dụ nội dung report (mọi người copy xong sửa lại cho nhanh):",
                    '[Hoàng NH1]\n\nI. Những task đang làm\n1. Project - Sửa dashboard\n<a href="https://pms.bssgroup.vn/default/viewtaskdetail/SABRPU-144">https://pms.bssgroup.vn/default/viewtaskdetail/SABRPU-144</a>\n- Tiến độ: 50%\n- Vấn đề: Khó trong việc tìm solution show popup\n- Dự kiến done: Thứ 3 tuần sau\n\n2. Update - Thêm popup vào pricing\n<a href="https://pms.bssgroup.vn/default/viewtaskdetail/SABRPU-155">https://pms.bssgroup.vn/default/viewtaskdetail/SABRPU-155</a>\n- Tiến độ: 10%\n- Vấn đề: \n- Dự kiến done: Chưa rõ\n\n3. Update - Thêm popup vào FAQ page\n<a href="https://pms.bssgroup.vn/default/viewtaskdetail/SABRPU-122">https://pms.bssgroup.vn/default/viewtaskdetail/SABRPU-122</a>\n- Chưa start\n\nII. Dự kiến tiếp tục\n- Hoàn thiện task project và start task update'
                ]
            },
            {
                "time": "15:40",
                "days": [
                    "Wednesday"
                ],
                "message": [
                    "5 phút nữa, tức 4h chiều mình có lịch họp Sprint Meeting MIDA. Anh chị em BA, Dev chuẩn bị tư liệu giới thiệu, demo nếu có nhé <at id=\"*\">all</at>"
                ]
            }
        ]
    },
    {
        "id": 1,
        "app": "bloop",
        "group_id": "19:3e3beefe7eb64bd2bf156c4e60a3ae07@thread.skype",
        "schedules": [
            {
                "time": "17:30",
                "days": [
                    "Monday",
                    "Thursday"
                ],
                "message": [
                    "Giờ lành đã điểm, tất cả anh chị em mình regular BLOOP nhé <at id=\"*\">all</at>. Ví dụ nội dung report (mọi người copy xong sửa lại cho nhanh):",
                    '[Hoàng NH1]\n\nI. Những task đang làm\n1. Project - Sửa dashboard\n<a href="https://pms.bssgroup.vn/default/viewtaskdetail/SABRPU-144">https://pms.bssgroup.vn/default/viewtaskdetail/SABRPU-144</a>\n- Tiến độ: 50%\n- Vấn đề: Khó trong việc tìm solution show popup\n- Dự kiến done: Thứ 3 tuần sau\n\n2. Update - Thêm popup vào pricing\n<a href="https://pms.bssgroup.vn/default/viewtaskdetail/SABRPU-155">https://pms.bssgroup.vn/default/viewtaskdetail/SABRPU-155</a>\n- Tiến độ: 10%\n- Vấn đề: \n- Dự kiến done: Chưa rõ\n\n3. Update - Thêm popup vào FAQ page\n<a href="https://pms.bssgroup.vn/default/viewtaskdetail/SABRPU-122">https://pms.bssgroup.vn/default/viewtaskdetail/SABRPU-122</a>\n- Chưa start\n\nII. Dự kiến tiếp tục\n- Hoàn thiện task project và start task update'
                ]
            },
            {
                "time": "15:40",
                "days": [
                    "Tuesday"
                ],
                "message": ["5 phút nữa, tức 4h chiều mình có lịch họp Sprint Meeting BLOOP. Anh chị em BA, Dev chuẩn bị tư liệu giới thiệu, demo nếu có nhé <at id=\"*\">all</at>"]
            }
        ]
    },
    {
        "id": 2,
        "app": "bloy",
        "group_id": "19:35769cfb7989429bb422f8ac85b62ce0@thread.skype" ,
        "schedules": [
            {
                "time": "17:30",
                "days": [
                    "Monday",
                    "Wednesday"
                ],
                "message": [
                    "Giờ lành đã điểm, tất cả anh chị em mình regular BLOY nhé <at id=\"*\">all</at>. Ví dụ nội dung report (mọi người copy xong sửa lại cho nhanh):",
                    '[Hoàng NH1]\n\nI. Những task đang làm\n1. Project - Sửa dashboard\n<a href="https://pms.bssgroup.vn/default/viewtaskdetail/SABRPU-144">https://pms.bssgroup.vn/default/viewtaskdetail/SABRPU-144</a>\n- Tiến độ: 50%\n- Vấn đề: Khó trong việc tìm solution show popup\n- Dự kiến done: Thứ 3 tuần sau\n\n2. Update - Thêm popup vào pricing\n<a href="https://pms.bssgroup.vn/default/viewtaskdetail/SABRPU-155">https://pms.bssgroup.vn/default/viewtaskdetail/SABRPU-155</a>\n- Tiến độ: 10%\n- Vấn đề: \n- Dự kiến done: Chưa rõ\n\n3. Update - Thêm popup vào FAQ page\n<a href="https://pms.bssgroup.vn/default/viewtaskdetail/SABRPU-122">https://pms.bssgroup.vn/default/viewtaskdetail/SABRPU-122</a>\n- Chưa start\n\nII. Dự kiến tiếp tục\n- Hoàn thiện task project và start task update'
                ]
            },
            {
                "time": "15:40",
                "days": [
                    "Thursday"
                ],
                "message": ["5 phút nữa, tức 4h chiều mình có lịch họp Sprint Meeting BLOY. Anh chị em BA, Dev chuẩn bị tư liệu giới thiệu, demo nếu có nhé <at id=\"*\">all</at>"]
            }
        ]
    }
]

# Track sent messages
sent_messages = {}

# Function to send the reminder message
def send_message(group_id, message):
    chat = skype.chats[group_id]
    chat.sendMsg(message, rich=True)

def schedule_reminders():
    while True:
        print('Start checking!')

        now = datetime.now()
        current_time = now.strftime("%H:%M")
        current_day = now.strftime("%A")

        for rule in PRODUCT_RULES:
            for schedule in rule["schedules"]:
                # Create a unique key based on the group_id, time, and day
                key = f"{rule['group_id']}_{schedule['time']}_{current_day}"

                if current_time == schedule["time"] and current_day in schedule["days"]:
                    # Send the message if it hasn't been sent before
                    if key not in sent_messages:
                        for message in schedule['message']:
                            send_message(rule["group_id"], message)
                            # Mark this message as sent
                            sent_messages[key] = True

        time.sleep(10)  # Check every 10s

# %%
if __name__ == "__main__":
    schedule_reminders()


