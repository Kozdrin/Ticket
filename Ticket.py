quant_ticket = int(input("Введите количество билетов, которые Вы хотите приобрести,\nесли Вы приобретаете больше 3 билетов, то получаете скидку 10% на заказ:\t"))
total_cost = 0
if quant_ticket > 3:
    diskount = True
else:
    diskount = False
for i in range(quant_ticket):
    age = int(input("Введите возраст посетителя:\t"))
    if age < 18:
        ticket_cost = 0
    elif 18 <= age < 25:
        ticket_cost = 990
    elif age >= 25:
        ticket_cost = 1390
    total_cost += ticket_cost
if diskount:
        total_cost_disc = total_cost*90/100
        diskount_cost = total_cost - total_cost_disc  #Ввел сумму скидки (мне кажется клиенту приятно видеть свою экономию)
print("Количество билетов :",quant_ticket, "Общая стоимость заказа :", total_cost)
if diskount:
    print("Общая стоимость заказа со скидкой :", total_cost_disc, "Сумма скидки", diskount_cost)