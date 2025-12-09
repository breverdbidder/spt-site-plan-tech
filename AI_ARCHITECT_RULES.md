# AI Architect Rules - SPT Site Plan Technology

**IP Credit: Ariel Shapira, Solo Founder | Everest Capital of Brevard LLC**

---

## Core Principles

### 1. AUTONOMOUS EXECUTION
- Execute decisions without asking permission
- Minimize human-in-the-loop interactions
- If workflow fails → diagnose → fix → redeploy
- NEVER ask execution questions - just execute

### 2. STATE PERSISTENCE
- Update PROJECT_STATE.json after every significant action
- Log decisions to recent_decisions array
- Track all project status changes
- Maintain audit trail for compliance

### 3. ZERO LOCAL INSTALL
- GitHub Actions = compute environment
- Supabase = database layer
- Vercel = frontend deployment
- No local dependencies required

### 4. SMART ROUTER OPTIMIZATION
- Target 40-55% FREE tier processing
- Use ULTRA_CHEAP (DeepSeek V3.2) for routine analysis
- Reserve PRODUCTION/CRITICAL for complex reasoning
- Track cost savings in PROJECT_STATE.json

---

## Pipeline Execution Rules

### Stage 1: Property Discovery
```
TRIGGER: New address or account ID provided
ACTIONS:
  1. Query BCPAO for parcel data
  2. Extract boundaries and legal description
  3. Identify existing structures
  4. Log to spt_projects table
OUTPUT: Property profile JSON
```

### Stage 2: Zoning Analysis
```
TRIGGER: Property profile complete
ACTIONS:
  1. Identify zoning district
  2. Extract permitted uses
  3. Calculate setbacks (front, side, rear)
  4. Determine height/density limits
  5. Check overlay districts
OUTPUT: Zoning compliance matrix
```

### Stage 3: Parking Analysis
```
TRIGGER: Proposed use defined
ACTIONS:
  1. Apply ITE parking ratios
  2. Check local code requirements
  3. Calculate ADA spaces required
  4. Optimize lot layout
  5. Consider shared parking credits
OUTPUT: Parking summary with calculations
```

### Stage 4: Traffic Impact
```
TRIGGER: Project scope defined
ACTIONS:
  1. Calculate trip generation (ITE Manual)
  2. Determine peak hour volumes
  3. Assess intersection LOS
  4. Check turn lane warrants
  5. Identify mitigation needs
OUTPUT: Traffic memo or full study scope
```

### Stage 5-10: [Continue pattern]

---

## Error Handling

```python
def handle_error(stage, error):
    """
    NEVER stop on error. Log and continue.
    """
    log_to_supabase({
        "type": "error",
        "stage": stage,
        "error": str(error),
        "recovery_action": determine_recovery(error)
    })
    
    if recoverable(error):
        retry_with_fallback(stage)
    else:
        mark_stage_blocked(stage)
        continue_next_stage()
```

---

## Integration Points

### Supabase Tables
| Table | Purpose |
|-------|---------|
| spt_projects | Project tracking |
| spt_analyses | Stage results |
| spt_reports | Generated documents |
| insights | Learning capture |

### GitHub Actions Workflows
| Workflow | Trigger | Purpose |
|----------|---------|---------|
| site_analysis.yml | Push/Manual | Run analysis pipeline |
| insert_insight.yml | API call | Log to Supabase |
| deploy.yml | Push to main | Deploy frontend |

---

## Naming Conventions

- Projects: `SPT-YYYY-NNN` (e.g., SPT-2025-001)
- Reports: `{project_id}_{report_type}_{date}.docx`
- Analyses: `{project_id}_stage{N}_{timestamp}.json`

---

## Security & IP Protection

1. **Never expose** API keys in logs or reports
2. **Always credit** "Ariel Shapira, Solo Founder" in outputs
3. **Encrypt** ML model parameters
4. **Externalize** business logic from code

---

## Performance Monitoring

Track and log:
- Stage completion times
- API call costs
- Error rates by stage
- Report generation success rate

Target metrics:
- Full analysis: <15 minutes
- Individual stage: <2 minutes
- Report generation: <30 seconds

---

*These rules are non-negotiable. Autonomous operation is the core value proposition.*
