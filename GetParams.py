from sqlite3 import OperationalError

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
import requests
from decimal import Decimal
from datetime import datetime
import json

# 创建数据库引擎
# engine = create_engine('mysql+mysqlconnector://root:zoharn421@121.40.98.93/smartvenue')
# engine = create_engine('mysql+mysqlconnector://root:111111@127.0.0.1/smartvenue')
try:
    engine = create_engine('mysql+mysqlconnector://root:zoharn421@121.40.98.93/smartvenue')
    connection = engine.connect()
    # print("连接成功")
    connection.close()
except OperationalError as e:
    print(f"连接失败: {e}")

# 创建会话工厂
SessionFactory = sessionmaker(bind=engine)

# 获取当前星期几
def GetWeek():
    # 星期字符串到数字的映射
    weekday_mapping = {
        'Monday': 1,
        'Tuesday': 2,
        'Wednesday': 3,
        'Thursday': 4,
        'Friday': 5,
        'Saturday': 6,
        'Sunday': 7
    }
    # 从时间服务器获取星期字符串
    response = requests.get('http://worldclockapi.com/api/json/utc/now')
    data = response.json()
    current_time = data['dayOfTheWeek']
    # 将星期字符串转换为数字
    weekday_number = weekday_mapping.get(current_time)
    return weekday_number
    #print("联网的北京时间是星期：", weekday_number)
# 返回场地名
def GetVenueName():
    try:
        # 创建会话
        session = SessionFactory()
        # 执行数据库操作
        result = session.execute(text("""
                        SELECT v.*, a.AreaName AS AreaName
                        FROM venue v
                        INNER JOIN venue_Areas a ON v.AreaID = a.AreaID;
                        """))
        rows = result.fetchall()

        # 创建列名到索引的映射字典
        column_index = {name: index for index, name in enumerate(result.keys())}

        sport_fields = []

        for row in rows:
            sport_fields.append({
                # "disciplines": row["VenueName"],
                # "vacancy": True,
                # "AreaName": row["AreaName"],
                # "VenueID": row["VenueID"]
                "disciplines": row[column_index.get("VenueName")],
                "vacancy": True,
                "AreaName": row[column_index.get("AreaName")],
                "VenueID": row[column_index.get("VenueID")]
            })

        # 转化为 JSON 格式
        # sport_fields_json = json.dumps(sport_fields, ensure_ascii=False)
        return sport_fields

    except Exception as e:
        print(f"Error: {e}")
        # 处理数据库操作中的错误

    finally:
        # 关闭会话
        session.close()
# 返回场地区域名
def GetVenueAreasName():
    try:
        # 创建会话
        session = SessionFactory()
        # 执行数据库操作
        result = session.execute(text("""
                        SELECT * from Venue_Areas order by AreaSortOrder
                        """))
        rows = result.fetchall()

        # 创建列名到索引的映射字典
        column_index = {name: index for index, name in enumerate(result.keys())}

        areas_name_list = []
        # areas_name_list.append({
        #         "AreaID":0,
        #         "AreaName":"全部"}
        #     )

        for row in rows:
            areas_name_list.append({
                "AreaID":row[column_index.get("AreaID")],
                "AreaName":row[column_index.get("AreaName")]
            })

        # 转化为 JSON 格式
        # sport_fields_json = json.dumps(areas_name_list, ensure_ascii=False)
        return areas_name_list

    except Exception as e:
        print(f"Error: {e}")
        # 处理数据库操作中的错误

    finally:
        # 关闭会话
        session.close()

