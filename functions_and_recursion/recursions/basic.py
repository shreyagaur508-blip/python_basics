#recursive function
def show(n):
    if n == 0: #base case
        return #base case
    print(n)
    show(n-1)

show(5)