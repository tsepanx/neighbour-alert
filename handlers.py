from telegram import Update, ForceReply
from telegram.ext import CallbackContext


def register_neighbour_command(update: Update, context: CallbackContext) -> None:
    """
    Adds neighbour's alias to user_data of current user.

    Syntax: /register_neighbour @{alias} @{alias} @{alias} ...

    key: 'neighbour_aliases'
    format: '@{alias} @{alias} @...'
    """

    key = 'neighbour_aliases'

    aliases = context.args

    if aliases:
        for alias in aliases:
            if '@' != alias[0]:
                # separate in errors.py later
                message = 'Use syntax /register_neighbour @alias @alias @alias ...'
                update.message.reply_text(
                    text=message
                )
                return

        # replace with db adding later
        context.user_data.update({key: ' '.join(aliases)})

        aliases_str = ', '.join(aliases)
        message = f"{aliases_str} was successfully added to neighbours' list" if len(aliases) == 1 \
            else f"{aliases_str} were successfully added to neighbours' list"
        update.message.reply_text(
            text=message
        )
    else:
        message = 'Use syntax /register_neighbour @alias @alias @alias ...'
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
