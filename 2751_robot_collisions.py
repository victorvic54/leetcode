class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        initial_pos = [i for i in range(len(positions))]
        sorted_pos = sorted(zip(positions, healths, directions, initial_pos))
        sorted_pos = [list(pos) for pos in sorted_pos]

        has_collision = True
        while has_collision:
            has_collision = False
            tmp_pos = []

            for i in range(len(sorted_pos)):
                tmp_pos.append(sorted_pos[i])
                while len(tmp_pos) >= 2 and tmp_pos[-2][2] == "R" and tmp_pos[-1][2] == "L":
                    has_collision = True
                    if tmp_pos[-1][1] < tmp_pos[-2][1]:
                        tmp_pos[-2][1] -= 1
                        tmp_pos.pop()
                    elif tmp_pos[-1][1] == tmp_pos[-2][1]:
                        tmp_pos.pop()
                        tmp_pos.pop()
                    else:
                        tmp = tmp_pos.pop()
                        tmp_pos.pop()
                        tmp[1] -= 1
                        tmp_pos.append(tmp)

            sorted_pos = tmp_pos
        
        final_result = []
        res_list = sorted(sorted_pos, key=lambda x: x[3])
        for res in res_list:
            final_result.append(res[1])
        
        return final_result

