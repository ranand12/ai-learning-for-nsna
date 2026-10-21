# Week 2 · Use AI better: outline

Goal: move from "asking a chatbot questions" to using AI to learn, research, think, create and delegate.
Outcome: someone who stops after Week 2 can still learn, research, verify, organize AI work and hand off useful tasks.

Source: `GenAI_4_Week_Training_Agenda.docx` (Week 2 has 10 "Better" topics). Grouped here into **6 stops** (Week 1 had 5; delegation got its own stop).
Format: 4 hours, about 40% concepts and 60% demos and hands-on. Every stop ends with a live demo and one pattern to take home.

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
- **Learn from *your* stuff**: PDFs, videos, screenshots and spreadsheets go into the desk. Introduce NotebookLM.
- **Beyond "summarize this"**: a messy pack turns into FAQ · timeline · study guide · action items. Cards flip one per click.
- **Demo / hands-on**: learn an unfamiliar topic in NotebookLM, then explain it back in your own words.

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

## Stop 5 · Organize & reuse (~25 min)
*Docx §8 + §9. Builds on Week 1: stateless.*

- **Stop living in 300 chats**: a messy chat sidebar vs tidy project folders (Projects / Gems / custom instructions).
- **Handoff summary**: Ghajini again. Before you start a new chat or switch models, ask for a summary so you aren't starting from zero.
- **The reuse ladder**: prompt → saved template → skill → agent. Climb one rung per click.
- **Hands-on**: set up one AI project (instructions + sources) for a real piece of work.

## Stop 6 · Delegate better: the agent levels (~50 min)
*Docx §10. Builds on Week 1: the spy agent and "you are the loop".*

**The idea:** "agent" isn't one thing. It's a ladder. Each rung gives the 🕵️ **more access** and you **less babysitting**, and it adds **more risk**.
**One running example on every rung:** *"Do my monthly expense report."* The audience sees the same job get more and more hands-off.

| Level | Where the agent lives | What it can touch | Example product | Expense-report example |
|---|---|---|---|---|
| **0 · Chat** | Inside the chat window | Only what you paste | ChatGPT / Claude / Gemini chat | Tells you the steps. *You* do everything. |
| **1 · Chat + tools** | A sandbox inside the chat | Files you upload, web search, code | ChatGPT / Claude with file upload | You upload receipt photos and get a spreadsheet to download. |
| **2 · Coworker** | The desktop app on your computer | Folders and apps you connect (Gmail, Drive, Calendar) | **ChatGPT Work**, **Claude Cowork** | Reads your Receipts folder + Gmail, builds the Excel file, drafts the email to finance. |
| **3 · Takes over your Mac** | Your actual screen | *Any* app: it points, clicks and types like you | Computer Use in Claude Cowork / ChatGPT Work | Logs into the clunky company expense portal (no connector) and fills in every field. |
| **4 · Its own cloud computer** | A computer in the cloud, always on | Its own browser + the logins you give it | OpenAI **dots**, Cowork cloud/scheduled tasks, Manus, Gemini Spark | On the 1st of every month, while your laptop is closed, it does the whole report and pings you: "Approve?" |
| *Side branch · Coding agents* | Your code folder / terminal | Code, commands, tests | Claude Code, Codex | → Week 3 |

Slides (one click per element):
- **"Agent" is a ladder**: a staircase with 5 rungs. The 🕵️ climbs one rung per click, and each rung lights up with its "where it lives" icon: 💬 chat bubble → 📦 sandbox box → 📁 your folders → 🖥️ your whole Mac → ☁️ a cloud computer.
- **One slide per level**: the same 🧑‍💻 asks "Do my expense report". Show what the agent can reach (lines out to the apps and folders it can touch), then the result. A small product-logo strip at the bottom.
- **Your Mac vs a cloud workstation** (side by side, after Level 4):
  - Your Mac: 💻 with the 🕵️ inside. It can reach your company's internal sites and your files, but the laptop must stay on and awake, and there's no wall between it and your stuff.
  - Cloud: ☁️🖥️ with the 🕵️ inside. It works while you sleep and you can start it from your phone, but it starts from nothing, so you hand over your logins.
  - Use a GIF for each (to be picked).
- **The trade-off dial**: three bars rise as you climb the ladder: 🔑 access ↑ · 😴 babysitting ↓ · ⚠️ risk ↑.
- **When *not* to delegate**: ✋ approval gate. Anything that spends money, sends to other people or deletes things → the agent asks first. Mention prompt injection in one line, plainly: "a webpage can trick it".
- **Which rung for which job?**: an audience quiz. Show 4 tasks and have the audience call out the level, then the answer moves to its rung, like Week 1's closed/open sort.
- **Demo**: the same task climbing three rungs live: Chat → ChatGPT Work or Claude Cowork on a folder → a scheduled cloud task.

---

## Wrap (~20 min)

- **Recap**: 6 cards flip, one per stop.
- **Your homework**: pick one weekly task and redesign it with AI. (Docx §7 "Work better" hands-on.)
- **Next week**: "Build with AI" (Week 3 teaser: APIs, tools, MCP).

---

## Open questions for Anand

1. Is 6 stops the right grouping, or do you want all 10 "Betters" as their own stops?
2. Agent levels: is a single running example (expense report) right, or do you want a different example for each level? Which products will you actually demo live (depends on what you have access to)?
3. Which tools do you want to demo live (NotebookLM, Perplexity, Deep Research, AI Studio, Claude Code)?
4. Should the old `week2-use-better.html` (59 slides, old text-heavy style) be mined for content, or should we start fresh as `new-week2-use-better.html`?
