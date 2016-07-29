class Student(object):
          def __init__(self,name,score):
                 self.__name = name
                 self.__score = score

          def print_score(self):
                    print('%s: %s' % (self.__name, self.__score))
          def return_name(self):
                    return self.__name

          def print_grade(self):
                     if self.__score > 90:
                                  return 'A'
                     elif self.__score > 60:
                             return 'B'
                     else:
                            return 'C'


bart = Student('Bart mkasdf',95)
lisa = Student('Lisa',88)
rick = Student('Rick',55)
bart.print_score()
lisa.print_score()
rick.print_score()
print(bart.print_grade())
print(lisa.print_grade())
print(rick.print_grade())
bart.__name = 'matt'
print(bart.__name)
bart._Student_name = 'liyu'
print(bart._Student_name)
bart.print_score()
print(bart.return_name())
