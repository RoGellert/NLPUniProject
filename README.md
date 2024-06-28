# Fine-tuning README

We ran our fine-tuning in Google Colab utilizing paid A100 GPU. If you want to replicate our results it's better to always have save_to_hub = True in parameters while being connected to your hugging face hub as colab tends to disconnect randomly.  

There are 4 files with fine-tuning procedures and 1 script to scrape the data in this folder, you can follow the steps described in the notebooks:

- NLP_Phi2.ipynb - fine tuning Phi2 through regular PEFT
- NLP_Unsloth_Gemma.ipynb - fine tuning Gemma through Unsloth
- NLP_Unsloth_Llama2.ipynb - fine tuning Llama2 through Unsloth
- starcode.ipynb - fine tuning starcoder through regular PEFT
- kotlin_dataset_donloader.py - file to scrape open-source code files from repositories

Datasets used are:

- Kotlin scraped dataset - availible in this folder in data.zip
- CodeInstruct - https://github.com/qishenghu/CodeInstruct
- Hugging face codebase dataset - https://huggingface.co/datasets/smangrul/hf-stack-v1