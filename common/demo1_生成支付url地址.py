from alipay import AliPay

# 1、准备支付宝的应用数据(调试阶段使用沙箱环境)
# 应用ID
app_id = '2016092000557568'
# 商户号:
pid = '2088102176523162'
# 公钥和私钥
public_key = open('alipay_public_key.pem').read()
private_key = open('app_private_key.pem').read()

# 2、订单支付的信息(自己系统的订单信息)
# 订单号
order_on = '202211140000909088'
# 订单金额
amount = '199.00'
# 支付页面显示的标题
subject = '生鲜商城订单{}支付'.format(order_on)

# 3、初始化一个支付的对象
pay = AliPay(
    # 应用ID
    appid=app_id,
    # app_notify_url支付回调咱们系统的url(部署到服务器上时可以配置)
    app_notify_url=None,
    # 私钥
    app_private_key_string=private_key,
    # 公钥
    alipay_public_key_string=private_key,
    # 开启Debug模式(沙箱环境下开启)
    debug=True,
)

# 4、生成手机应用的支付地址
# url = pay.api_alipay_trade_wap_pay(
# #     # 支付页面的标题
# #     subject=subject,
# #     # 商户生成的订单号(自己系统中订单的编号)
# #     out_trade_no=order_on,
# #     # 订单支付的金额
# #     total_amount=amount,
# #     # 需要将产品部署到服务器再进行配置
# #     return_url=None,
# #     notify_url=None,
# # )

# 5、生成PC浏览器网站的支付页面地址
url = pay.api_alipay_trade_page_pay(
    # 支付页面的标题
    subject=subject,
    # 商户生成的订单号(自己系统中订单的编号)
    out_trade_no=order_on,
    # 订单支付的金额
    total_amount=amount,
    # 需要将产品部署到服务器再进行配置
    return_url=None,
    notify_url=None,
)
pay_url = 'https://openapi.alipaydev.com/gateway.do?' + url
print(pay_url)

# 4、查询支付结果
result = pay.api_alipay_trade_query(out_trade_no=order_on)
print(result)

# 6、生成app支付的页面地址
# url = pay.api_alipay_trade_app_pay(
#     # 支付页面的标题
#     subject=subject,
#     # 商户生成的订单号(自己系统中订单的编号)
#     out_trade_no=order_on,
#     # 订单支付的金额
#     total_amount=amount,
#     # 需要将产品部署到服务器再进行配置
#     return_url=None,
#     notify_url=None,
# )
#
