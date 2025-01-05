def main():
# example data
    gradient = lambda x,y : [(2*x) -4,(2*y) + 6]
    alpha = 0.01
    x0 = 0
    y0 = 0
    while True:
        x = [x0,y0]
        y = multiply(alpha,gradient(x0,y0))
        new_answer = minus(x,y)
        print(new_answer)
        x0 = new_answer[0]
        y0 = new_answer[1]
        if abs(x[0]-new_answer[0]) < 0.0005 :
            break
def minus(x,y):
    xy = []
    for i in range(len(x)):
        xy.append(x[i]-y[i])
    return xy
def multiply(alpha,g):
    xy = []
    for i in g:
        xy.append(alpha*i)
    return(xy)
if __name__ == "__main__":
    main()