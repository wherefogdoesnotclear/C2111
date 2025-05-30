import requests
 
class CurrencyConverter:
    def __init__(self):
        self.exchange_rate = self.get_usd_rate()
 
    def get_usd_rate(self):
        url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&json"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data[0]['rate']
        except requests.RequestException as e:
            print(f"Помилка при отриманні курсу: {e}")
            return None
 
    def convert_to_usd(self, amount_uah):
        if self.exchange_rate is None:
            print("Неможливо виконати конвертацію через відсутність курсу.")
            return None
        return round(amount_uah / self.exchange_rate, 2)
 
def main():
    converter = CurrencyConverter()
    if converter.exchange_rate is None:
        return
    try:
        amount_uah = float(input("Введіть суму в гривнях: "))
        amount_usd = converter.convert_to_usd(amount_uah)
        if amount_usd is not None:
            print(f"{amount_uah} грн ≈ {amount_usd} USD")
    except ValueError:
        print("Будь ласка, введіть коректне числове значення.")
 
if __name__ == "__main__":
    main()