# AI Workflow Intelligence Suite (n8n + Gemini + Qdrant)

A collection of **n8n workflows** that turn a library of automation-workflow PDFs into a searchable knowledge base (Qdrant vector DB, Gemini embeddings) and then build business tools on top of it: market scoring, cost estimates, proposals, consulting reports, documentation, monitoring and more.

> You describe a business need (e.g. *"Build an AI invoice approval workflow"*). The suite finds the closest workflow in the knowledge base, then uses Gemini to produce an estimate, proposal, consultation, optimisation plan, etc. and stores the result in Google Sheets / PDF.

---

## How it fits together

```
PDF workflow library
        │
        ▼
 01 Knowledge Base Ingestion ──► Qdrant  (chunks + Gemini embeddings)
        │
        ▼
 02 Market Intelligence Engine ─► scores every workflow (rate, demand, hours …) back into Qdrant
        │
        ▼
 Query workflows (requirement ► embedding ► Qdrant search ► Gemini ► Google Sheets)
   03 Cost Estimator          07 Optimizer             11 Recommendation Engine
   04 Proposal Generator      08 Validator             13 Monitoring & Analytics
   05 Workflow Generator      09 Documentation (PDF)   14 Consultant Agent (LangChain agent)
   06 Consultant              10 Deployment Assistant
 
 21 LinkedIn Profile Enrichment  (stand-alone: Google Sheet ► Apify ► Google Sheet)
```

## Workflows

| File | What it does | Writes to |
|---|---|---|
| `01-knowledge-base-ingestion` | Reads PDFs, cleans, chunks (1000 / 200 overlap), embeds, upserts to Qdrant | Qdrant |
| `02-market-intelligence-engine` | Gemini scores each workflow (rate, Fiverr/Upwork demand, hours, difficulty…) and writes it onto **all** chunks of that workflow | Qdrant |
| `03-workflow-cost-estimator` | Freelancer / agency price, timeline, ROI estimate | Google Sheets |
| `04-proposal-generator` | Client proposal (JSON + HTML) | Google Sheets / HTML |
| `05-workflow-generator` | Generates a workflow blueprint from the closest match | Google Sheets |
| `06-workflow-consultant` | Consulting report with ROI and risk | Google Sheets |
| `07-workflow-optimizer` | Performance / cost optimisation suggestions | Google Sheets |
| `08-workflow-validator` | Validates a workflow design | Google Sheets |
| `09-documentation-generator` | Technical documentation → HTML → PDF (Gotenberg) → Google Drive | Sheets + Drive |
| `10-deployment-assistant` | Deployment plan for the matched workflow | Google Sheets |
| `11-recommendation-engine` | Top-5 distinct workflow recommendations | Google Sheets |
| `13-monitoring-analytics` | KPI / health analysis for the top-5 matches | Google Sheets |
| `14-workflow-consultant-agent` | n8n AI Agent with Qdrant as a tool, structured JSON output | n8n output |
| `21-linkedin-profile-enrichment` | Enriches LinkedIn URLs in a sheet through an Apify actor | Google Sheets |

## Requirements

