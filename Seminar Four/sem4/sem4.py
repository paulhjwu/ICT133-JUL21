def double(x):
    x = x.append(2)
    z = x
    return z

def main():
    z = [1]
    x = [10]
    y = double(x)
    print(x, y)

main()