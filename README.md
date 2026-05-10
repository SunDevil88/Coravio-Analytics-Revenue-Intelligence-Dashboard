# Coravio — Revenue Intelligence Dashboard

![Tableau](https://img.shields.io/badge/Tableau-Public-E97627?style=flat&logo=tableau&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Data](https://img.shields.io/badge/Records-1%2C720-4CAF50?style=flat)
![Status](https://img.shields.io/badge/Status-Live-success?style=flat)

> A revenue intelligence dashboard for Coravio, a fictional B2B SaaS company. Tracks MRR growth, plan tier distribution, regional revenue, customer segmentation, and expansion revenue across 74 customers and 3 global regions — 2022 through 2024.

🔗 **[View Live Dashboard on Tableau Public](https://public.tableau.com/app/profile/jaya.krishna.medimpudi7688/viz/Coravio-RevenueIntelligenceDashboard/Dashboard)**

---

## Dashboard

[![Dashboard Preview](assets/preview.png)](https://public.tableau.com/app/profile/jaya.krishna.medimpudi7688/viz/Coravio-RevenueIntelligenceDashboard/Dashboard)

---

## Overview

This project demonstrates the full analytics engineering workflow — from data model design to published BI output. The dataset mirrors what a `fct_mrr` mart model produces in a dbt pipeline: a flat, customer-month grain table pre-aggregated for BI consumption.

Five panels answer the core questions a revenue leadership team tracks weekly:

| Panel | Question answered |
|---|---|
| MRR Growth Trend | How is Monthly Recurring Revenue trending over time? |
| MRR by Plan Tier | Which plan tier drives the most revenue? |
| Revenue by Region | Where is revenue concentrated geographically? |
| Customers by Segment | Which customer segments are largest by count? |
| Expansion MRR by Channel | Which acquisition channels generate the most expansion revenue? |

---

## Data Model

**Grain:** One row per active customer per billing month (`customer_id × month`).

This structure maps directly to the output of a `fct_subscriptions` or `fct_mrr` mart model in dbt — optimized for BI consumption without window functions at query time.

### Schema

| Column | Type | Description |
|---|---|---|
| `customer_id` | STRING | Unique customer key (`CUST-XXXX`) |
| `company_name` | STRING | Customer company name |
| `plan_tier` | STRING | `Starter` · `Growth` · `Enterprise` |
| `segment` | STRING | `SMB` · `Mid-Market` · `Enterprise` |
| `region` | STRING | `Americas` · `EMEA` · `APAC` |
| `channel` | STRING | `Inbound` · `Direct Sales` · `Partner` · `Outbound` |
| `acquisition_date` | DATE | Date of first subscription |
| `month` | DATE | First day of the billing month |
| `mrr` | FLOAT | Monthly Recurring Revenue (USD) |
| `expansion_mrr` | FLOAT | Upsell / seat expansion revenue that month |
| `is_active` | INT | `1` = active subscription |

### Business rules

- MRR is recognized on the first of each billing month
- Expansion MRR is tracked separately to enable NRR calculation
- Churn is modeled probabilistically: Enterprise 0.8% / Growth 2.0% / Starter 3.5% per month
- Records only exist for months where `is_active = 1`

---

## Key Insights

| Finding | Detail |
|---|---|
| Enterprise concentration | $5.5M of total MRR — ~70% revenue from 12 customers |
| Americas leads regionally | $3.6M vs $2.2M APAC vs $2.1M EMEA |
| SMB drives volume, not revenue | 32 customers but only $311K MRR |
| Direct Sales expands most | $8,830 expansion MRR — highest of all channels |
| MRR peaked early 2023 | Churn outpacing new business — retention is the growth lever |

---

## Design decisions

**Two-color system:**
- Blue family → all total revenue metrics (MRR Trend, Plan Tier, Region, Segment)
- Teal → expansion revenue only (visually signals a different metric type)

**Plan Tier hierarchy:**
- Enterprise → darkest navy · Growth → medium blue · Starter → lightest blue

**Fixed Y-axis from $100K** — removes empty whitespace, amplifies trend movement visibility for leadership.

---

## Repo structure

```
coravio-revenue-dashboard/
├── README.md
├── .gitignore
├── data/
│   ├── saas_revenue_data.csv     ← source dataset (1,720 records)
│   ├── generate_data.py          ← reproducible generation script
│   └── schema.md                 ← full data dictionary
└── assets/
    └── preview.png               ← dashboard screenshot
```

---

## Reproduce locally

```bash
python data/generate_data.py
# → outputs data/saas_revenue_data.csv

# Then open Tableau Public Desktop → connect to the CSV → rebuild the dashboard
```

---

## Related projects

[**dbt Analytics Pipeline**](https://github.com/medimpudi/dbt-analytics) — BigQuery + dbt project with staging, intermediate, and mart layers on TPC-H seed data. The mart layer in that project produces tables of the same grain and structure as this dashboard's data source.

---

## Tech stack

| Tool | Role |
|---|---|
| Python 3.10 | Data generation |
| Tableau Public | Dashboard design and hosting |
| GitHub | Version control and portfolio |

---

**Jaya Krishna Medimpudi** · Analytics Engineer · Phoenix, AZ
[LinkedIn](https://linkedin.com/in/medimpudi) · [Tableau Public](https://public.tableau.com/app/profile/jaya.krishna.medimpudi7688) · [GitHub](https://github.com/medimpudi)

---
*Coravio is a fictional B2B SaaS company created for this portfolio project. All data is synthetically generated.*
