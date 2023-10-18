import Classes

# List of Brakes

Starter_Brakes = Classes.Brakes(1,1,1,1,1, "Starter_Brakes")            # Series 0
Essence = Classes.Brakes(14,13,12,25,0.76, "Essence")                   # Series 1
Crisis_SL = Classes.Brakes(27, 16, 18, 19, 0.51, "Crisis_SL")           # Series 2
Axiom = Classes.Brakes(14, 34, 18, 15, 0.67, "Axiom")                   # Series 3
Wildcore = Classes.Brakes(36, 23, 33, 22, 0.59, "Wildcore")             # Series 5
Suspense = Classes.Brakes(20,32,23,21,0.37, "Suspense")                 # Series 8
The_Warden = Classes.Brakes(26,28,27,25,0.43, "The_Warden")             # Series 10
Onyx = Classes.Brakes(26,23,25,50,0.49, "Onyx")                         # Series 12

Brakes_teamscore = [Starter_Brakes.teamscore, Essence.teamscore, Crisis_SL.teamscore, 
                    Axiom.teamscore, Wildcore.teamscore, Suspense.teamscore, 
                    The_Warden.teamscore, Onyx.teamscore]

Brakes = [Starter_Brakes, Essence, Crisis_SL, Axiom, Wildcore, Suspense, The_Warden, Onyx]

# List of Gearboxs

Starter_Gearbox = Classes.Gearbox(1,1,1,1,1, "Starter_Gearbox")        # Series 0
Switch_R_00 = Classes.Gearbox(12,13,11,14,0.47, "Switch_R_00")     # Series 1
Swiftcharge = Classes.Gearbox(14,23,22,16,0.71, "Swiftcharger")     # Series 2
Spectrum = Classes.Gearbox(20,25,21,23,0.53, "Spectrum")        # Series 4
Verdict = Classes.Gearbox(33,18,20,30,0.63, "Verdict")         # Series 6
Kick_Shift = Classes.Gearbox(18,19,29,19,0.45, "Kick_Shift")      # Series 7
Vector = Classes.Gearbox(24,38,22,36,0.55, "Vector")          # Series 10
Voyage = Classes.Gearbox(23,28,22,27,0, "Voyage")             # Series 12

Gearbox_teamscore = [Starter_Gearbox.teamscore, Switch_R_00.teamscore, Swiftcharge.teamscore, 
                    Spectrum.teamscore, Verdict.teamscore, Kick_Shift.teamscore, 
                    Vector.teamscore, Voyage.teamscore]

Gearbox = [Starter_Gearbox, Switch_R_00, Swiftcharge, Spectrum, Verdict, Kick_Shift, Vector, Voyage]

# List of Rear wings

Starter_Rearwing = Classes.Rear_wing(1,1,1,1,1, "Starter_Rearwing")     # Series 0
Phantom_X = Classes.Rear_wing(26,15,12,11,0.76, "Phantom_X")     # Series 1
The_Matador = Classes.Rear_wing(19,16,18,17,0.72, "The_Matador")   # Series 2
The_Wasp = Classes.Rear_wing(16,24,23,14,0.69, "The_Wasp")      # Series 4
The_Patron = Classes.Rear_wing(23,21,19,37,0.61, "The_Patrom")    # Series 6
Freeflare = Classes.Rear_wing(21,33,20,22,0.37, "Freeflare")     # Series 8
Transcendence = Classes.Rear_wing(24,22,36,37,0.53, "Transcendence") # Series 9
Typhoon = Classes.Rear_wing(50,27,26,23,0.53, "Typhoon")       # Series 11

Rear_wing_teamscore = [Starter_Rearwing.teamscore, Phantom_X.teamscore, The_Matador.teamscore, 
                       The_Wasp.teamscore, The_Patron.teamscore, Freeflare.teamscore, 
                       Transcendence.teamscore, Typhoon.teamscore]

Rear_wing = [Starter_Rearwing, Phantom_X, The_Matador, The_Wasp, The_Patron, Freeflare, Transcendence, Typhoon]

# List of Front wings

Starter_Front_wing = Classes.Front_wing(1,1,1,1,1, "Starter_Front_wing")  # Series 0
The_Scout = Classes.Front_wing(13,27,15,14,0.73, "The_Scout")    # Series 1
Feral_Punch = Classes.Front_wing(13,15,22,21,0.73, "Feral_Punch")  # Series 2
The_Vagabond = Classes.Front_wing(31,20,23,21,0.35, "The_Vagabond") # Series 3
Zeno = Classes.Front_wing(25,23,22,26,0.53, "Zeno")         # Series 5
Trailblazer = Classes.Front_wing(21,23,42,20,0.57, "Trailblazer")  # Series 8
Thunderclap = Classes.Front_wing(35,23,21,33,0.55, "Thunderclap")  # Series 10
Virtue = Classes.Front_wing(23,50,27,24,0.49, "Virtue")       # Series 11

