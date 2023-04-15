def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    onBridge = 0
    while bridge:
        answer += 1
        onBridge -= bridge.pop(0)
        if truck_weights:
            if onBridge + truck_weights[0] <= weight:
                truck = truck_weights.pop(0)
                bridge.append(truck)
                onBridge += truck
            else:
                bridge.append(0)
    return answer

print(solution(2, 10, [7,4,5,6]))