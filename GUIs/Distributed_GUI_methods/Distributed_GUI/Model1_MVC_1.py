"""
This file contains the data model for the application.
"""

class DataModel:
    def __init__(self):
        self.data = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

if __name__ == '__main__':
    # In this way Model1 can run stand-alone for debugging

    data_flow= DataModel()
    data_flow.set_data([1,2,3])
    data= data_flow.get_data()
    print("Data: ", data)