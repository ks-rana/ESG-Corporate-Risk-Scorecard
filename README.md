# ESG Corporate Risk Scorecard

A sector-adjusted ESG (Environmental, Social, Governance) risk scoring tool that uses SASB materiality weights to produce ESG ratings appropriate to the industry being scored — so a financial services company is weighted toward governance, an energy company toward environmental, and so on. TCFD-aligned, with OSFI Guideline B-15 climate risk context for Canadian financial-sector users.

**Live tool:** https://esg-corporate-risk-scorecard-2oky9ixncf9k384hvmantw.streamlit.app
*(Hosted on Streamlit Community Cloud — may take 30 seconds to load on first visit.)*

---

## What this tool does

ESG scoring is widely critiqued for treating all sectors the same — a one-size-fits-all approach that produces ratings disconnected from sector-specific reality. SASB (the Sustainability Accounting Standards Board) addressed this by publishing materiality maps that identify which ESG factors are financially material for each industry.

This tool applies that thinking to a corporate ESG scorecard:

- Select an industry (Financial Services, Energy, Technology, etc.)
- Input ESG indicators
- Receive a score weighted by SASB materiality for that sector

A financial services company's score will be heavily influenced by governance factors. An energy company's score will be dominated by environmental factors. A consumer goods company will weight social factors more heavily. The framing follows what is *financially material* in each sector rather than treating ESG as a single uniform construct.

The tool also incorporates TCFD (Task Force on Climate-related Financial Disclosures) alignment for climate risk disclosure structure, and references OSFI Guideline B-15 — the Canadian climate risk management expectation for federally regulated financial institutions.

---

## What I designed

The scoring architecture is mine. I designed:

- **The sector materiality mapping** drawing on SASB's published materiality framework
- **The scoring logic** — how indicators within a sector aggregate, and how sector-specific weights are applied
- **The output structure** — what the user sees, how component scores are surfaced
- **The TCFD alignment overlay** — which TCFD pillars inform which parts of the scorecard
- **The OSFI B-15 contextualization** for users in Canadian financial-sector contexts

## What I did not build from scratch

The Python/Streamlit implementation was built using AI-assisted development. The code captures inputs, applies the weighting logic I designed, and renders the score. The technical implementation is straightforward Streamlit; the originality lives in the sector-adjustment methodology and standards integration.

---

## Why this matters

Most accessible ESG scoring tools either ignore sector materiality entirely or apply it in ways that obscure the underlying logic. This tool surfaces the materiality reasoning explicitly — *here is why your sector weights environmental more heavily, here is the SASB rationale, here is how the score moves when you adjust an input.* Users can disagree with the weights, but they can see them.

For Canadian financial-sector users specifically, the OSFI B-15 framing connects ESG scoring to actual regulatory expectations rather than treating it as a separate, voluntary exercise.

---

## Standards referenced

- **SASB Materiality Map** (Sustainability Accounting Standards Board)
- **TCFD** — Task Force on Climate-related Financial Disclosures
- **OSFI Guideline B-15** — Climate Risk Management (Office of the Superintendent of Financial Institutions)

---

## Contact

Designed and architected by Khushi Rana — Psychology × AI Governance @ University of Waterloo.

- ks2rana@uwaterloo.ca
- linkedin.com/in/khushi-rana
- khushi-rana-website.vercel.app
