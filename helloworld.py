message = "Hello World!"

for i in range(10):
	print(message)

#tässä lisää tervehdyksiä
def hello(n):
    if n == 1:
        print("ja moi!")
        return 1
    else:
        print(message)
        return hello(n - 1)
    
hello(10)
