# Week 1 — Talk Track

Speaker notes for `new-week1-fundamentals.html`, in slide order. `[Click]` means press → to reveal the next step.

## 1. Title — AI, from zero.

Welcome. No prerequisites. By the end of today nobody should feel like AI is magic. It's a machine with a few very specific habits, and once you know them you'll use it far better than most people.

## 2. Prereqs

You don't need to code or know any math. Free tiers cover everything today. A single $20 plan gets you the bigger models and higher limits, and next week that makes a real difference.

## 3. The Arc — Four building blocks.

Four building blocks, each one stacks on the last. Week 1: understand the fundamentals. Week 2: use AI better. Week 3: build with AI. Week 4: how to think in the age of AI. [Click] Honestly, we don't know how long each one will take, so let's call them modules instead of weeks.

## 4. Agenda — The map

Ten stops. The three in green are the foundations, and everything after builds on them. Rule for today: every hard concept gets a short demo right after it, so you see it happen instead of just hearing about it.

## 5. Sticker Legend — Your stickers for the next two weeks

Green circle with the dancer 💃 means a model, the brain. Blue hexagon means a harness, the app or agent wrapped around the brain. That split matters a lot in part 6. Red means a demo is coming. Purple means I'm going to ask you first: take a guess before I reveal the answer. Wrong guesses are the point; they make the answer stick.

## 6. Section 01 — How a model works

When people say "the model", they mean one specific thing. Let's pin down what it is.

## 7. Next Word — What word comes next?

Ask the room first and let them shout. Everyone says "mat". Press → to reveal the odds: you just did what the model does. Press → again for the punchline. That's all it does. Given some text, it scores every possible next word and picks one. Then it does it again, and again. Essays, code and poems are all this one step repeated thousands of times. Keep the bar chart in mind; we'll come back to it in the demo.

## 8. Training Vs Inference — Training builds the model. Inference uses it.

Left side: books, articles and web pages pour in, and out comes the model. That's training. It happens once, in a data center, and costs a fortune. [Click] Right side: a question goes into the finished model, and an answer comes out. That's inference. Everything you do in ChatGPT or Claude is inference. You never train the model when you chat with it.

## 9. Training Up Close — Read the library. Then do the job training.

Pre-training is reading the entire library. The result is a base model: it knows a lot, but ask it a question and it might just carry on with more questions, because it's only autocompleting. Post-training is job training. People write example answers and rank responses, and the model learns to behave like an assistant. Much of what makes Claude feel different from GPT comes from this stage.

## 10. Weights — A giant file of numbers.

What is a model, physically? Strip away the hype and it's a file, a very large file of numbers. Each number is a dial, and they're called weights or parameters. Open models run from about 1 billion to about 1 trillion of them. Right now they're all moving: this is training. [Click] Text runs through the dials and out comes a guess. [Click] We compare that guess with the right answer and send the error backwards through every dial, nudging each one a tiny bit. That's called backpropagation, and it repeats billions of times until the guesses get good. [Click] Then training stops and the dials freeze. Key point: when you chat with it, it isn't learning from you. The dials don't move. Remember "weights"; it comes back in two slides.

## 11. Dyk: Cutoff — Ask it about last week's news. Why does it get it wrong?

Ask why before revealing. Someone usually says "it's not connected to the internet", which is half right. Press → for the timeline. The dials froze on a particular day. Anything after that, the model simply never read. That's why "search the web" buttons exist, and why a model will sometimes confidently tell you the wrong CEO or last year's price. Try it: ask any model "What's your knowledge cutoff?"

## 12. Inference Loop — One token at a time, on a loop.

White chips are what you typed. Green chips are what the model writes, one at a time. After each one it re-reads the whole thing and picks the next. That's why answers stream in word by word. It isn't typing for effect; it really does produce text one piece at a time.

## 13. Demo: Streaming — Same question, different answer. Why?

Run this live. Ask for the story, then hit regenerate two or three times. Ask the room why it changed and take a few guesses before pressing → to reveal. Link it back to the bar chart: it doesn't always take the 62% word, sometimes it takes the 14% one. That randomness is what makes it creative, and also why it's sometimes inconsistent.

## 14. Section 02 — Proprietary vs open weights

Remember the file of dials? This whole section is about who gets to hold it.

## 15. Quiz: Offline — Can you run ChatGPT on your laptop with the Wi-Fi off?

Take a show of hands for A, B and C. Most people pick A or B. Press → to strike the wrong ones, then → again for the reason. That reason is this whole section.

## 16. Vault Vs Zip — A vault, or a zip file.

