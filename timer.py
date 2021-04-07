class Timer:
    def __init__( self,h=0,m=0,s=0 ):
      self.h=h
      self.m=m
      self.s=s

    def __str__(self):
      return '{self.h:02d}:{self.m:02d}:{self.s:02d}'.format(self=self)

    def next_second(self):
        self.s+=1
        if self.s==60:
          self.s=0
          self.m+=1
          if self.m==60:
            self.m=0
            self.h+=1
            if self.h==24:
              self.h=0

    def prev_second(self):
        if self.s==0:
          self.s=59
          if self.m==0:
            self.m=59
            if self.h==0:
              self.h=23
            else:
              self.h-=1
          else:
            self.m-=1 
        else:
          self.s-=1



timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)

"""

Estimated time
30-60 minutes

Level of difficulty
Easy/Medium

Objectives
improving the student's skills in defining classes from scratch;
defining and using instance variables;
defining and using methods.
Scenario
We need a class able to count seconds. Easy? Not as much as you may think as we're going to have some specific expectations.

Read them carefully as the class you're about write will be used to launch rockets carrying international missions to Mars. It's a great responsibility. We're counting on you!

Your class will be called Timer. Its constructor accepts three arguments representing hours (a value from range [0..23] - we will be using the military time), minutes (from range [0..59]) and seconds (from range [0..59]).

Zero is the default value for all of the above parameters. There is no need to perform any validation checks.

The class itself should provide the following facilities:

objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the following form: "hh:mm:ss", with leading zeros added when any of the values is less than 10;
the class should be equipped with parameterless methods called next_second() and previous_second(), incrementing the time stored inside objects by +1/-1 second respectively.
Use the following hints:

all object's properties should be private;
consider writing a separate function (not method!) to format the time string.
Complete the template we've provided in the editor. Run your code and check whether the output looks the same as ours.

Expected output
23:59:59
00:00:00
23:59:59


"""