import sys
sys.path += ['stub/','../../modules/stub/','../modules/stub/','../modules','../bases','../../modules','../../bases']
import VS
import Director

def kfac (k):
    if (k==0):
        return 1
    return k*kfac(k-1)
Director.dontdoprint=1
import generate_dyn_universe
import dynamic_battle
dynamic_battle.UpdateCombatTurn()
import fg_util
conf = fg_util.SortedAllShips ('confed')
aera = fg_util.SortedAllShips ('aera')
def doit(n=1000):
    for i in range(n):
        dynamic_battle.UpdateCombatTurn()

    
doit(10000)
print 'hi'
import dynamic_mission
Director.dontdoprint=0
#VS.pushSystem("SYSTEMvs")
dynamic_mission.CreateMissions()
#VS.popSystem()
