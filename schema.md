# Data Dictionary — `saas_revenue_data.csv`

**Grain:** One row per active customer per billing month
**Date range:** January 2022 – December 2024
**Customers:** 74 unique
**Records:** ~1,720

## Columns

| # | Column | Type | Description | Example |
|---|---|---|---|---|
| 1 | `customer_id` | STRING | Unique key | `CUST-0042` |
| 2 | `company_name` | STRING | Company name | `Apex Ventures` |
| 3 | `plan_tier` | STRING | Subscription tier | `Growth` |
| 4 | `segment` | STRING | Market segment | `Mid-Market` |
| 5 | `region` | STRING | Geographic region | `EMEA` |
| 6 | `channel` | STRING | Acquisition channel | `Inbound` |
| 7 | `acquisition_date` | DATE | First subscription date | `03/15/2022` |
| 8 | `month` | DATE | Billing month (first day) | `06/01/2023` |
| 9 | `mrr` | FLOAT | Monthly Recurring Revenue | `1840.00` |
| 10 | `expansion_mrr` | FLOAT | Expansion/upsell revenue | `120.00` |
| 11 | `is_active` | INT | 1 = active | `1` |

## Enums

**plan_tier:** `Starter` (3.5% churn) · `Growth` (2.0%) · `Enterprise` (0.8%)

**segment:** `SMB` · `Mid-Market` · `Enterprise`

**region:** `Americas` · `EMEA` · `APAC`

**channel:** `Inbound` · `Direct Sales` · `Partner` · `Outbound`
