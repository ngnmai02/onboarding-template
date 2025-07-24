"""
Setting up the training process ad preprocess dataset if needed
"""
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    Trainer,
    TrainingArguments,
    DataCollatorForLanguageModeling
)
from datasets import load_dataset
import json

def main():
    model_name = 'gpt2' # TODOs: Change to the correct model that you want to use
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token  
    model = AutoModelForCausalLM.from_pretrained(model_name)
    model.resize_token_embeddings(len(tokenizer))

    # Convert JSON lines to plain text
    train_path = 'train_sample.json' #Dataset that has been loaded
    with open(train_path, 'r') as f:
        data = [json.loads(line) for line in f]
    with open('train.txt', 'w') as f:
        for item in data:
            f.write(item['text'] + '\n')

    # Load and split dataset
    dataset = load_dataset('text', data_files={'train': 'train.txt'})
    dataset = dataset['train'].train_test_split(test_size=0.1, seed=42)  # 90% train, 10% validation

    # TODOs: Preprocess data
    tokenized_dataset = dataset.map(
    ) 

    # TODOs: Set up training 
    training_args = TrainingArguments(
    )

    trainer = Trainer(
    )

    trainer.train()
    trainer.save_model('./finetuned-onboarding-model')
    tokenizer.save_pretrained('./finetuned-onboarding-model')
    print('Model fine-tuned and saved to ./finetuned-onboarding-model')

if __name__ == '__main__':
    main()
