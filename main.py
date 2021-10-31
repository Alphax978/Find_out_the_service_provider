import phonenumbers
from test import number

from phonenumbers import geocoder

loct = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(loct,"en"))

from phonenumbers import carrier
service = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service,"en"))
