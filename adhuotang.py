# -*- encoding=utf8 -*-
__author__ = "Lenovo"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["Android:///",])

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 获取设备的高度和宽度
width, height = device().get_current_resolution()
# 校准滑动的起点和终点
start_pt1 = (width / 2,height * 0.8)
end_pt1 = (width / 2,height * 0.1)
end_pt3 = (width / 2,height * 0.6)
start_pt2 = (width *0.9,height / 2)
end_pt2 = (width *0.1,height / 2)

#ad广告关闭类
def ad_clos():
    sleep(90)
    while poco(textMatches=".*秒后得.*").exists():
            swipe(start_pt1, end_pt1,1000)
            sleep(3)
    sleep(1)
    if poco(text="任务已完成").exists():
        keyevent("BACK")
        assert_equal("1", "1", "激励视频观看完成")
        sleep(1)
    sleep(1)
    if poco("closeBtn").exists():
        keyevent("BACK")
        assert_equal("1", "1", "激励视频观看完成")
        sleep(1)
    sleep(1)
    if poco(text="| 跳过").exists():
        poco(text="| 跳过").click()
        assert_equal("1", "1", "激励视频观看完成")
        sleep(1)
    sleep(1)
    if poco("com.byted.pangle.m:id/tt_reward_full_count_down_after_close").exists():
        poco("com.byted.pangle.m:id/tt_reward_full_count_down_after_close").click()
        assert_equal("1", "1", "激励视频观看完成")
        sleep(1)
    sleep(1)
    if poco("android.widget.ImageView").exists():
        poco("android.widget.ImageView").click()
        assert_equal("1", "1", "激励视频观看完成")
        sleep(1)
    sleep(5)
    
#推荐
def home_page():
    poco(text = "首页").wait_for_appearance()
    poco(text = "首页").click()
    sleep(1)
    poco(text = "推荐").click()
    sleep(1)
    swipe(start_pt1, end_pt1,1000)
    poco("com.jz.htdj:id/iv_collect").exists()
    poco("com.jz.htdj:id/iv_collect").click()
    assert_equal("1", "1", "推荐追剧成功")
    sleep(1) 
    poco("com.jz.htdj:id/iv_collect").exists()
    poco("com.jz.htdj:id/iv_collect").click()
    assert_equal("1", "1", "推荐取消追剧成功")
    sleep(1)
    poco("com.jz.htdj:id/iv_like").exists()
    poco("com.jz.htdj:id/iv_like").click()
    assert_equal("1", "1", "推荐点赞成功")
    sleep(1)
    poco("com.jz.htdj:id/iv_like").exists()
    poco("com.jz.htdj:id/iv_like").click()
    assert_equal("1", "1", "推荐取消点赞成功")
    poco("com.jz.htdj:id/tv_look").click()
    poco("com.jz.htdj:id/tv_select_drama_ad").wait_for_appearance()
    keyevent("BACK")
    while not poco(text="广告").exists():
        swipe(start_pt1, end_pt1,1000)
        sleep(2)
    assert_equal("1", "1", "推荐页信息流广告加载成功")
    for i in range(3):
        swipe(start_pt1, end_pt1,1000)
        sleep(1)
        if poco("com.jz.htdj:id/iv_collect").exists():
            poco("com.jz.htdj:id/iv_collect").click()
        sleep(1)
        if poco("com.jz.htdj:id/iv_like").exists():
            poco("com.jz.htdj:id/iv_like").click()
        sleep(3)

