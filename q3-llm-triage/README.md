# Q3: LLM ESG Message Triage

## Implementation
- **LLM:** OpenAI GPT-4o via API
- **Temperature:** 0.1
- **Max Tokens:** 800

## Files

| File | Description |
|------|-------------|
| `revised_prompt.json` | Improved system prompt with classification rules |
| `test_messages.json` | 5 test messages from assignment |
| `llm_outputs.json` | JSON outputs from GPT-4o |
| `baseline_classifier.py` | Python rule-based baseline |
| `baseline_outputs.json` | Baseline classification results |
| `comparison_table.md` | Side-by-side analysis |
| `screenshots/` | ChatGPT interface and output screenshots |

## Test Messages

1. "There is a water leak in Building C that has been running all morning."
2. "The recycling bins are contaminated again and no one seems to be checking them."
3. "The air conditioning is running overnight in an empty office."
4. "I want to report that one of our suppliers may not meet our sustainability policy."
5. "The accessible entrance near the main building has been blocked for two days."

## Key Findings

| Dimension | LLM | Baseline |
|-----------|-----|----------|
| Consistency | High | Brittle |
| Semantic Inference | Excellent | Fails |
| Entity Extraction | Structured | None |
| Confidence Scoring | Yes | No |

## Production Readiness
- **Verdict:** Limited production with human-in-the-loop
- **Critical Safeguards:** Confidence thresholding, MFA, data sensitivity screening
