from flask import Flask, jsonify, request
from flask_cors import CORS
import GetParams

app = Flask(__name__)
CORS(app)  # 允许跨域请求
# CORS(app, resources={r"/": {"origins": "*"}})  # 允许来自任何域名的跨域请求

# allowed_origin = "http://localhost:5173"
# CORS(app, resources={r"/*": {"origins": allowed_origin}})

@app.route('/')
def index():
    return '1/3 331'
# 返回场地区域名 ，返回场地名
@app.route('/api/Venue/Date', methods=['GET', 'POST'])
def VenueDate():
    if request.method == 'POST':
        # 接收前端发送的数据
        data = request.json
        return jsonify({'message': '数据已接收111112', 'receivedData': data})
    else:
        venue_data = GetParams.GetVenueName()  # 获取第一个数据
        areas_data = GetParams.GetVenueAreasName()  # 获取第二个数据

        # 将两个数据组合成一个字典
        combined_data = {
            'venue_data': venue_data,
            'areas_data': areas_data
        }
        print(combined_data)
        return jsonify(combined_data)

# # 根据场地名和所选时间返回该场地可预定时间
@app.route('/api/Venue/VenueTime', methods=['GET', 'POST'])
def VenueTime():
    if request.method == 'POST':
        # 接收前端发送的数据
        data = request.json
        print(data)
        # 处理数据
        # ...
        venueName = data.get('data')
        occupaDate = data.get('date')

        print(venueName, occupaDate)
        # 返回一个 JSON 响应
        # return jsonify({"message": "Data received successfully"})
        # data = jsonify(GetParams.GetSlotTImeWithVenueName(venueName, occupaDate))
        print(GetParams.GetSlotTImeWithVenueName(venueName, occupaDate))
        return jsonify(GetParams.GetSlotTImeWithVenueName(venueName, occupaDate))
#预定数据
@app.route('/api/Venue/insert_booking', methods=['POST'])
def insert_booking():
    try:
        # 接收前端发送的 JSON 数据
        data = request.json

        # 调用 insert_booking_info 函数并传递数据
        result_message = GetParams.insert_booking_info(data)

        return jsonify({"message": result_message})

    except Exception as e:
        return jsonify({"error": str(e)})
#

@app.route('/api/Membership/Get_membership_categories', methods=['GET'])
def get_membership_categories():
    try:
        # 调用获取会员类型信息的函数
        membership_categories = GetParams.Get_membership_categories()
        # 返回获取的会员类型信息
        print(membership_categories)
        return jsonify(membership_categories)

    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/api/Membership/Insert_membership_categories', methods=['POST'])
def insert_membership_category():
    try:
        # 从请求中获取 JSON 数据
        data = request.json
        # 调用插入会员类型信息的函数
        GetParams.Insert_membership_category(data)
        # 返回成功消息
        return jsonify({"message": "member category data inserted successfully"})

    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/api/Membership/Get_member_levels', methods=['GET'])
def get_member_levels():
    try:
        # 调用获取会员类型信息的函数
        member_levels = GetParams.Get_member_levels()
        # 返回获取的会员类型信息
        # print(member_levels)
        return jsonify(member_levels)

    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/api/Membership/Insert_member_levels', methods=['POST'])
def insert_member_levels():
    try:

        # 从请求中获取 JSON 数据
        data = request.json
        print(data)
        # 调用插入会员类型信息的函数
        GetParams.Insert_member_levels(data)

        # 返回成功消息
        return jsonify({"message": "Membership levels data inserted successfully"})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    # app.run("localhost" , "5173" , debug=True)
    # app.run("192.168.31.68", 5000 , debug=True)
    app.run("0.0.0.0", 5000, debug=True)

























