class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = []
        
        for f in folder:
            # If the result is empty or the current folder is not a subfolder of the last added
            if not result or not f.startswith(result[-1] + '/'):
                result.append(f)
        
        return result