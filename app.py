import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(
    page_title="ESG Corporate Risk Scorecard",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;900&family=DM+Sans:wght@300;400;500&family=DM+Mono:wght@300;400&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #f5f2eb !important;
    color: #1c1f17 !important;
}
.main, .block-container { background-color: #f5f2eb !important; }
[data-testid="stAppViewContainer"] { background-color: #f5f2eb !important; }
[data-testid="stHeader"] { background-color: #f5f2eb !important; }
h1, h2, h3 { font-family: 'Playfair Display', serif !important; color: #1c1f17 !important; }

p, span, label, div { color: #1c1f17; }

/* ---- SIDEBAR — DO NOT TOUCH ---- */
[data-testid="stSidebar"] { background: #1c1f17 !important; border-right: 1px solid rgba(255,255,255,0.06); }
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] div { color: #c8c4b0 !important; }
[data-testid="stSidebar"] input[type="text"] { background-color: #2a2d22 !important; color: #e8e4d4 !important; border: 1px solid rgba(255,255,255,0.1) !important; border-radius: 6px !important; }
[data-testid="stSidebar"] [data-baseweb="select"] > div { background-color: #2a2d22 !important; border: 1px solid rgba(255,255,255,0.1) !important; border-radius: 6px !important; color: #e8e4d4 !important; }
[data-testid="stSidebar"] [data-baseweb="select"] span { color: #e8e4d4 !important; }
[data-testid="stSidebar"] [data-baseweb="select"] svg { fill: #7a9a5a !important; }
[data-baseweb="popover"] [data-baseweb="menu"] { background-color: #2a2d22 !important; border: 1px solid rgba(255,255,255,0.1) !important; }
[data-baseweb="popover"] [role="option"] { background-color: #2a2d22 !important; color: #e8e4d4 !important; }
[data-baseweb="popover"] [role="option"]:hover,
[data-baseweb="popover"] [aria-selected="true"] { background-color: #3a4a2a !important; color: #b8d48a !important; }

/* ---- MAIN PAGE TYPOGRAPHY ---- */
.slabel {
    font-family: 'DM Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #4a6a2a;
    margin-bottom: 4px;
    margin-top: 24px;
    display: block;
}

/* ---- HERO ---- */
.hero {
    background: #1c1f17;
    border-radius: 20px;
    padding: 52px 48px 44px;
    margin-bottom: 28px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    width: 280px; height: 280px;
    border-radius: 50%;
    border: 1px solid rgba(122,154,90,0.1);
    bottom: -80px; right: -60px;
}
.hero-tag {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #7a9a5a;
    border: 1px solid rgba(122,154,90,0.3);
    background: rgba(122,154,90,0.1);
    padding: 4px 12px;
    border-radius: 4px;
    display: inline-block;
    margin-bottom: 18px;
}
.hero h1 {
    font-family: 'Playfair Display', serif !important;
    font-size: 2.6rem !important;
    font-weight: 900 !important;
    color: #f5f2eb !important;
    margin: 0 0 12px 0 !important;
    letter-spacing: -1px;
    line-height: 1.1;
}
.hero p { color: rgba(245,242,235,0.55) !important; font-size: 0.92rem; margin: 0; line-height: 1.7; max-width: 600px; }

/* ---- DISCLAIMER ---- */
.disclaimer {
    background: #fffbf0;
    border: 1px solid #e8d080;
    border-left: 3px solid #b89020;
    border-radius: 0 12px 12px 0;
    padding: 16px 20px;
    margin-bottom: 22px;
    font-size: 0.84rem;
    color: #3a3010;
    line-height: 1.7;
}
.disclaimer-title {
    font-family: 'DM Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #b89020;
    margin-bottom: 6px;
}

/* ---- PROGRESS ---- */
.progress-bar-outer { background: rgba(28,31,23,0.1); border-radius: 99px; height: 5px; margin: 20px 0 8px; overflow: hidden; }
.progress-bar-inner { height: 5px; border-radius: 99px; background: linear-gradient(90deg, #4a6a2a, #7a9a5a); }
.step-counter { font-family: 'DM Mono', monospace; font-size: 0.68rem; letter-spacing: 1px; color: #5a5a4a; margin-bottom: 24px; }

/* ---- PILLAR CARD ---- */
.pillar-card {
    background: #1c1f17;
    border-radius: 16px;
    padding: 28px 28px 22px;
    margin-bottom: 24px;
}
.pillar-card-title { font-family: 'Playfair Display', serif; font-size: 1.2rem; font-weight: 700; color: #f5f2eb !important; margin-bottom: 6px; }
.pillar-card-desc { font-size: 0.84rem; color: rgba(245,242,235,0.5) !important; line-height: 1.6; margin-bottom: 14px; }

/* ---- FW TAGS ---- */
.fw-tag {
    display: inline-block;
    font-family: 'DM Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 3px 9px;
    border-radius: 4px;
    margin: 2px 3px 2px 0;
    background: rgba(122,154,90,0.15);
    color: #8ab86a;
    border: 1px solid rgba(122,154,90,0.25);
}

/* ---- QUESTION CARD ---- */
.q-card {
    background: white;
    border: 1.5px solid #e0ddd4;
    border-radius: 12px;
    padding: 18px 20px 14px;
    margin-bottom: 10px;
    transition: border-color 0.2s, box-shadow 0.2s;
}
.q-card:hover {
    border-color: #7a9a5a;
    box-shadow: 0 2px 16px rgba(122,154,90,0.08);
}
.q-mat {
    font-family: 'DM Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 3px 9px;
    border-radius: 3px;
    display: inline-block;
    margin-bottom: 8px;
    font-weight: 500;
}
.mat-high   { background: #fce8e0; color: #8a3010; border: 1px solid #e8b0a0; }
.mat-medium { background: #fdf4d0; color: #6a5010; border: 1px solid #e0cc80; }
.mat-low    { background: #eaf4e0; color: #2a5010; border: 1px solid #a8d080; }
.q-text {
    font-size: 0.92rem;
    color: #1c1f17;
    line-height: 1.55;
    font-weight: 500;
    margin-bottom: 10px;
}
.q-explain {
    font-size: 0.81rem;
    color: #5a5a3a;
    line-height: 1.7;
    background: #f8f6f0;
    border-radius: 8px;
    padding: 10px 14px;
    margin-bottom: 10px;
    border-left: 2px solid #b8c8a0;
}
.q-explain-title {
    font-family: 'DM Mono', monospace;
    font-size: 0.58rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #4a6a2a;
    margin-bottom: 4px;
}

/* ---- RADIO — DARK VISIBLE OPTIONS ---- */
.stRadio > div { gap: 8px !important; flex-wrap: wrap !important; }
.stRadio label {
    background: #f0ede4 !important;
    border: 1.5px solid #d0cdc4 !important;
    border-radius: 8px !important;
    padding: 9px 16px !important;
    font-size: 0.84rem !important;
    color: #1c1f17 !important;
    cursor: pointer !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 500 !important;
    transition: all 0.15s !important;
}
.stRadio label:hover {
    background: #e0f0d0 !important;
    border-color: #7a9a5a !important;
    color: #1c3a10 !important;
}
/* selected state */
.stRadio label[data-checked="true"],
.stRadio label:has(input:checked) {
    background: #1c1f17 !important;
    border-color: #1c1f17 !important;
    color: #f5f2eb !important;
}

/* ---- BUTTONS ---- */
.stButton > button {
    background: white !important;
    color: #1c1f17 !important;
    border: 1.5px solid #c0bdb4 !important;
    border-radius: 8px !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.5px !important;
    padding: 10px 22px !important;
    transition: all 0.15s !important;
}
.stButton > button:hover {
    background: #1c1f17 !important;
    color: #f5f2eb !important;
    border-color: #1c1f17 !important;
}

/* ---- SCORE CARD ---- */
.score-card {
    background: #1c1f17;
    border-radius: 18px;
    padding: 34px 28px;
    text-align: center;
}
.score-num { font-family: 'Playfair Display', serif; font-size: 5rem; font-weight: 900; line-height: 1; margin: 10px 0 6px; }
.score-lbl { font-family: 'DM Mono', monospace; font-size: 0.62rem; letter-spacing: 2px; text-transform: uppercase; color: rgba(245,242,235,0.4); margin-bottom: 6px; }

/* ---- FINDINGS ---- */
.finding {
    border-left: 3px solid;
    padding: 14px 18px;
    margin-bottom: 8px;
    background: white;
    border-radius: 0 10px 10px 0;
    border-top: 1px solid #e8e4dc;
    border-right: 1px solid #e8e4dc;
    border-bottom: 1px solid #e8e4dc;
}
.finding-lbl { font-family: 'DM Mono', monospace; font-size: 0.6rem; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 5px; }
.finding-text { font-size: 0.87rem; color: #1c1f17; line-height: 1.55; font-weight: 500; }
.finding-explain { font-size: 0.79rem; color: #5a5a3a; line-height: 1.65; margin-top: 8px; padding-top: 8px; border-top: 1px solid #f0ede4; }

/* ---- RECS ---- */
.rec {
    background: white;
    border: 1.5px solid #e0ddd4;
    border-radius: 10px;
    padding: 18px 22px;
    margin-bottom: 10px;
    font-size: 0.88rem;
    color: #2a2a1a;
    line-height: 1.7;
}
.rec-n { font-family: 'Playfair Display', serif; font-size: 1.8rem; font-weight: 900; color: rgba(28,31,23,0.1); float: left; margin-right: 14px; line-height: 1; }
.rec-pillar { font-family: 'DM Mono', monospace; font-size: 0.6rem; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 5px; display: block; }

/* ---- FEATURE CARDS ---- */
.feature-card {
    background: white;
    border: 1.5px solid #e0ddd4;
    border-radius: 14px;
    padding: 22px 20px;
    transition: border-color 0.2s, transform 0.2s;
}
.feature-card:hover { border-color: #7a9a5a; transform: translateY(-2px); }
.feature-title { font-family: 'Playfair Display', serif; font-size: 1rem; font-weight: 700; color: #1c1f17; margin-bottom: 6px; }
.feature-desc { font-size: 0.79rem; color: #5a5a3a; line-height: 1.6; }

/* ---- SCORE TABLE ---- */
.score-table { width: 100%; border-collapse: collapse; font-size: 0.82rem; }
.score-table th { font-family: 'DM Mono', monospace; font-size: 0.6rem; letter-spacing: 1.5px; text-transform: uppercase; color: #4a6a2a; padding: 8px 12px; border-bottom: 1.5px solid #e0ddd4; text-align: left; }
.score-table td { padding: 8px 12px; border-bottom: 1px solid #f0ede4; color: #2a2a1a; vertical-align: top; }
.score-table tr:last-child td { border-bottom: none; }

/* ---- MISC ---- */
.stTextInput input { background: white !important; border: 1.5px solid #d0cdc4 !important; color: #1c1f17 !important; border-radius: 8px !important; }
.stDownloadButton button { background: #1c1f17 !important; color: #f5f2eb !important; border: none !important; border-radius: 8px !important; font-family: 'DM Mono', monospace !important; font-size: 0.75rem !important; }
.stDownloadButton button:hover { background: #3a4a2a !important; }
hr { border-color: #e0ddd4 !important; }
.streamlit-expanderHeader { background: white !important; color: #1c1f17 !important; border: 1.5px solid #e0ddd4 !important; border-radius: 10px !important; font-family: 'DM Sans', sans-serif !important; font-weight: 600 !important; }
.streamlit-expanderContent { background: #faf8f2 !important; border: 1.5px solid #e0ddd4 !important; border-top: none !important; border-radius: 0 0 10px 10px !important; }
[data-testid="stTabs"] button { color: #3a3a2a !important; font-family: 'DM Mono', monospace !important; font-size: 0.75rem !important; }
[data-testid="stTabs"] button[aria-selected="true"] { color: #1c1f17 !important; border-bottom-color: #4a6a2a !important; }
</style>
""", unsafe_allow_html=True)


# ============================================================
# FRAMEWORK DATA
# ============================================================
PILLARS = {
    "Environmental": {
        "icon": "◉", "color": "#4a6a2a", "accent": "#7a9a5a",
        "weight": 0.35,
        "description": "Climate risk, emissions management, resource use, and environmental compliance — aligned to TCFD and GRI 300 series.",
        "frameworks": ["TCFD", "GRI 300", "SASB", "UN SDG 13"],
        "questions": [
            (
                "Does the company disclose Scope 1, 2, and 3 greenhouse gas emissions?",
                "high",
                "Scope 1 covers direct emissions from owned operations. Scope 2 covers purchased energy. Scope 3 covers the entire value chain — suppliers, product use, and disposal. Full disclosure of all three is now expected under TCFD and the EU's CSRD. Without Scope 3, a company's climate picture is incomplete — for most industries, Scope 3 is over 70% of total emissions."
            ),
            (
                "Has the company set science-based emissions reduction targets (SBTi or equivalent)?",
                "high",
                "Science-based targets (SBTs) are emissions reduction goals aligned with what climate science says is needed to limit global warming to 1.5°C. The Science Based Targets initiative (SBTi) independently validates these. A company without approved targets may be making vague climate commitments that don't hold up to scrutiny — increasingly called 'greenwashing' by regulators and investors."
            ),
            (
                "Is there a formal climate risk assessment aligned to TCFD recommendations?",
                "high",
                "TCFD (Task Force on Climate-related Financial Disclosures) asks companies to assess both physical risks (floods, droughts) and transition risks (policy changes, technology shifts) from climate change. A formal assessment means the board and investors can see how climate change may affect the company's financial position. Increasingly mandatory in major markets."
            ),
            (
                "Does the company report on water usage and reduction targets?",
                "medium",
                "Water risk is sector-specific but growing in materiality — especially in agriculture, manufacturing, and tech (data centre cooling). Companies in water-stressed regions face operational and regulatory risk. Disclosure of usage volumes and targets signals proactive risk management."
            ),
            (
                "Are supply chain environmental risks assessed and disclosed?",
                "medium",
                "Many companies' largest environmental impacts sit outside their direct operations — in suppliers' factories, farms, or logistics networks. Assessing and disclosing these risks shows maturity in ESG governance and is increasingly required under mandatory due diligence laws like Germany's Supply Chain Act and the EU CSRD."
            ),
            (
                "Does the company have a credible net-zero or carbon neutrality pathway?",
                "high",
                "A credible pathway includes interim targets, clear methodology, and third-party verification. 'Net-zero by 2050' without interim milestones or offset transparency is widely considered insufficient. Investors and regulators are increasingly scrutinising whether net-zero claims are backed by real operational changes or just carbon offsets."
            ),
            (
                "Is biodiversity and land-use impact assessed and reported?",
                "low",
                "Biodiversity is emerging as the next major ESG disclosure frontier, driven by the Taskforce on Nature-related Financial Disclosures (TNFD) and COP15 biodiversity frameworks. Companies in sectors like agriculture, mining, and real estate face the highest exposure. While not yet widely mandatory, early disclosure signals forward-thinking governance."
            ),
        ]
    },
    "Social": {
        "icon": "◎", "color": "#2a5a7a", "accent": "#5a9ab8",
        "weight": 0.30,
        "description": "Workforce equity, labour practices, community impact, and human rights — aligned to GRI 400 series and ILO core conventions.",
        "frameworks": ["GRI 400", "UN SDG 8", "UN SDG 10", "ILO Core"],
        "questions": [
            (
                "Does the company publish pay equity and gender diversity data by seniority level?",
                "high",
                "Pay equity disclosure shows whether a company pays people equally for equal work regardless of gender, race, or other characteristics. Publishing data by seniority level is important — companies sometimes show overall pay parity while masking gaps at senior levels. The EU Pay Transparency Directive now mandates this for large companies. Investors use this to assess culture, retention, and litigation risk."
            ),
            (
                "Are human rights due diligence processes applied to the supply chain?",
                "high",
                "Human rights due diligence means actively identifying, preventing, and addressing risks like forced labour, child labour, and unsafe conditions — not just in direct operations but across the supply chain. The UN Guiding Principles on Business and Human Rights set the standard. Mandatory in France (Loi de Vigilance), Germany, and increasingly under CSRD."
            ),
            (
                "Does the company have a formal health, safety, and wellbeing policy with disclosed metrics?",
                "medium",
                "Beyond legal compliance, strong H&S disclosure — injury rates, lost-time incidents, wellbeing programmes — signals a culture of care and operational discipline. Companies with poor safety records face regulatory fines, reputational damage, and lower productivity. Investors treat this as a proxy for management quality."
            ),
            (
                "Is there a mechanism for employee grievance reporting with non-retaliation protection?",
                "medium",
                "Grievance mechanisms allow employees to report concerns — including ethics violations, discrimination, or safety issues — without fear of retaliation. This is a baseline expectation under the UN Guiding Principles and GRI 402. The absence of one is a governance red flag, particularly in sectors with labour-intensive operations."
            ),
            (
                "Does the company disclose community investment and local impact initiatives?",
                "low",
                "Community investment disclosure — social programmes, local hiring, economic contributions — reflects how a company manages its social licence to operate. For extractive, infrastructure, or consumer-facing companies, community relations directly affect operating permissions and brand trust."
            ),
            (
                "Are supplier labour standards assessed and enforced through audits?",
                "high",
                "Supplier audits verify that labour standards — living wages, working hours, no forced labour — are actually upheld, not just written in contracts. Without third-party audits, supplier commitments are unverifiable. High-profile supply chain scandals (Rana Plaza, fast fashion exposés) have made this a major reputational and regulatory risk."
            ),
        ]
    },
    "Governance": {
        "icon": "◈", "color": "#5a3a2a", "accent": "#a87a5a",
        "weight": 0.35,
        "description": "Board accountability, executive incentives, anti-corruption controls, and ESG integration into strategy — aligned to GRI 200 and OECD Corporate Governance Principles.",
        "frameworks": ["GRI 200", "SASB", "OECD Corp. Gov.", "TCFD Governance"],
        "questions": [
            (
                "Is there board-level oversight of ESG risks and opportunities, with named responsibility?",
                "high",
                "TCFD and most major ESG frameworks require that ESG be a board-level responsibility — not just a CSR team function. Named responsibility means one director or a committee is accountable. Without this, ESG commitments lack teeth. Investors increasingly vote against boards that cannot demonstrate ESG accountability at the governance level."
            ),
            (
                "Does executive compensation include ESG performance metrics?",
                "high",
                "Linking executive pay to ESG targets (emissions reductions, diversity, safety) signals that ESG goals are treated as serious business objectives, not just PR. Without this link, there is little financial incentive for leadership to prioritise ESG over short-term profit. Proxy advisors ISS and Glass Lewis now flag the absence of ESG pay metrics as a governance concern."
            ),
            (
                "Are anti-corruption and anti-bribery policies in place with disclosed breach data?",
                "high",
                "Anti-corruption policies aligned to the UK Bribery Act, US FCPA, or equivalent are governance table stakes. But disclosure of actual breach data — investigations, violations, fines — is the real test. Companies that only disclose the policy without breach data may be obscuring problems. Transparent reporting here is a strong positive signal."
            ),
            (
                "Is the board composition disclosed with diversity across gender, background, and expertise?",
                "medium",
                "Board diversity is linked to better decision-making, reduced groupthink, and stronger financial performance in research. Disclosure of gender, independence, tenure, and skills matrix allows investors and stakeholders to assess whether the board has the right capabilities — including climate, digital, and ESG expertise."
            ),
            (
                "Does the company conduct or commission third-party ESG assurance or verification?",
                "high",
                "Third-party assurance means an independent auditor has verified ESG data — similar to financial auditing. Without it, ESG disclosures are self-reported and unverifiable. Assurance is becoming mandatory under CSRD for large companies, and investors give significantly more credibility to assured data. It also signals confidence in disclosure quality."
            ),
            (
                "Are lobbying activities and political donations disclosed?",
                "medium",
                "Lobbying disclosure reveals whether a company's public ESG commitments are consistent with its political influence activities. A company that publicly supports climate action while lobbying against climate regulation has a credibility problem. Investors increasingly assess lobbying alignment as part of governance quality."
            ),
            (
                "Is there a formal stakeholder engagement process for material ESG issues?",
                "medium",
                "A formal stakeholder engagement process — surveying employees, communities, investors, and NGOs on what ESG issues matter most — underpins credible materiality assessments. GRI and SASB require this as the basis for deciding what to disclose. Ad hoc engagement is not sufficient; documented, structured processes are the expectation."
            ),
        ]
    }
}

RESPONSE_OPTS = ["Yes — fully disclosed", "Partially — in progress", "No — not addressed", "Not applicable"]
RISK_LEVELS   = {"Yes — fully disclosed": 1.0, "Partially — in progress": 0.5,
                 "No — not addressed": 0.0, "Not applicable": None}

SECTOR_MATERIALITY = {
    "Financial Services":    {"Environmental": 0.25, "Social": 0.30, "Governance": 0.45},
    "Energy & Utilities":    {"Environmental": 0.50, "Social": 0.25, "Governance": 0.25},
    "Technology":            {"Environmental": 0.25, "Social": 0.35, "Governance": 0.40},
    "Healthcare":            {"Environmental": 0.20, "Social": 0.45, "Governance": 0.35},
    "Manufacturing":         {"Environmental": 0.45, "Social": 0.30, "Governance": 0.25},
    "Consumer Goods/Retail": {"Environmental": 0.35, "Social": 0.35, "Governance": 0.30},
    "Real Estate":           {"Environmental": 0.40, "Social": 0.25, "Governance": 0.35},
    "Telecommunications":    {"Environmental": 0.25, "Social": 0.35, "Governance": 0.40},
    "Other":                 {"Environmental": 0.35, "Social": 0.30, "Governance": 0.35},
}

STEPS = ["Welcome", "Environmental", "Social", "Governance", "Results"]

REC_MAP = {
    "Environmental": "Prioritise TCFD-aligned climate risk disclosure and set interim emissions targets. Scope 3 supply chain emissions and biodiversity exposure are increasingly material to institutional investors and regulatory bodies.",
    "Social": "Develop a human rights due diligence framework for supply chain operations. Pay equity disclosure and grievance mechanisms are now baseline expectations under GRI 400 and emerging mandatory reporting regimes (e.g. CSRD).",
    "Governance": "Ensure board-level ESG accountability is named and documented — not just implied. Third-party ESG assurance is rapidly becoming a differentiator in capital markets and is a prerequisite for many investor ESG mandates.",
}

MATERIAL_RISKS = {
    "Financial Services":    ["Physical climate risk in loan portfolios", "Social washing / DEI disclosure gaps", "Governance failures in ESG-linked products"],
    "Energy & Utilities":    ["Stranded asset risk from energy transition", "Community impact of operations", "Board accountability for climate strategy"],
    "Technology":            ["Scope 3 emissions from hardware and cloud", "Labour practices in supply chain", "Executive pay alignment and data governance"],
    "Healthcare":            ["Supply chain human rights", "Access and affordability equity", "Board diversity and conflict of interest"],
    "Manufacturing":         ["Carbon intensity and transition risk", "Supplier labour audits", "Anti-corruption in procurement"],
    "Consumer Goods/Retail": ["Packaging and waste targets", "Living wage in supply chain", "Greenwashing and disclosure quality"],
    "Real Estate":           ["Building energy efficiency and GRESB alignment", "Community displacement and social impact", "Governance of ESG-linked debt"],
    "Telecommunications":    ["Energy use of network infrastructure", "Digital inclusion and access equity", "Lobbying disclosure and executive accountability"],
    "Other":                 ["Emissions reporting completeness", "Stakeholder engagement quality", "Board ESG oversight"],
}


# ============================================================
# SESSION STATE
# ============================================================
for k, v in [("step", 0), ("responses", {}), ("meta", {}), ("show_explain", {})]:
    if k not in st.session_state:
        st.session_state[k] = v


# ============================================================
# HELPERS
# ============================================================
def pillar_score(pillar):
    resp   = st.session_state.responses.get(pillar, {})
    scored = [RISK_LEVELS[v] for v in resp.values() if RISK_LEVELS.get(v) is not None]
    return (sum(scored) / len(scored) * 100) if scored else 0

def overall_score():
    sector  = st.session_state.meta.get("sector", "Other")
    weights = SECTOR_MATERIALITY.get(sector, SECTOR_MATERIALITY["Other"])
    scores  = {p: pillar_score(p) for p in PILLARS}
    total_w = sum(weights[p] for p in scores)
    return sum(scores[p] * weights[p] for p in scores) / total_w if total_w else 0

def rating(score):
    if score >= 80: return "Leading",    "#2a5a1a"
    if score >= 60: return "Developing", "#4a6a2a"
    if score >= 40: return "Lagging",    "#8a6010"
    return           "At Risk",          "#8a2010"

def sev_color(sev):
    return {"high": "#8a2010", "medium": "#8a6010", "low": "#2a5a1a"}.get(sev, "#555")

def get_findings():
    findings  = []
    downgrade = {"high": "medium", "medium": "low", "low": "low"}
    order     = {"high": 0, "medium": 1, "low": 2}
    for pillar, pd in PILLARS.items():
        resp = st.session_state.responses.get(pillar, {})
        for i, (q, wt, explain) in enumerate(pd["questions"]):
            r = resp.get(f"{pillar}_{i}", "Not applicable")
            if r == "No — not addressed":
                findings.append({"pillar": pillar, "q": q, "sev": wt,
                                  "status": "Gap", "explain": explain})
            elif r == "Partially — in progress":
                findings.append({"pillar": pillar, "q": q, "sev": downgrade[wt],
                                  "status": "Partial", "explain": explain})
    findings.sort(key=lambda x: order[x["sev"]])
    return findings

def radar_chart(scores, sector):
    pillars = list(scores.keys())
    vals    = [scores[p] for p in pillars]
    fig = go.Figure(go.Scatterpolar(
        r=vals + [vals[0]], theta=pillars + [pillars[0]],
        fill='toself', fillcolor='rgba(74,106,42,0.12)',
        line=dict(color='#4a6a2a', width=2.5),
    ))
    fig.update_layout(
        polar=dict(
            bgcolor='rgba(0,0,0,0)',
            radialaxis=dict(visible=True, range=[0,100],
                tickfont=dict(size=9, family='DM Mono', color='rgba(28,31,23,0.4)'),
                gridcolor='rgba(28,31,23,0.1)', linecolor='rgba(28,31,23,0.1)'),
            angularaxis=dict(
                tickfont=dict(size=11, family='Playfair Display', color='#1c1f17'),
                gridcolor='rgba(28,31,23,0.1)', linecolor='rgba(28,31,23,0.1)')
        ),
        paper_bgcolor='rgba(0,0,0,0)', showlegend=False,
        margin=dict(l=40,r=40,t=40,b=40), height=300
    )
    return fig

def bar_chart(scores):
    pillars = list(scores.keys())
    vals    = [scores[p] for p in pillars]
    colors  = ["#2a5a1a" if v>=80 else "#4a6a2a" if v>=60 else "#8a6010" if v>=40 else "#8a2010" for v in vals]
    fig = go.Figure(go.Bar(
        x=pillars, y=vals, marker_color=colors, marker_line_width=0,
        text=[f"{v:.0f}" for v in vals], textposition='outside',
        textfont=dict(family='DM Mono', size=12, color='#2a2a1a')
    ))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(range=[0,118], showgrid=True, gridcolor='rgba(28,31,23,0.07)',
                   tickfont=dict(family='DM Mono', size=9, color='rgba(28,31,23,0.4)')),
        xaxis=dict(tickfont=dict(family='Playfair Display', size=12, color='#1c1f17')),
        margin=dict(l=10,r=10,t=20,b=10), height=270, showlegend=False
    )
    return fig

def build_report():
    sc   = overall_score()
    rat  = rating(sc)[0]
    fnd  = get_findings()
    p_sc = {p: pillar_score(p) for p in PILLARS}
    meta = st.session_state.meta
    sector = meta.get("sector","—")
    short  = {"Yes — fully disclosed":"YES","Partially — in progress":"PARTIAL",
              "No — not addressed":"NO","Not applicable":"N/A"}
    lines  = [
        "="*68, "ESG CORPORATE RISK SCORECARD", "="*68,
        f"Company       : {meta.get('company','—')}",
        f"Sector        : {sector}",
        f"Assessment    : {meta.get('assessment_type','—')}",
        f"Assessed by   : {meta.get('assessor','—')}",
        f"Date          : {datetime.today().strftime('%B %d, %Y')}",
        f"Framework     : GRI Standards · TCFD · SASB · UN SDGs · OECD Corp. Gov.",
        "",
        "DISCLAIMER", "-"*68,
        "Educational reference tool only. Not a formal ESG rating, investment",
        "recommendation, or regulatory compliance determination.",
        "",
        "-"*68, "METHODOLOGY", "-"*68,
        "Yes=1.0 | Partial=0.5 | No=0.0 | N/A=excluded from average",
        f"Overall = sector-adjusted weighted average (sector: {sector})",
        "Weights reflect SASB materiality by sector.",
        "80-100 Leading · 60-79 Developing · 40-59 Lagging · <40 At Risk",
        "",
        "-"*68, "OVERALL SCORE", "-"*68,
        f"  {sc:.1f} / 100   —   {rat}", "",
        "-"*68, "PILLAR SCORES", "-"*68,
    ]
    weights = SECTOR_MATERIALITY.get(sector, SECTOR_MATERIALITY["Other"])
    for p, s in p_sc.items():
        lines.append(f"  {p:<20} {s:>5.1f}   {rating(s)[0]:<12}  weight: {weights[p]*100:.0f}%")
    risks = MATERIAL_RISKS.get(sector, [])
    if risks:
        lines += ["", "-"*68, f"SECTOR MATERIAL RISKS ({sector})", "-"*68]
        for r in risks: lines.append(f"  · {r}")
    lines += ["", "-"*68, "RESPONSE LOG", "-"*68]
    for pillar, pd in PILLARS.items():
        lines.append(f"\n  {pillar}")
        resp = st.session_state.responses.get(pillar, {})
        for i, (q, wt, _) in enumerate(pd["questions"]):
            r = resp.get(f"{pillar}_{i}", "Not applicable")
            lines.append(f"    [{short.get(r,'?')}] [{wt.upper()}] {q}")
    if fnd:
        lines += ["", "-"*68, f"FINDINGS ({len(fnd)})", "-"*68]
        for i, f in enumerate(fnd, 1):
            lines += [f"  [{f['sev'].upper()}] {f['pillar']} — {f['status']}",
                      f"  {i}. {f['q']}", ""]
    shown = set()
    recs  = []
    for f in fnd:
        if f["sev"] == "high" and f["pillar"] not in shown:
            shown.add(f["pillar"])
            recs.append(REC_MAP[f["pillar"]])
    if recs:
        lines += ["-"*68, "RECOMMENDATIONS", "-"*68]
        for i, r in enumerate(recs, 1):
            lines += [f"  {i}. {r}", ""]
    lines += ["="*68, "END OF REPORT", "="*68]
    return "\n".join(lines)


# ============================================================
# SIDEBAR — UNTOUCHED
# ============================================================
with st.sidebar:
    st.markdown('<span class="slabel" style="color:#7a9a5a;">Company Details</span>', unsafe_allow_html=True)
    st.session_state.meta["company"]         = st.text_input("Company Name", value=st.session_state.meta.get("company",""), placeholder="e.g. Rogers Communications")
    st.session_state.meta["sector"]          = st.selectbox("Sector", list(SECTOR_MATERIALITY.keys()))
    st.session_state.meta["assessment_type"] = st.selectbox("Assessment Type", ["Self-assessment","Third-party review","Investor due diligence","Academic / research"])
    st.session_state.meta["assessor"]        = st.text_input("Assessor", value=st.session_state.meta.get("assessor",""), placeholder="Your name")

    st.markdown("---")
    sector  = st.session_state.meta.get("sector","Other")
    weights = SECTOR_MATERIALITY.get(sector, SECTOR_MATERIALITY["Other"])
    st.markdown(f'<span class="slabel" style="color:#7a9a5a;">Sector Weights — {sector}</span>', unsafe_allow_html=True)
    for p, w in weights.items():
        bw = int(w * 100)
        st.markdown(f"""
        <div style="margin-bottom:8px;">
            <div style="display:flex;justify-content:space-between;margin-bottom:3px;">
                <span style="font-family:'DM Mono',monospace;font-size:0.65rem;color:#c8c4b0;letter-spacing:1px;">{p}</span>
                <span style="font-family:'DM Mono',monospace;font-size:0.65rem;color:#7a9a5a;">{bw}%</span>
            </div>
            <div style="background:rgba(255,255,255,0.06);border-radius:99px;height:3px;">
                <div style="width:{bw}%;height:3px;border-radius:99px;background:#7a9a5a;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('<p style="font-family:\'DM Mono\',monospace;font-size:0.6rem;color:rgba(200,196,176,0.35);margin-top:6px;line-height:1.6;">Weights adjust automatically per SASB materiality.</p>', unsafe_allow_html=True)

    st.markdown("---")
    cur = st.session_state.step
    pct = int((cur / (len(STEPS) - 1)) * 100)
    st.markdown(f'<span class="slabel" style="color:#7a9a5a;">Progress — {pct}%</span>', unsafe_allow_html=True)
    st.markdown(f'<div class="progress-bar-outer"><div class="progress-bar-inner" style="width:{pct}%;"></div></div>', unsafe_allow_html=True)
    for i, s in enumerate(STEPS):
        c      = "#7a9a5a" if i == cur else ("#b8d48a" if i < cur else "rgba(200,196,176,0.25)")
        prefix = "▶ " if i == cur else ("✓ " if i < cur else "○ ")
        st.markdown(f'<p style="font-family:\'DM Mono\',monospace;font-size:0.65rem;color:{c};letter-spacing:1px;margin:3px 0;">{prefix}{s}</p>', unsafe_allow_html=True)


# ============================================================
# STEP 0 — WELCOME
# ============================================================
step = st.session_state.step

if step == 0:
    st.markdown("""
    <div class="hero">
        <div class="hero-tag">◈ ESG · Corporate Risk Assessment</div>
        <h1>ESG Corporate<br>Risk Scorecard</h1>
        <p>Evaluate a company's Environmental, Social, and Governance performance against structured criteria drawn from GRI Standards, TCFD, SASB, and UN SDGs. Scores adjust by sector automatically.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="disclaimer">
        <div class="disclaimer-title">⚠ Reference Tool — Not a Formal ESG Rating</div>
        This scorecard is an <b>educational reference tool</b>. It is not a formal ESG rating, investment recommendation, or regulatory compliance determination. Scores are based on self-reported inputs only.<br><br>
        For real investment, procurement, or governance decisions, engage a qualified ESG analyst and verify using primary sources (CDP disclosures, company sustainability reports, MSCI ESG, Sustainalytics).
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    for col, icon, title, desc, col_c in [
        (c1, "◉", "3 ESG Pillars",           "Environmental, Social, Governance — each with sector-adjusted weighting", "#4a6a2a"),
        (c2, "◎", "20 Criteria with Context", "Each question includes a plain-language explanation of why it matters", "#2a5a7a"),
        (c3, "◈", "Sector-Adjusted Scoring",  "Weights shift per SASB materiality — Financial Services ≠ Energy", "#5a3a2a"),
    ]:
        col.markdown(f"""
        <div class="feature-card">
            <div style="font-size:1.3rem;color:{col_c};margin-bottom:10px;">{icon}</div>
            <div class="feature-title">{title}</div>
            <div class="feature-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    with st.expander("How scoring works — methodology & weights"):
        st.markdown("""
        <table class="score-table">
            <tr><th>Response</th><th>Value</th><th>What it means</th></tr>
            <tr><td><b>Yes — fully disclosed</b></td><td style="color:#2a5a1a;font-family:'DM Mono',monospace;font-weight:600;">1.0</td><td>Formally reported in sustainability report, CDP, or annual filing</td></tr>
            <tr><td><b>Partially — in progress</b></td><td style="color:#8a6010;font-family:'DM Mono',monospace;font-weight:600;">0.5</td><td>Disclosed partially, target set but not met, or in development</td></tr>
            <tr><td><b>No — not addressed</b></td><td style="color:#8a2010;font-family:'DM Mono',monospace;font-weight:600;">0.0</td><td>No disclosure or evidence of action</td></tr>
            <tr><td><b>Not applicable</b></td><td style="color:#888;font-family:'DM Mono',monospace;">excl.</td><td>Genuinely irrelevant — excluded from average</td></tr>
        </table>
        <p style="font-size:0.83rem;color:#3a3a2a;margin-top:16px;line-height:1.8;">
        <b>Pillar score</b> = average of scored responses × 100<br>
        <b>Overall score</b> = sector-weighted average using SASB materiality weights<br>
        <b>Ratings:</b> 80–100 Leading · 60–79 Developing · 40–59 Lagging · Below 40 At Risk
        </p>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background:white;border:1.5px solid #e0ddd4;border-radius:14px;padding:22px 24px;font-size:0.88rem;color:#2a2a1a;line-height:1.9;">
    Enter company details in the left sidebar, then work through each pillar one at a time.<br>
    Each question includes a <b>plain-language explanation</b> of why it matters — click the info toggle to read it.<br><br>
    Select the response that best reflects the company's <i>current disclosed position</i>:<br>
    &nbsp;&nbsp;<b style="color:#2a5a1a;">Yes — fully disclosed</b> &nbsp;· Formally reported and verifiable<br>
    &nbsp;&nbsp;<b style="color:#8a6010;">Partially — in progress</b> &nbsp;· Partial disclosure or work underway<br>
    &nbsp;&nbsp;<b style="color:#8a2010;">No — not addressed</b> &nbsp;· No disclosure or evidence<br>
    &nbsp;&nbsp;<b style="color:#888;">Not applicable</b> &nbsp;· Genuinely irrelevant to this company
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    _, cb, _ = st.columns([2,1,2])
    with cb:
        if st.button("Begin Assessment →", use_container_width=True):
            st.session_state.step = 1
            st.rerun()


# ============================================================
# STEPS 1–3 — PILLAR QUESTIONS
# ============================================================
elif 1 <= step <= 3:
    pillar_list = list(PILLARS.keys())
    pillar      = pillar_list[step - 1]
    pd_data     = PILLARS[pillar]
    pct         = int((step / (len(STEPS) - 1)) * 100)

    st.markdown(f"""
    <div class="progress-bar-outer"><div class="progress-bar-inner" style="width:{pct}%;"></div></div>
    <div class="step-counter">Pillar {step} of 3 &nbsp;·&nbsp; {pillar}</div>
    """, unsafe_allow_html=True)

    fw_tags = "".join(f'<span class="fw-tag">{f}</span>' for f in pd_data["frameworks"])
    st.markdown(f"""
    <div class="pillar-card">
        <div style="font-family:'DM Mono',monospace;font-size:0.65rem;letter-spacing:2px;text-transform:uppercase;color:{pd_data['accent']};margin-bottom:8px;">{pd_data['icon']} &nbsp; Pillar {step} of 3</div>
        <div class="pillar-card-title">{pillar}</div>
        <div class="pillar-card-desc">{pd_data['description']}</div>
        <div>{fw_tags}</div>
    </div>
    """, unsafe_allow_html=True)

    if pillar not in st.session_state.responses:
        st.session_state.responses[pillar] = {}

    for i, (q, wt, explain) in enumerate(pd_data["questions"]):
        key     = f"{pillar}_{i}"
        cur_val = st.session_state.responses[pillar].get(key, "Not applicable")
        idx     = RESPONSE_OPTS.index(cur_val) if cur_val in RESPONSE_OPTS else 3

        st.markdown(f"""
        <div class="q-card">
            <div class="q-mat mat-{wt}">{wt} materiality</div>
            <div class="q-text">{q}</div>
            <div class="q-explain">
                <div class="q-explain-title">Why this matters</div>
                {explain}
            </div>
        </div>
        """, unsafe_allow_html=True)

        resp = st.radio("", RESPONSE_OPTS, index=idx, horizontal=True,
                        key=f"radio_{key}", label_visibility="collapsed")
        st.session_state.responses[pillar][key] = resp
        st.markdown("<div style='margin-bottom:12px;'></div>", unsafe_allow_html=True)

    sc      = pillar_score(pillar)
    rat, col = rating(sc)
    st.markdown(f"""
    <div style="background:white;border:1.5px solid #e0ddd4;border-radius:12px;
                padding:16px 22px;margin-top:20px;display:flex;align-items:center;gap:18px;">
        <div style="font-family:'Playfair Display',serif;font-size:2.2rem;font-weight:900;color:{col};">{sc:.0f}</div>
        <div>
            <div style="font-family:'DM Mono',monospace;font-size:0.6rem;letter-spacing:2px;text-transform:uppercase;color:#8a8a6a;">Pillar Score So Far</div>
            <div style="font-family:'DM Mono',monospace;font-size:0.75rem;color:{col};font-weight:500;">{rat}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    nl, _, nr = st.columns([1,2,1])
    with nl:
        if st.button("← Back", use_container_width=True):
            st.session_state.step -= 1
            st.rerun()
    with nr:
        label = "View Results →" if step == 3 else "Next Pillar →"
        if st.button(label, use_container_width=True):
            st.session_state.step += 1
            st.rerun()


# ============================================================
# STEP 4 — RESULTS
# ============================================================
elif step == 4:
    sc       = overall_score()
    rat, col = rating(sc)
    p_scores = {p: pillar_score(p) for p in PILLARS}
    findings = get_findings()
    sector   = st.session_state.meta.get("sector","Other")
    high_cnt = sum(1 for f in findings if f["sev"]=="high")
    med_cnt  = sum(1 for f in findings if f["sev"]=="medium")
    low_cnt  = sum(1 for f in findings if f["sev"]=="low")

    st.markdown('<span class="slabel">Results</span>', unsafe_allow_html=True)
    st.markdown("## ESG Risk Scorecard Results")
    st.markdown("<br>", unsafe_allow_html=True)

    cs, cr, cb2 = st.columns([1,1.3,1.3])
    with cs:
        st.markdown(f"""
        <div class="score-card">
            <div class="score-lbl">Overall ESG Score</div>
            <div class="score-num" style="color:{col};">{sc:.0f}</div>
            <div style="font-family:'DM Mono',monospace;font-size:0.7rem;letter-spacing:1.5px;text-transform:uppercase;color:{col};margin-bottom:22px;">{rat}</div>
            <div style="font-family:'DM Mono',monospace;font-size:0.58rem;letter-spacing:2px;color:rgba(245,242,235,0.35);text-transform:uppercase;margin-bottom:10px;">Disclosure Gaps</div>
            <div style="font-size:0.83rem;line-height:2.2;text-align:left;padding-left:8px;">
                <span style="color:#e05030;">■</span> <span style="font-family:'DM Mono',monospace;font-size:0.72rem;color:rgba(245,242,235,0.7);">{high_cnt} High materiality</span><br>
                <span style="color:#d0a030;">■</span> <span style="font-family:'DM Mono',monospace;font-size:0.72rem;color:rgba(245,242,235,0.7);">{med_cnt} Medium</span><br>
                <span style="color:#7a9a5a;">■</span> <span style="font-family:'DM Mono',monospace;font-size:0.72rem;color:rgba(245,242,235,0.7);">{low_cnt} Low</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with cr:
        st.markdown('<span class="slabel">ESG Coverage</span>', unsafe_allow_html=True)
        st.plotly_chart(radar_chart(p_scores, sector), use_container_width=True)
    with cb2:
        st.markdown('<span class="slabel">Pillar Scores</span>', unsafe_allow_html=True)
        st.plotly_chart(bar_chart(p_scores), use_container_width=True)

    risks = MATERIAL_RISKS.get(sector, [])
    if risks:
        st.markdown("---")
        st.markdown('<span class="slabel">Sector Context</span>', unsafe_allow_html=True)
        st.markdown(f"### Key ESG Risks for {sector}")
        rcols = st.columns(3)
        for i, risk in enumerate(risks):
            rcols[i % 3].markdown(f"""
            <div style="background:white;border:1.5px solid #e0ddd4;border-radius:10px;
                        padding:14px 16px;margin-bottom:8px;font-size:0.83rem;color:#2a2a1a;
                        line-height:1.6;font-weight:500;">{risk}</div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<span class="slabel">Disclosure Gaps</span>', unsafe_allow_html=True)
    st.markdown(f"### {len(findings)} Gap{'s' if len(findings)!=1 else ''} Identified")

    if not findings:
        st.success("No gaps identified — all assessed criteria are fully disclosed.")
    else:
        for f in findings:
            c = sev_color(f["sev"])
            st.markdown(f"""
            <div class="finding" style="border-left-color:{c};">
                <div class="finding-lbl" style="color:{c};">{f['sev'].upper()} MATERIALITY · {f['pillar']} · {f['status']}</div>
                <div class="finding-text">{f['q']}</div>
                <div class="finding-explain"><b>Why this matters:</b> {f['explain']}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<span class="slabel">Recommendations</span>', unsafe_allow_html=True)
    st.markdown("### Priority Actions")

    shown = set()
    recs  = []
    for f in findings:
        if f["sev"] == "high" and f["pillar"] not in shown:
            shown.add(f["pillar"])
            recs.append((f["pillar"], REC_MAP[f["pillar"]]))

    if not recs:
        st.success("No high-materiality gaps. Focus on maintaining disclosure quality and preparing for mandatory reporting regimes (CSRD, ISSB).")
    else:
        for i, (pillar, r) in enumerate(recs, 1):
            color = PILLARS[pillar]["accent"]
            st.markdown(f"""
            <div class="rec">
                <span class="rec-n">{i:02d}</span>
                <span class="rec-pillar" style="color:{color};">{pillar}</span>
                {r}
                <div style="clear:both;"></div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<span class="slabel">Export</span>', unsafe_allow_html=True)
    st.markdown("### Report")

    report_text = build_report()
    meta        = st.session_state.meta
    fname = f"esg_scorecard_{(meta.get('company') or 'company').lower().replace(' ','_')}_{datetime.today().strftime('%Y%m%d')}.txt"

    tab1, tab2 = st.tabs(["Copy Report", "Download .txt"])
    with tab1:
        st.markdown('<p style="font-size:0.82rem;color:#5a5a3a;margin-bottom:8px;">Click inside the box → Ctrl+A / Cmd+A to select all → Ctrl+C / Cmd+C to copy.</p>', unsafe_allow_html=True)
        st.text_area("", value=report_text, height=360, label_visibility="collapsed")
    with tab2:
        st.markdown('<p style="font-size:0.82rem;color:#5a5a3a;margin-bottom:12px;">Downloads as .txt — open in Word (File → Open) or any text editor.</p>', unsafe_allow_html=True)
        st.download_button("⬇  Download Report (.txt)", data=report_text.encode("utf-8"),
                           file_name=fname, mime="text/plain", use_container_width=True)

    col_r, _ = st.columns([1,4])
    with col_r:
        if st.button("↺  Start Over", use_container_width=True):
            st.session_state.step = 0
            st.session_state.responses = {}
            st.rerun()

    st.markdown("""
    <p style="font-size:0.72rem;color:rgba(28,31,23,0.2);text-align:center;font-family:'DM Mono',monospace;letter-spacing:0.5px;padding:20px 0 8px;">
    Built by Khushi Rana &nbsp;·&nbsp; ESG Corporate Risk Scorecard &nbsp;·&nbsp; Educational purposes only
    </p>
    """, unsafe_allow_html=True)
