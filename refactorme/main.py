from refactorme.Parsers.futoshiki_parser import readFutoshiki
from refactorme.Parsers.crossmath_parser import readCrossMath
from refactorme.CSPs.futoshiki import FutoshikiCSP
from refactorme.CSPs.crossmath import CrossmathCSP
from refactorme.CSAlgorithms import AC3, backtracking
from refactorme.Problems import test_futoshiki_answers

def futoshiki_tests():
    for puzzle in range(1, 2):  # increase bound up to 5
        print()
        print()
        print()
        print('=====================================')
        print('  Running Test Trials for Puzzle #', puzzle)
        print('=====================================')
        print()
        problem = readFutoshiki('./Problems/test_futoshiki' + str(puzzle) + '.txt')
        for trial in range(1, 4):
            print('Backtracking trial ', trial)
            csp = FutoshikiCSP(problem[0], problem[1])
            csp.metrics.start()
            solution = backtracking.backtracking_search(csp)
            csp.metrics.stop()
            print(solution)
            csp.metrics.get_metrics()
            print()
        print()
        print()
        for trial in range(1, 4):
            print('Backtracking with AC3 preprocessing trial ', trial)
            csp = FutoshikiCSP(problem[0], problem[1])
            b = AC3.ac3(csp)
            csp.metrics.start()
            solution = backtracking.backtracking_search(csp)
            csp.metrics.stop()
            print(solution)
            csp.metrics.get_metrics()
            print()
        print()
        print()
        for trial in range(1, 4):
            print('FC trial ', trial)
            csp = FutoshikiCSP(problem[0], problem[1])
            csp.metrics.start()
            solution = backtracking.fc_backtracking_search(csp)
            csp.metrics.stop()
            print(solution)
            csp.metrics.get_metrics()
            print()
        print()
        print()
        for trial in range(1, 4):
            print('FC with AC3 preprocessing trial ', trial)
            csp = FutoshikiCSP(problem[0], problem[1])
            AC3.ac3(csp)
            csp.metrics.start()
            solution = backtracking.fc_backtracking_search(csp)
            csp.metrics.stop()
            print(solution)
            csp.metrics.get_metrics()
            print()
        print()
        print()
        for trial in range(1, 4):
            print('MAC trial ', trial)
            csp = FutoshikiCSP(problem[0], problem[1])
            csp.metrics.start()
            solution = backtracking.mac_backtracking_search(csp)
            csp.metrics.stop()
            print(solution)
            csp.metrics.get_metrics()
            print()
        print()
        print()
        for trial in range(1, 4):
            print('MAC with AC3 preprocessing trial ', trial)
            csp = FutoshikiCSP(problem[0], problem[1])
            AC3.ac3(csp)
            csp.metrics.start()
            solution = backtracking.mac_backtracking_search(csp)
            csp.metrics.stop()
            print(solution)
            csp.metrics.get_metrics()
            print()
        print()
        print()

def crossmath_tests():
    problem = readCrossMath('./Problems/test_crossmath.txt')
    csp = CrossmathCSP(problem[0], problem[1])
    csp.metrics.start()
    solution = backtracking.mac_backtracking_search(csp)
    csp.metrics.stop()
    print(solution)
    csp.metrics.get_metrics()
    print()


if __name__ == "__main__":
    #futoshiki_tests()
    crossmath_tests()