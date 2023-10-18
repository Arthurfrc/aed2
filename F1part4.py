import Functions
import Classes
import Parts
from Classes import Brakes, Gearbox, Rear_wing, Front_wing, Suspension, Engine, Bottle, Pilots
from Parts import Brakes, Gearbox, Rear_wing, Front_wing, Suspension, Engine, Bottle, Pilots

#Quero pegar os maiores valores, p/ isso posso percorrer a lista de objetos de cada classe

best_brake = max(Brakes, key=lambda brakes: brakes.teamscore)
best_gearbox = max(Gearbox, key=lambda gearbox: gearbox.teamscore)
best_rear_wing = max(Rear_wing, key=lambda rear_wing: rear_wing.teamscore)
best_front_wing = max(Front_wing, key=lambda front_wing: front_wing.teamscore)
best_suspension = max(Suspension, key=lambda suspension: suspension.teamscore)
best_engine = max(Engine, key=lambda engine: engine.teamscore)
best_bottle = max(Bottle, key=lambda bottle: bottle.teamscore)
best_pilot = max(Pilots, key=lambda pilots: pilots.teamscore)

print(f"Melhor freio: {best_brake.name} - Teamscore: {best_brake.teamscore}")
print(f"Melhor gearbox: {best_gearbox.name} - Teamscore: {best_gearbox.teamscore}")
print(f"Melhor rear wing: {best_rear_wing.name} - Teamscore: {best_rear_wing.teamscore}")
print(f"Melhor front wing: {best_front_wing.name} - Teamscore: {best_front_wing.teamscore}")
print(f"Melhor suspensão: {best_suspension.name} - Teamscore: {best_suspension.teamscore}")
print(f"Melhor motor: {best_engine.name} - Teamscore: {best_engine.teamscore}")
print(f"Melhor garrafa: {best_bottle.name} - Teamscore: {best_bottle.teamscore}")
print(f"Melhor piloto: {best_pilot.name} - Teamscore: {best_pilot.teamscore}")

total = best_brake.teamscore + best_gearbox.teamscore + best_rear_wing.teamscore + best_front_wing.teamscore + best_suspension.teamscore + best_engine.teamscore + best_bottle.teamscore + best_pilot.teamscore

print(f"Total: {total}")