# 根据场地名和所选时间返回该场地可预定时间
def GetSlotTImeWithVenueName(venuename, occupaDate):
    try:
        # 创建会话
        session = SessionFactory()
        # 执行数据库操作
        DayOfWeek = GetWeek()
        result = session.execute(text("""
            SELECT * 
            FROM Timing_Slot_Pricing TSP
            JOIN Timing_Rules_Slot_Pricing_Link TSPL ON TSP.SlotId = TSPL.SlotID 
            WHERE TSPL.RuleID IN (
                SELECT tr.Ruleid 
                FROM Timing_Rules tr 
                JOIN Timing_Venue_Rules_Link tvar ON tr.RuleID = tvar.RuleID
                WHERE tvar.VenueID IN (
                    SELECT venueid 
                    FROM venue 
                    WHERE venuename = :venuename 
                )
            )
            AND CONCAT(',', DayOfWeek, ',') LIKE :day_of_week_param
        """).bindparams(venuename=venuename,   day_of_week_param="%," + str(DayOfWeek) + ",%"))

        # 根据场地名查询该场地占用情况
        resultOccupancy = session.execute(text("""
                            SELECT vo.OccupaTime, m.MemberID
                            FROM Venue_Occupancy vo
                            JOIN Venue v ON vo.VenueID = v.VenueID
                            LEFT JOIN Members m ON vo.MemberID = m.MemberID
                            WHERE v.VenueName = :venuename and vo.occupaDate = :occupaDate
            """).bindparams(venuename=venuename, occupaDate=occupaDate))

        rows = result.fetchall()
        # print(rows)

        rowsOccupancy = resultOccupancy.fetchall()
        # print(rowsOccupancy)
        # 将时间范围字符串拆分成单独的时间点
        time_Occupancy = []
        for row in rowsOccupancy:
            time_Occupancy += [int(time_str) for time_str in row[0].split(',')]


        # print(time_Occupancy)
        # 创建列名到索引的映射字典
        column_index = {name: index for index, name in enumerate(result.keys())}

        price_list = []
        for row in rows:
            price_list.append({
                "TimeRange":row[column_index.get("TimeRange")],
                "Price":row[column_index.get("Price")],
                "MemberSpecialPrice":row[column_index.get("MemberSpecialPrice")],
                "MemberSpecialPriceEnabled":row[column_index.get("MemberSpecialPriceEnabled")]
            })
        # print(price_list)
        # 做一个0-24小时的数据
        pricing_data = price_list
        # print(pricing_data)
        result_list = []
        for i in range(24):
            time_range = f'{i:02}:00'
            data = {
                'Time': time_range,
                'DateStatus': 0, # 获取时间点对应的 DateStatus 值
                'Price': None  # 价格初始化为None
            }

            for item in pricing_data:
                # 将时间范围字符串分割为起始小时和结束小时
                time_range_parts = item['TimeRange'].split('-')
                start_hour, end_hour = map(int, time_range_parts)
                # 检查当前小时是否在时间范围内
                if start_hour <= i < end_hour:
                    # 如果 MemberSpecialPriceEnabled 为 1，将 Price 设置为 MemberSpecialPrice，否则设置为 Price
                    data['Price'] = item['MemberSpecialPrice'] \
                        if item['MemberSpecialPriceEnabled'] == 1 else item['Price']
                    # 在时间片内，设置 DateStatus 为可预定（1）
                    data['DateStatus'] = 1
                    break  # 已匹配到时间范围，退出循环

            # 假如被占用则设置成2
            if i in time_Occupancy:
                data['DateStatus'] = 2
            result_list.append(data)

        return result_list

    except Exception as e:
        print(f"Error: {e}")
        # 处理数据库操作中的错误

    finally:
        # 关闭会话
        session.close()

# 根据收到的会员id、场地名、日期、时间片,来改变场地状态
def ChangeVenueOccupancy(MemberId,VenueName, OccupaDate, OccupaTime):
    try:
        # 创建会话
        session = SessionFactory()
        # 执行数据库操作
        # 改变Venue_Occupancy，场地占用表
        result = session.execute(text("""
                            INSERT INTO Venue_Occupancy (VenueID, MemberID, OccupaTime, OccupaDate)
                            SELECT v.VenueID, :memberId, :OccupaTime, :OccupaDate
                            FROM Venue v
                            WHERE v.VenueName = :venuename;
                           """).bindparams(venuename=VenueName, memberId=MemberId, OccupaTime=OccupaTime, OccupaDate=OccupaDate))
        # 提交事务
        session.commit()
        print("插入到VenueOccupancy表成功")



    except Exception as e:
        print(f"Error: {e}")
        # 处理数据库操作中的错误
    finally:
        # 关闭会话
        session.close()

