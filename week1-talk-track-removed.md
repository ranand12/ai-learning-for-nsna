<!-- Talk track for slides removed from new-week1-fundamentals.html. Appended to week1-talk-track.md by extract-talk-track.py. -->

### Quiz: Offline — Can you run ChatGPT on your laptop with the Wi-Fi off?

**On screen**

- Quick question
- Can you run ChatGPT on your laptop with the Wi-Fi off?
- AYes, it's an app
- BNo, AI needs the cloud
- CNot ChatGPT. Some models, yes.
- It depends on who holds the file of numbers.
- ChatGPT's file never leaves OpenAI. Others hand you the file.
- Your guess?

**Say**

Take a show of hands for A, B and C. Most people pick A or B. Press → to strike the wrong ones, then → again for the reason. That reason is this whole section.

### Vault Vs Zip — A vault, or a zip file.

**On screen**

- Same kind of file, different rules
- A vault, or a zip file.
- Proprietary
- The weights stay on the company's servers. You rent access through their app or API.
- Claude · GPT · Gemini · Grok
- Open weights
- The weights are published. Download them and run them on your laptop, your server or your cloud.
- Llama · DeepSeek · Qwen · Gemma · Mistral · gpt-oss
- "Open weights" isn't the same as open source: you get the finished dials, not the training data or the recipe.

**Say**

Proprietary is a vault. The dials never leave the building, and you pay to send questions in and get answers out. Open weights is a zip file: the company publishes the numbers and you can download and run them yourself. Nuance for the curious: open weights usually doesn't mean open source. You get the trained model, not the data or the training code.

### What Changes — Training looks the same. Everything after it differs.

**On screen**

- What actually changes
- Training looks the same. Everything after it differs.
- Proprietary (vault)
- Open weights (zip)
- Where it runs
- Their servers
- Anywhere you choose
- Your data
- Sent to them
- Can stay on your machine
- You pay for
- Subscription or per-use API
- Your own hardware or cloud
- Top capability
- Usually the frontier
- Close behind, often months
- Customizing
- Limited, on their terms
- Fine-tune it however you like

**Say**

Pre-training and post-training happen the same way either way. The difference is what happens to the file afterwards. The main trade-off is privacy and control versus convenience and peak capability. For most people in this room, proprietary through an app is the right starting point. Open weights starts to matter for sensitive data, offline use, or cost at scale.

### Demo: Offline — Run an AI with the Wi-Fi off.

**On screen**

- Try it
- Run an AI with the Wi-Fi off.
- Install LM Studio or Ollama.
- Download a small open model (e.g. a Gemma, Qwen or Llama ~4–8B).
- Turn off Wi-Fi.
- Ask: Explain what you are in 2 sentences.
- It still answers. The whole "brain" is a file on this laptop.
- Live demo
- Free
- 💃Open model

**Say**

Pre-download the model before the session because it's several gigabytes. Pull the Wi-Fi on stage and it keeps working. That's the moment "open weights" clicks for people. Point out that it's slower and less capable than the frontier models, which is exactly the trade-off from the table.

### Section 03 — Tokens & the context window

**On screen**

- 03
- Tokens & the
- context window
- The single most useful idea today.

**Say**

If you remember one section from today, make it this one. Almost every "why did the AI do that?" moment traces back to it.

### Sticker Legend — Your stickers for the next two weeks

**On screen**

- Watch for these
- Your stickers for the next two weeks
- 💃Model
- The raw brain. Text in, text out.
- Agent harness
- The body around the brain: apps, tools, memory.
- Live demo
- Laptops out. We try it right now.
- Did you know?
- A fact worth repeating at dinner.
- Ask AI
- Don't memorize it. Ask the AI to explain it back.
- Free
- Paid
- What it costs to try this yourself.
- Your guess?
- A question first. Shout an answer, then we reveal it.

**Say**

Green circle with the dancer 💃 means a model, the brain. Blue hexagon means a harness, the app or agent wrapped around the brain. That split matters a lot in part 6. Red means a demo is coming. Purple means I'm going to ask you first: take a guess before I reveal the answer. Wrong guesses are the point; they make the answer stick.

