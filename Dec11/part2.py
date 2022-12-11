from dataclasses import dataclass, field

@dataclass
class Monkey:
    items: list[int] = field(default_factory=list)
    op_string: str = ""
    divisor: int = 0
    on_true: int = 0
    on_false: int = 0
    id: int = 0
    inspections: int = 0

    def use_operation(self, old):
        return eval(self.op_string)

monkeys: list[Monkey] = []
common_divisor = 1
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        parts = line.split(":")
        words = line.split()

        if parts[0][0:6] == "Monkey":
            monkey_id = int(words[1][:-1])
            monkeys.append(Monkey())
            monkeys[-1].id = monkey_id

        elif parts[0] == "Starting items":
            items = [int(x) for x in parts[1].split(",")]
            monkeys[-1].items = items

        elif parts[0] == "Operation":
            rhs = parts[1].split("=")[1].strip()
            monkeys[-1].op_string = rhs

        elif parts[0] == "Test":
            divisor = int(line.split()[-1])
            common_divisor *= divisor
            monkeys[-1].divisor = divisor

        elif parts[0] == "If true":
            on_true = int(words[-1])
            monkeys[-1].on_true = on_true

        elif parts[0] == "If false":
            on_false = int(words[-1])
            monkeys[-1].on_false = on_false

for round in range(10000):
    for monkey in monkeys:
        while len(monkey.items) > 0:
            monkey.inspections += 1

            worry = monkey.items.pop(0)
            after_op = monkey.use_operation(worry)
            new_worry = after_op % common_divisor

            if new_worry % monkey.divisor == 0:
                monkeys[monkey.on_true].items.append(new_worry)
            else:
                monkeys[monkey.on_false].items.append(new_worry)

inspection_counts = []
for monkey in monkeys:
    inspection_counts.append(monkey.inspections)

inspection_counts.sort(reverse=True)
print(inspection_counts)
print(inspection_counts[0] * inspection_counts[1])