# 根据收到的会员编号，会员姓名，会员电话，所属场地，所属区域，预定日期，预定时间片，总金额，
# 优惠金额，实付金额，支付方式，下单时间，所属场馆，备注来插入预定表Booking
def insert_booking_info(booking_info):
    try:
        # 创建会话
        session = SessionFactory()

        # 执行数据库操作
        result = session.execute(text("""
            INSERT INTO Booking (
                BillNumber, MemberID, MemberName, CardNumber, PhoneNumber, VenueName, AreaName,
                ReservationDate, ReservationTime, OrderStatusCode, OrderStatusDescription,
                TotalAmount, DiscountAmount, AmountPaid, PaymentMethodCode, PaymentMethodDescription,
                OrderTime, Store, Notes
            )
            VALUES (
                :BillNumber, :MemberID, :MemberName, :CardNumber, :PhoneNumber, :VenueName, :AreaName,
                :ReservationDate, :ReservationTime, :OrderStatusCode, :OrderStatusDescription,
                :TotalAmount, :DiscountAmount, :AmountPaid, :PaymentMethodCode, :PaymentMethodDescription,
                :OrderTime, :Store, :Notes
            )
        """), booking_info)

        # 提交事务
        session.commit()
        print("插入到Booking表成功")

    except Exception as e:
        print(f"Error: {e}")
        # 处理数据库操作中的错误

    finally:
        # 关闭会话
        session.close()

# 获取会员等级信息表membership_categories
def Get_membership_categories():
    try:
        # 创建会话
        session = SessionFactory()
        # 执行数据库操作
        result = session.execute(text("""
                        SELECT * from membership_categories order by CategoryID
                        """))
        rows = result.fetchall()

        membership_categories_list = []
        column_index = {name: index for index, name in enumerate(result.keys())}
        for row in rows:
            membership_categories_list.append(
                {
                    "CategoryName": row[column_index.get("CategoryName")],
                    "MembershipDuration": row[column_index.get("MembershipDuration")],
                    "MembershipFee": row[column_index.get("MembershipFee")],
                    "StartDate": row[column_index.get("StartDate")]
                }
            )

        # 转化为 JSON 格式
        # sport_fields_json = json.dumps(areas_name_list, ensure_ascii=False)
        print(membership_categories_list)
        return membership_categories_list

    except Exception as e:
        print(f"Error: {e}")
        # 处理数据库操作中的错误

    finally:
        # 关闭会话
        session.close()

# 插入会员信息表
def Insert_membership_category(data):
    try:
        # 创建会话
        session = SessionFactory()

        # 执行数据库插入操作
        session.execute(text("""
            INSERT INTO membership_categories (CategoryName, MembershipDuration, MembershipFee, StartDate)
            VALUES (:CategoryName, :MembershipDuration, :MembershipFee, :StartDate)
        """), data)

        # 提交事务
        session.commit()
        print("插入到membership_categories表成功")

    except Exception as e:
        print(f"Error: {e}")
        # 处理数据库操作中的错误

    finally:
        # 关闭会话
        session.close()

# 获取会员等级信息表membership_categories
def Get_member_levels():
    try:
        # 创建会话
        session = SessionFactory()
        # 执行数据库操作
        result = session.execute(text("""
                        SELECT * from Member_Levels order by LevelID
                        """))
        rows = result.fetchall()

        member_levels_list = []
        column_index = {name: index for index, name in enumerate(result.keys())}
        for row in rows:
            member_levels_list.append(
                {
                    "LevelName": row[column_index.get("LevelName")],
                    "ProductDiscount": row[column_index.get("ProductDiscount")],
                    "VenueDiscount": row[column_index.get("VenueDiscount")],
                    "AccumulatedRecharge": row[column_index.get("AccumulatedRecharge")],
                    "PointsRequiredForUpgrade": row[column_index.get("PointsRequiredForUpgrade")],
                    "PurchaseAmount": row[column_index.get("PurchaseAmount")],
                    "Points": row[column_index.get("Points")],
                    "PointsRatio": row[column_index.get("PointsRatio")],
                    "OnlineActivation": bool(row[column_index.get("OnlineActivation")]),
                    "OfflineActivation": bool(row[column_index.get("OfflineActivation")])
                }
            )

        # 打印获取的数据
        # print(member_levels_list)
        return member_levels_list
    except Exception as e:
        print(f"Error: {e}")
        # 处理数据库操作中的错误
    finally:
        # 关闭会话
        session.close()
