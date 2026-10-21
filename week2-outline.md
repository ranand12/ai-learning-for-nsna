# Week 2 · Use AI better: outline

Goal: move from "asking a chatbot questions" to using AI to learn, research, think, create and delegate.
Outcome: someone who stops after Week 2 can still learn, research, verify, organize AI work and hand off useful tasks.

Source: `GenAI_4_Week_Training_Agenda.docx` (Week 2 has 10 "Better" topics). Grouped here into **6 stops** (Week 1 had 5; delegation got its own stop).
Format: 4 hours, about 40% concepts and 60% demos and hands-on. Every stop ends with a live demo and one pattern to take home.
**Tool cards:** each time a tool is introduced (Gemini Notebook in Stop 2, Perplexity + Deep Research in Stop 3, AI Studio in Stop 4), a small card for it drops into a "toolbox" in the corner. Stop 6 tips the toolbox out onto the final map.

---

## Opening (~15 min)

1. **Title**: "Use AI better." The 💃 is back, with a 🎓 or 🛠️.
2. **The arc**: the same four building blocks as Week 1, with Module 2 lit up.
3. **Week 1 in 60 seconds**: recap cards flip one per click: frozen 💃 · closed vs open · tokens · desk fills up · Ghajini (stateless) · spy agent.
4. **The shift**: "Google gives you links. AI gives you a collaborator." Ask about the difference: you search Google, but you *brief* AI.
5. **The map**: 6 pins, one per click (below).

---

## Stop 1 · Ask better (~40 min)
*Docx §1. Builds on Week 1: the model only knows what's on the desk.*

- **"It can't read your mind"**: a vague prompt goes in and generic slop comes out. Use a mind-reader meme GIF.
- **The brief**: four cards drop onto the desk (the context window from Week 1), one per click: 🎯 Goal · 📎 Context · 🚧 Constraints · 📄 Output format.
- **Show, don't describe**: one example beats a paragraph of instructions. Show one example vs a wall of text.
- **"Ask me questions first"**: 💃 replies with "?" pills before it answers.
- **No magic prompt**: iterate. A loop icon cycles through v1 → v2 → v3 and the output improves each time.
- **Demo / hands-on**: take a weak prompt, upgrade it live in 3 rounds, and compare the results.

## Stop 2 · Learn & understand better (~45 min)
*Docx §2 + §4*

- **Explain it like I'm 5 → 15 → expert**: a depth dial on the same topic.
- **Make it quiz you (Socratic)**: the arrows reverse, so 💃 asks and you answer.
- **"What am I missing?"**: AI finds the gaps in your understanding.
- **Learn from *your* stuff**: PDFs, videos, screenshots and spreadsheets go into the desk. Introduce **Gemini Notebook** (formerly NotebookLM, renamed July 2026).
- **Beyond "summarize this"**: a messy pack turns into FAQ · timeline · study guide · action items. Cards flip one per click.
- **Demo / hands-on**: learn an unfamiliar topic in Gemini Notebook, then explain it back in your own words.

## — Break (10 min) —

## Stop 3 · Research better (~40 min)
*Docx §3. Builds on Week 1: the knowledge cutoff.*

- **Four ways to ask**: from memory (frozen 💃, cutoff) → web search (🔍 tool) → AI search (Perplexity) → deep research (the spy agent loops for minutes). The ladder reveals one rung per click.
- **Start with a plan**: ask AI for a research plan before you ask for answers.
- **Fact · inference · opinion**: three colour-coded buckets, and claims get sorted into them, like Week 1's closed/open sort.
- **Citations can lie**: a fake-citation meme. Verify important claims at the source.
- **Demo**: the same question in normal chat, then Perplexity, then Deep Research. Compare how each one works and what it returns.

## Stop 4 · Think & create better (~45 min)
*Docx §5 + §6 + §7*

- **Brainstorm, then judge**: lots of ideas → a scored shortlist against clear criteria.
- **Devil's advocate**: "Give me the strongest argument against my plan."
- **Pre-mortem**: "It's 6 months later and this failed. Why?"
- **Two models, two jobs**: 💃 A generates and 💃 B critiques. The second model reviews the first.
- **Rough → polished**: notes → doc, plan, deck. Rewrite the same content for a 10-year-old vs a CEO.
- **Make something you've never made**: ask for the process first, then build the smallest version. Introduce Google AI Studio.
- **AI as coach**: practise an interview or a hard conversation, and get feedback from AI as an editor.
- **Hands-on**: a realistic decision worked through with generate + critique.

## Stop 5 · Organize & reuse (~30 min)
*Docx §8 + §9. Builds on Week 1: stateless and the context window.*

