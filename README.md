# Eval10K: A Cross-Disciplinary Benchmark for Evaluating LLM Reasoning

Eval10K is a benchmark of 10,172 hand-written multiple-choice questions covering nine high-school and college-level subjects. The dataset is designed to measure both factual accuracy and structured reasoning across STEM and non-STEM domains.

This repository includes:
- The full Eval10K dataset  
- Subtopic metadata  
- Evaluation scripts  
- Example prompts  
- The LaTeX source of the research paper  
- Result summaries for major LLMs  

---

## Overview

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



## Results Summary

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

## 📊 Expanded Leaderboard: Accuracy & Ranking Across Key Subjects

| Model            | Overall (%) | Math (%) | Physics (%) | Chemistry (%) | Rank (Overall) | Rank (Math) | Rank (Physics) | Rank (Chemistry) |
|------------------|-------------|----------|-------------|----------------|----------------|-------------|-----------------|------------------|
| **GPT-5**            | **90.76**    | 84.54   | 85.29      | **94.03**       | 1              | 2           | 3 (tie)         | 1                |
| **GPT-4o**           | **87.99**    | 76.17   | 86.80      | 90.05          | 2              | 4           | 2               | 2                |
| **Gemini Flash**     | **87.58**    | 84.01   | **87.65**  | 89.76          | 3              | 3           | 1               | 3                |
| **Gemini Pro**       | 87.36        | **92.58** | 85.29      | 80.61          | 4              | 1           | 3 (tie)         | 6                |
| **GPT-4.1**          | 85.76        | 68.35   | 65.20      | 83.97          | 5              | 6           | 7               | 5                |
| **GPT-4o mini**      | 85.20        | 63.61   | 62.25      | 84.87          | 6              | 8           | 8               | 4                |
| **Grok 4.1**         | 75.11        | 70.08   | 76.50      | 74.17          | 7              | 5           | 5               | 7                |
| **Grok 4**           | 71.84        | 66.06   | 63.25      | 68.97          | 8              | 7           | 6               | 8                |
| **GPT-3.5 Turbo**    | 52.99        | 23.92   | 26.96      | 39.91          | 9              | 9           | 9               | 9                |

---

## Repository Structure

```
EVAL10K/
│
├── data/
│   └── eval10k.csv              # Full dataset (10,278 questions)
│
├── src/
│   └── evaluate.py              # Main evaluation script
│
├── paper/
│   ├── eval10k.tex              # LaTeX source of research paper
│   └── figures/                 # All plots and tables
│
├── results/
│   └── model_results/           # Accuracy summaries for all evaluated models
│
├── requirements.txt             # Python dependencies
│
└── README.md
```

---

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

This will install all Python packages needed to run the Eval10K benchmark, including model wrappers and utility tools.

---

## Running Evaluations

The main evaluation script is located in:

```
src/evaluate.py
```

To run an evaluation on a model (example uses GPT-4o):

```
python src/evaluate.py \
    --model gpt-4o \
    --dataset data/eval10k.csv
```

---

## Evaluating with Chain-of-Thought (Math, Physics, Chemistry)

For reasoning-heavy subjects, Eval10K automatically adds a chain-of-thought instruction:

```
"Think through the problem step by step and explain your reasoning before selecting your final answer."
```

This applies only to the following subjects:

- **Math**
- **Physics**
- **Chemistry**

---

## Optional Arguments

Eval10K supports several optional command-line flags:

```
--topics "Math,Chemistry"      # Evaluate only selected subjects
--n_samples 500                # Limit evaluation to first 500 questions
```

You can combine flags as needed. Example:

```
python src/evaluate.py --model gpt-4o --dataset data/eval10k.csv --topics "Math,Physics" --n_samples 300
```

---

## Expected Output

Running the script prints:

- Overall accuracy  
- Per-subject accuracy  
- Per-subtopic accuracy  

---

**Example Output:** 

Overall Accuracy: 85.76%

Accuracy by Topic:
- Math: 68.35%
- Chemistry: 83.97%
- Biology: 88.98%
- Environmental Science: 89.99%
- Psychology: 94.90%
- Physics: 65.20%
- Anatomy: 96.94%
- Statistics: 95.10%
- US History: 98.33%

Detailed tables and plots are available in:
- results/model_results/
- paper/figures/

---

## Citing Eval10K

If you use Eval10K in academic work, please cite:

```
@misc{eval10k2025,
  title        = {Eval10K: A Cross-Disciplinary Benchmark for Evaluating LLM Reasoning},
  author       = {Kian Keyhan},
  year         = {2025},
  howpublished = {\url{https://github.com/kianaghaiu-art/EVAL10K}}
}
```


## License
This project is released under the MIT License, allowing research and reproduction with attribution.



