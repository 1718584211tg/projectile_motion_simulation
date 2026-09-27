#     dictionary
#    一组数：data = { "key":value, ...}   ; 多组数：data = [ {"key":value, ...}, ...]
particle = {
    "mass": 5,
    "velocity": 10,
    "height": 50
}
print(particle)
print(particle["mass"])
print(particle["velocity"])
print(particle["height"])
particle["velocity"] = 20
particle["gravity"] = 9.8
print(particle)
#    删除： del dictionary["key"]
#    获取： print(dictionary.key())  ;  print(dictionary.value())
#    同时获取key跟value： print(dictionary,items())

#     计算
particle = {
    "mass": 5,
    "velocity": 10,
    "height": 50
}
mass = particle["mass"]
velocity = particle["velocity"]
kinetic_energy = 0.5*mass*velocity**2
print("Mass:", mass, "(kg)")
print("Velocity:", velocity, "(m/s)")
print("Kinetic Energy:", kinetic_energy, "(J)")

#     dictionary + for
experiment = {
    "mass": 2,
    "velocity": 15,
    "height": 30,
    "gravity": 9.8
}
for key, value in experiment.items():
    print(key, value)

#     list + dictionary
experiments = [
    {"mass": 2, "velocity": 10},
    {"mass": 5, "velocity": 20},
    {"mass": 3, "velocity": 15}
]
for experiment in experiments:
    mass = experiment["mass"]
    velocity = experiment["velocity"]
    energy = 0.5*mass*velocity**2
    print("Mass :", mass, "kg; Velocity :", velocity, "m/s; Kinetic Energy :", energy, "J")

#    组织数据
experiments = [
    {"mass": 2, "velocity": 10},
    {"mass": 5, "velocity": 20},
    {"mass": 3, "velocity": 15}
]
for experiment in experiments:
    mass = experiment["mass"]
    velocity = experiment["velocity"]
    energy = 0.5*mass*velocity**2
    experiment["energy"] = energy
print(experiments)