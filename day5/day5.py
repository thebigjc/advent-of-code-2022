from aocd import lines, submit
from itertools import batched
from parse import parse

stacks_a = []
stacks_b = []


def push_bottom(stacks, stack, value):
    while len(stacks) <= stack:
        stacks.append([])
    stacks[stack].insert(0, value)


done_stacks = False

for line in lines:
    pushed_any = False
    if not done_stacks:
        stack_slots = batched(line, 4)
        for i, stack_slot in enumerate(stack_slots):
            if stack_slot[1].isupper():
                push_bottom(stacks_a, i, stack_slot[1])
                push_bottom(stacks_b, i, stack_slot[1])

                pushed_any = True
        if not pushed_any:
            done_stacks = True
    else:
        p = parse("move {:d} from {:d} to {:d}", line)
        if not p:
            continue
        (count, from_stack, to_stack) = p
        for i in range(count):
            stacks_a[to_stack - 1].append(stacks_a[from_stack - 1].pop())

        print(f"Before B: {stacks_b[from_stack-1]}, {stacks_b[to_stack-1]}")
        new = []
        for i in range(count):
            new.append(stacks_b[from_stack - 1].pop())
        for i in range(count):
            stacks_b[to_stack - 1].append(new.pop())
        print(f"After B: {stacks_b[from_stack-1]}, {stacks_b[to_stack-1]}")


def top_of_stacks(stacks_to_top):
    top = []
    for stack in stacks_to_top:
        top.append(stack.pop())

    answer = "".join(top)
    return answer


answer_a = top_of_stacks(stacks_a)
submit(answer_a, part="a", day=5, year=2022)

answer_b = top_of_stacks(stacks_b)
submit(answer_b, part="b", day=5, year=2022)
