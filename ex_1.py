def caching_fibonacci():
    cache={} #Створити порожній словник cache
    def fibonacci(n): #внутр. функція перевіряє n і записує в кеш
         if n<=0 : #Якщо n <= 0, повернути 0
             return 0
         if n==1 :  #  Якщо n == 1, повернути 1
             return 1 
         if n in cache: #Якщо n у cache, повернути cache[n]
             return cache[n]  
         
         cache[n] = fibonacci(n-1)+ fibonacci(n-2)
         return cache[n]
    
    return fibonacci

fib=caching_fibonacci() #присвоюємо функцію
print(fib(10))
print(fib(20))
