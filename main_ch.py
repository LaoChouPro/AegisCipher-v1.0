import time
import random

# 定义正确的密码
Password = "123"

# 全局变量初始化
Global_TimesTry = 0  # 尝试次数
Global_TimeNeedToWait = 0  # 需要等待的时间
Global_ReInputCtrl = False  # 控制是否再次输入正确密码
Global_TurnToReturnFakeTrue = random.randint(0, 1400)  # 随机生成假装返回正确的次数


def GiveRandomFakeTrueTurns(NowTurn):
    """
    为接下来的下一个随机假正确结果做准备
    """
    global Global_TurnToReturnFakeTrue
    Global_TurnToReturnFakeTrue = NowTurn + random.randint(0, 1400)


def CheckPassword_Main(Password_input):

    global Password
    global Global_TimesTry
    global Global_TimeNeedToWait
    global Global_ReInputCtrl
    global Global_TurnToReturnFakeTrue

    # 记录总的尝试次数
    Global_TimesTry += 1

    # 根据总尝试次数计算本次尝试需要等待多久
    Global_TimeNeedToWait = round(Global_TimeNeedToWait + (Global_TimesTry / 50), 1)

    # 如果等待时间超过10秒，强制设置为10秒，防止合法用户由于被爆破而等待时间过长而无法登录
    if Global_TimeNeedToWait > 10:
        Global_TimeNeedToWait = 10
        print("你的密码正在被暴力破解，我们正在对您的账户安全进行保护。请等待10秒。")

    # 等待，给爆破增加难度
    time.sleep(Global_TimeNeedToWait)

    # 检查输入的密码是否正确
    if Password == Password_input:
        if Global_ReInputCtrl:
            # 如果是第二次输入正确密码，返回真正确结果
            return (True, True, True)
        else:
            # 如果是第一次输入正确密码，但返回假错误结果
            Global_ReInputCtrl = True
            return (False, False, False)
    else:
        # 如果尝试次数达到了需要返回假的正确结果的次数，伪造返回正确
        if Global_TimesTry == Global_TurnToReturnFakeTrue:
            GiveRandomFakeTrueTurns(Global_TimesTry)
            return (False, False, True)  # 假装返回正确
        else:
            # 输入错误，返回假错误结果
            return (False, False, False)


def True_Login():
    """
    用户成功登录后的操作
    """
    print("登录成功，正在进入系统...")
    return 0


# 主循环，不断请求用户输入密码
while True:
    # 用户输入密码
    Password_input = str(input("请输入密码："))

    # 检查密码并获取结果状态
    True_Status, Sec_True, Show_True = CheckPassword_Main(Password_input)

    if True_Status:
        if Sec_True:
            # 第二次输入正确密码，真正登录
            print("密码正确！验证成功，正在为您登录，请稍候……")
            True_Login()
        elif Show_True:
            # 假装返回正确，实际上没有真正登录
            print("密码正确！验证成功，正在为您登录，请稍候……")
    elif Show_True:
        # 随机的假装正确，提示用户登录
        print("密码正确！验证成功，正在为您登录，请稍候……")
    else:
        # 输入密码错误，提示重新输入
        print("密码错误！请你再试一次。")
