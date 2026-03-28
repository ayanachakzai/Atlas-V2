# Atlas Speaks

An AI cultural guide to Balochistan and Pakistan — built by Muhammad Ayan Achakzai, filmmaker and cultural storyteller from Quetta, now studying MSc Applied Machine Learning for Creatives at UAL's Creative Computing Institute in London.

Atlas Speaks is not a search engine. It is a conversation. Ask it about myths, music, culture, or just talk. It speaks *from* Balochistan, not about it.

---

## What it does

- **Myth-Busting** — Challenge common misconceptions about Pakistan and Balochistan with verified cultural facts
- **Music Discovery** — A guided questionnaire that recommends Pakistani and Balochi music based on your mood and taste
- **Cultural Comparison** — Compare Pakistan with any country across food, values, family, and more
- **Just Converse** — Free-form chat with Atlas about anything cultural

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Next.js 16 (App Router), Framer Motion, Canvas API |
| Backend | FastAPI (Python) |
| AI | Groq API (LLaMA 3) |
| Fonts | DM Sans, Jersey 10, Humble Nostalgia |
| Deployment | Vercel (frontend), Render (backend) |

---

## Project Structure

```
├── app/
│   ├── page.tsx          # Homepage — globe, mountains, embroidery
│   ├── about/page.tsx    # About the creator
│   └── chat/page.tsx     # Chat interface (4 modes)
├── public/
│   ├── assets/           # Images (Quetta, London)
│   └── fonts/            # Custom font (Humble Nostalgia)
├── main.py               # FastAPI server
├── atlas_speaks.py       # Core chatbot logic + Groq integration
├── data/                 # Cultural knowledge base (JSON)
│   ├── myths_facts_comparisons.json
│   └── music_database.json
└── requirements.txt
```

---

## Running Locally

### Backend

```bash
# Install dependencies
pip install -r requirements.txt

# Create a .env file with your Groq API key
echo "GROQ_API_KEY=your_key_here" > .env

# Start the server
uvicorn main:app --reload --port 8000
```

### Frontend

```bash
cd atlas-v2
npm install

# Create .env.local
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local

npm run dev
```

Open [http://localhost:3000](http://localhost:3000)

---

## Environment Variables

### Frontend (`atlas-v2/.env.local`)
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### Backend (`.env`)
```
GROQ_API_KEY=your_groq_api_key
```

Get a free Groq API key at [console.groq.com](https://console.groq.com)

---

## Deployment

- **Frontend** → [Vercel](https://vercel.com) — import the repo, set `NEXT_PUBLIC_API_URL` to your backend URL
- **Backend** → [Render](https://render.com) — set start command to `uvicorn main:app --host 0.0.0.0 --port 10000`, add `GROQ_API_KEY` as environment variable

---

## The Story

> "I come from a place the world knows mostly through its absence — through what it lacks in headlines, through what gets left out of maps."

Atlas Speaks began as a university project. But somewhere between writing the code and feeding it 205 cultural facts about my home, it became something else. A conversation I had always wanted to have.

Balochistan is not a conflict. It is not a statistic. It is a sunrise over Koh-e-Murdar. It is poetry in Brahui. It is hospitality that does not ask your name before feeding you.

---

*Made in Quetta · Built for the world*
