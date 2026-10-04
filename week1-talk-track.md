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

Four building blocks, each one stacks on the last. [Click] Week 1: understand the fundamentals. [Click] Week 2: use AI better. [Click] Week 3: build with AI. [Click] Week 4: how to think in the age of AI. [Click] Honestly, we don't know how long each one will take, so let's call them modules instead of weeks.

## 3. How — How?

**On screen**

- How?
- Lots of memes and GIFs
- No jargon
- Won't bog down with technical details

**Say**

How are we going to do this? [Click] Lots of memes and GIFs. A lot. [Click] No jargon. If I use a technical word, I'll explain it in plain English first. [Click] And we won't get bogged down in technical details. No math. You'll understand how it works well enough to use it better, and that's the goal.

## 4. Expectations — Expectations

**On screen**

- Expectations
- Ask a lot of questions (me-pick GIF)
- Interact (a bit more interactive GIF)
- Camera on, if possible (camera on GIF)

**Say**

A few expectations from my side. [Click] Ask a lot of questions. There are no dumb questions here; if you're wondering about it, someone else is too. [Click] Interact. Jump in, react, use the chat. This works much better as a conversation than a lecture. [Click] And if possible, keep your camera on. It helps me see when something lands and when I've lost you.

## 5. Agenda (Map) — The map

**On screen**

- The map
- 01 How a model works
- 02 Closed vs open models
- 03 Tokens & the context window
- 04 Models, apps & agents
- 05 Getting access: plans & pricing

**Say**

Here's the route for today. Five stops, and we'll take them in order. [Click] Stop 1: How a model works. [Click] Stop 2: Closed vs open models. [Click] Stop 3: Tokens & the context window. [Click] Stop 4: Models, apps & agents. [Click] Stop 5: Getting access: plans & pricing. Every stop builds on the one before it, so if anything along the way doesn't land, stop me and ask.

## 6. Section 01 — How a model works

**On screen**

- How a model works

**Say**

When people say "the model", they mean one specific thing. Let's pin down what it is.

## 7. Next Word — What word comes next?

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

## 8. Training Vs Inference — Training builds the model. Inference uses it.

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

## 9. Training Up Close — Read the library. Then do the job training.

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

## 10. Weights — A giant file of numbers.

**On screen**

- What is a "model", physically?
- A giant file of numbers.
- Think billions of tiny dials. They're called weights or parameters.
- Training = turning the dials until the guesses get good.
- After training, the dials are frozen. Chatting with it doesn't change them.
- Open models run from ~1 billion to ~1 trillion dials.

**Say**

What is a model, physically? Strip away the hype and it's a file, a very large file of numbers. Each number is a dial, and they're called weights or parameters. Open models run from about 1 billion to about 1 trillion of them. Right now they're all moving: this is training. [Click] Text runs through the dials and out comes a guess. [Click] We compare that guess with the right answer and send the error backwards through every dial, nudging each one a tiny bit. That's called backpropagation, and it repeats billions of times until the guesses get good. [Click] Then training stops and the dials freeze. Key point: when you chat with it, it isn't learning from you. The dials don't move. Remember "weights"; it comes back in two slides.

## 11. Closed Vs Open — Closed vs open.

**On screen**

- Closed vs open.

**Say**

Here's our frozen model from the last slide. Training is done and the dials are locked. Now the company that made it has a choice: what do they do with this file? [Click] Some lock it up. The weights never leave their servers, and you rent access through their app or API. That's a closed, or proprietary, model. Others open the door and publish the file so anyone can download it. That's an open-weights model. [Click] Where it runs: closed models live inside big companies' data centers, and you visit them over the internet. [Click] Open models can run right here, on your own laptop, even with the Wi-Fi off. [Click] Your data: with a closed model, every file and question you send goes to their servers. With an open model running locally, it never leaves your machine. It even works with no internet at all. [Click] What you pay for: closed means a subscription or per-use API fees to cover their data centers. Open means your own hardware or a cloud you choose, and the model itself is free. [Click] Customizing: with open weights you have the file, so you can fine-tune it on your own data however you like. Closed models give you limited options, on their terms. [Click] Top capability: the closed models are usually the cutting edge. [Click] Open models are playing catch-up, close behind, often by a few months. So the trade-off is privacy and control versus convenience and peak capability.

