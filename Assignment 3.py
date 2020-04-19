Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> Family = ['Annie', 'JS', 'Henry', 'June', 'Ken']
>>> Hero = ['A', 'B', 'C', 'D']
>>> import random
>>> def hello():
	print(random.choice(Family + Hero))

	
>>> hello()
JS
>>> 