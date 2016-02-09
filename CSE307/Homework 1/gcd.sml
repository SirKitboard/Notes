fun gcd(a,b):int = if a=b then a
else if a>b then gcd(a-b,b)
else gcd(a,b-a);