## 12. Sort: Closed Or Open — Closed or open?

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

## 13. Closed Vs Open: How You Use It — Renting a closed model.

**On screen**

- Renting a closed model.
- How does an open model work?

**Say**

Let's zoom in on the closed one. [Click] When you use ChatGPT or Claude, or a developer calls their API, your question travels over the internet to the company's servers. It runs through their frozen model, and the answer comes back to you. That round trip is an API call. [Click] Every one of those trips is inference, and inference is what you pay for. The money goes to the company that owns the model: a monthly subscription, or a fee per token through the API. [Click] Take my money. [Click] Now flip it. How does an open model work? [Click] Same questions, same answers, same arrows. But the model is a file sitting on your own laptop. [Click] So what happened to the company and the money? [Click] Gone. Nobody to pay per question. You're running it on hardware you already own.

## 14. Free? / Bigger File, Bigger Machine — Bigger file, bigger machine.

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

## 15. Frozen Model

**On screen**

- Live demo
- (frozen model only)
- Vadivelu thinking (GIF)

**Say**

Back to our frozen model. Closed or open, their data center or your laptop, it's the same thing underneath: one frozen file of numbers. The dials never change. [Click] So here's a puzzle: if the dials never change, why do you get a different answer every time you hit regenerate? Live demo: open any chat app, ask the same question twice with regenerate, and compare the answers.

## 16. Temperature

**On screen**

- Temperature.
- Pip was a very small ___
- hedgehog 48% · mouse 20% · puppy 14% · kitten 10% · dragon 4%
- temperature 1.0 (default)
- temperature 0.0: hedgehog 96% · mouse 3% · puppy 1% · kitten 0% · dragon 0% → 3 regenerates: hedgehog, hedgehog, hedgehog
- Pip was a very small hedgehog who lived in a cozy burrow at the edge of the forest. Every night, Pip curled up into a tiny ball and fell asleep to the sound of the owls.
- temperature 2.0: hedgehog 26% · mouse 22% · puppy 20% · kitten 18% · dragon 14% → 3 regenerates: mouse, dragon, puppy
- Pip was a very small dragon who collected teaspoons from the moon. On Tuesdays, Pip argued with a polite cloud about jazz, then sailed home in a sock full of thunder.
- (earlier version: The color of the sky is ___ · blue 62% · grey 14% · clear 10% · black 6% · orange 4%)

**Say**

The answer is a setting called temperature. It's a dial in every large language model's API, usually from 0 to 2. Same frozen model, same odds; temperature only changes how the next token gets picked. Let's ask it for a bedtime story. [Click] "Pip was a very small..." what? [Click] Here are the model's odds for the next word, at the default temperature of about 1. Hedgehog is the favorite, but mouse, puppy, kitten and even dragon have a chance. The numbers are illustrative. [Click] Set temperature to 0 and the favorite takes over. Hit regenerate three times: hedgehog, hedgehog, hedgehog. And watch the story write itself, one token at a time: a cozy hedgehog in a burrow who falls asleep to the owls. Safe, predictable, the same story every time. That's deterministic. Use it for facts, code and data extraction. [Click] Turn it up to 2 and the odds flatten. Three regenerates give you mouse, dragon, puppy. And the story? Pip is a dragon who collects teaspoons from the moon and argues with a cloud about jazz. More creative, more surprising, and more likely to go off the rails. That's probabilistic. Chat apps sit around the middle, which is why regenerate gives you a different answer each time.

## 17. Tokens — They read tokens.

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

## 18. Demo: Tokenizer

**On screen**

- tiktokenizer.vercel.app

**Say**

