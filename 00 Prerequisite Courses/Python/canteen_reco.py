# Author: Nirmallya Mukherjee
#
# This program is provided as part of the training and does not carry any warranty
# Using this code in any other context will be at your own risk.
#

#The below lists will have a one to one relationships. At a later point in time these can be read from a CSV as well
canteens = ["canteen1", "canteen2", "canteen3", "canteen4", "canteen5", "canteen6"]   #Will contain the name of the canteens
price_range = [(10,20), (65,200), (20,40), (15,25), (5,35)]  #will contain the min and max price range of each of the canteens as a tuple


def get_price():
    while True:
        try:
            money = int(input("How much you are willing to spend upto 200 bucks? "))
            if money > 200:
                raise Exception("You have too much money! you need to find a better canteen :)")
            break

        except Exception as ex:
            print(ex)

    return money


def filter_canteens(money):
  #The program needs to create a dictionary of the matching canteen as the key and the corresponding price range tuple as the value
  result_set={}

  for canteen, price_r in zip(canteens, price_range):
    if(price_r[0]<=money and money<=price_r[1]):
      result_set.update({canteen:price_r})

  #Let's sort the dictionary based on the second value of the tuple!
  sorted_result_set = sorted(result_set.items(), key = lambda e: e[1][1], reverse=True)
  return sorted_result_set


def pretty_print(sorted_result_set):
  #Let's pretty print the results for a better human readable output
  for el in sorted_result_set:
    print(el[0], "has a min price of", el[1][0], " and max price of", el[1][1])


def main():
  money = get_price()
  sorted_result_set = filter_canteens(money)
  pretty_print(sorted_result_set)


if __name__ == "__main__":
    main()

