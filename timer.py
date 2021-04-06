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