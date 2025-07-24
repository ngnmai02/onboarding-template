"""
Loading dataset from Huggingface and saving to json
"""
from datasets import load_dataset

def main():
    # load dataset (the smallest one to test)
    dataset = load_dataset('DATASET FROM HF')
    # Save a small sample for quick fine-tuning
    train_sample = dataset['train'].select(range(1000))
    train_sample.to_json('train_sample.json')
    print('Sample data saved to train_sample.json')

if __name__ == '__main__':
    main() 