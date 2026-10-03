# Week 1 — Talk Track

Speaker notes for `new-week1-fundamentals.html`, in slide order. **On screen** is the slide's text (kept even after it's stripped from the slide); **Say** is the talk track. `[Click]` means press → to reveal the next step.

## 1. Title — AI, from zero.

**On screen**

- Week 1 of 2 · Fundamentals
- AI,
- from zero.
- How it actually works, in plain English.

**Say**

Welcome. No prerequisites. By the end of today nobody should feel like AI is magic. It's a machine with a few very specific habits, and once you know them you'll use it far better than most people.

## 2. The Arc — Four building blocks.

**On screen**

- The journey
- Four building blocks.
- Module 1Week 1
- Fundamentals
- Module 2Week 2
- Use AI better
- Module 3Week 3
- Build with AI
- Module 4Week 4
- Think in the age of AI

**Say**

Four building blocks, each one stacks on the last. Week 1: understand the fundamentals. Week 2: use AI better. Week 3: build with AI. Week 4: how to think in the age of AI. [Click] Honestly, we don't know how long each one will take, so let's call them modules instead of weeks.

## 3. How — How?

**On screen**

- How?
- Lots of memes and GIFs
- No jargon
- Won't bog down with technical details

**Say**

How are we going to do this? [Click] Lots of memes and GIFs. A lot. [Click] No jargon. If I use a technical word, I'll explain it in plain English first. [Click] And we won't get bogged down in technical details. No math. You'll understand how it works well enough to use it better, and that's the goal.

## 4. Agenda — The map

**On screen**

- Today · 2 hours
- The map
- 01How a model works20m
- 06Model vs app vs agent harness15m
- 02Proprietary vs open weights10m
- 07Specialized vs general tools10m
- 03Tokens & the context window15m
- 08Skills & MCP10m
- 04How do I get access?10m
- 09AI slop: what makes you different10m
- 05Which model, when?10m
- 10Context engineering10m
- Each hard idea gets followed by a short live demo.

**Say**

Ten stops. The three in green are the foundations, and everything after builds on them. Rule for today: every hard concept gets a short demo right after it, so you see it happen instead of just hearing about it.

## 5. Section 01 — How a model works

**On screen**

- 01
- How a model works
- Two words: training and inference.

**Say**

When people say "the model", they mean one specific thing. Let's pin down what it is.

## 6. Next Word — What word comes next?

**On screen**

- Finish this sentence
- What word comes next?
- The color of the sky is ___ → blue
- blue 62% · grey 14% · clear 10% · black 6% · orange 4%
- The color of the sky at sunset is ___ → orange
- orange 48% · red 21% · pink 14% · purple 9% · gold 5%
- Your guess?
- That's the whole trick: guess the next word.
- Illustrative numbers. It's your phone's autocomplete, trained on a big chunk of the internet.

**Say**

Finish this sentence for me. [Click] "The color of the sky is..." Let the room shout. Everyone says "blue". [Click] Here are the model's odds for the next word. Blue is the favorite, but grey, clear, black and even orange get a slice. These numbers are illustrative. [Click] It picks blue. You just did exactly what the model does. [Click] Now a different version of the same question: "The color of the sky at sunset is..." [Click] Look how the odds shift. Two extra words, "at sunset", and orange jumps from 4% to the top. The model doesn't look anything up; the words before the blank change the odds. [Click] Orange. [Click] That's the whole trick: guess the next word. Given some text, it scores every possible next word and picks one. Then it does it again, and again. Essays, code and poems are all this one step repeated thousands of times. It's your phone's autocomplete, trained on a big chunk of the internet. Keep these bars in mind; they come back when we talk about temperature.

## 7. Training Vs Inference — Training builds the model. Inference uses it.

**On screen**

- Two phases
- Training builds the model. Inference uses it.
- TRAINING
- INFERENCE
- Learning. Months, many millions of dollars, done once.
- Like going to school.
- Using. Seconds, fractions of a cent, every time you hit enter.
- Like sitting the exam.

**Say**

Left side: books, articles and web pages pour in, and out comes the model. That's training. [Click] It's the learning part: months of work and many millions of dollars, and it's done once, in a data center. Like going to school. [Click] Right side: a question goes into the finished model, and an answer comes out. That's inference, the using part. [Click] It takes seconds and costs fractions of a cent, and it happens every time you hit enter. Like sitting the exam. Everything you do in ChatGPT or Claude is inference. You never train the model when you chat with it.

## 8. Training Up Close — Read the library. Then do the job training.

**On screen**

- Training, up close
- Read the library. Then do the job training.
- Pre-training
- Read a huge slice of the internet, books and code. Learn to predict the next word.
- Base model
- Knows a lot. Brilliant autocomplete. No manners, doesn't follow instructions.
- Post-training
- Humans show and rate good answers. It learns to be helpful, honest and safe.
- Assistant
- What you actually talk to: Claude, GPT, Gemini, Grok, DeepSeek…