- **Stop living in 300 chats**: a messy chat sidebar vs tidy project folders (Projects / Gems / custom instructions).
- **Handoff summary**: Ghajini again. Before you start a new chat or switch models, ask for a summary so you aren't starting from zero.
- **The reuse ladder**: prompt → saved template → skill → agent. Climb one rung per click.
- **Introducing: Skills** (the "skill" rung of the ladder):
  - **What it is:** a saved recipe card, meaning instructions + examples + files for one task ("how we write our newsletter", "how I want expense reports done"). The AI pulls it out **only when the task comes up**.
  - **Visual:** a shelf of recipe cards beside the desk. A request comes in, the right card slides onto the desk (the Week 1 context window), and the other cards stay on the shelf. *Callback:* the desk stays clean because the cards don't fill it until they're needed.
  - **vs a saved prompt:** you paste a prompt yourself every time, but the AI picks the right skill on its own.
  - **Where you'll see it:** Claude Skills, custom GPTs, Gemini Gems (close cousins). How to build your own → Week 3.
  - **Demo:** a "write it in my style" skill. Ask the same thing with and without it and compare.
- **Hands-on**: set up one AI project (instructions + sources) for a real piece of work.

## Stop 6 · Pick the right tool (~60 min)
*Docx §10 + "choose tools". Builds on Week 1: the spy agent and "you are the loop".*
**Goal:** everyone leaves knowing *which tool for which job*, what each tool actually does, and how it differs from the others.

### Part A · Two families: specialists vs general-purpose
**Metaphor:** a specialist doctor vs your family doctor. The family doctor handles almost anything, and the specialist does one thing extremely well.

| | **Specialized tools / agents** | **General-purpose agents** |
|---|---|---|
| What it is | Built for **one job** | **One assistant, any job** |
| Strength | Best result for that job, with the workflow already built in | Flexible. One place for everything |
| Weakness | Useless outside its job | You have to steer it more, and it's "good" rather than "best" at specialist jobs |
| Examples | Gemini Notebook (learn from your sources), Perplexity (web answers with sources), Deep Research (long reports), AI Studio (try out and prototype), Claude Code / Codex (code → Week 3) | ChatGPT, Claude, Gemini, along with their agent modes (ChatGPT Work, Claude Cowork) |

Slides:
- **Two families**: the stage splits. 🩺 Specialists on the left, 💃 general-purpose on the right. Tool cards from the toolbox fly to the correct side, one per click.
- **Specialist close-ups**: one slide each, shown the same way every time (**What it does · What makes it different · Use it when**):
  - **Gemini Notebook**: only answers from *your* sources, and every claim links back to the exact spot it came from. It can turn them into an audio "podcast", video, quiz or flashcards. *vs ChatGPT with an uploaded file:* the chat mixes in what it already knows. Gemini Notebook stays strictly inside your sources.
  - **Perplexity**: an AI search engine that gives a quick answer from the live web with sources. Seconds, not minutes.
  - **Deep Research** (ChatGPT / Gemini / Claude): the spy agent goes off for 5–30 minutes, reads hundreds of pages and comes back with a long cited report. *vs Perplexity:* a quick answer vs a full report.
  - **Google AI Studio**: a playground for trying models and building quick prototypes. A bridge to Week 3.
- **Same question, three tools**: one question, three columns (chat · Perplexity · Deep Research). Each column reveals its time taken, number of sources and length of answer. This makes the difference visible.

### Part B · The general-purpose spectrum: how much access?
**The idea:** a general-purpose assistant can sit at different levels. Each step up, the 🕵️ gets **more access**, you watch it **less**, and there's **more risk**.
**The same example at every level:** *"Do my monthly expense report."*
**MCP is introduced at Level 2**, the moment the agent first reaches into your apps (see the slide below).

| Level | Where it lives | What it can touch | Example product | Expense report |
|---|---|---|---|---|
| **0 · Chat** | The chat window | Only what you paste | ChatGPT / Claude / Gemini chat | Tells you the steps. *You* do everything. |
| **1 · Chat + tools** | A sandbox inside the chat | Uploads, web search, code | ChatGPT / Claude with files | You upload receipt photos and get a spreadsheet back. |
| **2 · Coworker** | The desktop app | The folders and apps you connect | **ChatGPT Work**, **Claude Cowork** | Reads your Receipts folder and Gmail, builds the Excel file, drafts the email to finance. |
| **3 · Takes over your Mac** | Your actual screen | *Any* app: it points, clicks, types | Computer Use in Cowork / ChatGPT Work | Fills in the clunky company expense site that has no connection to AI. |
| **4 · Its own cloud computer** | A computer in the cloud, always on | Its own browser + the logins you give it | OpenAI **dots**, Cowork cloud/scheduled tasks, Manus, Gemini Spark | Does the report on the 1st of every month with your laptop closed, then pings you: "Approve?" |