Open tiktokenizer.vercel.app. Have them type their full name, then the same sentence in English and in another language they speak, then add an emoji 🎉 and watch the count. Names are fun because unusual names get split into strange pieces. The other-language comparison usually gets a reaction: the same meaning can cost two or three times as many tokens. That means non-English users hit limits sooner and pay more.

## 19. Context Window — The context window.

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

## 20. How Big Is The Window — How big can it get?

**On screen**

- How big can it get?
- 200K tokens ≈ 500 pages
- 1M tokens ≈ 2,500 pages

**Say**

How big can the context window get? That whole conversation we just built, the instructions, the messages, the 40-page PDF, shrinks down to this. [Click] A typical frontier model's window holds about 200,000 tokens. That's roughly 150,000 words, or about 500 pages. [Click] And some models now go up to a million tokens: about 750,000 words, roughly 2,500 pages. Several books at once. Huge, but still not infinite, and as we'll see, a fuller desk isn't always a better one.

## 21. Desk Fills Up — Three hours into one chat.

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

## 22. Stateless — Stateless.

**On screen**

- Live demo
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

This surprises almost everyone. The model has no memory. [Click] Turn 1: you send a message. [Click] Turn 2: the app bundles up the entire conversation so far, puts it all in the context window, and sends all of it again. [Click] Turn 3: again, the whole script. It feels like a conversation, but the model is reading everything fresh each time. [Click] Open a new chat and the desk is empty. It has never met you. [Click] The model is Ghajini: no short-term memory, so it relies on the notes you hand it, and every turn it reads them from scratch. Live demo: tell a chat your favorite color, open a new chat, and ask what it is.

## 23. Dyk: Cutoff — Every model has a knowledge cutoff date.

**On screen**

- Live demo
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

Frozen dials have a side effect. Ask it about last week's news: why does it get it wrong? Someone usually says "it's not connected to the internet", which is half right. Every model has a knowledge cutoff date. [Click] Training: it reads everything up to a certain day. [Click] Then the dials freeze. That's the cutoff. [Click] After that, we only use it: inference, right up to today. Without web search it can't know what happened after the cutoff, and it may not even know that it doesn't know. Anything after that, the model simply never read. That's why "search the web" buttons exist, and why a model will sometimes confidently tell you the wrong CEO or last year's price. Try it: ask any model "What's your knowledge cutoff?" Live demo: ask a model "What's your knowledge cutoff?" and then ask about something from last week, with web search off.

## 24. Recap — Recap so far.

**On screen**

- Recap so far.
- 1 · Training & inference
- 2 · Closed vs open
- 3 · Guess the next word
- 4 · Tokens
- 5 · Context window

**Say**

Let's recap what we've covered so far. [Click] One: training and inference. The model reads a huge library once, at great cost, then freezes. Every time you use it, that's inference: question in, answer out. [Click] Two: closed versus open. Closed models stay locked in the company's servers and you rent them. Open models are a file you can download and run yourself. [Click] Three: it's all probabilistic prediction. The model guesses the next word from the odds, and temperature controls how adventurous those guesses are. [Click] Four: tokens. Models read chunks, not words, and tokens are the currency: limits and pricing are all counted in them. [Click] Five: the context window. That's the model's desk: everything it can see right now. It's big but not infinite, it fills up, and the model remembers nothing outside it.

## 25. Inside The Model — What's inside the model?

**On screen**

- What's inside the model?
- Big green circle (the model) with 💃
- Inside: ⚖️⚖️⚖️⚖️ Weights · 📚 What it read
- Dotted ice ring with ❄️ 🧊: ❄️ Frozen at the cutoff
- Outside, crossed out (NOT inside the model): 💬 Your chats ✕ · 📂 Your files ✕ · 📰 Today's news ✕ · 🗒️ Notes about you ✕

**Say**

Before we get to agents, let's open the model up and look inside, and see what's actually in there. [Click] Here's the model. [Click] Inside: the weights. The billions of dials we tuned during training. [Click] Those dials hold everything it picked up from what it read: language, facts, how to write code, how to reason. [Click] And all of it is frozen at the cutoff date. Nothing gets added while you use it. That's it. That's everything inside. Now, what's NOT inside? [Click] Your chats. [Click] Your files. [Click] Today's news. [Click] Notes about you. None of that lives in the model. Every single time you use it, the model starts from zero. So where does all that stuff live? Outside the model.

