# Patrick Johnson         3/16/2020 #
# SWDV 630 3W 20/SP2         Week 1 #
#####################################

# 1) Add the __contains__ protocol and show whether or not  'Tim' and
#    'Sam' are part of our team.  
# 
# 2) Add the __iter__ protocol and show how you can print each member
#    of the classmates object.
# 
# 3) Determine if the class classmates implements the __len__ method.
# 
# 4) Explain the difference between interfaces and implementation. 
# 
# 5) Using both visual and written descriptions, think through the
#    interface-implementation of a large scale storage system.   In
#    many systems today, we have the ability to store information 
#    from a single application to a variety of storage devices - local
#    storage (hard drive, usb), the cloud and/or some new medium in 
#    the future.   How would you design an interface structure such 
#    that all of the possible implementations could store data effectively.

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

    print('1. Steve in classmates:  ','Steve' in classmates) 
    print('   Sam in classmates:    ','Sam' in classmates)
    
    print('2. Iterate over classmates:')
    for classmate in classmates:
        print(classmate)
    
    print('3. Length of classmates: ',len(classmates))
main()