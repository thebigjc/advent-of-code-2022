from aocd import lines, submit

ip = 1
x = 0
score = 0

def increment_ip():
    

for l in lines:
    (opcode, value) = l.split(" ")
    
    match opcode:
        case "noop":
            increment_ip()
        case "addx":
            increment_ip()
            x += int(value)
            increment_ip()
    
            