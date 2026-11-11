# Changes made before publishing

Security clean-up and bug fixes applied to the original exports. Node names are in `code`.

## Project 01
- `Read/Write Files from Disk` — Personal Windows path replaced with portable path
- `HTTP Request` — Gemini key removed from URL/query -> Header Auth credential
- `Qdrant Upsert` — Qdrant api-key removed -> Header Auth credential; host placeholder
- `Code (Build Qdrant Payload)` — Point-ID collision fixed (char-code sum -> deterministic UUID); nested metadata added for the Agent project
- `Code Chunk` — Exact total_chunks; no duplicate tail chunk
- `Code (Smart Metadata)` — Category detection uses whole-word match for short keywords (hr/seo/rag/crm)

## Project 02
- `HTTP Request (Gemini)` — Gemini key removed from URL/query -> Header Auth credential
- `HTTP Request (Qdrant Upsert)` — Qdrant api-key removed -> Header Auth credential; host placeholder
- `Qdrant Scroll` — Qdrant api-key removed -> Header Auth credential; host placeholder
- `Code (Group Chunks By Workflow)` — Was: first chunk only + vectors. Now: all chunks grouped, already-scored workflows skipped, refuses partial (>5000) scroll
- `Code (Extract + Validate AI Data)` — Values clamped/validated; failed Gemini call is skipped instead of crashing the loop
- `HTTP Request (Qdrant Set Payload)` — Was: re-uploading whole point + vector. Now: set_payload by workflow_name filter (all chunks, no vectors transferred)
- `HTTP Request (Gemini)` — Gemini JSON mode forced (responseMimeType)

## Project 03
- `HTTP Request Qdrant Search` — Qdrant api-key removed -> Header Auth credential; host placeholder
- `Code (Extract Top Workflow)` — Min-score guard + market data looked up across chunks (was: blindly used top chunk)
- `Code (Extract JSON)` — JSON extraction tolerant to extra text
- `HTTP Request Gemini Embedding API1` — Gemini key removed from URL/query -> Header Auth credential
- `HTTP Request (Gemini)` — Gemini key removed from URL/query -> Header Auth credential
- `HTTP Request (Gemini)` — Gemini JSON mode forced (responseMimeType)

## Project 04
- `Code (Extract Proposal JSON)` — JSON extraction tolerant to extra text
- `HTTP Request Gemini Embedding API1` — Gemini key removed from URL/query -> Header Auth credential
- `HTTP Request Qdrant Search` — Qdrant api-key removed -> Header Auth credential; host placeholder
- `Code (Extract Top Workflow)1` — Min-score guard + market data looked up across chunks (was: blindly used top chunk)
- `HTTP Request (Gemini)` — Gemini key removed from URL/query -> Header Auth credential
- `Code (Generate HTML)` — Was disconnected (never ran) + injected raw LLM text into HTML. Now wired after proposal JSON, escaped, brand configurable
- `HTTP Request (Gemini)` — Gemini JSON mode forced (responseMimeType)

## Project 05
- `HTTP Request Gemini Embedding API1` — Gemini key removed from URL/query -> Header Auth credential
- `HTTP Request Qdrant Search` — Qdrant api-key removed -> Header Auth credential; host placeholder
- `HTTP Request (Gemini 3.5 Flash Lite)` — Gemini key removed from URL/query -> Header Auth credential
- `Code (Extract Workflow JSON)` — JSON extraction tolerant to extra text
- `Code (Extract Best Workflow)` — Min-score guard + market data looked up across chunks (was: blindly used top chunk)
- `HTTP Request (Gemini 3.5 Flash Lite)` — Gemini JSON mode forced (responseMimeType)

## Project 06
- `HTTP Request Gemini Embedding API1` — Gemini key removed from URL/query -> Header Auth credential
- `HTTP Request Qdrant Search` — Qdrant api-key removed -> Header Auth credential; host placeholder
- `Code (Extract Best Workflow)` — Min-score guard + market data looked up across chunks (was: blindly used top chunk)
- `HTTP Request (Gemini 3.5 Flash Lite)` — Gemini key removed from URL/query -> Header Auth credential
- `Code (Extract Consultant JSON)` — JSON extraction tolerant to extra text
- `HTTP Request (Gemini 3.5 Flash Lite)` — Gemini JSON mode forced (responseMimeType)

