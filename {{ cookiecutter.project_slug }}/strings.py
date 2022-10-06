from dataclasses import dataclass


@dataclass
class Strings:
    cmd_start: str
    faq: str
    contact: str


ENGLISH = Strings(
    "Hello {}!\nWelcome to the Super Bot\n\n/faq - Frequently asked questions!\n"
    "/contact - Contact Us!",

    "How to use this bot?\nYou should make an admin to your group!\n"
    "Why bot is not working in my group?\nYou need to enable delete messages admin rights for this bot!",

    "Send you question and feadback here: @feadbackbot"
)

LANGUAGES = {
    'en': ENGLISH
}


def get_language(language_code: str) -> Strings:
    return LANGUAGES.get(language_code, ENGLISH)
