motrocycles = ['honda','yamaha','suzuki']
print(motrocycles)
motrocycles[0]='ducati'
print(motrocycles[0])

motrocycles.append('ducati')
print(motrocycles)

motrocycles = []
motrocycles.append('honda')
motrocycles.append('yamaha')
motrocycles.append('suzuki')
print(motrocycles)

motrocycles = ['honda','yamaha','suzuki']
motrocycles.insert(0,'ducati')
print(motrocycles)

motrocycles = ['honda','yamaha','suzuki']
print(motrocycles)
del motrocycles[0]
print(motrocycles)


motrocycles = ['honda','yamaha','suzuki']
print(motrocycles)

popped_motrocycle=motrocycles.pop()
print(motrocycles)
print(popped_motrocycle)

motrocycles = ['honda','yamaha','suzuki']

last_owned = motrocycles.pop()
print("The last motrocycles I owned was a "+last_owned+".")

first_owned = motrocycles.pop(0)
print("The first motrocycles I owned was a "+first_owned+".")

motrocycles = ['honda','yamaha','suzuki','ducati']
print(motrocycles)

motrocycles.remove('ducati')
print(motrocycles)

motrocycles = ['honda','yamaha','suzuki','ducati']
print(motrocycles)

too_expensive = 'ducati'
motrocycles.remove(too_expensive)
print(motrocycles)
print("\nA "+too_expensive.title()+" is too expensive for me.")