# 插入会员等级
def Insert_member_levels(data):
    try:
        # 创建会话
        session = SessionFactory()

        # 执行数据库插入操作
        session.execute(text("""
            INSERT INTO Member_Levels (LevelName, ProductDiscount, VenueDiscount, AccumulatedRecharge,
                                       PointsRequiredForUpgrade, PurchaseAmount, Points, PointsRatio,
                                       OnlineActivation, OfflineActivation)
            VALUES (:LevelName, :ProductDiscount, :VenueDiscount, :AccumulatedRecharge,
                    :PointsRequiredForUpgrade, :PurchaseAmount, :Points, :PointsRatio,
                    :OnlineActivation, :OfflineActivation)
        """), data)


        # 提交事务
        session.commit()
        print("插入到Member_Levels表成功")

    except Exception as e:
        print(f"Error: {e}")
        # 处理数据库操作中的错误

    finally:
        # 关闭会话
        session.close()

# 获取会员信息
def Get_members(search_query=None):
    try:
        # 创建会话
        session = SessionFactory()

        # 构建查询SQL语句，包括查询条件
        query = text("""
            SELECT * FROM Members
            WHERE (MemberID LIKE :query OR PhoneNumber LIKE :query OR Name LIKE :query)
            ORDER BY AutoIncrementID
        """).params(query=f"%{search_query}%" if search_query else "%")

        # 执行数据库操作
        result = session.execute(query)
        rows = result.fetchall()

        members_list = []
        column_index = {name: index for index, name in enumerate(result.keys())}
        for row in rows:
            members_list.append(
                {
                    "MemberID": row[column_index.get("MemberID")],
                    "MemberAvatar": row[column_index.get("MemberAvatar")],
                    "PlateNumber": row[column_index.get("PlateNumber")],
                    "Name": row[column_index.get("Name")],
                    "PhoneNumber": row[column_index.get("PhoneNumber")],
                    "IDNumber": row[column_index.get("IDNumber")],
                    "Gender": row[column_index.get("Gender")],
                    "CardFaceNumber": row[column_index.get("CardFaceNumber")],
                    "Birthday": row[column_index.get("Birthday")],
                    "Password": row[column_index.get("Password")],
                    "CardIssuanceFee": row[column_index.get("CardIssuanceFee")],
                    "Address": row[column_index.get("Address")],
                    "CurrentBalance": row[column_index.get("CurrentBalance")],
                    "StartDateTime": row[column_index.get("StartDateTime")],
                    "Locked": bool(row[column_index.get("Locked")]),
                    "Operator": row[column_index.get("Operator")]
                }
            )

        # 打印获取的数据
        print(members_list)
        return members_list
    except Exception as e:
        print(f"Error: {e}")
        # 处理数据库操作中的错误
    finally:
        # 关闭会话
        session.close()

# 插入会员信息
def Insert_members(data):
    try:
        # 创建会话
        session = SessionFactory()

        # 执行数据库插入操作
        session.execute(text("""
            INSERT INTO Members (MemberID, MemberAvatar, PlateNumber, Name, PhoneNumber, IDNumber, Gender,
                                CardFaceNumber, Birthday, Password, CardIssuanceFee, Address, CurrentBalance,
                                StartDateTime, Locked, Operator)
            VALUES (:MemberID, :MemberAvatar, :CardNumber, :Name, :PhoneNumber, :IDNumber, :Gender,
                    :CardFaceNumber, :Birthday, :Password, :CardIssuanceFee, :Address, :CurrentBalance,
                    NOW(), FALSE, :Operator)
        """), data)

        # 提交事务
        session.commit()
        print("插入到Members表成功")

    except Exception as e:
        print(f"Error: {e}")
        # 处理数据库操作中的错误

    finally:
        # 关闭会话
        session.close()


