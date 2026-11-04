from ride import Ride, RideMatching, RideRequest, RideSharing
from users import Rider, Driver
from vehicle import Vehicle, Car, Bike

niye_jao = RideSharing("niye jao")
# print(niye_jao)


rahim = Rider("Rahim", "rahim@gmail.com", 343432, "Jatrabari", 1000)
niye_jao.add_rider(rahim)
# print(niye_jao)

khairul = Driver("Khairul", "khairul@gmail.com", 3984793, "Gulshan")
niye_jao.add_driver(khairul)
rahim.request_ride(niye_jao, "Uttare", "car")
khairul.reach_destination(rahim.current_ride)
rahim.show_current_ride()
# print(niye_jao)
