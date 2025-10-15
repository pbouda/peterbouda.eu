Title: Running AI at home
Date: 2025-10-15 16:47
Tags: AI

The first reviews of NVIDIA DGX Spark review are being published, so I want to
write about the current state of self-hosting LLMs.

First, I think it's quite amazing that you can run state-of-the-art models on
your own machines. This sets AI apart from technologies like search engines and
cloud service providing that are hard to replicate "at home". It brings back
experiences from personal computing after the mainframe era:
["There is no reason for any individual to have a computer in their home"](https://www.computinghistory.org.uk/pages/3971/There-is-no-reason-anyone-would-want-a-computer-in-their-home)
:)

Models that you can run at home nowadays show performance similar to models that
the big AI companies published 9-12 months ago, so GPT-4 performance is not
compeletely out of reach.

The main problem that home AI enthusiasts currently face is limited, fast
memory. The LLMs that reach GPT-4 performance require probably more than 128GB
of memory, which might be out-of-scope with limited financial budgets. If you
want to run AI with reasonable resources you basically have two options:

First, you buy a consumer GPU where currently the maximum memory would be 24GB.
But that memory is super-fast, which is what you want.

Second, you use the option with unified memory that is shared between CPU and
GPU, where you can choose among Apple's platforms, AMD Ryzen AI Max or now the
NVIDIA DGX Spark. Unfortunately unified memory is slower then pure GPU memory,
the fastest you get with Apple's M\* Max series. But up to 64GB memory or even
128GB are possible then!

When you know your memory size you can begin to choose the models. Normally
models come in a size labelled in billions, like "30b", which means they have
so-and-so many paramers, e.g. 30 billion parameters. Each parameter in standard
models has 2 bytes, so a "30b" model is roughly 60 gigabytes. With unified
memory you need some memory to run applications besides the models, so a
standard 30b model will barely fit into 64GB unified memory, and definitely not
on any consumer GPU. People started to "quantize" models, so that each parameter
has only 1 byte or even half a byte, and voilà, 30b models fit into 24GB GPU
memory (maybe try [Qwen3 30b](https://ollama.com/library/qwen3:30b-a3b-instruct-2507-q4_K_M),
my standard model now for local inference) and a 106b model into your 64GB
Macbook Pro (possibly
[GLM-4.5 Air](https://simonwillison.net/2025/Jul/29/space-invaders/)).

To run models you can start with [Ollama](https://ollama.com/).

Hope that helps to start your first local chat :) and let me know about any
doubts or questions about running your local AI!
