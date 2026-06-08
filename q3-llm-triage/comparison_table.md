# LLM vs Baseline Comparison

| Message | LLM Category | Baseline Category | LLM Urgency | Baseline Urgency | Analysis |
|---------|-------------|-------------------|-------------|------------------|----------|
| Water leak Building C | water_leak | water_leak | HIGH | HIGH | Match |
| Recycling contaminated | waste_contamination | waste_contamination | MEDIUM | HIGH | LLM more nuanced |
| Aircon overnight | energy_waste | energy_waste | MEDIUM | HIGH | LLM infers "empty office" = less urgent |
| Supplier compliance | supplier_compliance | supplier_compliance | HIGH | LOW | Baseline misses urgency |
| Accessibility blocked | accessibility_barrier | accessibility_barrier | HIGH | HIGH | Match |

## Key Differences

| Dimension | LLM | Baseline |
|-----------|-----|----------|
| Semantic inference | Understands context | Keyword-only |
| Confidence scoring | Explicit 0.87-0.94 | None |
| Entity extraction | Structured | None |
| Uncertainty flagging | Yes | No |
| Error pattern | Subtle misattribution | Systematic under-classification |