## 26. Outside: The App — Everything else lives in the app.

**On screen**

- Everything else lives in the app.
- ❄️ Frozen model 💃 (center) · label: Model
- Plain blue box around it with a title bar: App
- Inside the app, outside the model:
- Context window (red box: grey instructions bar, yellow memory bar, white your message, green reply)
- Instructions: grey card 📝 “Be helpful. Be safe. Keep it short.” 🔒 (you never see it)
- Memory: yellow sticky note 🗒️ Likes short answers
- Chat screen: “Plan my trip?” / “Sure! Where to?”

**Say**

So where does everything else live? [Click] Here's our frozen model again. [Click] Around it is the app. ChatGPT, Claude, Gemini: what you download or open in your browser is the app. The model sits inside the company's computers; the app is everything wrapped around it. Now let's fill it in. [Click] The context window. The desk lives in the app, not in the model. Every time you hit send, the app builds the desk and hands the whole thing to the model. The model reads it, writes a reply, and keeps nothing. That's why it's stateless. [Click] Instructions. Before you type a single word, the company has already put a note at the top of the desk: be helpful, be safe, keep it short. You never see it, but it's there in every chat. [Click] Memory. When ChatGPT or Claude "remembers" you, it's the app keeping a sticky note like this, and pasting it onto the desk next time. The model still remembers nothing. [Click] And the chat screen itself: the box you type in and your past conversations. All of this is the app. Only the 💃 in the middle is the model.

## 27. You Are The Loop — You are the loop.

**On screen**

- You are the loop.
- 💃 model (green circle)
- 🧑‍💻 You → white "?" arrow → model
- Model → green answer card → back to you
- You → "copy · paste · click" → apps box (📊 Excel · 📧 email · 🌐 web)
- Yellow dashed ring spinning around you + 🔁

**Say**

So that's how you use it today: you open the app and type. Let's watch what actually happens. [Click] Here's our model, the dancer. [Click] You ask it a question through the app. [Click] It gives you an answer. Text. That's all it ever gives you. [Click] And then what do you do? You copy that answer, open Excel or your email or a website, paste it, click around, do the actual work yourself. Then you come back with whatever happened and ask the next question. [Click] So who is going round and round here? You are. You're the loop. You carry every answer out into the world and carry every result back in. Hold on to that picture.

## 28. The Model Can'T Do Anything — The model can't do anything.

**On screen**

- The model can't do anything.
- 💃 model (big green circle) in the middle
- Four crossed-out actions around it: 📂 Open a file ✕ · 🌐 Search the web ✕ · 📧 Send an email ✕ · 🖱️ Click a button ✕
- White speech bubble from the model: ✍️ “search flights to Chennai”

**Say**

Here's the fact that surprises people. [Click] The model, on its own, can't actually do anything. Remember, it's a giant file of numbers that guesses the next word. [Click] It can't open a file on your computer. [Click] It can't go and search the web. [Click] It can't send an email. [Click] It can't click a button. [Click] The only thing it can do is write words. It can write "search flights to Chennai", but writing it doesn't make the search happen. Somebody has to read those words and actually go and run the search. So far that somebody has been you.

## 29. Give It Tools — Give it tools.

**On screen**

- Give it tools.
- Four blue tool cards drop in: 🔍 Search · 📄 Read file · ✏️ Write file · 📧 Email
- 💃 model writes a request pill: 🔍 search: flights to Chennai
- → plain blue app box ⚙️ App (the software around the model) runs it
- → blue result: ✈️ 14 flights found
- Yellow curved arrow back to the model: back into the context window

**Say**