Front_wing_teamscore = [Starter_Front_wing.teamscore, The_Scout.teamscore, Feral_Punch.teamscore, 
                        The_Vagabond.teamscore, Zeno.teamscore, Trailblazer.teamscore, 
                        Thunderclap.teamscore, Virtue.teamscore]

Front_wing = [Starter_Front_wing, The_Scout, Feral_Punch, The_Vagabond, Zeno, Trailblazer, Thunderclap, Virtue]

# List of Suspesions

Starter_Suspension = Classes.Suspension(1,1,1,1,1, "Starter_Suspension")  # Series 0
The_Equator = Classes.Suspension(20,19,18,21,0.61, "The_Equator")  # Series 1
Rodeo = Classes.Suspension(23,22,15,14,0.69, "Rodeo")        # Series 3
Icon_V3 = Classes.Suspension(17,13,16,23,0.54, "Icon_V3")      # Series 4
Radiance = Classes.Suspension(25,17,26,19,0.65, "Radiance")     # Series 6
Horizon = Classes.Suspension(22,36,24,37,0.53, "Horizon")      # Series 7
Presence = Classes.Suspension(23,26,24,22,0.2, "Presence")      # Series 9
Sigma = Classes.Suspension(32,28,30,29,0.39, "Sigma")        # Series 11

Suspesion_teamscore = [Starter_Suspension.teamscore, The_Equator.teamscore, Rodeo.teamscore, 
                       Icon_V3.teamscore, Radiance.teamscore, Horizon.teamscore, 
                       Presence.teamscore, Sigma.teamscore]

Suspension = [Starter_Suspension, The_Equator, Rodeo, Icon_V3, Radiance, Horizon, Presence, Sigma]

# List of Engines

Starter_Engine = Classes.Engine(1,1,1,1,1, "Starter_Engine")      # Series 0
Brute_Force = Classes.Engine(21,19,36,18,0.63, "Brute_Force")  # Series 1
Nova = Classes.Engine(31,13,15,16,0.71, "Nova")         # Series 2
Enigma = Classes.Engine(16,13,23,25,0.69, "Enigma ")       # Series 3
Twinburst = Classes.Engine(16,29,18,18,0.51, "Twinburst")    # Series 5
The_Rover = Classes.Engine(27,25,28,24,0.53, "The_Rover")    # Series 7
Avalanche = Classes.Engine(34,22,25,21,0.35, "Avalanche")    # Series 9
Cloudroar = Classes.Engine(26,24,50,27,0.55, "Cloudroar")    # Series 12

Engine_teamscore = [Starter_Engine.teamscore, Brute_Force.teamscore, Nova.teamscore, 
                     Enigma.teamscore, Twinburst.teamscore, The_Rover.teamscore, 
                     Avalanche.teamscore, Cloudroar.teamscore]

Engine = [Starter_Engine, Brute_Force, Nova, Enigma, Twinburst, The_Rover, Avalanche, Cloudroar]

#List of Bottles

