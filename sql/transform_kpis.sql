create or replace view V_TRANSACTION_KPIS as
select
    reporting_date,
    count(*) as total_transactions,
    sum(case when status = 'approved' then amount else 0 end) as total_revenue,
    avg(case when status = 'approved' then amount end) as average_order_value,
    avg(is_approved) as approval_rate,
    avg(is_refunded) as refund_rate
from CURATED_TRANSACTIONS
group by reporting_date
order by reporting_date;
