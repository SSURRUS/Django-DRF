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
order_on = '2022111400009090898'
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
    alipay_public_key_string=public_key,
    # 开启Debug模式(沙箱环境下开启)
    debug=True,
)

# 4、查询支付结果
result = pay.api_alipay_trade_query(out_trade_no=order_on)
print(result)
"""
{
'code': '10000', 
'msg': 'Success', 
'buyer_logon_id': 'lli***@sandbox.com', 
'buyer_pay_amount': '0.00', 
'buyer_user_id': '2088102176818981', 
'buyer_user_type': 'PRIVATE', 
'invoice_amount': '0.00', 
'out_trade_no': '2022111400009090898', 
'point_amount': '0.00', 
'receipt_amount': '0.00', 
'send_pay_date': '2022-11-14 16:22:15',
'total_amount': '199.00', 
'trade_no': '2022111422001418980503051530', 
'trade_status': 'TRADE_SUCCESS'
 }


"""

