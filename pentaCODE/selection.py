class Selection_Sorting():
    def __init__(self):
        self.list = []
    
    def add_data(self, data):
        self.list.append(data)
    
    def selection_sort(self):
        lowest = self.list[0]
        current_lowest = 0
        index = 0
        for i in range(0, len(self.list)):
            for j in range(0, len(self.list)):
                if j == len(self.list)-1:
                    if self.list[j] < self.list[j-1] and (self.list[j] <= lowest) and (self.list[j] > current_lowest):
                        lowest = self.list[j]
                        index = j
                elif self.list[j] == current_lowest:
                    pass
                elif self.list[j] < self.list[j+1] and (self.list[j] <= lowest) and (self.list[j] > current_lowest):
                    lowest = self.list[j]
                    index = j
                elif self.list[j+1] < self.list[j] and (self.list[j+1] <= lowest) and (self.list[j+1] > current_lowest):
                    lowest = self.list[j+1]
                    index = j+1
                j+=1
            if current_lowest != lowest:
                self.list[i], self.list[index] = self.list[index], self.list[i]
                current_lowest = lowest
                i+=1
                if i == len(self.list)-1:
                    break
                lowest = self.list[i]
                print(self.list)