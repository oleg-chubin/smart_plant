from fake import sensors, switchers
import time
import os
import pandas as pd
import openpyxl
from openpyxl.chart import ScatterChart, Reference, Series

os.chdir('C:\\Users\\trofi\\PycharmProjects\\untitled2\\HW_8\\smart_plant')

BIO_CYCLE = []
dict_to_excel = {}
time_data = []
full_time_data = []
light_data = []
temperature_data = []
moisture_data = []
humidity_data = []


def data_to_excel():
    time_data.append(round(x_time[0]))
    full_time_data.append(round(x_time[1]))
    light_data.append(sensors.light1.get_value() + (sensors.light2.get_value()))
    temperature_data.append(round(sensors.temperature.get_value(), 2))
    moisture_data.append(round(sensors.moisture.get_value(), 2))
    humidity_data.append(round(sensors.humidity.get_value(), 2))
    dict_to_excel.update({'Bioсycle Time': time_data, 'Full Time': full_time_data, 'Temperature': temperature_data,
                          'Moisture': moisture_data, 'Humidity': humidity_data, 'Light': light_data})


def timer():
    cycle_time_count = time.time() - time_zero
    full_time_count = time.time() - full_time_zero
    return [cycle_time_count, full_time_count]


def bio_cycle_gen():
    period = int(input('\n' + 'Введите желаемое время цикла в секундах '))
    light = int(input('Введите желаемый уровень освещения в люменах (доступно три режима: 0, 500 и 1000 люмен) '))
    temperature = float(input('Введите желаемую температуру в градусах Цельсия '))
    moisture = float(input('Введите желаемую влажность почвы в % '))
    humidity = float(input('Введите желаемую влажность воздуха в % '))
    bio_cycle = {}
    bio_cycle.update({'period': period, 'light': light, 'temperature': temperature,
                      'moisture': moisture, 'humidity': humidity})
    return bio_cycle


class DeviceOperator:
    def check_and_control(self, set_value, sensor_value, switcher):
        if set_value > sensor_value:
            switcher.turn_on()
        elif set_value < sensor_value:
            switcher.turn_off()


print('###############  НЯНЕЧКА ДЛЯ КАБАЧКА  ###############')
print('          Давайте настроим нашу тепличку' + '\n')
print('Хотите загрузить данные по биоциклам из файла BIO.txt?')
print('Если да - введите любой символ и нажмите Enter')
read_BIO = bool(input('Если нет - просто нажмите Enter' + '\n'))
if read_BIO is False:
    print('Давайте настроим биоцикл')
    BIO_CYCLE.append(bio_cycle_gen())
    print('\n' + 'Хотите добавить еще один биоцикл?')
    print('Если да - введите любой символ и нажмите Enter')
    new_cycle = bool(input('Если нет - просто нажмите Enter' + '\n'))

    while new_cycle is True:
        BIO_CYCLE.append(bio_cycle_gen())
        print('\n' + 'Хотите добавить еще один биоцикл?')
        print('Если да - введите любой символ и нажмите Enter')
        new_cycle = bool(input('Если нет - просто нажмите Enter' + '\n'))

    with open('BIO_CYCLE_input.txt', 'w', encoding='utf-8') as f:
        for cycle in BIO_CYCLE:
            f.write(repr(cycle) + '\n')
    print('Данные по введенным биоциклам Вы сможете найти в файле   BIO_CYCLE_input.txt')
else:
    with open('BIO.txt', 'r', encoding='utf-8') as f:
        for line in f:
            BIO_CYCLE.append(eval(line))

print('Показания датчиков и графики отображаются в файле   BIO_Data.xlsx')
time.sleep(5)

time_zero = time.time()
full_time_zero = time.time()

switchers.temperature.turn_on()
switchers.moisture.turn_on()
switchers.humidity.turn_on()
switchers.light1.turn_on()
switchers.light2.turn_on()

while True:
    for cycle in BIO_CYCLE:
        while True:
            x_time = timer()
            if cycle.get('period') > x_time[0]:
                temp_operator = DeviceOperator()
                temp_operator.check_and_control(cycle.get('temperature'), sensors.temperature.get_value(),
                                                switchers.temperature)

                moist_operator = DeviceOperator()
                moist_operator.check_and_control(cycle.get('moisture'), sensors.moisture.get_value(),
                                                 switchers.moisture)

                hum_operator = DeviceOperator()
                hum_operator.check_and_control(cycle.get('humidity'), sensors.humidity.get_value(),
                                               switchers.humidity)

                light_operator1 = DeviceOperator()
                light_operator1.check_and_control(cycle.get('light'), (sensors.light1.get_value() +
                                                                       sensors.light2.get_value()),
                                                  switchers.light1)
                light_operator2 = DeviceOperator()
                light_operator2.check_and_control(cycle.get('light'), (sensors.light1.get_value() +
                                                                       sensors.light2.get_value()),
                                                  switchers.light2)

                if round(x_time[0] % 2) == 0:
                    print(f'Current BioCycle {cycle}')
                    print(f'Light            {sensors.light1.get_value() + (sensors.light2.get_value())}')
                    print(f'Temperature      {round(sensors.temperature.get_value(), 2)}')
                    print(f'Moisture         {round(sensors.moisture.get_value(), 2)}')
                    print(f'Humidity         {round(sensors.humidity.get_value(), 2)}')
                    print(f'BioCycle Timer   {round(x_time[0])}')
                    print(f'Full Timer       {round(x_time[1])}' + '\n')

                    data_to_excel()

                    x = pd.DataFrame(dict_to_excel)
                    x.to_excel('./BIO_Data.xlsx', sheet_name='BIO', index=False)

                    wb = openpyxl.load_workbook('BIO_Data.xlsx')
                    sheet = wb.active
                    sheet.column_dimensions['A'].width = 16
                    sheet.column_dimensions['B'].width = 12
                    sheet.column_dimensions['C'].width = 14
                    sheet.column_dimensions['D'].width = 11
                    sheet.column_dimensions['E'].width = 11
                    chart = ScatterChart()
                    chart.title = 'BIO DATA'
                    chart.x_axis.title = 'Time'
                    chart.y_axis.title = 'Value'
                    x_values = Reference(sheet, min_col=2, min_row=2, max_row=sheet.max_row)

                    for i in range(3, 6):
                        values = Reference(sheet, min_col=i, min_row=1, max_row=sheet.max_row)
                        series = Series(values, x_values, title_from_data=True)
                        chart.series.append(series)

                    chart_light = ScatterChart()
                    chart_light.title = 'LIGHT'
                    chart_light.x_axis.title = 'Time'
                    chart_light.y_axis.title = 'Value'
                    light_values = Reference(sheet, min_col=6, min_row=1, max_row=sheet.max_row)
                    series = Series(light_values, x_values, title_from_data=True)
                    chart_light.series.append(series)

                    sheet.add_chart(chart, "I2")
                    sheet.add_chart(chart_light, "I19")

                    wb.save('BIO_Data.xlsx')

                time.sleep(0.5)

            else:
                time_zero = time.time()
