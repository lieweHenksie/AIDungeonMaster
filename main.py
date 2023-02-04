#!/usr/bin/env python3
import click
from pyfiglet import Figlet
from chatgpt_templates.answer_factual_questions import answer_factual_question
from chatgpt_templates.answer_factual_questions import answer_factual_question_angry
from decouple import config
import openai
# from vanilla_swaps.engine.trade_designation_engine import designate_trades
# from presenter.app import run as runPresenter
# from vanilla_swaps.engine.trs_effectiveness import calculate_active_trs_effectiveness
# from vanilla_swaps.engine.trs_designation import designate_trs_trades


@click.group()
def cli():
    pass
@cli.command()
@click.option('--prompt', prompt='What do you want mortal? \n',required=True, help='Ask a factual question.')
def invoke_bob(prompt):
    f = Figlet(font='slant')
    openai.api_key = config("OPENAI_API_KEY")
    response = answer_factual_question(prompt)
    click.secho(response, fg='red')

@cli.command()
@click.option('--prompt', prompt='WHO AWAKES ME FROM MY SLUMBER!? \n',required=True, help='Ask a factual question.')
def invoke_bob_angry(prompt):
    f = Figlet(font='slant')
    openai.api_key = config("OPENAI_API_KEY")
    response = answer_factual_question_angry(prompt)
    click.secho(response, fg='red')

if __name__ == '__main__':
    cli()
