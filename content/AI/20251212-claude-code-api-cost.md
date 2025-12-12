Title: Claude Code API cost
Date: 2025-12-12 09:55
Tags: AI

Today I was curious about the API costs for Claude Code, so I tried to implement a new feature in the Nodehaus AI Platform. Normally I use the monthly Pro plan, but I didn't want to buy it this month as I don't know how much I will use it and then there is (mainly AI-free) Christmas :)

So the plan was to add streaming support to an existing OpenAI API compatible endpoint. The challenge was that we receive streams from a Ollama on Runpod and the data that comes in is wrapped into Runpod specific JSON in each chunk. We need to extract it and then forward it. I had a Python script that demonstrates it and I added that to the prompt. The full prompt for Claude is here:

[https://github.com/Nodehaus/ai-platform/blob/main/prompts/update_endpoint.txt#L13](https://github.com/Nodehaus/ai-platform/blob/main/prompts/update_endpoint.txt#L13)

It implemented the working streaming feature in one go, the code is here:

[https://github.com/Nodehaus/ai-platform/commit/0fbad4bf4af9feca98999ec74b965dfaf75ad160](https://github.com/Nodehaus/ai-platform/commit/0fbad4bf4af9feca98999ec74b965dfaf75ad160)

So that resulted in the following token usage and cost (mostly it used Sonnet, just around 8000 token went to Haiku):

- Tokens In: 1.332.000
- Tokens Out: 17.658
- Cost: $ 0,90

Quite expensive I think! I can do several of those feature implementations normally in the monthly plan before my 4h limits run out. In a normal month I would probably spend a few hundred $ via the API. If the API plan reflects some real costs at Anthropic's side then the monthly plan definitely does not cover the costs for them. Or most people (unlike me) just sign up even if they don't use it.

I still compared this to an implementation of VS Code Agent, in the free plan, I think it used Anthropic's Haiku model mostly:

[https://github.com/Nodehaus/ai-platform/commit/d892e5ce97e0343a2512cace2d2aea441fb79608](https://github.com/Nodehaus/ai-platform/commit/d892e5ce97e0343a2512cace2d2aea441fb79608)

Also a working feature. I am not a good enough Go developer to judge which one is "better" and I didn't actually analyze it in depth, normally during vibe coding I only look at the general architecture and the code organization. This seems to be fine in both cases.
