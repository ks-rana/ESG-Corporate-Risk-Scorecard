# ESG Corporate Risk Scorecard

An interactive self-assessment tool that evaluates a company's Environmental, Social, and Governance performance against structured criteria drawn from GRI Standards, TCFD, SASB, and UN SDGs. Scores adjust automatically by sector using SASB materiality weights.

**Live tool:** https://esg-corporate-risk-scorecard-2oky9ixncf9k384hvmantw.streamlit.app

> Hosted on Streamlit Community Cloud — may take ~30 seconds to wake up on first visit.

---

## What it does

- Evaluates 20 criteria across 3 ESG pillars — Environmental, Social, and Governance
- Each question includes a plain-language explanation of why it matters
- Sector-adjusted scoring using SASB materiality weights — Financial Services weights governance higher, Energy weights environmental higher
- Generates a radar chart, bar chart, and pillar breakdown
- Identifies disclosure gaps by materiality level (High, Medium, Low)
- Produces prioritised recommendations per pillar
- Downloadable report as .txt file

## Sectors supported

Financial Services, Energy and Utilities, Technology, Healthcare, Manufacturing, Consumer Goods and Retail, Real Estate, Telecommunications, Other

## Frameworks referenced

- GRI Standards (200, 300, 400 series)
- TCFD (Task Force on Climate-related Financial Disclosures)
- SASB (Sustainability Accounting Standards Board)
- UN Sustainable Development Goals
- OECD Corporate Governance Principles
- ILO Core Conventions

## Scoring methodology

| Response | Value |
|---|---|
| Yes — fully disclosed | 1.0 |
| Partially — in progress | 0.5 |
| No — not addressed | 0.0 |
| Not applicable | excluded |

Overall score = sector-weighted average of pillar scores using SASB materiality weights.

Ratings: 80-100 Leading · 60-79 Developing · 40-59 Lagging · Below 40 At Risk

## Run locally

```bash
git clone https://github.com/ks-rana/ESG-Corporate-Risk-Scorecard
cd ESG-Corporate-Risk-Scorecard
pip install -r requirements.txt
streamlit run esg_scorecard.py
```

## Disclaimer

This is an educational reference tool only. It is not a formal ESG rating, investment recommendation, or regulatory compliance determination. Scores are based on self-reported inputs and have not been independently verified.

---

Built by Khushi Rana · Psychology x AI Governance · University of Waterloo
