# ESG Corporate Risk Scorecard

> **Live Tool →** [https://esg-corporate-risk-scorecard-2oky9ixncf9k384hvmantw.streamlit.app/](https://esg-corporate-risk-scorecard-2oky9ixncf9k384hvmantw.streamlit.app/)
> *(Hosted on Streamlit Cloud — may take ~30s to wake up on first load)*

---

## What This Is

An interactive ESG (Environmental, Social, Governance) risk scorecard that evaluates organizations across **20 criteria** using **sector-adjusted materiality weights**. Select your sector and the weighting shifts automatically — Financial Services prioritizes Governance, Energy prioritizes Environmental. The tool produces a radar chart, domain breakdown, sector-specific risk cards, and a downloadable report.

---

## Why Sector-Adjusted Weights Matter

ESG is not one-size-fits-all. A bank's most material ESG risk is not its carbon footprint — it's the governance of the models it uses to make credit decisions, and the social impact of who gets access to capital. An energy company's biggest risk is stranded assets from the climate transition.

This tool operationalizes that insight using **SASB (Sustainability Accounting Standards Board) materiality** — a widely adopted framework that defines which ESG topics are financially significant by industry sector. Flat ESG scores without sector adjustment produce misleading comparisons. This tool doesn't make that mistake.

---

## The 3 Pillars

### Environmental (E)
Aligned to TCFD, GRI 300 series, and OSFI B-15 (Climate Risk Management).

| Question | Materiality | Why It Matters |
|---|---|---|
| Scope 1, 2, and 3 GHG emissions disclosure | High | Scope 3 is typically 70%+ of total emissions; without it, climate picture is incomplete. Required under TCFD and EU CSRD. |
| Science-based emissions reduction targets (SBTi) | High | Targets not validated by SBTi are increasingly flagged as greenwashing by regulators and investors. |
| TCFD-aligned climate risk assessment | High | Assesses both physical risks (floods) and transition risks (policy). Increasingly mandatory in major markets. |
| Water usage and reduction targets | Medium | Sector-specific but growing in materiality; relevant to agriculture, manufacturing, tech. |
| Supply chain environmental risk assessment | Medium | Many companies' largest environmental impacts sit in their supplier network — required under Germany's Supply Chain Act, EU CSRD. |
| Net-zero pathway credibility | High | Interim targets, clear methodology, third-party verification. "Net-zero by 2050" without milestones is insufficient. |
| Biodiversity and land-use impact | Low | Emerging frontier driven by TNFD and COP15. Early disclosure signals forward-thinking governance. |

### Social (S)
Aligned to GRI 400 series, ILO Core Conventions, and UN SDGs 8 and 10.

| Question | Materiality | Why It Matters |
|---|---|---|
| Pay equity and gender diversity data by seniority | High | EU Pay Transparency Directive now mandates this. Proxy advisors use it to assess culture and retention risk. |
| Human rights due diligence in supply chain | High | Mandatory under France's Loi de Vigilance, Germany's Supply Chain Act, EU CSRD. UN Guiding Principles standard. |
| Health, safety, and wellbeing policy with metrics | Medium | Injury rates and lost-time incidents signal management quality. Investors treat H&S data as a proxy for operational discipline. |
| Employee grievance mechanism | Medium | Baseline expectation under UN Guiding Principles and GRI 402. Absence is a governance red flag in labour-intensive sectors. |
| Community investment and local impact | Low | Social licence to operate — directly affects operating permissions and brand trust in extractive/infrastructure sectors. |
| Supplier labour standards with third-party audits | High | Unverified supplier commitments are legally insufficient after high-profile supply chain scandals. |

### Governance (G)
Aligned to GRI 200 series, OECD Corporate Governance Principles, and TCFD Governance pillar.

| Question | Materiality | Why It Matters |
|---|---|---|
| Board-level ESG oversight with named responsibility | High | TCFD requires board-level accountability. Investors vote against boards that cannot demonstrate ESG governance. |
| Executive compensation linked to ESG metrics | High | Without this link, ESG goals are PR — not business objectives. ISS and Glass Lewis flag absence as governance concern. |
| Anti-corruption policies with breach data disclosure | High | Disclosing actual breach data, not just the policy, is the real test of governance quality. |
| Board diversity across gender, background, expertise | Medium | Diversity linked to better decisions and reduced groupthink. Skills matrix signals ESG expertise at board level. |
| Third-party ESG assurance or verification | High | Without assurance, ESG disclosures are self-reported and unverifiable. Becoming mandatory under CSRD for large companies. |
| Lobbying and political donations disclosure | Medium | Tests whether public ESG commitments align with political influence activities. |
| Formal stakeholder engagement for materiality | Medium | GRI and SASB require structured engagement as the basis for materiality assessments. Ad hoc engagement is insufficient. |

---

## Sector-Adjusted Materiality Weights

Weights shift automatically when you select your sector. Aligned to SASB materiality maps.

| Sector | E | S | G |
|---|---|---|---|
| Financial Services | 25% | 30% | 45% |
| Energy & Utilities | 50% | 25% | 25% |
| Technology | 25% | 35% | 40% |
| Healthcare | 20% | 45% | 35% |
| Manufacturing | 45% | 30% | 25% |
| Consumer Goods/Retail | 35% | 35% | 30% |
| Real Estate | 40% | 25% | 35% |
| Telecommunications | 25% | 35% | 40% |

---

## Scoring Methodology

| Response | Value |
|---|---|
| Yes — fully disclosed | 1.0 |
| Partially — in progress | 0.5 |
| No — not addressed | 0.0 |
| Not applicable | excluded from average |

**Pillar score** = average of scored responses × 100  
**Overall score** = sector-weighted average using SASB materiality  
**Ratings:** 80–100 Leading · 60–79 Developing · 40–59 Lagging · <40 At Risk

---

## Key Features

- **Step-by-step assessment** — work through each pillar sequentially with live domain score tracking
- **Plain-language explanations** — every question includes a "Why this matters" section explaining the regulatory and business case
- **Sector-specific risk cards** — results surface the top 3 ESG material risks for your selected sector
- **Radar chart** — visual overview of E, S, G balance at a glance
- **Domain bar chart** — pillar-by-pillar breakdown with colour-coded ratings
- **Downloadable report (.txt)** — company metadata, pillar scores, sector weights, full response log, findings, and priority recommendations

---

## Canadian Regulatory Context

The Governance pillar and sector weighting logic are particularly relevant for Canadian financial institutions:

- **OSFI B-15 (Climate Risk Management)** — banks and insurers are expected to assess physical and transition climate risk. The Environmental pillar's TCFD questions directly map to B-15 expectations.
- **OSFI E-23** — model governance is a Governance ESG criterion. A bank that cannot demonstrate board-level accountability for its AI models has a Governance gap under both OSFI E-23 and SASB Financial Services materiality.
- **TCFD** — now mandatory for large Canadian public companies under CSA climate disclosure rules.

---

## Regulatory Disclaimer

This scorecard is an educational reference tool. It is not a formal ESG rating, investment recommendation, or regulatory compliance determination. Scores are based on self-reported inputs only. For investment, procurement, or governance decisions, engage a qualified ESG analyst and verify using primary sources (CDP disclosures, company sustainability reports, MSCI ESG, Sustainalytics).

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web application framework |
| Plotly | Radar chart, bar chart, sector visualizations |

---

## Running Locally

```bash
git clone https://github.com/ks-rana/ESG-Corporate-Risk-Scorecard.git
cd ESG-Corporate-Risk-Scorecard
pip install streamlit plotly
streamlit run app.py
```

---

## About

Built by **Khushi Rana** — Psychology × AI Governance, University of Waterloo. Currently AI Risk Governance Intern at Rogers Communications.

The sector-adjusted weighting logic was built to address a gap in most ESG tools: a flat score without materiality context is not useful for decision-making. This tool asks *what matters for this industry* before scoring anything.

[LinkedIn](https://www.linkedin.com/in/khushi-rana-00764223a) · [Portfolio](https://khushi-rana-website.vercel.app/)
