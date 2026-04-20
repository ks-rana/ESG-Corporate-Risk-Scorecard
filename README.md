# AI Governance Audit Framework

> **Live Tool →** [https://ai-governance-audit-9abmdtb9a4zsyrffdqzkbc.streamlit.app/](https://ai-governance-audit-9abmdtb9a4zsyrffdqzkbc.streamlit.app/)
> *(Hosted on Streamlit Cloud — may take ~30s to wake up on first load)*

---

## What This Is

An interactive AI governance audit tool that evaluates AI systems across **6 domains and 30 questions**, estimates a Canada AIA Impact Level (1–4), and generates a compliance report with a cross-regulatory reference matrix and sign-off block.

This is not a general-purpose framework — it is specifically designed for the **Canadian regulatory context**, incorporating the Treasury Board Secretariat's Algorithmic Impact Assessment (AIA) methodology, OSFI Guideline E-23 (2027), PIPEDA, and the Canadian Human Rights Act alongside international standards (EU AI Act, NIST AI RMF, ISO 42001).

---

## Why It Was Built

Most AI governance tools produce a flat score. Canadian regulators and financial institutions want something more specific: a **Raw Impact Score**, a **Mitigation Score**, an estimated **AIA Level**, a mapping to specific regulatory clauses, and a plan for what to measure after deployment.

This tool automates all of that — producing an artifact that a Risk Officer, Privacy Officer, or AIA Peer Reviewer could actually use as a starting document.

---

## The 6 Domains

| # | Domain | Weight | Frameworks |
|---|---|---|---|
| 1 | Transparency & Explainability | 18% | EU AI Act Art. 13 · NIST AI RMF MAP · ISO 42001 §8.4 · AIA Level 2+ |
| 2 | Fairness & Non-Discrimination | 20% | EU AI Act Art. 10 · NIST MEASURE · AIA GBA+ · Canadian Human Rights Act |
| 3 | Accountability & Oversight | 20% | OSFI E-23 §4 · NIST GOVERN · ISO 42001 §5.3 · AIA Level 2+ |
| 4 | Security & Robustness | 16% | NIST MANAGE · ISO 42001 §8.5 · EU AI Act Art. 15 · OSFI B-13 |
| 5 | Privacy & Data Governance | 16% | PIPEDA · ISO 42001 §8.3 · OSFI E-23 §6 · AIA Privacy §50–59 |
| 6 | **OSFI E-23 — Model Risk Management** | 10% | OSFI E-23 §1–9 · OSFI B-13 · OSFI B-10 |

Domain 6 is specific to federally regulated financial institutions (FRFIs). Non-OSFI organizations should mark those questions N/A.

---

## Key Features

### Canada AIA Proxy Scoring
Each response contributes to a weighted **Raw Impact Score** and **Mitigation Score**:
- `No — not addressed` → adds to Raw Score (gap increases risk level)
- `Partially — in progress` → partial Raw Score addition + partial Mitigation credit
- `Yes — fully in place` → full Mitigation credit

**Estimated Impact Level thresholds:**
| Raw Score | Level | Label |
|---|---|---|
| < 30 | 1 | Minimal |
| 30–49 | 2 | Moderate |
| 50–69 | 3 | Significant |
| ≥ 70 | 4 | High |

Each level's mandatory Canadian requirements are displayed — notice requirements, explanation standards, peer review obligations, GBA+ assessment, human oversight, and approval authority.

### OSFI E-23 Domain (Domain 6)
Five questions specific to federally regulated financial institutions:
1. **Model Inventory** — unique ID and designated owner per E-23 §1.1
2. **Independent Validation** — methodology validated by party independent of developers per §2.1
3. **Breach Thresholds** — performance drift triggers defined per §7
4. **Scope Controls** — model use limited to approved purpose per §3.2
5. **Change Management** — formal process for all model updates per §8

### AIA-Specific Privacy Questions
- **AIA Q55** — Has a formal Privacy Impact Assessment been completed or initiated?
- **AIA Q58** — Will personal information be de-identified at any point in the system lifecycle?

### Compliance Matrix
Every question is mapped to its source regulatory clause — shown inline on each question card and as a full expandable table in the results. Every finding can be traced to a specific AIA section, OSFI clause, or ISO/NIST reference.

### KPI Blueprint
After assessment, a **Governance KPI Blueprint** is generated with 16 KPIs across three phases, filtered to the user's estimated AIA level. Each KPI includes:
- Plain-language name and why it matters
- Formula with target thresholds
- Alert flag with specific trigger numbers
- Regulatory reference

**Pre-Deployment KPIs** (establish before go-live):
- Data Completeness Rate
- Proxy Correlation Score
- Training Data Bias Score
- PII De-identification Coverage
- Model Inventory Completeness

**Post-Deployment KPIs** (measure after launch):
- Disparate Impact Ratio (4/5 Rule — Canadian Human Rights Act)
- Explainability Coverage
- Human Override Rate (with both failure modes explained)
- False Negative Rate by Demographic
- Recourse Utilization Rate

**Continuous KPIs** (never stop measuring):
- Model Drift Velocity (Population Stability Index)
- Mean Time to Detect Bias (MTTD)
- Audit Trail Completeness
- Model Inventory Currency
- PII Exposure Incidents
- GBA+ Re-assessment Frequency

### Ticket-Based Findings
Findings are presented as structured issue tickets with:
- Unique IDs (`GOV-TE-001`, `GOV-FA-002`, etc.)
- Severity badge (Critical / High / Medium / Low)
- Domain and status (Gap / Partial)
- Why-it-matters explanation
- Specific Canadian regulatory context

### Compliance Report Export
A downloadable `.txt` report containing:
1. Canada AIA proxy assessment (Raw Score, Mitigation Score, Level, mandatory requirements)
2. Governance framework scores by domain
3. Full response log (all 30 questions)
4. Findings (all tickets)
5. Recommendations (domain-specific, Canadian-framed)
6. KPI Blueprint (filtered by AIA level)
7. Compliance matrix
8. Three-party sign-off block:
   - **Model Risk Officer** (OSFI E-23 §4)
   - **Chief Privacy Officer** (PIPEDA / AIA Privacy)
   - **AIA Peer Reviewer** (AIA Level 2 §Peer Review) — includes "Review Published" field with URL line

---

## Scoring Methodology

| Response | Score Value | AIA Effect |
|---|---|---|
| Yes — fully in place | 1.0 | Full Mitigation credit |
| Partially — in progress | 0.5 | Partial credit in both |
| No — not addressed | 0.0 | Adds to Raw Impact Score |
| Not applicable | excluded | No effect |

**Overall Score** = weighted average across 6 domains  
**AIA Level** = estimated from proxy Raw Impact Score using GC Directive thresholds  
**Ratings:** 80–100 Strong · 60–79 Adequate · 40–59 Needs Work · <40 High Risk

---

## Regulatory Disclaimer

This tool is an educational reference. It does not constitute a formal AIA submission, legal opinion, or OSFI supervisory determination. For real automated decision systems:
- Complete the official AIA at [canada.ca/aia-tool](https://canada.ca/aia-tool)
- For OSFI-regulated institutions, engage your Model Risk Officer and consult OSFI Guidelines E-23 and B-13

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web application framework |
| Plotly | Radar chart, domain bar chart |

No additional dependencies beyond base Streamlit.

---

## Running Locally

```bash
git clone https://github.com/ks-rana/ai-governance-audit.git
cd ai-governance-audit
pip install streamlit plotly
streamlit run app.py
```

---

## About

Built by **Khushi Rana** — Psychology × AI Governance, University of Waterloo. Currently AI Risk Governance Intern at Rogers Communications.

This framework was stress-tested against real-world AIA disclosures (including IRCC's International Student Program AIA, Impact Level 2) to verify scoring accuracy and ensure the Canadian regulatory context is accurate.

[LinkedIn](https://www.linkedin.com/in/khushi-rana-00764223a) · [Portfolio](https://khushi-rana-website.vercel.app/)
