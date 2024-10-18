function factorial(n::Int) 
   if n == 0 || 1
	   return 1
   else
	   result = n*factorial(n-1)
   end
end

print(factorial(5))
