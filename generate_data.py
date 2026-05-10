#!/usr/bin/env python3
"""
generate_data.py
Reproducible synthetic data generator for Coravio revenue dataset.

Usage:
    python generate_data.py
    python generate_data.py --seed 42
    python generate_data.py --out custom_path.csv
"""
import csv, random, argparse
from datetime import date, timedelta

COMPANIES = [
    "Apex Ventures","BlueStar Systems","Cascade Analytics","Drift Technologies",
    "Echo Digital","Forge Solutions","GridPoint Inc","Helix Data",
    "Iris Software","Juno Platforms","Keystone Labs","Luminary Corp",
    "Mesa Systems","Nova Analytics","Orbit Technologies","Prism Software",
    "Quantum Digital","Ridge Solutions","Slate Technologies","Titan Corp",
    "Union Analytics","Vertex Systems","Wave Digital","Xenon Labs",
    "Yellow Brick","Zenith Analytics","Arc Systems","Bridge Corp",
    "Cedar Analytics","Delta Software","Eagle Platforms","Falcon Digital",
    "Granite Solutions","Harbor Labs","Ionic Systems","Jasper Corp",
    "Kinetic Analytics","Lotus Systems","Marble Digital","Nexus Platforms",
    "Oak Analytics","Peak Software","Quest Labs","Reef Systems",
    "Stone Analytics","Tidal Digital","Uplift Corp","Valor Systems",
    "Westgate Labs","Pinnacle Systems","Meridian Analytics","Cobalt Digital",
    "Ellipsis Corp","Momentum Labs","Stratum Systems","Ironclad Analytics",
    "Cobblestone Tech","Clearview Digital","Polar Analytics","Redwood Corp",
    "Everest Systems","Sunridge Labs","Fathom Analytics","Coastal Digital",
    "Summit Corp","Highpoint Labs","Groundswell Analytics","Harbor Digital",
    "Landmark Systems","Solstice Corp","Tempest Analytics","Ironbridge Labs",
    "Driftwood Digital","Northstar Systems","Cloudbase Analytics","Seagate Labs",
]
PLAN_TIERS = {
    "Starter":    {"mrr_base": (250, 900),    "churn_rate": 0.035},
    "Growth":     {"mrr_base": (900, 4500),   "churn_rate": 0.020},
    "Enterprise": {"mrr_base": (4500, 22000), "churn_rate": 0.008},
}
SEGMENT_PLAN = {
    "SMB":        {"Starter": 0.70, "Growth": 0.28, "Enterprise": 0.02},
    "Mid-Market": {"Starter": 0.12, "Growth": 0.65, "Enterprise": 0.23},
    "Enterprise": {"Starter": 0.02, "Growth": 0.25, "Enterprise": 0.73},
}
REGIONS  = ["Americas", "EMEA", "APAC"]
CHANNELS = ["Inbound", "Direct Sales", "Partner", "Outbound"]
FIELDS   = ["customer_id","company_name","plan_tier","segment","region",
            "channel","acquisition_date","month","mrr","expansion_mrr","is_active"]

def weighted_choice(d):
    r = random.random(); c = 0
    for k, w in d.items():
        c += w
        if r < c: return k
    return list(d)[-1]

def generate(seed=2024):
    random.seed(seed)
    customers = []
    for i, name in enumerate(COMPANIES):
        seg  = weighted_choice({"SMB":0.45,"Mid-Market":0.35,"Enterprise":0.20})
        plan = weighted_choice(SEGMENT_PLAN[seg])
        lo, hi = PLAN_TIERS[plan]["mrr_base"]
        customers.append({
            "customer_id": f"CUST-{i+1:04d}", "company_name": name,
            "plan_tier": plan, "segment": seg,
            "region": random.choice(REGIONS), "channel": random.choice(CHANNELS),
            "acquisition_date": date(2021,1,1) + timedelta(days=random.randint(0,730)),
            "base_mrr": round(random.uniform(lo, hi), -1),
            "churn_rate": PLAN_TIERS[plan]["churn_rate"],
        })
    rows = []
    for c in customers:
        active, mrr = True, c["base_mrr"]
        for yr in range(2022, 2025):
            for mo in range(1, 13):
                mdt = date(yr, mo, 1)
                if mdt < c["acquisition_date"].replace(day=1) or not active: continue
                if random.random() < c["churn_rate"]: active = False; continue
                exp = round(mrr * random.uniform(0, 0.06), -1) if random.random() < 0.12 else 0
                mrr = round(mrr + exp, -1)
                rows.append({
                    "customer_id": c["customer_id"], "company_name": c["company_name"],
                    "plan_tier": c["plan_tier"], "segment": c["segment"],
                    "region": c["region"], "channel": c["channel"],
                    "acquisition_date": c["acquisition_date"].strftime("%m/%d/%Y"),
                    "month": mdt.strftime("%m/%d/%Y"), "mrr": mrr,
                    "expansion_mrr": exp, "is_active": 1,
                })
    return rows

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out",  default="data/saas_revenue_data.csv")
    parser.add_argument("--seed", default=2024, type=int)
    args = parser.parse_args()
    rows = generate(seed=args.seed)
    with open(args.out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader(); w.writerows(rows)
    print(f"Generated {len(rows):,} records → {args.out}")

if __name__ == "__main__":
    main()
