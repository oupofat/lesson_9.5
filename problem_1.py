def lowest_score(scores):
    x = 10
    for low in scores:
        if low < x:
            x = low    
    return (x)
def highest_score(scores):
    y = 0
    for high in scores:
        if high > y:
            y = high        
    return (y)

def total_score(scores):
    lowest = lowest_score(scores)
    highest = highest_score(scores)
    total =sum(scores) - lowest - highest
    lenght = len(scores)
    average = total / (lenght - 2)
    return average

    
scores = [7, 8, 9, 10, 5, 6, 7, 3, 4]


totals = total_score(scores)
print (totals)