So let's fix that. Let's give the model tools. [Click] A search tool. [Click] A tool to read a file. [Click] A tool to write a file. [Click] A tool to send an email. Now here's the part that most people get wrong, so watch closely. [Click] The model still only writes words. It writes a request: "search: flights to Chennai". [Click] The app around the model reads that request and actually runs the search. The model asks; the software does. [Click] The search comes back: fourteen flights found. [Click] And that result goes back into the context window, the desk we talked about earlier. Now the model can read it and decide what to do next. That's what a tool is: the model asks, the software runs it, the result comes back as more tokens.

## 30. Now Let It Loop — Now let it loop.

**On screen**

- Now let it loop.
- 🧑‍💻 “Find 3 cheap flights and put them in a spreadsheet.”
- Context window (red box, left) fills up lap by lap:
- 🧑‍💻 3 cheap flights → spreadsheet · ✈️ Search: 14 flights found · 💃 Picked the 3 cheapest · 📊 Spreadsheet saved · ✅ Done. Here's your file.
- Loop (right): 💃 Think → Act (🔍 Search flights, then 📊 Make sheet) → 👀 See result → back to Think · 🔁 with token dots circling
- Green exit arrow from Think → ✅ Done

**Say**

Now the big step. Remember who was going round in circles? You. What if the model could go round by itself? [Click] You give it one goal: find three cheap flights and put them in a spreadsheet. [Click] That goes into the context window, the desk. [Click] The model reads the desk and thinks: what's the first thing I need? [Click] It acts: it asks for the search tool, and the app runs it. [Click] It sees the result: fourteen flights, now sitting on the desk. [Click] And now it goes back to thinking, with that new information on the desk. It picks the three cheapest. That's the loop: think, act, see the result, think again. Round and round, as many laps as it needs. [Click] Next lap: it acts again with a different tool, and makes the spreadsheet. The result lands on the desk. [Click] And on the last lap, the model thinks: is the job finished? Yes. So it stops and tells you it's done. You gave it one sentence. It did all the copying, pasting and clicking that you used to do.

## 31. Outside: The Agent — An agent adds more outside.

**On screen**

- An agent adds more outside.
- Same plain blue app box, same frozen model 💃 in the middle, same Context window · Instructions · Memory · Chat screen
- New: Tools (🔍 📄 ✏️ 📧 blue tiles along the bottom)
- New: 🔁 Loop (yellow ring spinning around the model)
- New: 🛡️ Ask first (permissions)
- Box label App → Agent, spy icon in green circle appears

**Say**

Remember the app picture? Same app around it, same frozen model in the middle, same context window, instructions, memory and chat. So what turns an app into an agent? The three things we just saw, and all three are outside the model. [Click] Tools: search, read files, write files, send email. The model asks, the app runs them. [Click] The loop: instead of one question, one answer, the app keeps calling the model, think, act, see, think again, until the job is done. [Click] And permissions: because it can now actually do things, a good agent asks you first before anything risky. [Click] Add those three and the app becomes an agent. Model plus tools plus a loop, run by the app. We'll draw agents as this spy from now on. Look at the middle: the model didn't change. Not one dial. It just got hands and a loop, and all of it was added on the outside.

## 32. App Vs Agent — App vs agent.

**On screen**

- App vs agent.
- Columns: App (plain blue box icon) · Agent (spy icon)
- INSIDE · The model: 💃 / 💃 (identical)
- OUTSIDE · 📜 Context window ✓ / ✓ · 📝 Instructions ✓ / ✓ · 🗒️ Memory ✓ / ✓
- 🧰 Tools: a few / many
- 🔁 Loop: one reply / until done
- 🛡️ Permissions: — / asks first
- Same inside. More outside.

**Say**

Let's put the two side by side so the difference is crystal clear. [Click] An app on the left, an agent on the right. [Click] Inside: the model. Identical. Often literally the same model; Claude chat and Claude Code can run the very same Claude. [Click] Outside, both have a context window, both have hidden instructions, both can have memory. No difference there. [Click] Here's where they split. Tools: a chat app has a few, like web search; an agent has many, and can work with your files and apps. [Click] The loop: an app gives you one reply and waits for you. An agent keeps going until the job is done. [Click] And because it acts on its own, an agent asks permission before risky steps. One honest note: the line is blurring, and chat apps keep adding agent features. That's fine. Just ask: who runs the loop? [Click] So if you remember one thing: same brain inside, more hands outside. Everything that makes it an app or an agent lives outside the model.