**Say**

Pre-training is reading the entire library. The result is a base model: it knows a lot, but ask it a question and it might just carry on with more questions, because it's only autocompleting. Post-training is job training. People write example answers and rank responses, and the model learns to behave like an assistant. Much of what makes Claude feel different from GPT comes from this stage.

## 9. Weights — A giant file of numbers.

**On screen**

- What is a "model", physically?
- A giant file of numbers.
- Think billions of tiny dials. They're called weights or parameters.
- Training = turning the dials until the guesses get good.
- After training, the dials are frozen. Chatting with it doesn't change them.
- Open models run from ~1 billion to ~1 trillion dials.

**Say**

What is a model, physically? Strip away the hype and it's a file, a very large file of numbers. Each number is a dial, and they're called weights or parameters. Open models run from about 1 billion to about 1 trillion of them. Right now they're all moving: this is training. [Click] Text runs through the dials and out comes a guess. [Click] We compare that guess with the right answer and send the error backwards through every dial, nudging each one a tiny bit. That's called backpropagation, and it repeats billions of times until the guesses get good. [Click] Then training stops and the dials freeze. Key point: when you chat with it, it isn't learning from you. The dials don't move. Remember "weights"; it comes back in two slides.

## 10. Closed Vs Open — Closed vs open.

**On screen**

- Closed vs open.

**Say**

Here's our frozen model from the last slide. Training is done and the dials are locked. Now the company that made it has a choice: what do they do with this file? [Click] Some lock it up. The weights never leave their servers, and you rent access through their app or API. That's a closed, or proprietary, model. Others open the door and publish the file so anyone can download it. That's an open-weights model. [Click] Where it runs: closed models live inside big companies' data centers, and you visit them over the internet. [Click] Open models can run right here, on your own laptop, even with the Wi-Fi off. [Click] Your data: with a closed model, every file and question you send goes to their servers. With an open model running locally, it never leaves your machine. It even works with no internet at all. [Click] What you pay for: closed means a subscription or per-use API fees to cover their data centers. Open means your own hardware or a cloud you choose, and the model itself is free. [Click] Customizing: with open weights you have the file, so you can fine-tune it on your own data however you like. Closed models give you limited options, on their terms. [Click] Top capability: the closed models are usually the cutting edge. Open models are close behind, often by a few months. So the trade-off is privacy and control versus convenience and peak capability.

## 11. Sort: Closed Or Open — Closed or open?

**On screen**

- Closed or open?
- OpenAI GPT-5.6
- DeepSeek
- All Anthropic models
- Gemini
- Gemma
- Llama
- Qwen
- Mistral

**Say**

Let's sort some. I'll put a name up, you shout "closed" or "open", then I'll move it. [Click] OpenAI's GPT-5.6? [Click] Closed. (OpenAI does also publish a separate open model called gpt-oss.) [Click] DeepSeek? [Click] Open. The Chinese lab that shocked everyone by publishing a top model for free. [Click] Anthropic's Claude models? [Click] All closed. [Click] Gemini? [Click] Closed. Google's flagship. [Click] Gemma? [Click] Open. That's Google too: Gemma is Gemini's open little sibling, so one company can do both. [Click] Llama? [Click] Open, from Meta. [Click] Qwen? [Click] Open, from Alibaba. [Click] Mistral? [Click] Open. A French lab, best known for open models, though it also sells some closed ones. Notice the pattern: closed is the big US labs' flagships, open is a mix of Meta, Chinese labs and Europe.

## 12. Closed Vs Open: How You Use It — Renting a closed model.

**On screen**

- Renting a closed model.
- How does an open model work?

**Say**

Let's zoom in on the closed one. [Click] When you use ChatGPT or Claude, or a developer calls their API, your question travels over the internet to the company's servers. It runs through their frozen model, and the answer comes back to you. That round trip is an API call. [Click] Every one of those trips is inference, and inference is what you pay for. The money goes to the company that owns the model: a monthly subscription, or a fee per token through the API. [Click] Take my money. [Click] Now flip it. How does an open model work? [Click] Same questions, same answers, same arrows. But the model is a file sitting on your own laptop. [Click] So what happened to the company and the money? [Click] Gone. Nobody to pay per question. You're running it on hardware you already own.

## 13. Free? / Bigger File, Bigger Machine — Bigger file, bigger machine.

**On screen**

- "Can I run one?"
- Bigger file, bigger machine.
- ~8B ≈ 5 GB — Laptop, even a phone
- ~30B ≈ 20 GB — Strong laptop / Mac
- ~70B ≈ 40 GB — Workstation, big GPU
- ~670B+ ≈ 400 GB — Data center
- B = billion dials. Rough rule for compressed ("4-bit") models: ~0.6 GB of memory per billion. A rule of thumb, not a spec.