# 播放详情页
def play_details_page(password="680401"):
    poco(text = "首页").wait_for_appearance()
    poco(text = "首页").click()
    sleep(1)
    poco(text = "推荐").click()
    sleep(1)
    swipe(start_pt1, end_pt1,1000)
    sleep(1)
    if not poco("com.jz.htdj:id/tv_look").exists():
        swipe(start_pt1, end_pt1,1000)
        sleep(1)
    poco("com.jz.htdj:id/tv_look").click()
    poco("com.jz.htdj:id/tv_select_drama_ad").wait_for_appearance()
    sleep(3)
    dtad=poco("com.jz.htdj:id/iv_close_ad_bottom").exists()
    assert_equal(dtad, True, "推荐页信息流广告加载成功")
    sleep(1)
    touch([0.5,0.5],duration=10)
    poco("com.jz.htdj:id/tv_select_drama_ad").click()
    poco(text="1-20").wait_for_appearance()
    poco(text="1-20").click()
    sleep(1)
    poco(text="3").click()
    sleep(1)
    poco(textMatches=".*第3集.*").exists()  
    assert_equal("1", "1", "详情页选集成功")
    sleep(1)
    swipe(start_pt1, end_pt1,1000)
    touch([0.5,0.5])
    sleep(1)
    poco("com.jz.htdj:id/iv_collect").exists()
    poco("com.jz.htdj:id/iv_collect").click()
    assert_equal("1", "1", "详情追剧成功")
    sleep(1) 
    poco("com.jz.htdj:id/iv_collect").exists()
    poco("com.jz.htdj:id/iv_collect").click()
    assert_equal("1", "1", "详情取消追剧成功")
    sleep(1)
    poco("com.jz.htdj:id/iv_like").exists()
    poco("com.jz.htdj:id/iv_like").click()
    assert_equal("1", "1", "详情点赞成功")
    sleep(1)
    poco("com.jz.htdj:id/iv_like").exists()
    poco("com.jz.htdj:id/iv_like").click()
    assert_equal("1", "1", "详情取消点赞成功")
    for i in range(3):
        while not poco(text="观看广告 立即解锁第 ").exists():
            swipe(start_pt1, end_pt1,1000)
            sleep(1)
        poco(text="观看广告 立即解锁第 ").click()
        ad_clos()
    keyevent("BACK")
    swipe(start_pt1, end_pt1,1000)

#剧场tab
def theater():
    poco(text="剧场").wait_for_appearance()
    poco(text="剧场").click()
    sleep(1)
    poco(text="必看榜").wait_for_appearance()
    sleep(1)
    poco("com.jz.htdj:id/vp_main").click()
    poco("com.jz.htdj:id/tv_select_drama_ad").wait_for_appearance()
    assert_equal("1", "1", "banner页进入成功")
    keyevent("BACK")
    poco(text="必看榜").wait_for_appearance()
    poco(text="必看榜").click()
    sleep(1)
    poco(textMatches="已完结.*?")[0].click()
    keyevent("BACK")
    poco(text="热播榜").wait_for_appearance()
    poco(text="热播榜").click()
    poco(textMatches="已完结.*?")[0].click()
    keyevent("BACK")
    poco("com.jz.htdj:id/tv_hot_more").wait_for_appearance()
    poco("com.jz.htdj:id/tv_hot_more").click()
    poco(text="必看榜").wait_for_appearance()
    poco(text="必看榜").click()
    poco("com.jz.htdj:id/tv_num_01").click()
    keyevent("BACK")
    poco(text="热播榜").wait_for_appearance()
    poco(text="热播榜").click()
    sleep(1)
    while not poco(text="休夫后，她名动京城").exists():
        swipe(start_pt1, end_pt1,1000)
        sleep(1)
    else:
        poco(text="休夫后，她名动京城").wait_for_appearance()
        poco(text="休夫后，她名动京城").click()
        sleep(1)
        touch([0.5,0.5])
        touch([0.5,0.5])
        if poco("com.jz.htdj:id/iv_collect").exists():
            poco("com.jz.htdj:id/iv_collect").click()
            assert_equal("1", "1", "详情追剧成功")
            sleep(1)
        poco("com.jz.htdj:id/tv_select_drama_ad").wait_for_appearance()
        keyevent("BACK")
        sleep(1)
        
    keyevent("BACK")
    sleep(1)
    poco(text="古装").wait_for_appearance()
    poco(text="古装").click()
    assert_equal("1", "1", "剧场切换类型古装成功")
    sleep(1)
    if poco(text="追剧").exists():
        poco(text="追剧").click()
        sleep(2)
        keyevent("BACK")
    if poco("com.jz.htdj:id/iv_close_btn").exists():
        poco("com.jz.htdj:id/iv_close_btn").click()
        sleep(1)
    for i in range(5):
        swipe(start_pt1, end_pt1,1000)
        sleep(1)

#看过tab
def history():
    poco(text = "首页").wait_for_appearance()
    poco(text = "首页").click()
    sleep(1)
    poco(text="在看剧").click()
    sleep(1)
    poco(text="我的收藏").wait_for_appearance()
    poco(text="休夫后，她名动京城").click()
    assert_equal("1", "1", "观看记录成功")
    poco("com.jz.htdj:id/iv_close_ad_bottom").wait_for_appearance()
    keyevent("BACK")
    sleep(1)
    if poco("com.jz.htdj:id/tv_play").exists():
        poco("com.jz.htdj:id/tv_play").click()
        assert_equal("1", "1", "追剧进入成功")
        sleep(1)  
    else:
        poco(textMatches="已完结.*?")[0].click()
    keyevent("BACK")

