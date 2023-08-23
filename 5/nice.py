import sys


#############
# Part 1
#############

class Person1:
    def __init__(self, s):
        self.my_deeds = s
    def is_nice(self):
        if self._vowel_check() and self._double_check() and self._adjacent_check():
            return True
        return False
    def _vowel_check(self):
        count = 0
        for a in 'aeiou':
            count += self.my_deeds.count(a)
        return count >= 3
    def _double_check(self):
        for i,x in enumerate(self.my_deeds):
            if i+1 < len(self.my_deeds) and self.my_deeds[i] == self.my_deeds[i+1]:
                return True #could break-else if necessary
        return False
    def _adjacent_check(self):
        for ab in ['ab','cd','pq','xy']:
            if ab in self.my_deeds:
                return False
        return True

#############
# Part 2
#############

class Person2:
    def __init__(self, s):
        self.my_deeds = s
    def is_nice(self):
        if self._double_check() and self._adjacent_check():
            return True
        return False
    def _double_check(self):
        for i,_ in enumerate(self.my_deeds):
            if i+4 < len(self.my_deeds):
                ab = self.my_deeds[i:i+2]
                if len(self.my_deeds.split(ab)) > 2:
                    return True
        return False
    def _adjacent_check(self):
        for i,_ in enumerate(self.my_deeds):
            if i+2 < len(self.my_deeds) and self.my_deeds[i] == self.my_deeds[i+2]:
                return True #could break-else if necessary
        return False

##########
# Main
##########

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as fin:
        nice_people = 0
        for line in fin:
            p = Person2(line)
            if p.is_nice():
                nice_people+=1
        print(f"nice ppl: {nice_people}")
