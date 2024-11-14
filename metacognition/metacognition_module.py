# metacognition/metacognition_module.py

def metacognition(s1_solution, confidence, problem, system2_solver, confidence_threshold=1):
    system2_solver = system2_solver
    confidence_threshold = confidence_threshold
    s1_solution = s1_solution
    confidence = confidence
    problem = problem
    if confidence >= confidence_threshold:
        return s1_solution  # Return System 1 solution if confidence is sufficient
    else:
        return system2_solver.solve(problem)  # Call System 2 otherwise
