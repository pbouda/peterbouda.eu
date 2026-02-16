Title: Model Assistant
Date: 2026-02-16 16:28
Tags: AI

Running LLMs locally is amazing, but choosing which model to actually use? That's where it gets tricky. You're juggling benchmarks from different leaderboards, trying to figure out which models even fit in your memory, and wondering if that model that looks great on paper actually works for your use case.

So I built a small tool to help with this: [Model Assistant](https://model-assistant.aiworkshops.eu/)

It's deliberately simple right now. You describe your use case (or pick from a list), and it matches that against benchmark descriptions using TF-IDF scoring. The tool only shows open models (minimum open weights) that run in less than 128GB VRAM, most need much less.

A few honest limitations: Not every model has benchmarks, and different models get tested on different benchmarks, so results won't be complete. But it gives you a starting point based on what data exists. I'm actively expanding the dataset to include more benchmark sources, and models get updated regularly. The pipeline to update is automatic (check the link to the code on the site).

Embeddings will replace/enhance TF-IDF soon for better matching, but I wanted to ship something useful now rather than wait for perfect.

If you're self-hosting or thinking about it, give it a try. Feedback welcome: what other features would actually be useful here?