### Section 02 — Proprietary vs open weights

**On screen**

- 02
- Proprietary vs
- open weights
- Who holds the file of numbers?

**Say**

Remember the file of dials? This whole section is about who gets to hold it.

### Dyk: Strawberry — "How many r's are in strawberry?"

**On screen**

- The famous mistake
- "How many r's are in strawberry?"
- A2
- B3
- C4
- So why did older models confidently say 2?
- strawberry
- They never saw the letters, only the chunks.
- Newer "thinking" models spell it out first, so they usually get it right.
- Your guess?
- Did you know?

**Say**

Vote first: A, B or C? It's 3, so press → to mark it. Then ask the real question, why would a smart model say 2, and let people guess before the final →. This is the best example of tokens leaking through. A model that can write a legal brief used to fail at counting letters, because it doesn't see letters. The lesson generalizes: be skeptical of AI for letter counts, exact character limits and precise arithmetic unless it's using a tool.

### Quiz: Where Is It Stored — You told it your name ten messages ago. Where is your name stored right now?

**On screen**

- Quick question
- You told it your name ten messages ago. Where is your name stored right now?
- AIt was learned into the model's dials
- BIn the model's memory
- CNowhere in the model. The app sends the chat again.
- Every turn, the model reads the whole script from scratch.
- Your guess?

**Say**

Most people pick B, and some pick A. Remind them of the frozen dials: that rules out A. Press → to reveal C, then → for the one-liner. The next slide shows what that looks like.

### Demo: Streaming — Same question, different answer. Why?

**On screen**

- Try it
- Same question, different answer. Why?
- Open any chat app (ChatGPT, Claude, Gemini).
- Ask: Write a 6-word story about Mondays.
- Watch it stream, token by token.
- Hit regenerate. Compare.
- Different answers come from the "Pick" step: it samples from the odds instead of always taking the top word.
- Live demo
- Free

**Say**

Run this live. Ask for the story, then hit regenerate two or three times. Ask the room why it changed and take a few guesses before pressing → to reveal. Link it back to the bar chart: it doesn't always take the 62% word, sometimes it takes the 14% one. That randomness is what makes it creative, and also why it's sometimes inconsistent.

###  — That's the app, not the model.

**On screen**

- "But ChatGPT remembers my name!"
- Name: Priya
- Likes: teal
- Job: nurse
- That's the app, not the model.
- The app keeps notes about you and quietly slips them onto the desk at the start of each chat.
- 💃 Green circle = model (no memory).
- Blue hexagon = the app around it (memory, search, files).
- More on this in part 06.
- 💃Model
- Harness

**Say**

Someone always pushes back here, and that's good. Yes, ChatGPT and Claude have memory features. But that memory lives in the app, not the model. The app writes sticky notes about you and pastes them onto the desk before you type. The model is still stateless underneath. This is our first look at the harness, the blue hexagon, and we'll unpack it properly in part 6.

### Demo: Forgetful — The forgetful genius.

**On screen**

- Try it
- The forgetful genius.
- Chat A: My favorite color is teal. Remember that.
- Open a new chat.
- Chat B: What's my favorite color?
- Now try it again with the app's memory turned off (or in a temporary chat).
- If it "remembers", the app put a note on the desk. If it doesn't, you've met the real model.
- Live demo
- Free

**Say**

Results depend on whether memory is on, and either result teaches something. If it remembers, ask: where did that come from? The app's sticky notes. If it doesn't, that's the stateless model. Temporary or incognito chat modes are the cleanest way to show it.

### Checkpoint — If you forget everything else…

**On screen**

- Checkpoint
- If you forget everything else…
- 1
- A model guesses the next token, over and over.
- 2
- Its dials froze after training. It doesn't learn from your chats, and it has a cutoff date.
- 3
- The context window is its only working memory. New chat, empty desk.
- Ask AI
- Homework: ask any AI to "Explain tokens and context windows to me like I'm 12." Up next: 04, how do I get access?