Proprietary is a vault. The dials never leave the building, and you pay to send questions in and get answers out. Open weights is a zip file: the company publishes the numbers and you can download and run them yourself. Nuance for the curious: open weights usually doesn't mean open source. You get the trained model, not the data or the training code.

## 17. What Changes — Training looks the same. Everything after it differs.

Pre-training and post-training happen the same way either way. The difference is what happens to the file afterwards. The main trade-off is privacy and control versus convenience and peak capability. For most people in this room, proprietary through an app is the right starting point. Open weights starts to matter for sensitive data, offline use, or cost at scale.

## 18. Hardware — Bigger file, bigger machine.

The question people always ask is: can I run this at home? It depends on the size of the file. Small models with a few billion dials fit on a laptop. The giant ones need a data center. The big open models are real, but most people run the small ones locally and use the big ones through a hosted service.

## 19. Demo: Offline — Run an AI with the Wi-Fi off.

Pre-download the model before the session because it's several gigabytes. Pull the Wi-Fi on stage and it keeps working. That's the moment "open weights" clicks for people. Point out that it's slower and less capable than the frontier models, which is exactly the trade-off from the table.

## 20. Section 03 — Tokens & the context window

If you remember one section from today, make it this one. Almost every "why did the AI do that?" moment traces back to it.

## 21. Tokens — They read tokens: chunks of text.

A token is a chunk, usually part of a word. Common words are a single token, rare words get split up. Why care? Because limits, pricing and memory are all counted in tokens, not words. Rule of thumb: a thousand tokens is about 750 words.

## 22. Demo: Tokenizer — See your own words get chopped up.

Names are fun because unusual names get split into strange pieces. The other-language comparison usually gets a reaction: the same meaning can cost two or three times as many tokens. That means non-English users hit limits sooner and pay more.

## 23. Dyk: Strawberry — "How many r's are in strawberry?"

Vote first: A, B or C? It's 3, so press → to mark it. Then ask the real question, why would a smart model say 2, and let people guess before the final →. This is the best example of tokens leaking through. A model that can write a legal brief used to fail at counting letters, because it doesn't see letters. The lesson generalizes: be skeptical of AI for letter counts, exact character limits and precise arithmetic unless it's using a tool.

## 24. Context Window — The model's desk.

Picture a desk. Whatever is on the desk, the model can see. Anything off the desk doesn't exist for it. Every message, every reply, every file you upload goes on the desk and takes up space. Even the app's hidden instructions sit there. Desks are big now, hundreds of pages, but they're not infinite.

## 25. Quiz: Where Is It Stored — You told it your name ten messages ago. Where is your name stored right now?

Most people pick B, and some pick A. Remind them of the frozen dials: that rules out A. Press → to reveal C, then → for the one-liner. The next slide shows what that looks like.

## 26. Stateless — The model remembers nothing between turns.

This surprises almost everyone. The model has no memory. Every time you hit enter, the app bundles up the entire conversation so far and sends all of it again. It feels like a conversation, but the model is reading the whole script fresh each time. Open a new chat and the desk is empty. It has never met you.

## 27.  — That's the app, not the model.

Someone always pushes back here, and that's good. Yes, ChatGPT and Claude have memory features. But that memory lives in the app, not the model. The app writes sticky notes about you and pastes them onto the desk before you type. The model is still stateless underneath. This is our first look at the harness, the blue hexagon, and we'll unpack it properly in part 6.

## 28. Desk Fills Up — Three hours into one chat. Is it sharper now, or sloppier?

Ask it straight: sharper or sloppier? Most people assume it's gotten to know them. Press → for the answer, then → again for the three reasons. Three things go wrong on a full desk. One: the oldest stuff falls off or gets compressed, which is why it "forgets" what you said an hour ago. Two: every turn re-reads everything, so it gets slower and you hit usage limits sooner. Three, the sneaky one: models pay most attention to the beginning and end, and the middle blurs. Imagine one sticky note tucked into a thousand-page book. We'll come back to how to beat this.

## 29. Demo: Forgetful — The forgetful genius.

Results depend on whether memory is on, and either result teaches something. If it remembers, ask: where did that come from? The app's sticky notes. If it doesn't, that's the stateless model. Temporary or incognito chat modes are the cleanest way to show it.

## 30. Checkpoint — If you forget everything else…

Three sentences. If people leave with these, they'll already use AI better than most. The Ask AI sticker is the habit I want: when a concept feels fuzzy, have the AI teach it back to you at your level. Next: how to actually get your hands on Claude, Grok, GPT, DeepSeek and the rest.