Slides:
- **The ladder**: the 🕵️ climbs one level per click: 💬 → 📦 → 📁 → 🖥️ → ☁️.
- **One slide per level**: the same 🧑‍💻 request each time, lines out to what the agent can reach, then the result, with a product logo strip.
- **Introducing: MCP (connectors)**, between Level 2 and Level 3:
  - **The question:** "How does Cowork actually get into my Gmail?"
  - **What it is:** **MCP (Model Context Protocol)** is one standard plug that lets any AI connect to any app. In the apps it shows up as **"Connectors"**.
  - **Visual:** a USB-C metaphor. *Before:* a tangle of different cables, a custom one for every AI × every app. *After:* one universal port. Then the 🕵️ plugs into Gmail · Drive · Calendar · Slack · Notion, one per click. *Callback to Week 1's "Give it tools":* MCP is how tools get plugged in.
  - **Leads into Level 3:** "No connector for your company's expense site? Then the agent has to click through the screen like a human." That's Level 3.
  - **Safety, in one line:** only plug in apps you trust, because a connector is a key to that app.
  - **Demo:** turn on the Gmail or Calendar connector in Claude or ChatGPT and ask about your actual week.
- **Agent = model + tools + skills + loop**: the Week 1 spy formula gets updated. Tools come in through MCP connectors, skills come from the recipe shelf, and both cards land on the spy one per click.
- **Your Mac vs a cloud computer**: on your Mac it reaches your files and company sites, but the laptop must stay awake and nothing stands between it and your stuff. In the cloud it works while you sleep and you can start it from your phone, but you hand over your logins. Use a GIF for each.
- **The trade-off dial**: 🔑 access ↑ · 😴 how much you watch it ↓ · ⚠️ risk ↑.
- **When *not* to hand it off**: ✋ it asks first before anything that spends money, sends something to other people or deletes things. "A webpage can trick it" (prompt injection, in one line).

### Part C · Which tool when (the payoff)
- **The "I want to…" map**: the toolbox tips out and every tool lands on its job, one per click.

| I want to… | Use | Why this one |
|---|---|---|
| Ask, draft, brainstorm, rewrite | General chat (ChatGPT / Claude / Gemini) | Fast and flexible. Good enough for most things |
| Learn from **my** documents, videos, notes | **Gemini Notebook** | Stays inside your sources and points to the exact spot each answer came from |
| A quick answer on something **current** | **Perplexity** | Live web, sources, seconds |
| A **deep report** on a big question | **Deep Research** | Reads hundreds of pages, cited report, takes minutes |
| A finished file (deck, sheet, doc) or work across my apps and folders | **ChatGPT Work / Claude Cowork** | Works with your actual files and apps |
| A website or app with no AI connection | Computer Use (level 3) | Clicks through it like you would |
| Something **recurring** or overnight | Cloud agents (level 4) | Runs with your laptop closed |
| Try an idea or a prototype | **Google AI Studio** | Playground for testing ideas |
| Write code | Claude Code / Codex | → Week 3 |
| Make the AI do a task **my way, every time** | A **skill** | A saved recipe card, picked up automatically |
| Let the AI reach **my apps** (Gmail, Drive, Slack) | Turn on a **connector (MCP)** | One standard plug into each app |

- **The decision flowchart** (one question per click):
  1. Is it about **my own** documents? → Gemini Notebook
  2. Does it need **fresh info from the web**? → quick: Perplexity · deep: Deep Research
  3. Does it need to **do things** in my apps or files? → Coworker (level 2) → no connection: level 3 → recurring: level 4
  4. Anything else → general chat
- **Quiz: "Which tool?"**: show 6 real tasks. The audience shouts out an answer, then the task flies to its tool, like Week 1's closed/open sort.
- **Demo**: one task climbing three levels live: chat → ChatGPT Work or Claude Cowork on a folder → a scheduled cloud task.

---

## Wrap (~20 min)

- **Recap**: 6 cards flip, one per stop. The Stop 5 card shows 🃏 Skills and the Stop 6 card shows 🔌 MCP.
- **Your homework**: pick one weekly task and redesign it with AI. (Docx §7 "Work better" hands-on.)
- **Next week**: "Build with AI" (Week 3 teaser: APIs, tools, building your own skills and MCP connections).

---

## Open questions for Anand

1. Is 6 stops the right grouping, or do you want all 10 "Betters" as their own stops?
2. Stop 6: is a single running example (expense report) right, or do you want a different example for each level? Which products will you actually demo live (depends on what you have access to)?
3. Which tools do you want to demo live (Gemini Notebook, Perplexity, Deep Research, AI Studio, Claude Code)?
4. Should the old `week2-use-better.html` (59 slides, old text-heavy style) be mined for content, or should we start fresh as `new-week2-use-better.html`?
