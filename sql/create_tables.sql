create or replace table CURATED_TRANSACTIONS (
    transaction_id string,
    transaction_date timestamp,
    customer_id number,
    product_category string,
    region string,
    status string,
    amount float,
    is_approved number,
    is_refunded number,
    reporting_date date
);