**Say**

So I can run these models for free? [Click] Mostly yes, but the file has to fit on your machine. Bigger file, bigger machine. B means billion dials. Rough rule for compressed, "4-bit" models: about 0.6 GB of memory per billion. A small model, around 8 billion, is about 5 GB and runs on a laptop, even a phone. [Click] Around 30 billion, about 20 GB: a strong laptop or a Mac. [Click] Around 70 billion, about 40 GB: a workstation with a big GPU. [Click] And the giants, 670 billion and up, about 400 GB: that's a data center. [Click] Which is why this man is dancing: every one of those data centers runs on Nvidia chips. Most people run the small ones locally and use the big ones through a hosted service.

## 14. Frozen Model

**On screen**

- (frozen model only)
- Vadivelu thinking (GIF)

**Say**

Back to our frozen model. Closed or open, their data center or your laptop, it's the same thing underneath: one frozen file of numbers. The dials never change. [Click] So here's a puzzle: if the dials never change, why do you get a different answer every time you hit regenerate?

## 15. Temperature

**On screen**

- Temperature.
- The color of the sky is ___
- blue 62% · grey 14% · clear 10% · black 6% · orange 4%
- temperature 1.0 (default)
- temperature 0.0: blue 97% · grey 2% · clear 1% · black 0% · orange 0% → 3 regenerates: blue, blue, blue
- temperature 2.0: blue 30% · grey 22% · clear 19% · black 15% · orange 14% → 3 regenerates: grey, blue, orange

**Say**

The answer is a setting called temperature. It's a dial in every large language model's API, usually from 0 to 2. Same frozen model, same odds; temperature only changes how the next token gets picked. [Click] The color of the sky is... what? [Click] Here are the model's odds for the next word, at the default temperature of about 1. Blue is the favorite, but grey, clear, black and orange all have a chance. The numbers are illustrative. [Click] Set temperature to 0 and the favorite takes over. The model almost always picks the single most likely token. Hit regenerate three times: blue, blue, blue. That's deterministic, the same answer every time. Use it for facts, code and data extraction. [Click] Turn it up to 2 and the odds flatten. Now every word has a real shot, and three regenerates give you grey, blue, orange. That's probabilistic: more varied, more creative, and more likely to go off the rails. Chat apps sit around the middle, which is why regenerate gives you a different answer each time.

## 16. Dyk: Cutoff — Every model has a knowledge cutoff date.

**On screen**

- Frozen dials have a side effect
- Ask it about last week's news. Why does it get it wrong?
- Every model has a knowledge cutoff date.
- What it read in training
- CUTOFF
- Today
- Without web search it can't know what happened after the cutoff, and it may not know that it doesn't know.
- Your guess?
- Did you know?

**Say**

Frozen dials have a side effect. Ask it about last week's news: why does it get it wrong? Someone usually says "it's not connected to the internet", which is half right. Every model has a knowledge cutoff date. [Click] Training: it reads everything up to a certain day. [Click] Then the dials freeze. That's the cutoff. [Click] After that, we only use it: inference, right up to today. Without web search it can't know what happened after the cutoff, and it may not even know that it doesn't know. Anything after that, the model simply never read. That's why "search the web" buttons exist, and why a model will sometimes confidently tell you the wrong CEO or last year's price. Try it: ask any model "What's your knowledge cutoff?"

## 17. Inference Loop — One token at a time, on a loop.

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

## 18. Tokens — They read tokens.

**On screen**

- Models don't read letters or words
- They read tokens: chunks of text.
- unbelievable
- ≈ 4
- characters per token (English)
- of a word per token
- 1,000
- tokens ≈ 750 words ≈ 1½ pages
- Other languages, code and emoji usually take more tokens for the same meaning. Exact splits vary by model.

**Say**

Models don't read letters or words. They read tokens: chunks of text. [Click] And tokens are the currency of AI models. Limits, pricing and memory are all counted in tokens, not words. When you pay per use, you're paying per token. [Click] A token is a chunk, usually part of a word. "Unbelievable" becomes un, believ, able. Common words are a single token, rare words get split up. [Click] In English, a token is about 4 characters, [Click] or roughly three-quarters of a word. [Click] Rule of thumb: a thousand tokens is about 750 words, about a page and a half. Other languages, code and emoji usually take more tokens for the same meaning, and exact splits vary by model.

## 19. Demo: Tokenizer — See your own words get chopped up.

**On screen**

- Try it
- See your own words get chopped up.
- Open tiktokenizer.vercel.app
- Type your full name.
- Type the same sentence in English, then in another language you speak.
- Add an emoji 🎉 and watch the count.
- Live demo
- Free

**Say**

