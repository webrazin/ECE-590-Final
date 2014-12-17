import hubo_ach as ha
import ach
import sys
import time
import math
from ctypes import *


# Open Hubo-Ach feed-forward and feed-back (reference and state) channels
s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
r = ach.Channel(ha.HUBO_CHAN_REF_NAME)

# feed-forward will now be refered to as "state"
state = ha.HUBO_STATE()

# feed-back will now be refered to as "ref"
ref = ha.HUBO_REF()

def simdelay(simtime, delay):
	ti=simtime
	t = simtime + delay	
	while(simtime < t):		
		[statuss, framesizes] = s.get(state, wait=False, last=False)
		return simtime

def raisehand():
    REB=0
    LEB=0
    for i in range(0,500):
      REB=REB+0.004
      ref.ref[ha.RSP] = -REB
      LEB=LEB+0.001
      ref.ref[ha.RSR] = -LEB
      r.put(ref)
      r.put(ref)

def wave1():
    REB=0
    LEB=0
    for i in range(0,500):
      
      LEB=LEB+0.001
      ref.ref[ha.RSR] = -LEB
      r.put(ref)
      r.put(ref)

    while((state.time-simtime)<=1):
        [statuss, framesizes] = s.get(state, wait=False, last=False) 
        t=state.time-simtime    
def wave():
    REB=2
    LEB=.5
    for i in range(0,500):
      LEB=LEB-0.002
      ref.ref[ha.RSR] = -LEB
      r.put(ref)
      r.put(ref)

    while((state.time-simtime)<=1):
        [statuss, framesizes] = s.get(state, wait=False, last=False) 
        t=state.time-simtime     
raisehand();
while(1):
# Get the current feed-forward (state) 
  [statuss, framesizes] = s.get(state, wait=False, last=False)
  simtime=state.time
  
  wave();
  wave1();
 
  while((state.time-simtime)<=2):
        [statuss, framesizes] = s.get(state, wait=False, last=False) 
        t=state.time-simtime
        print t
  
