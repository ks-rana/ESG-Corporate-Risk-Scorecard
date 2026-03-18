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
    color: #1c1f17;
}
.main, .block-container { background-color: #f5f2eb !important; }
[data-testid="stAppViewContainer"] { background-color: #f5f2eb !important; }
[data-testid="stHeader"] { background-color: #f5f2eb !important; }

h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: #1c1f17 !important;
    letter-spacing: -0.3px;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: #1c1f17 !important;
    border-right: 1px solid rgba(255,255,255,0.06);
}
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] div { color: #c8c4b0 !important; }
[data-testid="stSidebar"] input[type="text"] {
    background-color: #2a2d22 !important;
    color: #e8e4d4 !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 6px !important;
}
[data-testid="stSidebar"] [data-baseweb="select"] > div {
    background-color: #2a2d22 !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 6px !important;
    color: #e8e4d4 !important;
}
[data-testid="stSidebar"] [data-baseweb="select"] span { color: #e8e4d4 !important; }
[data-testid="stSidebar"] [data-baseweb="select"] svg { fill: #7a9a5a !important; }
[data-baseweb="popover"] [data-baseweb="menu"] {
    background-color: #2a2d22 !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
}
[data-baseweb="popover"] [role="option"] { background-color: #2a2d22 !important; color: #e8e4d4 !important; }
[data-baseweb="popover"] [role="option"]:hover,
[data-baseweb="popover"] [aria-selected="true"] { background-color: #3a4a2a !important; color: #b8d48a !important; }

/* LABELS */
.slabel {
    font-family: 'DM Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #7a9a5a;
    margin-bottom: 4px;
    margin-top: 24px;
    display: block;
}

/* HERO */
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
.hero::after {
    content: '';
    position: absolute;
    width: 160px; height: 160px;
    border-radius: 50%;
    border: 1px solid rgba(122,154,90,0.06);
    bottom: -20px; right: 40px;
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
.hero p { color: rgba(245,242,235,0.5); font-size: 0.92rem; margin: 0; line-height: 1.7; max-width: 600px; }

/* DISCLAIMER */
.disclaimer {
    background: #fff8e8;
    border: 1px solid #e8d48a;
    border-left: 3px solid #c8a428;
    border-radius: 0 10px 10px 0;
    padding: 14px 18px;
    margin-bottom: 20px;
    font-size: 0.82rem;
    color: #5a4a18;
    line-height: 1.7;
}
.disclaimer-title {
    font-family: 'DM Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #c8a428;
    margin-bottom: 5px;
}

/* PROGRESS */
.progress-bar-outer { background: rgba(28,31,23,0.08); border-radius: 99px; height: 4px; margin: 20px 0 8px; overflow: hidden; }
.progress-bar-inner { height: 4px; border-radius: 99px; background: linear-gradient(90deg, #7a9a5a, #b8d48a); }
.step-counter { font-family: 'DM Mono', monospace; font-size: 0.68rem; letter-spacing: 1px; color: rgba(28,31,23,0.4); margin-bottom: 24px; }

/* PILLAR CARD */
.pillar-card {
    background: white;
    border: 1px solid rgba(28,31,23,0.08);
    border-radius: 16px;
    padding: 26px 26px 22px;
    margin-bottom: 20px;
}
.pillar-title { font-family: 'Playfair Display', serif; font-size: 1.15rem; font-weight: 700; color: #1c1f17; margin-bottom: 6px; }
.pillar-desc { font-size: 0.83rem; color: rgba(28,31,23,0.5); line-height: 1.6; margin-bottom: 14px; }

/* QUESTION */
.q-item {
    background: #fafaf7;
    border: 1px solid rgba(28,31,23,0.07);
    border-radius: 10px;
    padding: 13px 16px;
    margin-bottom: 6px;
}
.q-weight {
    font-family: 'DM Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 2px 8px;
    border-radius: 3px;
    display: inline-block;
    margin-bottom: 6px;
}
.w-high   { background: rgba(28,31,23,0.08); color: #1c1f17; border: 1px solid rgba(28,31,23,0.15); }
.w-medium { background: rgba(122,154,90,0.1); color: #4a6a2a; border: 1px solid rgba(122,154,90,0.2); }
.w-low    { background: rgba(122,154,90,0.05); color: #6a8a4a; border: 1px solid rgba(122,154,90,0.12); }
.q-text { font-size: 0.87rem; color: rgba(28,31,23,0.78); line-height: 1.5; }

/* BUTTONS */
.stButton > button {
    background: white !important;
    color: #1c1f17 !important;
    border: 1px solid rgba(28,31,23,0.15) !important;
    border-radius: 8px !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.5px !important;
    padding: 10px 22px !important;
}
.stButton > button:hover { background: #1c1f17 !important; color: #f5f2eb !important; border-color: #1c1f17 !important; }

/* RADIO */
.stRadio > div { gap: 6px !important; }
.stRadio label {
    background: white !important;
    border: 1px solid rgba(28,31,23,0.1) !important;
    border-radius: 8px !important;
    padding: 8px 14px !important;
    font-size: 0.83rem !important;
    color: rgba(28,31,23,0.65) !important;
    cursor: pointer !important;
}
.stRadio label:hover { background: #f0f4e8 !important; border-color: rgba(122,154,90,0.4) !important; color: #1c1f17 !important; }

/* SCORE CARD */
.score-hero {
    background: #1c1f17;
    border-radius: 20px;
    padding: 36px 32px;
    text-align: center;
}
.score-num { font-family: 'Playfair Display', serif; font-size: 5rem; font-weight: 900; line-height: 1; margin: 10px 0 6px; }
.score-lbl { font-family: 'DM Mono', monospace; font-size: 0.65rem; letter-spacing: 2px; text-transform: uppercase; color: rgba(245,242,235,0.35); margin-bottom: 6px; }

/* FINDINGS */
.finding {
    border-left: 3px solid;
    padding: 13px 17px;
    margin-bottom: 8px;
    background: white;
    border-radius: 0 10px 10px 0;
    font-size: 0.86rem;
    line-height: 1.6;
    color: rgba(28,31,23,0.75);
}
.finding-lbl { font-family: 'DM Mono', monospace; font-size: 0.6rem; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 5px; }

/* RECS */
.rec {
    background: white;
    border: 1px solid rgba(28,31,23,0.08);
    border-radius: 10px;
    padding: 16px 20px;
    margin-bottom: 8px;
    font-size: 0.86rem;
    color: rgba(28,31,23,0.72);
    line-height: 1.65;
}
.rec-n { font-family: 'Playfair Display', serif; font-size: 1.6rem; font-weight: 900; color: rgba(28,31,23,0.1); float: left; margin-right: 14px; line-height: 1; }

/* FW TAGS */
.fw-tag {
    display: inline-block;
    font-family: 'DM Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 3px 8px;
    border-radius: 4px;
    margin: 2px 3px 2px 0;
    background: rgba(122,154,90,0.1);
    color: #4a6a2a;
    border: 1px solid rgba(122,154,90,0.2);
}

/* SCORE TABLE */
.score-table { width: 100%; border-collapse: collapse; font-size: 0.82rem; }
.score-table th { font-family: 'DM Mono', monospace; font-size: 0.6rem; letter-spacing: 1.5px; text-transform: uppercase; color: #7a9a5a; padding: 8px 12px; border-bottom: 1px solid rgba(28,31,23,0.08); text-align: left; }
.score-table td { padding: 8px 12px; border-bottom: 1px solid rgba(28,31,23,0.04); color: rgba(28,31,23,0.65); vertical-align: top; }
.score-table tr:last-child td { border-bottom: none; }

.stTextInput input { background: white !important; border-color: rgba(28,31,23,0.15) !important; color: #1c1f17 !important; border-radius: 8px !important; }
.stDownloadButton button { background: #1c1f17 !important; color: #f5f2eb !important; border: none !important; border-radius: 8px !important; font-family: 'DM Mono', monospace !important; font-size: 0.75rem !important; }
.stDownloadButton button:hover { background: #2a2d22 !important; }
hr { border-color: rgba(28,31,23,0.08) !important; }
.streamlit-expanderHeader { background: white !important; color: #1c1f17 !important; border-radius: 10px !important; font-family: 'DM Sans', sans-serif !important; border: 1px solid rgba(28,31,23,0.08) !important; }
.streamlit-expanderContent { background: #fafaf7 !important; border: 1px solid rgba(28,31,23,0.06) !important; border-radius: 0 0 10px 10px !important; }
</style>
""", unsafe_allow_html=True)


# ============================================================
# FRAMEWORK DATA
# Aligned to GRI Standards, SASB, TCFD, UN SDGs
# ============================================================
PILLARS = {
    "Environmental": {
        "icon": "◉",
        "color": "#4a6a2a",
        "accent": "#7a9a5a",
        "weight": 0.35,
        "description": "Climate risk exposure, emissions management, resource use, and environmental compliance. Aligned to TCFD climate disclosure and GRI 300 series.",
        "frameworks": ["TCFD", "GRI 300", "SASB", "UN SDG 13"],
        "questions": [
            ("Does the company disclose Scope 1, 2, and 3 greenhouse gas emissions?", "high"),
            ("Has the company set science-based emissions reduction targets (SBTi or equivalent)?", "high"),
            ("Is there a formal climate risk assessment aligned to TCFD recommendations?", "high"),
            ("Does the company report on water usage and reduction targets?", "medium"),
            ("Are supply chain environmental risks assessed and disclosed?", "medium"),
            ("Does the company have a credible net-zero or carbon neutrality pathway?", "high"),
            ("Is biodiversity and land-use impact assessed and reported?", "low"),
        ]
    },
    "Social": {
        "icon": "◎",
        "color": "#2a5a7a",
        "accent": "#5a9ab8",
        "weight": 0.30,
        "description": "Workforce equity, labour practices, community impact, and human rights in operations and supply chains. Aligned to GRI 400 series and UN SDGs 8, 10.",
        "frameworks": ["GRI 400", "UN SDG 8", "UN SDG 10", "ILO Core"],
        "questions": [
            ("Does the company publish pay equity and gender diversity data by seniority level?", "high"),
            ("Are human rights due diligence processes applied to the supply chain?", "high"),
            ("Does the company have a formal health, safety, and wellbeing policy with disclosed metrics?", "medium"),
            ("Is there a mechanism for employee grievance reporting with non-retaliation protection?", "medium"),
            ("Does the company disclose community investment and local impact initiatives?", "low"),
            ("Are supplier labour standards assessed and enforced through audits?", "high"),
        ]
    },
    "Governance": {
        "icon": "◈",
        "color": "#5a3a2a",
        "accent": "#a87a5a",
        "weight": 0.35,
        "description": "Board composition, executive accountability, anti-corruption controls, and ESG integration into strategy and risk management. Aligned to GRI 200 series.",
        "frameworks": ["GRI 200", "SASB", "OECD Corp. Gov.", "TCFD Governance"],
        "questions": [
            ("Is there board-level oversight of ESG risks and opportunities, with named responsibility?", "high"),
            ("Does executive compensation include ESG performance metrics?", "high"),
            ("Are anti-corruption and anti-bribery policies in place with disclosed breach data?", "high"),
            ("Is the board composition disclosed with diversity across gender, background, and expertise?", "medium"),
            ("Does the company conduct or commission third-party ESG assurance or verification?", "high"),
            ("Are lobbying activities and political donations disclosed?", "medium"),
            ("Is there a formal stakeholder engagement process for material ESG issues?", "medium"),
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
    "Environmental": "Prioritize TCFD-aligned climate risk disclosure and set interim emissions targets. Scope 3 supply chain emissions and biodiversity exposure are increasingly material to institutional investors and regulatory bodies.",
    "Social": "Develop a human rights due diligence framework for supply chain operations. Pay equity disclosure and grievance mechanisms are now baseline expectations under GRI 400 and emerging mandatory reporting regimes (e.g. CSRD).",
    "Governance": "Ensure board-level ESG accountability is named and documented — not just implied. Third-party ESG assurance is rapidly becoming a differentiator in capital markets and is a prerequisite for many investor ESG mandates.",
}

MATERIAL_RISKS = {
    "Financial Services":    ["Physical climate risk in loan portfolios", "Social washing / DEI disclosure gaps", "Governance failures in ESG-linked products"],
    "Energy & Utilities":    ["Stranded asset risk from energy transition", "Community impact of operations", "Board accountability for climate strategy"],
    "Technology":            ["Scope 3 emissions (hardware, cloud)", "Labour practices in supply chain", "Data governance and executive pay alignment"],
    "Healthcare":            ["Supply chain human rights", "Access and affordability equity", "Board diversity and conflict of interest"],
    "Manufacturing":         ["Carbon intensity and transition risk", "Supplier labour audits", "Anti-corruption in procurement"],
    "Consumer Goods/Retail": ["Packaging and waste targets", "Living wage in supply chain", "Greenwashing and disclosure quality"],
    "Real Estate":           ["Building energy efficiency and GRESB alignment", "Community displacement and social impact", "Governance of ESG-linked debt"],
    "Telecommunications":    ["Energy use of network infrastructure", "Digital inclusion and access equity", "Executive accountability and lobbying disclosure"],
    "Other":                 ["Emissions reporting completeness", "Stakeholder engagement quality", "Board ESG oversight"],
}


# ============================================================
# SESSION STATE
# ============================================================
for k, v in [("step", 0), ("responses", {}), ("meta", {})]:
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
    if score >= 80: return "Leading",       "#4a6a2a"
    if score >= 60: return "Developing",    "#7a9a5a"
    if score >= 40: return "Lagging",       "#c8a428"
    return           "At Risk",             "#c85428"

def sev_color(sev):
    return {"high": "#c85428", "medium": "#c8a428", "low": "#7a9a5a"}.get(sev, "#888")

def get_findings():
    findings = []
    downgrade = {"high": "medium", "medium": "low", "low": "low"}
    order     = {"high": 0, "medium": 1, "low": 2}
    for pillar, pd in PILLARS.items():
        resp = st.session_state.responses.get(pillar, {})
        for i, (q, wt) in enumerate(pd["questions"]):
            r = resp.get(f"{pillar}_{i}", "Not applicable")
            if r == "No — not addressed":
                findings.append({"pillar": pillar, "q": q, "sev": wt, "status": "Gap"})
            elif r == "Partially — in progress":
                findings.append({"pillar": pillar, "q": q, "sev": downgrade[wt], "status": "Partial"})
    findings.sort(key=lambda x: order[x["sev"]])
    return findings

def radar_chart(scores, sector):
    weights = SECTOR_MATERIALITY.get(sector, SECTOR_MATERIALITY["Other"])
    pillars = list(scores.keys())
    vals    = [scores[p] for p in pillars]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=vals + [vals[0]], theta=pillars + [pillars[0]],
        fill='toself', fillcolor='rgba(122,154,90,0.15)',
        line=dict(color='#7a9a5a', width=2), name='Score'
    ))
    fig.update_layout(
        polar=dict(
            bgcolor='rgba(0,0,0,0)',
            radialaxis=dict(visible=True, range=[0,100],
                tickfont=dict(size=9, family='DM Mono', color='rgba(28,31,23,0.3)'),
                gridcolor='rgba(28,31,23,0.08)', linecolor='rgba(28,31,23,0.08)'),
            angularaxis=dict(
                tickfont=dict(size=11, family='Playfair Display', color='rgba(28,31,23,0.65)'),
                gridcolor='rgba(28,31,23,0.08)', linecolor='rgba(28,31,23,0.08)')
        ),
        paper_bgcolor='rgba(0,0,0,0)', showlegend=False,
        margin=dict(l=40,r=40,t=40,b=40), height=300
    )
    return fig

def bar_chart(scores):
    pillars = list(scores.keys())
    vals    = [scores[p] for p in pillars]
    colors  = [rating(v)[1] for v in vals]
    fig = go.Figure(go.Bar(
        x=pillars, y=vals, marker_color=colors, marker_line_width=0,
        text=[f"{v:.0f}" for v in vals], textposition='outside',
        textfont=dict(family='DM Mono', size=11, color='rgba(28,31,23,0.5)')
    ))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(range=[0,115], showgrid=True, gridcolor='rgba(28,31,23,0.06)',
                   tickfont=dict(family='DM Mono', size=9, color='rgba(28,31,23,0.3)')),
        xaxis=dict(tickfont=dict(family='Playfair Display', size=11, color='rgba(28,31,23,0.6)')),
        margin=dict(l=10,r=10,t=20,b=10), height=260, showlegend=False
    )
    return fig

def build_report():
    sc   = overall_score()
    rat  = rating(sc)[0]
    fnd  = get_findings()
    p_sc = {p: pillar_score(p) for p in PILLARS}
    meta = st.session_state.meta
    sector = meta.get("sector", "—")
    lines = [
        "=" * 68, "ESG CORPORATE RISK SCORECARD", "=" * 68,
        f"Company       : {meta.get('company','—')}",
        f"Sector        : {sector}",
        f"Assessment    : {meta.get('assessment_type','—')}",
        f"Assessed by   : {meta.get('assessor','—')}",
        f"Date          : {datetime.today().strftime('%B %d, %Y')}",
        f"Framework     : GRI Standards · TCFD · SASB · UN SDGs · OECD Corp. Gov.",
        "",
        "DISCLAIMER",
        "-" * 68,
        "This scorecard is an educational reference tool. It is not a formal ESG",
        "rating, investment recommendation, or regulatory compliance determination.",
        "Scores are based on self-reported inputs and should not be used as the sole",
        "basis for investment, procurement, or governance decisions.",
        "",
        "-" * 68, "SCORING METHODOLOGY", "-" * 68,
        "Response values: Yes=1.0 | Partial=0.5 | No=0.0 | N/A=excluded",
        "Pillar scores = average of scored responses × 100",
        f"Overall score = sector-adjusted weighted average (sector: {sector})",
        "Weights reflect materiality by sector per SASB Materiality Map.",
        "Rating: 80-100 Leading · 60-79 Developing · 40-59 Lagging · <40 At Risk",
        "",
        "-" * 68, "OVERALL SCORE", "-" * 68,
        f"  {sc:.1f} / 100   —   {rat}",
        "",
        "-" * 68, "PILLAR SCORES", "-" * 68,
    ]
    weights = SECTOR_MATERIALITY.get(sector, SECTOR_MATERIALITY["Other"])
    for p, s in p_sc.items():
        lines.append(f"  {p:<18} {s:>5.1f}   {rating(s)[0]:<12} weight: {weights[p]*100:.0f}%")

    risks = MATERIAL_RISKS.get(sector, [])
    if risks:
        lines += ["", "-" * 68, f"SECTOR MATERIAL RISKS ({sector})", "-" * 68]
        for r in risks:
            lines.append(f"  · {r}")

    lines += ["", "-" * 68, "RESPONSE LOG", "-" * 68]
    for pillar, pd in PILLARS.items():
        lines.append(f"\n  {pillar}")
        resp = st.session_state.responses.get(pillar, {})
        for i, (q, wt) in enumerate(pd["questions"]):
            r = resp.get(f"{pillar}_{i}", "Not applicable")
            short = {"Yes — fully disclosed":"YES","Partially — in progress":"PARTIAL",
                     "No — not addressed":"NO","Not applicable":"N/A"}.get(r,"?")
            lines.append(f"    [{short}] [{wt.upper()}] {q}")

    if fnd:
        lines += ["", "-" * 68, f"FINDINGS ({len(fnd)})", "-" * 68]
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
        lines += ["-" * 68, "RECOMMENDATIONS", "-" * 68]
        for i, r in enumerate(recs, 1):
            lines += [f"  {i}. {r}", ""]

    lines += ["=" * 68, "END OF REPORT", "=" * 68]
    return "\n".join(lines)


# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.markdown('<span class="slabel" style="color:#7a9a5a;">Company Details</span>', unsafe_allow_html=True)
    st.session_state.meta["company"]         = st.text_input("Company Name",      value=st.session_state.meta.get("company",""),      placeholder="e.g. Rogers Communications")
    st.session_state.meta["sector"]          = st.selectbox("Sector",
        list(SECTOR_MATERIALITY.keys()))
    st.session_state.meta["assessment_type"] = st.selectbox("Assessment Type",
        ["Self-assessment", "Third-party review", "Investor due diligence", "Academic / research"])
    st.session_state.meta["assessor"]        = st.text_input("Assessor",           value=st.session_state.meta.get("assessor",""),      placeholder="Your name")

    st.markdown("---")
    sector = st.session_state.meta.get("sector","Other")
    weights = SECTOR_MATERIALITY.get(sector, SECTOR_MATERIALITY["Other"])
    st.markdown(f'<span class="slabel" style="color:#7a9a5a;">Sector Weights — {sector}</span>', unsafe_allow_html=True)
    for p, w in weights.items():
        bar_w = int(w * 100)
        st.markdown(f"""
        <div style="margin-bottom:8px;">
            <div style="display:flex;justify-content:space-between;margin-bottom:3px;">
                <span style="font-family:'DM Mono',monospace;font-size:0.65rem;color:#c8c4b0;letter-spacing:1px;">{p}</span>
                <span style="font-family:'DM Mono',monospace;font-size:0.65rem;color:#7a9a5a;">{bar_w}%</span>
            </div>
            <div style="background:rgba(255,255,255,0.06);border-radius:99px;height:3px;">
                <div style="width:{bar_w}%;height:3px;border-radius:99px;background:#7a9a5a;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('<p style="font-family:\'DM Mono\',monospace;font-size:0.6rem;color:rgba(200,196,176,0.35);margin-top:6px;line-height:1.6;">Weights adjust automatically per SASB materiality. Financial Services weights Governance most heavily; Energy weights Environmental.</p>', unsafe_allow_html=True)

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
        <p>Evaluate a company's Environmental, Social, and Governance performance against structured criteria drawn from GRI Standards, TCFD, SASB materiality, and UN SDGs. Scores adjust by sector. Generate a findings report.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="disclaimer">
        <div class="disclaimer-title">⚠ Reference Tool — Not an ESG Rating</div>
        This scorecard is an <b>educational reference tool</b> intended to support structured thinking about ESG risk exposure. It is not a formal ESG rating, investment recommendation, or regulatory compliance determination. Scores reflect self-reported inputs only.<br><br>
        For real investment, procurement, or governance decisions, please engage a qualified ESG analyst, use verified data sources (CDP, MSCI ESG, Sustainalytics), and review the company's own sustainability disclosures.
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    for col, icon, title, desc, color in [
        (c1, "◉", "3 ESG Pillars",           "Environmental, Social, Governance — each with sector-adjusted weighting", "#4a6a2a"),
        (c2, "◎", "20 Disclosure Criteria",  "Drawn from GRI, TCFD, SASB and UN SDGs", "#2a5a7a"),
        (c3, "◈", "Sector-Adjusted Score",   "Weights shift automatically based on SASB materiality by sector", "#5a3a2a"),
    ]:
        col.markdown(f"""
        <div style="background:white;border:1px solid rgba(28,31,23,0.08);border-radius:14px;padding:22px 20px;">
            <div style="font-size:1.3rem;color:{color};margin-bottom:10px;">{icon}</div>
            <div style="font-family:'Playfair Display',serif;font-size:0.95rem;font-weight:700;color:#1c1f17;margin-bottom:6px;">{title}</div>
            <div style="font-size:0.78rem;color:rgba(28,31,23,0.45);line-height:1.6;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    with st.expander("How scoring works — methodology & sector weights"):
        st.markdown("""
        <div style="padding:4px 0;">
        <p style="font-size:0.84rem;color:rgba(28,31,23,0.55);line-height:1.8;margin-bottom:14px;">
        Each criterion is rated on a 4-point scale, then converted to a score:
        </p>
        <table class="score-table">
            <tr><th>Response</th><th>Value</th></tr>
            <tr><td>Yes — fully disclosed</td><td style="color:#4a6a2a;font-family:'DM Mono',monospace;">1.0 (full credit)</td></tr>
            <tr><td>Partially — in progress</td><td style="color:#c8a428;font-family:'DM Mono',monospace;">0.5 (half credit)</td></tr>
            <tr><td>No — not addressed</td><td style="color:#c85428;font-family:'DM Mono',monospace;">0.0 (no credit)</td></tr>
            <tr><td>Not applicable</td><td style="color:#888;font-family:'DM Mono',monospace;">excluded</td></tr>
        </table>
        <p style="font-size:0.82rem;color:rgba(28,31,23,0.5);margin-top:14px;line-height:1.8;">
        <b>Pillar score</b> = average of scored responses × 100<br>
        <b>Overall score</b> = sector-weighted average — weights reflect SASB materiality by sector.<br>
        For example, Energy companies weight Environmental at 50%, while Financial Services weight Governance at 45%.<br><br>
        <b>Rating:</b> 80–100 Leading · 60–79 Developing · 40–59 Lagging · Below 40 At Risk
        </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background:white;border:1px solid rgba(28,31,23,0.08);border-radius:14px;padding:22px 24px;font-size:0.87rem;color:rgba(28,31,23,0.55);line-height:1.9;">
    Enter company details in the left sidebar (sector adjusts the weights automatically), then work through the three ESG pillars.<br><br>
    For each criterion, select the response that best reflects the company's <i>current disclosed position</i>:<br>
    &nbsp;&nbsp;<b style="color:#4a6a2a;">Yes — fully disclosed</b> &nbsp;· Formally reported in sustainability/annual report or CDP<br>
    &nbsp;&nbsp;<b style="color:#c8a428;">Partially — in progress</b> &nbsp;· Disclosed partially, target set but not yet met, or in development<br>
    &nbsp;&nbsp;<b style="color:#c85428;">No — not addressed</b> &nbsp;· Not disclosed or no evidence of action<br>
    &nbsp;&nbsp;<b style="color:rgba(28,31,23,0.3);">Not applicable</b> &nbsp;· Genuinely irrelevant to this company's operations
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    _, cb, _ = st.columns([2, 1, 2])
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
        <div class="pillar-title">{pillar}</div>
        <div class="pillar-desc">{pd_data['description']}</div>
        <div>{fw_tags}</div>
    </div>
    """, unsafe_allow_html=True)

    if pillar not in st.session_state.responses:
        st.session_state.responses[pillar] = {}

    for i, (q, wt) in enumerate(pd_data["questions"]):
        key     = f"{pillar}_{i}"
        cur_val = st.session_state.responses[pillar].get(key, "Not applicable")
        idx     = RESPONSE_OPTS.index(cur_val) if cur_val in RESPONSE_OPTS else 3

        st.markdown(f"""
        <div class="q-item">
            <div class="q-weight w-{wt}">{wt} materiality</div>
            <div class="q-text">{q}</div>
        </div>
        """, unsafe_allow_html=True)

        resp = st.radio("", RESPONSE_OPTS, index=idx, horizontal=True,
                        key=f"radio_{key}", label_visibility="collapsed")
        st.session_state.responses[pillar][key] = resp
        st.markdown("<div style='margin-bottom:6px;'></div>", unsafe_allow_html=True)

    sc      = pillar_score(pillar)
    rat, col = rating(sc)
    st.markdown(f"""
    <div style="background:white;border:1px solid rgba(28,31,23,0.08);border-radius:10px;
                padding:14px 20px;margin-top:16px;display:flex;align-items:center;gap:16px;">
        <div style="font-family:'Playfair Display',serif;font-size:2rem;font-weight:900;color:{col};">{sc:.0f}</div>
        <div>
            <div style="font-family:'DM Mono',monospace;font-size:0.6rem;letter-spacing:2px;text-transform:uppercase;color:rgba(28,31,23,0.3);">Pillar Score</div>
            <div style="font-family:'DM Mono',monospace;font-size:0.72rem;color:{col};">{rat}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    nl, _, nr = st.columns([1, 2, 1])
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
    high_cnt = sum(1 for f in findings if f["sev"] == "high")
    med_cnt  = sum(1 for f in findings if f["sev"] == "medium")
    low_cnt  = sum(1 for f in findings if f["sev"] == "low")

    st.markdown('<span class="slabel">Results</span>', unsafe_allow_html=True)
    st.markdown("## ESG Risk Scorecard Results")
    st.markdown("<br>", unsafe_allow_html=True)

    cs, cr, cb2 = st.columns([1, 1.3, 1.3])

    with cs:
        st.markdown(f"""
        <div class="score-hero">
            <div class="score-lbl">Overall ESG Score</div>
            <div class="score-num" style="color:{col};">{sc:.0f}</div>
            <div style="font-family:'DM Mono',monospace;font-size:0.7rem;letter-spacing:1.5px;text-transform:uppercase;color:{col};margin-bottom:20px;">{rat}</div>
            <div style="font-family:'DM Mono',monospace;font-size:0.58rem;letter-spacing:2px;color:rgba(245,242,235,0.3);text-transform:uppercase;margin-bottom:10px;">Disclosure Gaps</div>
            <div style="font-size:0.83rem;line-height:2.2;text-align:left;padding-left:12px;">
                <span style="color:#c85428;">■</span> <span style="font-family:'DM Mono',monospace;font-size:0.72rem;color:rgba(245,242,235,0.6);">{high_cnt} High materiality</span><br>
                <span style="color:#c8a428;">■</span> <span style="font-family:'DM Mono',monospace;font-size:0.72rem;color:rgba(245,242,235,0.6);">{med_cnt} Medium</span><br>
                <span style="color:#7a9a5a;">■</span> <span style="font-family:'DM Mono',monospace;font-size:0.72rem;color:rgba(245,242,235,0.6);">{low_cnt} Low</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with cr:
        st.markdown('<span class="slabel">ESG Coverage</span>', unsafe_allow_html=True)
        st.plotly_chart(radar_chart(p_scores, sector), use_container_width=True)

    with cb2:
        st.markdown('<span class="slabel">Pillar Scores</span>', unsafe_allow_html=True)
        st.plotly_chart(bar_chart(p_scores), use_container_width=True)

    # Sector material risks
    risks = MATERIAL_RISKS.get(sector, [])
    if risks:
        st.markdown("---")
        st.markdown('<span class="slabel">Sector Material Risks</span>', unsafe_allow_html=True)
        st.markdown(f"### Key ESG Risks for {sector}")
        cols = st.columns(3)
        for i, risk in enumerate(risks):
            cols[i % 3].markdown(f"""
            <div style="background:white;border:1px solid rgba(28,31,23,0.08);border-radius:10px;padding:14px 16px;margin-bottom:8px;">
                <div style="font-size:0.82rem;color:rgba(28,31,23,0.65);line-height:1.6;">{risk}</div>
            </div>
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
                {f['q']}
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
                <span style="font-family:'DM Mono',monospace;font-size:0.62rem;letter-spacing:1.5px;text-transform:uppercase;color:{color};display:block;margin-bottom:4px;">{pillar}</span>
                {r}
                <div style="clear:both;"></div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<span class="slabel">Export</span>', unsafe_allow_html=True)
    st.markdown("### Report")

    report_text = build_report()
    meta        = st.session_state.meta
    fname       = f"esg_scorecard_{(meta.get('company') or 'company').lower().replace(' ','_')}_{datetime.today().strftime('%Y%m%d')}.txt"

    tab1, tab2 = st.tabs(["Copy Report", "Download .txt"])
    with tab1:
        st.markdown('<p style="font-size:0.8rem;color:rgba(28,31,23,0.4);margin-bottom:8px;">Click inside the box then Ctrl+A / Cmd+A to select all, Ctrl+C / Cmd+C to copy.</p>', unsafe_allow_html=True)
        st.text_area("", value=report_text, height=360, label_visibility="collapsed")
    with tab2:
        st.markdown('<p style="font-size:0.8rem;color:rgba(28,31,23,0.4);margin-bottom:12px;">Downloads as .txt — open in Word (File → Open) or any text editor.</p>', unsafe_allow_html=True)
        st.download_button("⬇  Download Report (.txt)", data=report_text.encode("utf-8"),
                           file_name=fname, mime="text/plain", use_container_width=True)

    col_r, _ = st.columns([1, 4])
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