#福利tab
def welfare():
    poco(text="福利").wait_for_appearance()
    poco(text="福利").click()
    sleep(5)
    if poco(text="去登录").exists():
        log("需要人工干预登录")
    else:
        if poco(text="签到").exists():
            poco(text="签到").click()
            poco(text="签到成功").wait_for_appearance()
            assert_equal("1", "1", "签到成功")
            poco(text="奖励翻倍").click()
            ad_clos()
            poco(text="开心收下").click()
            assert_equal("1", "1", "奖励翻倍成功")
        if poco(text="补签").exists(): 
            poco(text="补签")[0].click()
            ad_clos()
            poco(text="补签成功").exists()
            sleep(1)
            poco("com.jz.htdj:id/btn_close").click()
            assert_equal("1", "1", "补签成功")
        if poco(text="去看剧").exists(): 
            poco(text="去看剧").click()
            sleep(1)
            poco(textMatches="已完结.*?")[3].click()
            wait_time = 650  # 30分钟
            start_time = time.time()
            while True:
                # 计算已经等待的时间
                elapsed_time = time.time() - start_time

                # 如果已经超过等待时间，退出循环
                if elapsed_time >= wait_time:
                    print("已等待超过10分钟，退出程序")
                    break

                try:                 
                    # 等待元素加载（根据实际情况修改选择器）
                    for i in range(3):
                        sleep(220)
                        keyevent("BACK")
                        sleep(1)
                        poco(textMatches="已完结.*?")[i+3].click()
                        sleep(1)
                except Exception as e:
                    # 捕获任何异常并打印
                    print("发生异常:", str(e))

                # 等待一段时间后继续循环，这里可以根据实际情况调整等待时间
                sleep(5)            
            keyevent("BACK")
            sleep(1)
            poco(text="福利").click()
        if poco(text="去收藏").exists(): 
            poco(text="去收藏").click()
            poco(textMatches="已完结.*?")[5].click()
            sleep(1)
            touch([0.5,0.5])
            touch([0.5,0.5])
            if poco("com.jz.htdj:id/iv_collect").exists():
                poco("com.jz.htdj:id/iv_collect").click()
                assert_equal("1", "1", "详情追剧成功")
                sleep(1)
            keyevent("BACK")
            sleep(1)
            poco(text="福利").click()
        count = 0
        while poco(text="领取").exists():
            poco(text="领取")[0].click()
            sleep(1)
            poco("com.jz.htdj:id/btn_close").click()
            assert_equal("1", "1", "领取奖励成功")
            sleep(2)
            count += 1
        print("福利领取{}次，一般情况是3次如果不是请检查福利页".format(count))
            
#我的tab
def my():
    poco(text="我的").wait_for_appearance()
    poco(text="我的").click()
    sleep(1)
#     if poco("您还未登录").exists():
#         poco("立即登录")[1].click()
#         sleep(1)
#         if poco(text="同意").exists():
#             poco(text="同意").click()
#             sleep(1)
#             assert_equal("1", "1", "一键登录成功")
#         if poco("欢迎来到").exists():
#             poco(text="请输入手机号").set_text("15868385402")
#             sleep(1)
#             poco("获取验证码").click()
#             sleep(1)
#             poco(text="请输入验证码").set_text("1100")
#             sleep(1)
#             poco("我已阅读并同意").click()
#             sleep(1)
#             poco("立即登录").click()
#             sleep(1)
#             assert_equal("1", "1", "登录成功")
    poco(textMatches=".*?集全").click()
    sleep(2)
    keyevent("BACK")
    poco(text="全部").click()
    poco(text="观看历史").exists()
    poco("android.widget.LinearLayout").offspring("com.jz.htdj:id/rv_history_list").child("com.jz.htdj:id/layout_root")[0].child("com.jz.htdj:id/collect_btn").click()
    sleep(1)
    poco("android.widget.LinearLayout").offspring("com.jz.htdj:id/rv_history_list").child("com.jz.htdj:id/layout_root")[0].child("com.jz.htdj:id/collect_btn").click() 
    sleep(1)
    poco(textMatches="已完结.*?")[0].click()
    sleep(2)
    keyevent("BACK")
    sleep(1)
    swipe(start_pt1, end_pt1,1000)
    sleep(1)
    keyevent("BACK")
    sleep(1)
    poco(text="我的收藏").click()
    sleep(2)
    poco(textMatches="观看至第.*?")[0].click()
    sleep(2)
    keyevent("BACK")
    sleep(1)
    keyevent("BACK")
    sleep(1)
    poco(text="我的点赞").click()
    sleep(1)
    poco(textMatches="第.*?")[0].click()
    sleep(2)
    keyevent("BACK")
    sleep(1)
    keyevent("BACK")
    sleep(1)
    poco(text="关于我们").click()
    poco(text="《用户协议》").wait_for_appearance()
    poco(text="《用户协议》").click()
    sleep(1)
    swipe(start_pt1, end_pt1,1000)
    sleep(1)
    keyevent("BACK")
    sleep(1)
    poco(text="《隐私政策》").click()
    sleep(1)
    swipe(start_pt1, end_pt1,1000)
    sleep(1)
    keyevent("BACK")
    sleep(1)
    poco(text="《收集个人信息明示清单》").click()
    sleep(1)
    swipe(start_pt1, end_pt1,1000)
    sleep(1)
    keyevent("BACK")
    sleep(1)
    poco(text="《个人信息第三方共享清单》").click()
    sleep(1)
    swipe(start_pt1, end_pt1,1000)
    sleep(1)
    keyevent("BACK")
    sleep(1)
    keyevent("BACK")
    sleep(1)
    poco(text="设置").click()
    sleep(1)
    poco(text="账户与安全").wait_for_appearance()
    poco(text="意见反馈").click()
    sleep(2)
    poco(text="反馈与投诉").wait_for_appearance()
    poco(text="功能体验与使用").click()
