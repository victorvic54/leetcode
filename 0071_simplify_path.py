class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        path_list = path.split("/")
        
        for path in path_list:
            if (path == '' or path == '.'):
                continue
            elif (path == '..'):
                if (stack):
                    stack.pop()
            else:
                stack.append(path)
                
        return "/" + "/".join(stack)