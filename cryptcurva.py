import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def update_c_label(event):
    code = combobox.get()
    name = cur[code]
    c_label.config(text = name)


def exchange():
    code = combobox.get()

    code_dollar = 'usd'

    if code and code_dollar:
        try:
            response = requests.get(
                'https://api.coingecko.com/api/v3/exchange_rates?x_cg_demo_api_key=CG-4w4KCPwRCfNLjRrWtQGvKHkP')
            response.raise_for_status()
            data = response.json()
            if code in data['rates']:

                if code_dollar in data['rates']:
                    exchange_rate = data['rates'][code_dollar]['value'] / data['rates'][code]['value']
                    mb.showinfo('Курс обмена', f'Курс: 1 {cur[code]} = {exchange_rate:.2f} $. ')
            else:
                mb.showerror('Ошибка!', f'Валюта {code} не найдена.')
        except Exception as e:
            mb.showerror('Ошибка', f'Произошла ошибка: {e}.')
    else:
        mb.showwarning('Внимание!', 'Введите код валюты.')


window = Tk()
window.title('Курсы обмена валют')
window.geometry('360x180')

Label(text='Выберите криптовалюту:').pack(padx=10, pady=10)
cur = {
    'btc': 'Биткоин',
    'eth': 'Эфириум',
    'bch': 'Биткоин Кэш',
    'bits': 'Битс',
    'bnb': 'Бинанс коин',
    'eos': 'ЕОС',
    'link': 'Чайнлинк',
    'ltc': 'Лайткоин',
    'dot': 'Полкадот',
    'xlm': 'Люменс'
}

combobox = ttk.Combobox(values = list(cur.keys()))
combobox.pack(padx=10, pady=10)
combobox.bind('<<ComboboxSelected>>', update_c_label)

c_label = ttk.Label()
c_label.pack(padx = 10, pady = 10)

# entry = Entry()
# entry.pack(padx = 10, pady = 10)

Button(text='Курс обмена к доллару США', command=exchange).pack(padx=10, pady=10)

window.mainloop()