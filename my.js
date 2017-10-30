//点击优惠内购，跳转到MATE9购买页面
var str = window.location.href;
var srcurlformate = 'https://www.vmall.com/member/enterprise'
if(str == srcurlformate)
{
	window.location.href='https://www.vmall.com/member/enterprise?showListId=4&categoryId=9&p=2&categoryName=%E5%8D%8E%E4%B8%BA%E6%89%8B%E6%9C%BA&index=9-%E5%8D%8E%E4%B8%BA%E6%89%8B%E6%9C%BA';
}



function ScTotalBtn()
{
	document.getElementsByClassName("sc-total-btn")[0].click();
	window.setTimeout(function(){
		Pay();
	}, 500);
}

//第四步：点击提交订单
function OrderSubmitBtn()
{
	document.getElementsByClassName("order-submit-btn")[0].click();
}

//第三步：点击立即结算
function CartPay()
{
	for (var i = 0; i < $("a").length; i += 1) {
		if($("a")[i].getAttribute("seed") == "cart-pay")
		{
			$("a")[i].click();
			window.setTimeout(function(){
				ScTotalBtn();
			}, 500);
		}
	}
}

var src = window.location.href;
var dst = 'https://www.vmall.com/cart';
if(str == dst)
{
	CartPay();
}

//第二步：点击去结算
function GoCart()
{
	document.getElementsByClassName("button-go-cart box-ok")[0].click();
	//window.setTimeout(function(){
		//CartPay();
	//}, 500);	
}

//第一步：点击加入购物车
function main()
{
	document.getElementById("hwep-buy-620322982").click();
	window.setTimeout(function(){
		GoCart();
	}, 500);
}

window.setTimeout(function(){
	if(document.getElementById("hwep-buy-620322982").getAttribute("title") != "库存暂不足")
	{
		main();
	}
},500)
