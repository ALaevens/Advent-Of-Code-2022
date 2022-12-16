class Valve:
    def __init__(self, name, flow, connections):
        self.name = name
        self.flow = flow
        self.connections = connections

    def __str__(self):
        return f"Valve(name: {self.name}, flow: {self.flow}, connections: {self.connections})"

    def __repr__(self) -> str:
        return self.__str__()

def dfs(valve_name: str, valves: dict[Valve], depth=0):
    pass


with open("input.txt") as f:
    valves = {}

    for line in f:
        parts = line.strip().split()
        valve = parts[1]
        rate = int(parts[4][5:-1])
        connections = "".join(parts[9:]).split(",")

        valves[valve] = Valve(valve, rate, connections)

    print(dfs("AA", valves))




