class Solution:
    def solveSudoku(self, puzzle: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # Change all the value string into integer
        for i in range(9):
            for j in range(9):
                if (puzzle[i][j] != '.'):
                    puzzle[i][j] = int(puzzle[i][j])
        
        self.puzzle = puzzle # self.puzzle is a list of lists
        self.ans = copy.deepcopy(puzzle) # self.ans is a list of lists

        self.counter = 0 # used to count number of nodes explored
        self.domains = {} # used for inference function below
        
        # initialises domain dictionary
        for r,row in enumerate(self.ans):
            for c,val in enumerate(row):
                if val != '.':
                    self.domains[(r,c)] = (val,)
                else:
                    self.domains[(r,c)] = set(i for i in range(1,10))
        
        # runs inference on initial state
        for r,row in enumerate(self.ans):
            for c,val in enumerate(row):
                if val != '.':
                    self.inference(val, r, c)

        if self.fill() == False:
            print("No solution exists")
        
        # Else completed successfully
        # modify initial puzzle in place
        for i in range(9):
            for j in range(9):
                self.puzzle[i][j] = str(self.ans[i][j])
        

    # MOST CONSTRAINTED VARIABLE
    # variable ordering heuristic 
    #
    # returns the next zero to fill with smallest domain size (most constraint)
    def find_next_zero(self):

        chosen_index = (-1,-1)
        small = 9

        for coordinates, domain in self.domains.items():
            # we ignore when it is tuple because it is already filled by the question
            if type(domain) == set:
                size = len(domain)
                if size < small:
                    small = size
                    chosen_index = coordinates
            
        return chosen_index

    
    # value ordering heuristic
    #
    # returns the order of value to explore at self.ans[r][c]
    # must contain all the values in self.domains[(r,c)]
    def get_ordered_values(self, r, c):
        return self.domains[(r,c)]

    
    # ARC CONSISTENCY AC3
    # inference
    #
    # reduces self.domains AND
    # returns a tuple of
    #     1. dictionary from index to the set of removed values for the domain at that index
    #     2. boolean indicating if no domain is reduced to empty (False means failure)
    #
    # example: ({(1,1): {1}, (1,2): {1}, (1,3): {1}}, True) means the inference removed 1 from domains of indices
    #           (1,1), (1,2), (1,3) and no domain is reduced to empty set 
    def inference(self, val, r, c):
        removed_values = {}
        to_check = [(r,c)]
        
        while len(to_check) > 0:
            r, c = to_check.pop()
            val = list(self.domains[(r,c)])[0]  # size of domain = 1
            
            # check row wise
            for i in range(9):
                if i != c and val in self.domains[(r,i)]:
                    if len(self.domains[(r,i)]) == 1:  # removing val will reduce domain to empty
                        return removed_values, False
                    
                    self.domains[(r,i)].remove(val)
                    
                    if (r,i) in removed_values:
                        removed_values[(r,i)].add(val)
                    else:
                        removed_values[(r,i)] = set([val])
                    
                    if len(self.domains[(r,i)]) == 1:
                        to_check.append((r,i))

            # check col wise
            for i in range(9):
                if i != r and val in self.domains[(i,c)]:
                    if len(self.domains[(i,c)]) == 1:
                        return removed_values, False
                    
                    self.domains[(i,c)].remove(val)
                    
                    if (i,c) in removed_values:
                        removed_values[(i,c)].add(val)
                    else:
                        removed_values[(i,c)] = set([val])

                    if len(self.domains[(i,c)]) == 1:
                        to_check.append((i,c))

            R = r//3
            C = c//3
            for i in range(R*3, R*3+3):
                for j in range(C*3, C*3+3):
                    if not (i == r and j == c) and val in self.domains[(i,j)]:
                        if len(self.domains[(i,j)]) == 1:
                            return removed_values, False
                        
                        self.domains[(i,j)].remove(val)
                        
                        if (i,j) in removed_values:
                            removed_values[(i,j)].add(val)
                        else:
                            removed_values[(i,j)] = set([val])

                        if len(self.domains[(i,j)]) == 1:
                            to_check.append((i,j))
        
        return removed_values, True


    # helper function to get 3x3 subgrid. Only used in valid_value function.
    def get_subgrid(self, r, c):
        R = r//3
        C = c//3
        temp = []

        for i in range(R*3, R*3+3):
            for j in range(C*3, C*3+3):
                if self.ans[i][j] != 0:
                    temp.append(self.ans[i][j])
        return temp    


    # helper function to check if value val is valid at (r,c) coordinates
    def valid_value(self, val, r, c):
        if val in self.ans[r] or val in [j[c] for j in self.ans] or val in self.get_subgrid(r, c):
            return False
        return True 
        

    # recursive backtracking search
    def fill(self):
        r,c = self.find_next_zero()
        
        # base case
        if r == -1 and c == -1:
            return True
        
        # iterate through values
        value_order = self.get_ordered_values(r, c)
        
        for curr in value_order: 
            if self.valid_value(curr, r, c):
                self.ans[r][c] = curr
                
                # domain at (r,c) is reduced to just curr
                domain_before = self.domains[(r, c)]
                self.domains[(r,c)] = (curr,)
                    
                # infer domain reduction given that we just set the domain of (r,c) to curr
                removed_values, is_ok = self.inference(curr, r, c)
                if is_ok:
                    # recursive call
                    self.counter += 1

                    from_child = self.fill()

                    if from_child == True: # child has found a solution
                        return True
                                            
                # undo changes as recursive step above failed
                for index in removed_values:
                    # add removed values back to domain
                    self.domains[index].update(removed_values[index])

                self.domains[(r,c)] = domain_before
                self.ans[r][c] = '.'
            
        return False