#     poco(text="请输入手机号便于联系").set_text("15868385402")
    sleep(1)
    poco(text="加载缓慢/失败").click()
    sleep(1)
    poco("form-desc").set_text("功能回归自动化测试数据无需回复")
    sleep(1)
    poco(text="提 交").click()
    sleep(1)
    poco(text="提交成功，感谢您的反馈").exists()
    poco(text="确定").click()
    assert_equal("1", "1", "我的反馈意见成功")
    sleep(1)
#     keyevent("BACK")
    poco(text="清除缓存").click()
    sleep(1)
    poco(text="联系客服").click()
    sleep(1)
    keyevent("BACK")
    sleep(1)
    poco(textMatches="版本号.*?").click()
    sleep(1)
#    退出登录和注销只能二选一
#     poco("com.jz.htdj:id/tv_logout").click()
#     poco(text="退出后无法享用以下功能和权益").exists()
#     sleep(1)
#     poco("com.jz.htdj:id/tv_sure").click()
#     poco(text="设置").click()
    poco(text="账户与安全").wait_for_appearance()
    poco(text="账户与安全").click()
    sleep(1)
    poco(text="注销账号").wait_for_appearance()
    a = poco("com.jz.htdj:id/si_id").offspring(name="com.jz.htdj:id/tv_hint").get_text()
    print("用户id{}".format(a))
    poco(text="注销账号").click()
    sleep(1)
    poco(text="注销账号").wait_for_appearance()
    sleep(1)
    poco("com.jz.htdj:id/check_btn").click()
    sleep(1)
    poco("com.jz.htdj:id/logoff_btn").click()
    sleep(1)
    poco(text="注销账号后所有充值余额和会员权益将会永久失效，您确认注销吗?").wait_for_appearance
    poco(text="坚持注销账号").click()
    assert_equal("1", "1", "用户注销成功")
    sleep(1)
    
                
        
        
        
        
        
try:
    wake()
    swipe(start_pt1, end_pt1,1000)
    start_app('com.jz.htdj')
    home_page()
    print("推荐自动化任务执行成功")
except Exception as e:
    print("发生异常:", str(e))
    print("推荐自动化任务执行失败")
    
# try:
#     play_details_page()
#     print("播放详情页自动化任务执行成功")
# except Exception as e:
#     print("发生异常:", str(e))
#     print("播放详情页自动化任务执行失败")

# try:
#     theater()
#     print("剧场tab自动化任务执行成功")
# except Exception as e:
#     print("发生异常:", str(e))
#     print("剧场tab自动化任务执行失败")

# try:
#     history()
#     print("在看剧自动化任务执行成功")
# except Exception as e:
#     print("发生异常:", str(e))
#     print("在看剧自动化任务执行失败")

# try:
#     welfare()
#     print("福利自动化任务执行成功")
# except Exception as e:
#     print("发生异常:", str(e))
#     print("福利自动化任务执行失败")
    
# try:
#     my()
#     stop_app('com.jz.htdj')
#     print("我的自动化任务执行成功")
# except Exception as e:
#     print("发生异常:", str(e))
#     print("我的自动化任务执行失败")

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)