**Say**

Three sentences. If people leave with these, they'll already use AI better than most. The Ask AI sticker is the habit I want: when a concept feels fuzzy, have the AI teach it back to you at your level. Next: how to actually get your hands on Claude, Grok, GPT, DeepSeek and the rest.

### Inference Loop — One token at a time, on a loop.

**On screen**

- What happens when you hit enter
- One token at a time, on a loop.
- ThecapitalofFranceis Paris.Itisknownfor…
- 1 · Read
- Take in everything written so far.
- 2 · Score
- Rate every possible next token.
- 3 · Pick
- Choose one. A bit of randomness is allowed.
- 4 · Repeat
- Stick it on the end and go again.

**Say**

White chips are what you typed. Green chips are what the model writes, one at a time. After each one it re-reads the whole thing and picks the next. That's why answers stream in word by word. It isn't typing for effect; it really does produce text one piece at a time.

### Model ≠ Agent

**On screen**

- 💃 (model, green circle) ≠ 🕵️ (agent, spy in green circle)
- Model ≠ agent

**Say**

Before we go on, one thing people mix up all the time. [Click] This is the model, our dancer: the brain that guesses the next word. [Click] It is not the same thing as [Click] an agent. An agent is the model plus the ability to go and do things for you. People use the words interchangeably; they're not the same. Let's see what an agent actually does.

### Ai Agents

**On screen**

- (Title "AI agents." removed from screen)
- 🧑‍💻 “Find me the cheapest flight and add it to my calendar.”
- Context window
- 🧑‍💻 Cheapest flight → add to calendar
- 💃 Think 💭
- Use tool: 🔍 Search flights
- ✈️ Flight search: 14 flights found
- 🔁 Repeat (tokens loop: context → think → tool → back into context)
- 💃 Best pick: Fri 7am · $89
- Use tool: 📅 Check calendar
- 📅 Calendar: Friday morning is free
- Use tool: 📝 Create event
- ✅ Event created: Fri 7am flight
- Blue dashed frame around everything (context window + model + tools + loop) with the spy icon: = AI agent
- AI agent: same LLM, but now it can do things between answers. It can read files/web/data, use tools/APIs, take actions, see the result, put that result back into its context window, and decide the next step.
- Flow: Goal → Context Window → Think → Use Tool → Result comes back into Context → Think again → Repeat

**Say**

So what's an AI agent? It's the same model, the same LLM we've been talking about all day. The only difference: now it can do things between answers. It can read files, the web or your data, use tools and apps, take actions, see what happened, and decide what to do next. Let's watch one work. [Click] You give it a goal: "Find me the cheapest flight and add it to my calendar." [Click] That goes into the context window, the desk we just talked about. The agent understands your request. [Click] The model thinks: what do I need to do first? [Click] It decides to use a tool: search flights. Strictly speaking, the model can't click anything. It just writes a request, "search flights for Friday", and the app around it runs the tool for it. [Click] And here's the key part: the result comes back into the context window. Fourteen flights, now sitting on the desk. [Click] Then it thinks again, with that new information, and picks the best match: Friday 7am, 89 dollars. That's the loop: context, think, use a tool, result back into context, think again, repeat. [Click] Next tool: check your calendar. [Click] Context updated: Friday morning is free. [Click] Last tool: create the calendar event. [Click] Done. [Click] So what's the agent? It's not the dancer in the middle. The model is still just the brain, called again on every lap of the loop. The agent is the whole package: the model, its desk, its tools, and the app running the loop. We'll draw agents as this guy from now on. Notice it never stopped being a next-word guesser. Everything it learned along the way just landed on its desk as more tokens. Which also means a long task fills up that context window fast.

### Chat Vs Agent — Chat vs agent.

**On screen**

- Chat vs agent.
- 🧑‍💻 “Find me the cheapest flight and add it to my calendar.”
- Left: 💃 (model, green circle) · Chat
- White reply bubble: ✈️ Here are 3 cheap flights. Now go book one yourself.
- 😩 You do the clicking
- Divider
- Right: 🕵️ (agent spy in green circle) · Agent
- 🔁 🔍 → 📅 → 📝 (loop through tools)
- ✅ Booked · on your calendar
- Answers. (left) · Does. (green, right)