## 33. Models, Apps, Agents — Models, apps, agents.

**On screen**

- Models, apps, agents.
- Column 1 · 💃 Models (green chips): GPT-5.6 · GPT-6 Astra · Claude Opus 5.5 · Gemini 3.8 Flash · Grok 4.7 · DeepSeek V4.1 Flash
- Column 2 · plain blue app box · Apps (logo chips): ChatGPT · Claude · Gemini
- Column 3 · spy icon · Agents (logo chips): Codex · Claude Code · Hermes · DeepSeek Harness · Antigravity · Grok Bot · Muse

**Say**

Let's finish by putting real names on the three words. [Click] Models: the brains, the frozen files of numbers. [Click] GPT-5.6 and GPT-6 Astra from OpenAI, Claude Opus from Anthropic, Gemini 3.8 Flash from Google, Grok 4.7 from xAI, and DeepSeek V4.1 Flash, an open model from China. You never touch these directly; you reach them through something. [Click] Apps: the thing you actually open. [Click] ChatGPT, Claude, Gemini. Notice Gemini is both a model and an app name, and ChatGPT is the app while GPT is the model. Companies reuse names, which is why this gets confusing. [Click] Agents: apps that add tools, a loop and permissions. [Click] Codex and Claude Code for coding, Hermes, DeepSeek Harness, Google's Antigravity, Grok Bot from xAI, and Meta's Muse, which books and buys things for you. Most of these were launched in just the last few months. When you hear a new AI name, ask one question: is it the brain, the app, or an app that runs the loop for you?

## 34. How To Get Access — How to get access?

**On screen**

- How to get access?
- Want / demand (GIF)

**Say**

So now you know what these models are. How do you actually get your hands on one? [Click] Everyone wants in. Let's talk about whether it's worth paying, and how.

## 35. Worth Paying? — Is it worth paying?

**On screen**

- Is it worth paying?
- Counting money (Santhanam) vs Vadivelu (GIFs)

**Say**

Is it worth paying? [Click] Option one: hold on to your money and stick with the free tiers. [Click] Option two: pay for a plan. [Your punchline for the Vadivelu GIF goes here.]

## 36. How To Pick — How to pick the right one?

**On screen**

- How to pick the right one?
- Tamil chat star (GIF)

**Say**

So how do you pick the right one? There are so many options. [Click] My recommendation: start with a closed model. Then look at the benchmarks to compare them. Open models are the third option. We'll talk about building with them and installing them locally later in the course, but for now, go with a closed model.

## 37. Subscription Vs Tokens — Subscription or pay per token?

**On screen**

- Should I choose subscription or pay per tokens?
- Netflix (subscription) vs tokens (pay per use) (GIFs)

**Say**

Should you pay for a subscription or pay per token? There are two approaches. [Click] A subscription works like Netflix: one flat monthly fee, and you use it as much as the plan allows. [Click] Pay per token is a meter: through the API you pay for exactly the tokens you send and get back. If you're starting out, always prefer the subscription: the cost is predictable and you won't get a surprise bill. And if you had to pick just one, choose Codex or Claude Code. You can't go wrong with either.

## 38. Pick One — Pick one of these.

**On screen**

- Pick one of these.
- Logos of AI models and companies, scattered: Grok, Claude, Claude Code, OpenAI, Codex, Hermes, Gemini, Antigravity, DeepSeek, Qwen, Meta, Mistral, Gemma, Perplexity, Microsoft, Cohere, NVIDIA, Hugging Face, Kimi, Zhipu, MiniMax, Copilot, Cursor. Circle: OpenAI and Claude.

**Say**

Look at how many models and companies there are. [Click] Let's narrow it down: the two big names are OpenAI and Claude. [Click] Pick one of these. Either is a great place to start.


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
