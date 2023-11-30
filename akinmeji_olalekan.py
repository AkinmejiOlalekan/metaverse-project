"""
    author: akinmejiaolalekan7@gmail.com
"""

question_one = """
select txn_type, count (txn_type) as total_btc_transactions
from raw.transactions
where ticker = 'BTC'
group by txn_type;
"""

question_two = """
select distinct (extract (year from cast (txn_date as date))) as txn_year, txn_type, count(txn_type) as txt_count, sum(quantity) as total_quantity, avg(quantity) as average_quantity
from raw.transactions
group by txn_year, txn_type
order by txn_year;
"""

question_three = """
with buy as (
	select 
		extract (month from cast (txn_date as date)) as calender_month,
		sum(quantity) as buy_quantity
	from raw.transactions
	where (ticker = 'ETH' and txn_type = 'BUY') and extract (year from cast (txn_date as date)) = '2020'
	group by calender_month
),
	sell as (
	select 
		extract (month from cast (txn_date as date)) as calender_month,
		sum(quantity) as sell_quantity
	from raw.transactions
	where (ticker = 'ETH' and txn_type = 'SELL') and extract (year from cast (txn_date as date)) = '2020'
	group by calender_month
)
select 
	buy.calender_month,
	buy.buy_quantity,
	sell.sell_quantity
from buy 
inner join sell
	on buy.calender_month = sell.calender_month
group by buy.calender_month, buy.buy_quantity, sell.sell_quantity;
"""


question_four = """
with btc_bought as(
	select 
		member_id,
		sum (quantity) as bought_quantity
	from raw.transactions
	where ticker = 'BTC' and txn_type = 'BUY'
	group by member_id),
btc_sold as (
	select 
		member_id, 
		sum(quantity) as sold_quantity
	from raw.transactions
	where ticker = 'BTC' and txn_type = 'SELL'
	group by member_id)
select
	members.first_name, (btc_bought.bought_quantity - btc_sold.sold_quantity) as total_quantity
from btc_bought
inner join btc_sold
	on btc_bought.member_id = btc_sold.member_id
inner join raw.members
	on btc_bought.member_id = members.member_id
order by total_quantity desc
limit 3;
"""