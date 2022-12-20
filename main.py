import click
import tools
from transformers import AutoTokenizer, AutoModelForTokenClassification
 from transformers import pipeline
@click.command()
@click.option('--text', default="Aujourd'hui c'est l'anniversaire de Mona. Paul est dehors.")

def run(text):
    tokenizer = AutoTokenizer.from_pretrained("gilf/french-postag-model")
    model = AutoModelForTokenClassification.from_pretrained("gilf/french-postag-model")
    
    nlp_token_class = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")
    my_text = 'Face à un choc inédit, les mesures mises en place par le gouvernement ont permis une protection forte et efficace des ménages'
    res = nlp_token_class(text)

    print(res)
    print(tools.addPauseTag(res))

if __name__ == '__main__':
    run()