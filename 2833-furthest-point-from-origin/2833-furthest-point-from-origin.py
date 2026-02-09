class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        listMoves = list(moves)

        return abs(listMoves.count("L") - listMoves.count("R")) + listMoves.count("_")
