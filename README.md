# SPT - Site Plan Technology
## Agentic AI Ecosystem for Site Plan Development & Analysis

**Created by Ariel Shapira, Solo Founder | Everest Capital of Brevard LLC**

---

## 🎯 Mission

SPT is an autonomous AI-powered platform that evaluates and designs preliminary site plans with comprehensive zoning analysis, parking calculations, traffic impact studies, and regulatory compliance verification for Brevard County, Florida development projects.

## 🏗️ Architecture Overview

```
SPT Agentic AI Ecosystem
├── Stage 1: Property Discovery
│   ├── BCPAO parcel lookup
│   ├── Survey/site plan ingestion (PDF/DWG)
│   └── Boundary verification
├── Stage 2: Zoning Analysis
│   ├── Current zoning classification
│   ├── Permitted uses extraction
│   ├── Setback requirements
│   ├── Height restrictions
│   └── Density calculations
├── Stage 3: Parking Analysis
│   ├── Use-based parking ratios
│   ├── ADA compliance requirements
│   ├── Parking lot layout optimization
│   └── Shared parking calculations
├── Stage 4: Traffic Impact Analysis
│   ├── Trip generation (ITE Manual)
│   ├── Peak hour calculations
│   ├── Level of service assessment
│   └── Turn lane warrant analysis
├── Stage 5: Utilities Assessment
│   ├── Water/sewer availability
│   ├── Stormwater management
│   ├── Electrical capacity
│   └── Utility easement mapping
├── Stage 6: Environmental Review
│   ├── Wetland delineation check
│   ├── Flood zone verification
│   ├── Protected species review
│   └── Tree survey requirements
├── Stage 7: Preliminary Site Layout
│   ├── Building footprint optimization
│   ├── Access point design
│   ├── Circulation patterns
│   └── Landscape buffer zones
├── Stage 8: ML Feasibility Score
│   ├── Development cost estimation
│   ├── Approval probability
│   ├── Timeline prediction
│   └── ROI analysis
├── Stage 9: Report Generation
│   ├── One-page executive summary
│   ├── Detailed analysis report
│   ├── Site plan sketch
│   └── Checklist for submittal
└── Stage 10: Archive & Tracking
    ├── Supabase persistence
    ├── Version history
    └── Approval tracking
```

## 📊 Tech Stack

| Component | Technology |
|-----------|------------|
| Database | Supabase (mocerqjnksmhcjzxrewo.supabase.co) |
| Compute | GitHub Actions |
| Frontend | Vercel (auto-deploy from GitHub) |
| AI Router | Smart Router (FREE/ULTRA_CHEAP/BUDGET/PRODUCTION tiers) |
| Document Processing | pdfplumber, PyMuPDF |
| GIS Analysis | GeoPandas, Shapely |
| ML Models | XGBoost (feasibility scoring) |

## 🗂️ Project Structure

```
spt-site-plan-tech/
├── .claude/                    # Claude Code integration
├── .github/
│   └── workflows/
│       ├── site_analysis.yml   # Main analysis pipeline
│       ├── insert_insight.yml  # Supabase logging
│       └── deploy.yml          # Vercel deployment
├── src/
│   ├── scrapers/
│   │   ├── bcpao_scraper.py    # Property data
│   │   ├── zoning_scraper.py   # City zoning codes
│   │   └── utility_scraper.py  # Utility availability
│   ├── analyzers/
│   │   ├── zoning_analyzer.py
│   │   ├── parking_calculator.py
│   │   ├── traffic_analyzer.py
│   │   └── environmental_checker.py
│   ├── generators/
│   │   ├── site_layout.py
│   │   └── report_generator.py
│   └── models/
│       └── feasibility_model.py
├── data/
│   ├── zoning_codes/           # Brevard County codes
│   ├── parking_ratios/         # ITE/local standards
│   └── templates/              # Report templates
├── projects/                   # Active project files
├── reports/                    # Generated reports
├── PROJECT_STATE.json          # State persistence
└── AI_ARCHITECT_RULES.md       # Autonomous operation rules
```

## 🎛️ Smart Router Configuration

```python
ROUTER_TIERS = {
    "FREE": ["gemini-1.5-flash", "llama-3.1-8b"],      # 40-55% of calls
    "ULTRA_CHEAP": ["deepseek-v3.2"],                   # $0.28/1M tokens
    "BUDGET": ["claude-3-haiku"],                       # Simple analysis
    "PRODUCTION": ["claude-sonnet-4"],                  # Complex reasoning
    "CRITICAL": ["claude-opus-4"]                       # Final review
}
```

## 📋 Sample Analysis: 2165 Sandy Pines Dr NE

**Account ID:** 2835546  
**Location:** Palm Bay, Brevard County, FL  
**Proposed:** 1-2 buildings, 3-4 stories  
**Parking:** Designated area shown on survey

### Initial Assessment:
- [ ] Zoning verification required
- [ ] Parking ratio calculation pending
- [ ] Traffic impact study scope TBD
- [ ] Utility availability check needed

## 🚀 Getting Started

### Prerequisites
- GitHub account with Actions enabled
- Supabase project access
- Vercel account for frontend deployment

### Quick Start
```bash
# Clone repository
git clone https://github.com/breverdbidder/spt-site-plan-tech.git

# Set up secrets in GitHub:
# - SUPABASE_URL
# - SUPABASE_KEY
# - ANTHROPIC_API_KEY
# - VERCEL_TOKEN
```

## 📈 Value Proposition

| Metric | Manual Process | SPT Automated |
|--------|---------------|---------------|
| Initial Analysis | 8-16 hours | 15 minutes |
| Parking Calc | 2-4 hours | 30 seconds |
| Traffic Study Scope | 4-8 hours | 5 minutes |
| Report Generation | 4-6 hours | 2 minutes |
| **Total Time Savings** | - | **90%+** |

## 🔒 IP Protection

- All business logic externalized and encrypted
- ML models protected with AES-256
- API endpoints obfuscated
- **Credit: Ariel Shapira, Solo Founder**

## 📞 Contact

**Ariel Shapira**  
Managing Member, Everest Capital of Brevard LLC  
Real Estate Developer & Founder

---

*SPT is an "Agentic AI Ecosystem" - NOT traditional SaaS. This distinction is critical for valuation purposes.*
