//点击优惠内购，跳转到MATE9购买页面
var str = window.location.href;
var srcurlformate = 'https://www.vmall.com/member/enterprise'
if(str == srcurlformate)
{
	window.location.href='https://www.vmall.com/member/enterprise?showListId=4&categoryId=9&p=2&categoryName=%E5%8D%8E%E4%B8%BA%E6%89%8B%E6%9C%BA&index=9-%E5%8D%8E%E4%B8%BA%E6%89%8B%E6%9C%BA';
}

//第四步：点击提交订单
function OrderSubmitBtn()
{
	if(document.getElementsByClassName("order-submit-btn").length >= 1
	&& document.getElementsByClassName("order-submit-btn")[0] != null)
	{
		document.getElementsByClassName("order-submit-btn")[0].click();
	}
}
window.setInterval(function(){
	OrderSubmitBtn();
}, 100);

//第三步：点击立即结算
function CartPay()
{
	for (var i = 0; i < $("a").length; i += 1) {
		if($("a")[i].getAttribute("seed") == "cart-pay")
		{
			$("a")[i].click();
		}
	}
}
window.setInterval(function(){
	CartPay();
}, 300);

//第二步：点击去结算
function GoCart()
{
	if(document.getElementsByClassName("button-go-cart box-ok").length >= 1
	&& document.getElementsByClassName("button-go-cart box-ok")[0] != null)
	{
		document.getElementsByClassName("button-go-cart box-ok")[0].click();
	}
}
window.setInterval(function(){
	GoCart();
}, 100);

//第一步：点击加入购物车
function main()
{
	if(document.getElementById("hwep-buy-620322982") != null 
	&& 	document.getElementById("hwep-buy-620322982").getAttribute("title") != "库存暂不足")
	{
		document.getElementById("hwep-buy-620322982").click();
	}
}
window.setInterval(function(){
	main();
}, 100);
