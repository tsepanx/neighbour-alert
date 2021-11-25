from telegram import Update, ForceReply
from telegram.ext import CallbackContext


def register_neighbour_command(update: Update, context: CallbackContext) -> None:
    """
    Adds neighbour's alias to user_data of current user.

    Syntax: /register_neighbour @{alias}

    key: 'neighbour_aliases'
    format: '@{alias} @{alias} @...'
    """

    key = 'neighbour_aliases'

    try:
        value = update.message.text.split(' ')[1]

        if key in context.user_data.keys():
            context.user_data[key] += value + ' '
        else:
            context.user_data.update({key: value+' '})

        message = f'Neighbour {value} successfully added'
        update.message.reply_text(
            text=message
        )
    except IndexError:
        message = 'Use syntax /register_neighbour @alias'
        update.message.reply_text(
            text=message
        )


def start_command(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)