Names are fun because unusual names get split into strange pieces. The other-language comparison usually gets a reaction: the same meaning can cost two or three times as many tokens. That means non-English users hit limits sooner and pay more.

## 20. Context Window — The context window.

**On screen**

- The context window
- Everything it can see right now
- Hidden instructions from the app
- You: "Summarize this report"
- 📄 The 40-page PDF you pasted
- AI: "Here are the 5 key points…"
- You: "Now make it shorter"
- The model's desk.
- The model only works with what's on the desk. Your messages, its replies, your files, the app's instructions: it's all tokens, and it all takes up space.
- Frontier desks today: roughly 200K to 1M+ tokens.
- 200K tokens ≈ 150,000 words ≈ 500 pages.

**Say**

This is the context window, the model's desk. [Click] The box is everything the model can see right now; the gauge shows how full it is. The model only works with what's in this box. Anything outside doesn't exist for it. [Click] This box is the context window. [Click] Before you type anything, the app puts its own hidden instructions in. Those are tokens too. [Click] You: "Summarize this report." A few tokens. [Click] Then the 40-page PDF you pasted. Look how much space that takes. [Click] The AI's reply: "Here are the 5 key points…" Its own answer goes in the box too. [Click] You: "Now make it shorter." Every message, every reply, every file: it's all tokens, the coins we talked about, and it all takes up space. Frontier desks today hold roughly 200K to 1M+ tokens; 200K is about 150,000 words, or 500 pages. Big, but not infinite.

## 21. Stateless — Stateless.

**On screen**

- The surprising part
- The model remembers nothing between turns.
- Turn 1: You 1 → model
- Turn 2: You 1, AI 1, You 2 → model
- Turn 3: You 1, AI 1, You 2, AI 2, You 3 → model
- New chat: empty desk → model: "Who are you?"
- The app re-sends the whole conversation every time. One session never leaks into the next.
- Stateless.
- Model = Ghajini (GIF)

**Say**

This surprises almost everyone. The model has no memory. [Click] Turn 1: you send a message. [Click] Turn 2: the app bundles up the entire conversation so far, puts it all in the context window, and sends all of it again. [Click] Turn 3: again, the whole script. It feels like a conversation, but the model is reading everything fresh each time. [Click] Open a new chat and the desk is empty. It has never met you. [Click] The model is Ghajini: no short-term memory, so it relies on the notes you hand it, and every turn it reads them from scratch.

## 22.  — That's the app, not the model.

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

## 23. Desk Fills Up — Three hours into one chat.

**On screen**

- When the desk fills up
- Three hours into one chat.
- Three hours into one chat. Is it sharper now, or sloppier?
- Your guess?
- Sloppier. Long chats get worse, not better.
- Oldest gets dropped
- Or squashed into a summary. Early details quietly disappear.
- Every turn costs more
- It re-reads the whole desk each time. Slower, and it burns through your limits.
- Lost in the middle
- It pays most attention to the start and the end. The middle blurs.
- We'll fix this in part 10, context engineering.

**Say**

Three hours into one chat. [Click] You've been at it all night, like a phone call that never ends. Ask it straight: is it sharper now, or sloppier? Most people assume it's gotten to know them. Answer: sloppier. Long chats get worse, not better. Three things go wrong on a full desk. [Click] One: [Click] the oldest stuff gets dropped, or squashed into a summary, which is why it "forgets" what you said an hour ago. [Click] Two: [Click] every turn costs more. It re-reads the whole desk each time, so it gets slower and you hit usage limits sooner. [Click] Three, the sneaky one: [Click] lost in the middle. Models pay most attention to the beginning and end, and the middle blurs. Imagine one sticky note tucked into a thousand-page book. We'll fix this in part 10, context engineering.

## 24. Demo: Forgetful — The forgetful genius.

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

## 25. Checkpoint — If you forget everything else…

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

## 26. Subscription Vs Tokens — Subscription or pay per token?

**On screen**

- Should I choose subscription or pay per tokens?
- Netflix (subscription) vs tokens (pay per use) (GIFs)

**Say**

Should you pay for a subscription or pay per token? There are two approaches. [Click] A subscription works like Netflix: one flat monthly fee, and you use it as much as the plan allows. [Click] Pay per token is a meter: through the API you pay for exactly the tokens you send and get back. If you're starting out, always prefer the subscription: the cost is predictable and you won't get a surprise bill. And if you had to pick just one, choose Codex or Claude Code. You can't go wrong with either.

## 27. Worth Paying? — Is it worth paying?

**On screen**

- Is it worth paying?
- Counting money (Santhanam) vs Vadivelu (GIFs)

**Say**

Is it worth paying? [Click] Option one: hold on to your money and stick with the free tiers. [Click] Option two: pay for a plan. [Your punchline for the Vadivelu GIF goes here.]


---

## Removed slides

_Kept for reference; these slides are no longer in the deck._

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
