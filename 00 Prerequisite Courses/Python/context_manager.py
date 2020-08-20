# Author: Nirmallya Mukherjee
#
# This program is provided as part of the training and does not carry any warranty
# Using this code in any other context will be at your own risk.
#

class FileResource():
  def __init__(self, filename, mode):
    self.filename = filename
    self.mode = mode
    self.file = None  #File handle
    print('Initializing the file resource context manager')

  def __enter__(self):
    self.file = open(self.filename, self.mode)
    print('Opened the file resource')
    return self.file

  def __exit__(self, exc_type, exc_value, exc_traceback):
    #The parameters in this method are used to manage exceptions
    print("Exec type:", type(exc_type), "\nValue:",  type(exc_value), "\nTraceback:", type(exc_traceback))
    print('\nClosing the file resource')
    self.file.close()


with FileResource('inpfile1.csv', 'r') as inpFile:
  for line in inpFile:
    print("Line is", line)

