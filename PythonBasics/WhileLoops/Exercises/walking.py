total_steps = 0
is_goal_reached = False

while True:
    command = input()
    if command == "Going home":
        total_steps += int(input())
        break
    total_steps += int(command)
    if total_steps >= 10000:
        is_goal_reached = True
        break

if total_steps >= 10000:
    is_goal_reached = True

if is_goal_reached:
    print(f"Goal reached! Good job!")
    print(f"{total_steps - 10000} steps over the goal!")
else:
    print(f"{10000 - total_steps} more steps to reach goal.")