# Get_members()
#
# data = {
#     "MemberID": "M12345",
#     "MemberAvatar": b'\x00\x01\x02\x03',  # 二进制头像数据
#     "PlateNumberNumber": "C78901",
#     "Name": "张三",
#     "PhoneNumber": "1234567890",
#     "IDNumber": "123456789012345",
#     "Gender": "男",
#     "CardFaceNumber": "CF123",
#     "Birthday": "1990-01-15",
#     "Password": "my_password",
#     "CardIssuanceFee": 50.00,
#     "Address": "北京市朝阳区",
#     "CurrentBalance": 1000.00,
#     "Operator": "Admin"
# }
#
# # 调用插入函数
# Insert_members(data)
#





# data = {'LevelName': 'qqq', 'ProductDiscount': '10', 'VenueDiscount': '10', 'AccumulatedRecharge': '123', 'PointsRatio': '1.00', 'OnlineActivation': '0', 'OfflineActivation': '0', 'Points': '1', 'PurchaseAmount': '1', 'PointsRequiredForUpgrade': '0'}
#
# Insert_member_level(data)

# Get_member_levels()

# data = {
#     "LevelName": "Silver",
#     "ProductDiscount": 0.90,
#     "VenueDiscount": 0.85,
#     "AccumulatedRecharge": 500.00,
#     "PointsRequiredForUpgrade": 100,
#     "PurchaseAmount": 300.00,
#     "Points": 50,
#     "PointsRatio": 0.05,
#     "OnlineActivation": True,
#     "OfflineActivation": False
# }






# # 创建一个包含数据的字典
# membership_category_data = {
#     "CategoryName": "测试卡",
#     "MembershipDuration": 12,  # 会员时长
#     "MembershipFee": 1000.00,  # 会员费用
#     "StartDate": "购买当日"  # 开始日期
# }
# # 调用函数并传递数据字典
# Insert_membership_category(membership_category_data)
#


# Get_membership_categories()






# 创建预定信息字典，包括新的字段
# booking_info = {
#     "BillNumber": "1234567890",  # 单据号
#     "MemberID": "1001",          # 会员编号
#     "MemberName": "王小明",      # 会员姓名
#     "CardNumber": "A12345",      # 会员卡号
#     "PhoneNumber": "13812345678",  # 会员手机
#     "VenueName": "羽毛球1",      # 所属场地
#     "AreaName": "篮球场",        # 所属区域
#     "ReservationDate": "2024-01-10",  # 预定日期
#     "ReservationTime": "1,3,4",  # 预定时间片
#     "OrderStatusCode": 1,        # 订单状态代码 (1: 待核销, 2: 已核销, 3: 未支付, 4: 已撤单, 5: 已超时或过期, 6: 挂单中)
#     "OrderStatusDescription": "待核销",  # 订单状态描述
#     "TotalAmount": 100.00,       # 消费金额
#     "DiscountAmount": 10.00,     # 优惠金额
#     "AmountPaid": 90.00,         # 实收金额
#     "PaymentMethodCode": 1,      # 支付方式代码 (1: 现金, 2: 余额, 3: pos机, 4: 银行卡, 5: 支付宝, 6: 微信, 7: 积分, 8: 扣次)
#     "PaymentMethodDescription": "现金",  # 支付方式描述
#     "OrderTime": "2024-01-05 12:00:00",  # 下单时间
#     "Store": "深圳分店",          # 门店
#     "Notes": "备注信息"           # 备注
# }
#
# 调用函数并传递预定信息字典
# insert_booking_info(booking_info)


# 调用函数获取数据
# print(GetVenueName())
# print(GetVenueAreasName())
# print(GetSlotTImeWithVenueName("羽毛球1" , "2023-12-31"))
# ChangeVenueOccupancy("1001", "篮球1","2023-12-31","6,7")