**Say**

So let's put the two side by side. [Click] Same request as before: find me the cheapest flight and add it to my calendar. [Click] First, a plain chat. Just the model. [Click] It gives you a nice answer: here are three cheap flights. And then it stops. [Click] You still open the airline site, you still book it, you still open your calendar. You do the clicking. [Click] Now the agent. [Click] It goes round the loop we just saw: search flights, check the calendar, create the event, as many laps as it needs. [Click] And it comes back with the job done: booked, and on your calendar. [Click] That's the whole difference. A chat answers. An agent does. Same brain inside; the agent just keeps going until the task is finished.

### Meet The Agent — Meet the agent.

**On screen**

- Meet the agent.
- 💃 Model (center)
- Context (red context window, left)
- Tools (blue tiles, right): 🔍 📄 ✏️ 📧
- 🔁 Loop (yellow dashed ring spinning around the model)
- Spy icon in green circle: = AI agent
- Agent = Model + Tools + a Loop

**Say**

So let's put the pieces together. [Click] The model. The same dancer we met at the start of today: the file of numbers that guesses the next word. Nothing new. [Click] The context window: its desk, where the goal, the tool results and its own notes pile up. [Click] Tools: the things the app will run for it when it asks. [Click] And the loop: think, act, see, think again, until the job is done. [Click] Put all of that together and that's an AI agent. Model plus tools plus a loop. We'll draw agents as this spy from now on. The thing to remember: it's the same model you met an hour ago. It didn't get smarter. It just got hands and a loop.

### Chat Vs Agent — Chat vs agent.

**On screen**

- Chat vs agent.
- Left: 💃 (model, green circle) · Chat · logos: Claude · ChatGPT · Gemini · Grok
- Divider
- Right: 🕵️ (agent spy in green circle) · Agent · logos: Claude Code · Codex · Antigravity · Hermes
- You run the loop. (left) · It runs the loop. (green, right)

**Say**

So let's name some names. [Click] On one side, chat. [Click] Claude, ChatGPT, Gemini, Grok: you type, it answers. [Click] On the other side, agents. [Click] Claude Code, Codex, Antigravity, Hermes: you give them a goal, and they use tools on your computer until it's done. The lines are blurring: the chat apps keep adding agent features. So don't worry about which box a product sits in. Ask one question. [Click] In a chat, you run the loop. [Click] With an agent, it runs the loop. Same brain inside. That's the whole difference.

### What It Still Can'T Escape — What it still can't escape.

**On screen**

- What it still can't escape.
- Tile 1 (red): haystack-dive GIF · Desk fills up (every tool result lands in the context window; long jobs get messy, lost in the middle)
- Tile 2 (purple): Ghajini GIF · Forgets between chats (still stateless; it only "remembers" by writing notes to a file and reading them back)
- Tile 3 (ice blue): no-internet dino GIF · Cutoff → 🔍 search (still has a knowledge cutoff; a web search tool is how it gets fresh info)
- Tile 4 (yellow): ⚠️ · Ask before it acts (more freedom = more can go wrong; permissions and approvals)

**Say**

An agent is not magic, though. Everything you learned about the model today still applies, because the model inside hasn't changed. [Click] First: the desk fills up. Every search result, every file it reads, lands in the context window. On a long job the desk gets crowded, it gets lost in the middle, and the oldest stuff gets dropped. Same problem as three hours into one chat, just faster. [Click] Second: it's still Ghajini. It's stateless. Close the session and it remembers nothing. When an agent seems to "remember" you, it's because it wrote notes to a file and reads them back next time. [Click] Third: it still has a knowledge cutoff. The difference is, now it can fix that with a tool: give it web search and it can look up today's news. [Click] And fourth, the new one: an agent can actually do things. It can delete a file or send the wrong email. More freedom means more can go wrong. So good agents ask permission before anything risky, and you should keep it that way.
