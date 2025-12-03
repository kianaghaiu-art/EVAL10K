import csv
import os
import chardet
import requests
from collections import defaultdict
from deepeval.models import GPTModel

# ============================================================
# CONFIGURATION
# ============================================================

DATASET_PATH = "data/eval10k.csv"   # Your uploaded dataset


# ============================================================
# BENCHMARK CLASS (Supports Subtopic Evaluation + CoT)
# ============================================================

class Eval10K:
    """
    Dataset Format:
      Column 0: Question Text
      Column 1: Topic
      Column 2: Subtopic
      Column 3: Correct Answer Letter (A/B/C/D)
    """

    COT_TOPICS = {"Math", "Chemistry", "Physics"}

    def __init__(self, dataset_path, topics=None, n_samples=None):
        self.dataset_path = dataset_path
        self.topics = topics or []
        self.n_samples = n_samples

        self.questions = self._load_data()

        self.overall_score = 0.0
        self.topic_scores = {}
        self.subtopic_scores = {}

    # --------------------------------------------------------
    # LOAD DATA
    # --------------------------------------------------------
    def _load_data(self):
        # Detect encoding
        with open(self.dataset_path, "rb") as raw:
            enc = chardet.detect(raw.read(50000))["encoding"] or "utf-8"

        data = []
        with open(self.dataset_path, newline="", encoding=enc, errors="replace") as f:
            reader = csv.reader(f)
            headers = next(reader)  # skip header

            for row in reader:
                if len(row) < 4:
                    continue

                question = row[0].strip()
                topic = row[1].strip()
                subtopic = row[2].strip()
                correct = row[3].strip().upper()

                if self.topics and topic not in self.topics:
                    continue

                data.append({
                    "question": question,
                    "topic": topic,
                    "subtopic": subtopic,
                    "correct": correct,
                })

        if self.n_samples:
            data = data[:self.n_samples]

        print(f"Loaded {len(data)} questions.")
        return data

    # --------------------------------------------------------
    # PARSE MODEL OUTPUT LETTER
    # --------------------------------------------------------
    def _parse_answer(self, text):
        text = str(text).strip().upper()
        for letter in "ABCD":
            if text.startswith(letter):
                return letter
        return "?"

    # --------------------------------------------------------
    # RUN EVALUATION
    # --------------------------------------------------------
    def evaluate(self, model):
        total = 0
        correct_total = 0

        per_topic = defaultdict(lambda: [0, 0])      # [correct, total]
        per_subtopic = defaultdict(lambda: [0, 0])   # [correct, total]

        print(f"\nEvaluating {len(self.questions)} questions...\n")

        for i, q in enumerate(self.questions, start=1):

            # Chain-of-thought for STEM topics
            if q["topic"] in self.COT_TOPICS:
                extra_instruction = (
                    "\n\nThink through the problem step by step and explain your reasoning "
                    "before selecting your final answer."
                )
            else:
                extra_instruction = ""

            prompt = (
                f"{q['question']}\n"
                f"Return ONLY the correct letter (A, B, C, or D)."
                f"{extra_instruction}"
            )

            response = model.generate(prompt)
            response_text = response[0] if isinstance(response, tuple) else response

            pred = self._parse_answer(response_text)

            total += 1
            per_topic[q["topic"]][1] += 1
            per_subtopic[q["subtopic"]][1] += 1

            if pred == q["correct"]:
                correct_total += 1
                per_topic[q["topic"]][0] += 1
                per_subtopic[q["subtopic"]][0] += 1

            if i % 200 == 0:
                print(f"Processed {i} questions...")

        # Final results
        self.overall_score = correct_total / total if total else 0.0

        for topic, (c, t) in per_topic.items():
            self.topic_scores[topic] = c / t if t else 0.0

        for sub, (c, t) in per_subtopic.items():
            self.subtopic_scores[sub] = c / t if t else 0.0

        print("\n========== FINAL RESULTS ==========")
        print(f"Overall Accuracy: {self.overall_score * 100:.2f}%\n")

        print("Accuracy by Topic:")
        for topic, acc in sorted(self.topic_scores.items()):
            print(f"  • {topic}: {acc * 100:.2f}%")

        print("\nAccuracy by Subtopic:")
        for sub, acc in sorted(self.subtopic_scores.items()):
            print(f"  • {sub}: {acc * 100:.2f}%")


# ============================================================
# RUN THE BENCHMARK
# ============================================================

if __name__ == "__main__":
    model = GPTModel(model="gpt-4o", temperature=0.0)
    benchmark = Eval10K(dataset_path=DATASET_PATH)
    benchmark.evaluate(model)
