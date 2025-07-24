"""
Setting up for fine tune assistant bot in command line
"""
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def main():
    model_dir = './finetuned-onboarding-model' # where you saved your trained model
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model = AutoModelForCausalLM.from_pretrained(model_dir)
    print('Onboarding AI Assistant. Type your question (or "exit" to quit):')
    while True:
        question = input('> ')
        if question.lower() == 'exit':
            break
        
        # TODOs: Setting up inputs and outputs
        inputs = tokenizer(

        )
        outputs = model.generate(

        )

        answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print('Assistant:', answer)

if __name__ == '__main__':
    main() 