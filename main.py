import phonenumbers
from test import number

from phonenumbers import geocoder

loct = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(loct,"en"))

from phonenumbers import carrier
service = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service,"en"))

# i would like to add a comment here
# ho ho yestai ho


##i aslo added a another comment here and i am going to add a third comment