- n8n (self-hosted or cloud) — a recent version with the AI Agent / Qdrant Vector Store nodes
- A [Google AI Studio](https://aistudio.google.com/) API key (Gemini embeddings + generation)
- A [Qdrant](https://qdrant.tech/) cluster (Cloud free tier is enough)
- Google account (Sheets, and Drive for project 09)
- Optional: [Gotenberg](https://gotenberg.dev/) for project 09 · [Apify](https://apify.com/) token for project 21

## Setup

### 1. Import
n8n → *Workflows → Import from file* → pick any file in [`workflows/`](workflows). Import 01 and 02 first.

### 2. Create credentials (never paste keys into nodes)
All secrets live in **n8n Credentials**. The workflows reference them by name — create these once:

| Credential (type) | Name it | Fields |
|---|---|---|
| Header Auth | `Gemini API Key (Header Auth)` | Name: `x-goog-api-key` · Value: your Gemini key |
| Header Auth | `Qdrant API Key (Header Auth)` | Name: `api-key` · Value: your Qdrant key |
| Header Auth | `Header Auth account` (project 21) | Name: `Authorization` · Value: `Bearer <APIFY_TOKEN>` |
| Google Gemini (PaLM) API | any | Gemini key — used by project 14 |
| Qdrant API | any | Cluster URL + key — used by project 14 |
| Google Sheets OAuth2 / Google Drive OAuth2 | any | OAuth login |

After import, open each node that shows a red credential warning and select the credential you created.

### 3. Point the workflows at your Qdrant cluster
Every Qdrant HTTP node contains the placeholder:

```
https://YOUR-CLUSTER-ID.YOUR-REGION.cloud.qdrant.io:6333
```

Replace it with your cluster URL (Find & replace per workflow is fine). Collection name used everywhere: `workflow-knowledge-basev-2`.

### 4. Create the Qdrant collection and index

```bash
# vector size = output size of gemini-embedding-001 (3072 by default; check `vector_dimension` if unsure)
curl -X PUT "$QDRANT_URL/collections/workflow-knowledge-basev-2" \
  -H "api-key: $QDRANT_API_KEY" -H "Content-Type: application/json" \
  -d '{"vectors": {"size": 3072, "distance": "Cosine"}}'

# required by project 02 (filtered payload update by workflow_name)
curl -X PUT "$QDRANT_URL/collections/workflow-knowledge-basev-2/index" \
  -H "api-key: $QDRANT_API_KEY" -H "Content-Type: application/json" \
  -d '{"field_name": "workflow_name", "field_schema": "keyword"}'
```

### 5. Google Sheets
Tab names and exact column headers for every workflow: [`docs/google-sheets-setup.md`](docs/google-sheets-setup.md). Replace `YOUR_GOOGLE_SHEET_ID` by selecting your spreadsheet in each Sheets node.

### 6. Add your PDFs and run
Put the workflow PDFs in the folder configured in node *Read/Write Files from Disk* of project 01 (default `/home/node/.n8n-files/knowledge-base/workflows/`, change to your path). Then run:

1. **01** — ingest
2. **02** — score (safe to re-run; already-scored workflows are skipped, set `FORCE_REFRESH = true` to redo)
3. Any of **03–14** — edit the requirement in the *Prepare User Request* node and execute

Project 09 needs Gotenberg: `docker run -d -p 3000:3000 gotenberg/gotenberg:8` (use `http://host.docker.internal:3000` if n8n runs in Docker).

## Security

- No keys, tokens, cluster hosts, sheet IDs or personal paths are committed. Run the check before every commit:
  ```bash
  python scripts/check_secrets.py
  ```
- When exporting workflows from n8n, credentials are exported as references only — but **HTTP Request nodes with typed-in keys are not**. Always use *Credentials → Header Auth* as shown above.
- If a key was ever committed, deleting it from the file is not enough: **revoke and rotate it** (it stays in Git history).
- Project 21 scrapes LinkedIn through a third-party actor. Check LinkedIn's and Apify's terms and data-protection law (GDPR etc.) before using it on real people's data.

## Known limitations

- Retrieval returns text **chunks**; the pipeline picks the best chunk and ignores matches below a similarity score of 0.55 (constant `MIN_SCORE` in each *Extract Best Workflow* node).
- Project 14 (agent) cannot see raw similarity scores through the n8n retriever tool, so `match_score` is the model's own estimate.
- Gemini model names (`gemini-3.5-flash-lite`, `gemini-embedding-001`) are set in the nodes — update them if Google renames or retires a model.
- Changing the embedding model requires re-ingesting everything (new vector size / space).

## Repo layout

```
workflows/      n8n workflow JSON exports (sanitised)
docs/           Google Sheets schema
scripts/        check_secrets.py
CHANGES.md      every fix applied to the original exports
```

## License

MIT — see [`LICENSE`](LICENSE).
