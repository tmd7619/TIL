import pandas as pd

''' 1. displ(배기량)이 4 이2하인 자동차와 5 이상인 자동차 중
어떤 자동차의 hwy(고속도로 연비)가 평균적으로 더 높은지 확인하세요.'''

class Car(object):

    sum = 0

    def __init__(self, manufacturer, model, displ, year, cyl, trans, drv,
                 cty, hwy, fl, carclass):

        self.manufacturer = manufacturer
        self.model = model
        self.displ = displ
        self.year = year
        self.cyl = cyl
        self.trans = trans
        self.drv = drv
        self.cty = cty
        self.hwy = hwy
        self.fl = fl
        self.carclass = carclass
        self.avg = (cty + hwy)/2

        # print("{}{}가 생성되었습니다.".format(self.manufacturer, self.model))


    def __repr__(self):
        return "{} {} {} {} {} {} {} {} {} {} {}".format(self.manufacturer, self.model, self.displ, self.year, self.cyl,
                                                  self.trans, self.drv, self.cty, self.hwy, self.fl, self.carclass, self.avg)

file = open(" "r")
car_list = list()
line = file.readline()
while True:
    line = file.readline()
    if not line:
        break

    line = line.replace("\n", "")
    car_data = line.split(",", 11)

    #print(car_data)
    car_list.append(Car(car_data[0], car_data[1], float(car_data[2]),
                        int(car_data[3]), int(car_data[4]), car_data[5],
                        car_data[6], int(car_data[7]), int(car_data[8]),
                        car_data[9], car_data[10]))