Tsar =          Classes.Bottle(0,15,0,0,0,0,10,0,25, "Tsar")
Frost =         Classes.Bottle(0,0,0,10,0,0,0,15,25, "Frost")
Tulip =         Classes.Bottle(0,0,0,20,20,0,10,0,0, "Tulip")
Dragon =        Classes.Bottle(0,0,0,15,0,20,0,0,15, "Dragon")
Kawaii =        Classes.Bottle(0,0,0,0,15,0,0,15,20, "Kawaii")
Pretzel =       Classes.Bottle(0,0,0,15,10,0,0,0,25, "Pretzel")
Vice =          Classes.Bottle(10,0,15,25,0,0,0,0,0, "Vice")
Schooner =      Classes.Bottle(0,0,0,25,15,0,10,0,0, "Schooner")
Djinn =         Classes.Bottle(0,0,15,20,0,0,15,0,0, "Djinn")
Oud =           Classes.Bottle(0,10,0,0,25,15,0,0,0, "Oud")
Eternal_Flame = Classes.Bottle(0,0,0,15,0,25,0,0,10, "Eternal_Flame")
Eagle =         Classes.Bottle(0,0,0,15,0,0,0,15,20, "Eagle")
Iron_Force =    Classes.Bottle(0,0,20,20,0,0,0,0,10, "Iron_Force")
Lumberjack =    Classes.Bottle(0,0,0,25,0,0,15,0,10, "Lumberjack")
Cranberry =     Classes.Bottle(0,0,0,10,0,20,20,0,0, "Cranberry")
Butterfly =     Classes.Bottle(0,0,25,0,5,0,0,0,20, "Butterfly")
Tune_in =       Classes.Bottle(10,15,0,0,25,0,0,0,0, "Tune_in")
Self_Control =  Classes.Bottle(0,0,5,5,0,0,0,0,5, "Self_Control")
Warrior =       Classes.Bottle(10,0,0,0,0,5,5,0,0, "Warrior")
Ballast =       Classes.Bottle(0,10,0,0,10,0,0,5,0, "Ballast")
Instinct =      Classes.Bottle(0,0,15,5,0,0,0,10,0, "Instinct")
Downforce =     Classes.Bottle(0,5,0,0,0,0,15,0,15, "Downforce")
Hex =           Classes.Bottle(15,0,0,0,5,20,0,0,0, "Hex")
Eggception =    Classes.Bottle(0,0,10,0,25,0,15,0,0, "Eggception")
Rooster =       Classes.Bottle(0,0,10,0,0,20,0,20,0, "Rooster")
Cuppa =         Classes.Bottle(0,20,0,0,0,10,0,20,0, "Cuppa")
Street_Shark =  Classes.Bottle(15,0,0,0,0,10,0,25,0, "Street_Shark")
Herald =        Classes.Bottle(0,15,0,0,0,10,0,25,0, "Herald")
Prince =        Classes.Bottle(0,20,0,0,0,0,10,20,0, "Prince")
Unstoppable =   Classes.Bottle(15,0,10,0,25,0,0,0,0, "Unstoppable")
Dead_Fast =     Classes.Bottle(25,0,20,0,0,0,0,0,5, "Dead_Fast")
Gladiator =     Classes.Bottle(0,0,10,0,0,0,25,15,0, "Gladiator")
Taurus =        Classes.Bottle(20,0,25,0,0,5,0,0,0, "Taurus")
Merlion =       Classes.Bottle(15,25,0,0,10,0,0,0,0, "Merlion")
Samba =         Classes.Bottle(5,0,25,0,20,0,0,0,0, "Samba")
Caveira =       Classes.Bottle(25,0,10,0,0,15,0,0,0, "Caveira")
Fogos =         Classes.Bottle(20,0,0,0,0,15,0,15,0, "Fogos")
Movember =      Classes.Bottle(0,25,0,0,0,0,15,0,10, "Movember")
Palmeira =      Classes.Bottle(0,0,0,0,0,0,20,10,20, "Palmeira")
Nazal =         Classes.Bottle(0,0,0,15,0,0,0,20,15, "Nazal")
Aderencia =     Classes.Bottle(0,25,0,15,0,0,0,10,0, "Aderencia")
Arco_Iris =     Classes.Bottle(20,0,0,0,0,0,25,5,0, "Arco_Iris")
Eclipse =       Classes.Bottle(25,0,0,0,10,15,0,0,0, "Eclipse")
Rena =          Classes.Bottle(0,10,0,0,20,0,20,0,0, "Rena")

Bottle = [Tsar, Frost, Tulip, Dragon, Kawaii, Pretzel, Vice, Schooner, Djinn, Oud,
          Eternal_Flame, Eagle, Iron_Force, Lumberjack, Cranberry, Butterfly, Tune_in,
          Self_Control, Warrior, Ballast, Instinct, Downforce, Hex, Eggception, Rooster,
          Cuppa, Street_Shark, Herald, Prince, Unstoppable, Dead_Fast, Gladiator, Taurus,
          Merlion, Samba, Caveira, Fogos, Movember, Palmeira, Nazal, Aderencia, Arco_Iris, Eclipse, Rena]

#List of Pilots

Verstappen = Classes.Pilots("Max_Verstappen", 97, 86, 99, 89, 94)
Leclerc = Classes.Pilots("Charles_Leclerc", 93, 99, 97, 87, 89)
Alonso = Classes.Pilots("Fernando_Alonso", 99, 92, 89, 97, 88)
Hamilton = Classes.Pilots("Lewis_Hamilton", 81, 86, 89, 94, 90)
Norris = Classes.Pilots("Lando_Norris", 99, 95, 99, 99, 99)
Russell = Classes.Pilots("George_Russell", 95, 90, 91, 83, 86)
Perez = Classes.Pilots("Sergio_Perez", 85, 96, 89, 91, 84)
Sainz = Classes.Pilots("Carlos_Sainz", 84, 85, 95, 90, 91)
Stroll = Classes.Pilots("Lance_Stroll", 92, 83, 87, 94, 89)
Gasly = Classes.Pilots("Pierre_Gasly", 88, 93, 83, 85, 96)

Pilots = [Verstappen, Leclerc, Alonso, Hamilton, Norris, Russell, Perez, Sainz, Stroll, Gasly]
