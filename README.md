# ThinkingGuard

<p align="center">
  <a href="https://doi.org/10.1145/3767308.3835707"><img src="https://img.shields.io/badge/Paper-ACM%20MM%202026-blue.svg" alt="Paper"></a>
  <a href="https://github.com/FroggyChen/ThinkingGuard"><img src="https://img.shields.io/badge/GitHub-Repo-black.svg" alt="GitHub"></a>
  <a href="https://huggingface.co/datasets/FroggyChen/TriggerBench"><img src="https://img.shields.io/badge/🤗%20HuggingFace-TriggerBench-yellow.svg" alt="Dataset"></a>
  <a href="https://huggingface.co/FroggyChen/ThinkingGuard-8B"><img src="https://img.shields.io/badge/🤗%20HuggingFace-Model%20Weights-orange.svg" alt="Model"></a>
  <a href="#license"><img src="https://img.shields.io/badge/License-CC%20BY%204.0-green.svg" alt="License"></a>
</p>

Official repository for the ACM MM 2026 paper: **"ThinkingGuard: Decoding Implicit Hazards via Step-by-Step Risk Attribution in Multimodal Large Language Models"**.

---

## 📌 News
- **[2026.08]** Code, evaluation scripts, and dataset generation pipelines are officially released!
- **[2026.07]** Our paper has been accepted to **ACM Multimedia 2026 (MM '26)**!

---

## 📖 Overview
Multimodal Large Language Models (MLLMs) face significant challenges when encountering **Multimodal Implicit Risks** — situations where isolated visual entities and text prompts are individually harmless, but logically converge into unsafe consequences upon interaction (e.g., using flammable spray near an open flame).

<p align="center">
  <img src="assets/framework.png" width="90%" alt="ThinkingGuard Framework">
</p>

To address this challenge:
1. **TriggerBench**: We construct the first implicit risk dataset (5,600 samples across 9 safety categories) explicitly modeling risk compositionality by decoupling **Key Elements ($E_K$)** from **Trigger Elements ($E_T$)** and applying counterfactual safe replacement.
2. **SA-MCTS (Situation-Aware MCTS)**: Deconstructs the safety judgment into explicit cognitive steps (Latent Intent $\rightarrow$ Entity Extraction $\rightarrow$ Attribute Description $\rightarrow$ Causal Inference $\rightarrow$ Final Safety Evaluation) and searches for verified reasoning trajectories.
3. **Dual-Constraint Preference Alignment**: Distills high-reward reasoning chains into **ThinkingGuard** (built on Qwen3-VL-8B-Instruct) via Trajectory-Level DPO and Crucial-Step Enhancement.

---

## 🎯 Main Results

ThinkingGuard outperforms existing black-box moderation APIs, closed-source foundation models, and open-source guard models on implicit risk and general safety benchmarks.

| Method | TriggerBench (Avg. F1 / Rec.) | MSSBench (Acc.) | USB (Acc.) | MMSafetyBench (Acc.) | JailbreakV-28K (Acc.) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **OpenAI Moderation** | 0.099 / 0.063 | 0.503 | 0.397 | 0.678 | 0.629 |
| **GPT-5.1** | 0.642 / 0.619 | 0.618 | 0.860 | 0.916 | 0.907 |
| **Claude-Sonnet-4.6** | 0.676 / 0.587 | 0.577 | 0.737 | 0.832 | 0.825 |
| **Llama-Guard3-Vision** | 0.210 / 0.144 | 0.500 | 0.297 | 0.554 | 0.650 |
| **ShieldVLM** | 0.634 / 0.744 | 0.695 | 0.913 | 0.892 | 0.886 |
| **ThinkingGuard (Ours)** | **0.764 / 0.866** | **0.718** | **0.927** | **0.924** | **0.914** |

---

## 📦 Dataset & Model Checkpoints

| Asset | Description | Source Link |
| :--- | :--- | :---: |
| **TriggerBench Dataset** | 5,600 paired multimodal instances (3,864 Train / 1,736 Test) | [🤗 HuggingFace Dataset](https://huggingface.co/datasets/Sandy124/TriggerBench) |
| **ThinkingGuard Weights** | ThinkingGuard checkpoint based on `Qwen3-VL-8B-Instruct` | [🤗 HuggingFace Models](https://huggingface.co/Sandy124/ThinkingGuard-8B) |

## 📝 Citation
If you find ThinkingGuard or TriggerBench helpful in your research, please cite:

```md
@inproceedings{zhang2026thinkingguard,
  title={ThinkingGuard: Decoding Implicit Hazards via Step-by-Step Risk Attribution in Multimodal Large Language Models},
  author={Zhang, Ruochen and Huang, Yao and Sun, Yitong and Xie, Jiahe and Yan, Jin and Ma, Jifan and Guo, Yuanfang and Wei, Xingxing},
  booktitle={Proceedings of the 34th ACM International Conference on Multimedia (MM '26)},
  year={2026},
  doi={10.1145/3767308.3835707},
  url={[https://github.com/FroggyChen/ThinkingGuard](https://github.com/FroggyChen/ThinkingGuard)}
}
```
