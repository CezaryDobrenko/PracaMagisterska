class FolderTranslator:

    @staticmethod
    def interval_to_pl(value: str) -> str:
        translation_dict = {
            "MINUTE5": "Co 5 minut",
            "MINUTE10": "Co 10 minut",
            "MINUTE15": "Co 15 minut",
            "MINUTE30": "Co 30 minut",
            "MINUTE45": "Co 45 minut",
            "HOUR1": "Co godzinę",
            "HOUR2": "Co 2 godziny",
            "HOUR3": "Co 3 godziny",
            "HOUR6": "Co 6 godzin",
            "HOUR12": "Co 12 godzin",
            "DAY1": "Codziennie",
            "DAY2": "Co 2 dni",
            "DAY3": "Co 3 dni",
            "DAY4": "Co 4 dni",
            "DAY5": "Co 5 dni",
            "DAY6": "Co 6 dni",
            "WEEK": "Co tydzień",
        }
        return translation_dict[value]

    @staticmethod
    def is_ready_to_pl(value: bool) -> str:
        if value:
            return "Tak"
        return "Nie"

    @staticmethod
    def scraping_date_to_pl(value):
        converted_date = value.strftime("%H:%M:%S, %d-%B-%Y")
        lookup_table = {
            "January": "Styczeń",   "February": "Luty",
            "March": "Marzec",       "April": "Kwiecień",
            "May": "Maj",           "June": "Czerwiec",
            "July": "Lipiec",       "August": "Sierpień",
            "September": "Wrzesień",  "October": "Październik",
            "November": "Listopad", "December": "Grudzień"
        }
        for k, v in lookup_table.items():
            if k in converted_date:
                converted_date = converted_date.replace(k, v)
        return converted_date
