# Eval10K: A Cross-Disciplinary Benchmark for Evaluating LLM Reasoning

Eval10K is a benchmark of 10,278 hand-written multiple-choice questions covering nine high-school and college-level subjects. The dataset is designed to measure both factual accuracy and structured reasoning across STEM and non-STEM domains.

This repository includes:
- The full Eval10K dataset  
- Subtopic metadata  
- Evaluation scripts  
- Example prompts  
- The LaTeX source of the research paper  
- Result summaries for major LLMs  

---

## 📘 Overview

Eval10K spans **nine academic subjects**:
- Mathematics  
- Physics  
- Chemistry  
- Biology  
- Environmental Science  
- Anatomy & Physiology  
- Psychology  
- Statistics  
- U.S. History  

Each subject is divided into **specificc subtopics** (74 total).  
Questions were manually written or adapted from reliable high-school and college textbooks and do not originate from online forums or crowd-sourced sources.

The benchmark supports:
- **Final-answer evaluation**  
- **Chain-of-Thought reasoning evaluation** (Math, Physics, Chemistry)  
- **Subject-level and subtopic-level accuracy**  
- **Error analysis for reasoning-heavy questions**

---



## 📊 Results Summary

Eval10K was used to evaluate several major LLMs, including:

- GPT-3.5 Turbo  
- GPT-4o mini  
- GPT-4o  
- GPT-4.1  
- GPT-5  
- Gemini 2.5 Pro  
- Gemini 2.5 Flash  
- Grok 4  
- Grok 4.1  

Across all models, the weakest performance consistently appears in:
- **Mathematics**  
- **Physics**  
- **Chemistry**  

These subjects require multi-step reasoning and procedural understanding, and the results suggest current LLMs still struggle to generalize beyond familiar patterns in open training data.

Full tables, figures, and subtopic breakdowns are provided in the paper and `paper/figures/`.

---





