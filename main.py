from typing import List, Dict
import datetime


# эмулируем функцию получения текущей дислокации вагонов
def get_current_dislocation() -> List[Dict[str, any]]:
    return [
        {'car_id': 1, 'arrival_date': '2022-12-31', 'invoice': 'inv1'},
        {'car_id': 2, 'arrival_date': None, 'invoice': 'inv2'},
        {'car_id': 3, 'arrival_date': None, 'invoice': 'inv3'}
    ]


# эмулируем функцию предсказания даты прибытия по накладной
def get_predicted_date_by_invoices(invoice_list: List[str]) -> Dict[str, str]:
    predicted_dates = {}
    for invoice in invoice_list:
        predicted_dates[invoice] = '2022-12-31'
    return predicted_dates


# главная функция, которая вызывает две эмулированные функции
def api_call() -> List[Dict[str, any]]:
    # получаем список вагонов и их текущую дислокацию
    dislocation_list = get_current_dislocation()

    # формируем список накладных для вагонов, у которых нет даты прибытия
    missing_arrival_dates = []
    for car in dislocation_list:
        if not car['arrival_date']:
            missing_arrival_dates.append(car['invoice'])

    # вызываем функцию предсказания даты прибытия и получаем словарь с предсказанными датами
    predicted_arrival_dates = get_predicted_date_by_invoices(missing_arrival_dates)

    # обновляем даты прибытия для вагонов без этой информации
    for car in dislocation_list:
        if not car['arrival_date']:
            car['arrival_date'] = predicted_arrival_dates[car['invoice']]

    return dislocation_list


# пример использования функции api_call
dislocation_list_with_predictions = api_call()
for car in dislocation_list_with_predictions:
    print(car)