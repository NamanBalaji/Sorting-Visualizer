import time

def selectionSort(data, drawData, timeTick):
    for i in range(len(data)): 
      min_idx = i 
      for j in range(i+1, len(data)): 
        if data[min_idx] > data[j]: 
            min_idx = j
            drawData(data, ['green'if x == i or x == i+1 else 'red' for x in range(len(data))] )
            time.sleep(timeTick)      
      data[i], data[min_idx] = data[min_idx], data[i]
    drawData(data, ['green' for x in range(len(data))])  