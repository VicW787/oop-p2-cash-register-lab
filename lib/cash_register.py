#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
      self._discount = 0
      self.total = 0
      self.items = []
      self.previous_transactions = []    
      self.discount = discount

  @property
  def discount(self):
      return self._discount

  @discount.setter
  def discount(self, value):
      if type(value) == int and 0 <= value <= 100:
          self._discount = value
      else:
          print("Not valid discount")

  def add_item(self, item, price, quantity=1):
      self.total += price * quantity
      for i in range(quantity):
          self.items.append(item)

      transaction = {"item": item, "price": price, "quantity": quantity}
      self.previous_transactions.append(transaction)

  def apply_discount(self):
      if len(self.previous_transactions) == 0 or self.discount == 0:
        print("There is no discount to apply.")
      else:
          self.total = self.total - (self.total * self.discount / 100)
          if self.total == int(self.total):
              self.total = int(self.total)         
          print(f"After the discount, the total comes to ${self.total}.")

  def void_last_transaction(self):
      if len(self.previous_transactions) == 0:
          print("There are no transactions to void.")
      else:
          last = self.previous_transactions.pop()
          self.total -= last["price"] * last["quantity"]
          for i in range(last["quantity"]):
                self.items.pop() 



      