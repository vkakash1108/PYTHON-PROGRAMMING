class Solve():
   def Anagrams( self, li ):

       dictionary = {}
       for word in li:
           sortedWord = ''.join(sorted(word))

           if sortedWord not in dictionary:
               dictionary[sortedWord] = [word]

           else:
               dictionary[sortedWord] += [word]
       return [dictionary[i] for i in dictionary]

if _name_ == '_main_':
   li = ['eat','tea','tan','ate','nat','bat']

   print(Solve().Anagrams(li))