## Project 07
- `HTTP Request Gemini Embedding API1` — Gemini key removed from URL/query -> Header Auth credential
- `HTTP Request Qdrant Search` — Qdrant api-key removed -> Header Auth credential; host placeholder
- `Code (Extract Best Workflow)` — Min-score guard + market data looked up across chunks (was: blindly used top chunk)
- `HTTP Request (Gemini 3.5 Flash Lite)` — Gemini key removed from URL/query -> Header Auth credential
- `HTTP Request (Gemini 3.5 Flash Lite)` — Gemini JSON mode forced (responseMimeType)

## Project 08
- `HTTP Request Gemini Embedding API1` — Gemini key removed from URL/query -> Header Auth credential
- `HTTP Request Qdrant Search` — Qdrant api-key removed -> Header Auth credential; host placeholder
- `Code (Extract Best Workflow)` — Min-score guard + market data looked up across chunks (was: blindly used top chunk)
- `HTTP Request (Gemini 3.5 Flash Lite)` — Gemini key removed from URL/query -> Header Auth credential
- `HTTP Request (Gemini 3.5 Flash Lite)` — Gemini JSON mode forced (responseMimeType)

## Project 09
- `HTTP Request Gemini Embedding API1` — Gemini key removed from URL/query -> Header Auth credential
- `HTTP Request Qdrant Search` — Qdrant api-key removed -> Header Auth credential; host placeholder
- `Code (Extract Best Workflow)` — Min-score guard + market data looked up across chunks (was: blindly used top chunk)
- `HTTP Request (Gemini 3.5 Flash Lite)` — Gemini key removed from URL/query -> Header Auth credential
- `Code (Extract Documentation JSON)` — JSON extraction tolerant to extra text
- `Code (Generate HTML)` — HTML-escapes model output (XSS/HTML injection into the PDF renderer)
- `Upload file` — Filename bug "=={{...}}" (leading "=") fixed + illegal characters stripped
- `HTTP Request (Gemini 3.5 Flash Lite)` — Gemini JSON mode forced (responseMimeType)

## Project 10
- `HTTP Request Gemini Embedding API1` — Gemini key removed from URL/query -> Header Auth credential
- `HTTP Request Qdrant Search` — Qdrant api-key removed -> Header Auth credential; host placeholder
- `Code (Extract Best Workflow)` — Min-score guard + market data looked up across chunks (was: blindly used top chunk)
- `HTTP Request (Gemini 3.5 Flash Lite)` — Gemini key removed from URL/query -> Header Auth credential
- `HTTP Request (Gemini 3.5 Flash Lite)` — Gemini JSON mode forced (responseMimeType)

## Project 11
- `HTTP Request Gemini Embedding API1` — Gemini key removed from URL/query -> Header Auth credential
- `HTTP Request Qdrant Search` — Qdrant api-key removed -> Header Auth credential; host placeholder
- `HTTP Request (Gemini 3.5 Flash Lite)` — Gemini key removed from URL/query -> Header Auth credential
- `Code (Extract Top 5 Workflows)` — Top-5 were often 5 chunks of the same workflow; now deduped per workflow (search limit 30 chunks)
- `HTTP Request (Gemini 3.5 Flash Lite)` — Gemini JSON mode forced (responseMimeType)

## Project 13
- `HTTP Request Gemini Embedding API1` — Gemini key removed from URL/query -> Header Auth credential
- `HTTP Request Qdrant Search` — Qdrant api-key removed -> Header Auth credential; host placeholder
- `HTTP Request (Gemini 3.5 Flash Lite)` — Gemini key removed from URL/query -> Header Auth credential
- `Code (Extract Top 5 Workflows)` — Top-5 were often 5 chunks of the same workflow; now deduped per workflow (search limit 30 chunks)
- `HTTP Request (Gemini 3.5 Flash Lite)` — Gemini JSON mode forced (responseMimeType)

## Project 14
- `Qdrant Vector Store` — Wrong collection (old v1) + payload keys fixed so workflow_name metadata is actually readable
- `Embeddings Google Gemini` — Embedding model pinned to gemini-embedding-001 (must match the model used at ingestion, otherwise vector size mismatch)
- `AI Agent` — "No match" case now returns schema-valid JSON instead of breaking the structured parser

## Project 21
- `Rename for Google Sheet` — Processes all batch items, keeps sheet URL for row matching, flags failed profiles
- `Only rows not yet enriched` — NEW: skips rows already enriched (stops paying Apify twice)
- `IF Profile Found` — NEW: a failed profile no longer breaks/overwrites rows or stalls the loop
