from functions.covid_ph.DriveCsvFile import DriveCsvFile
from functions.covid_ph.keyboards import get_cases_markup
from utils import extract_message

# Create CVS File instance
f = DriveCsvFile('109QO862DYDFaZsbu3YRpEWdemyMiTyT2')


def process_update_csv_id(bot, message):
    file_id = extract_message(message.text)
    if file_id is not None:
        f.update_file_id(file_id)
        bot.reply_to(message, "Updated file id")

    else:
        bot.reply_to(message, "Include a file id")


def process_get_cases(bot, message):
    bot.reply_to(message, 'Select City:', reply_markup=get_cases_markup())
