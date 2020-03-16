# Patrick Johnson         3/16/2020 #
# SWDV 630 3W 20/SP2         Week 1 #
#####################################
# Expansion of Teams class provided in assignment:
# 1) Add the __contains__ protocol and show whether or not  'Tim' and
#    'Sam' are part of our team.  
# 2) Add the __iter__ protocol and show how you can print each member
#    of the classmates object.
# 3) Determine if the class classmates implements the __len__ method.

class Teams:
    def __init__(self, members):
        self.__myTeam = members

    def __len__(self):
        return len(self.__myTeam)

    def __contains__(self, member):
        return member in self.__myTeam
    
    def __iter__(self):
        self.__i = 0
        return self
        
    def __next__(self):
        if self.__i < len(self.__myTeam):
            nextItem = self.__myTeam[self.__i]
            self.__i += 1
            return nextItem
        else:
            raise StopIteration

def main():
    classmates = Teams(['John', 'Steve', 'Tim'])

    print('1. Tim in classmates:','Tim' in classmates) 
    print('   Sam in classmates:','Sam' in classmates)
    
    print('2. Iterate over classmates:')
    for classmate in classmates:
        print(classmate)
    
    print('3. Length of classmates:',len(classmates))
    
main()

