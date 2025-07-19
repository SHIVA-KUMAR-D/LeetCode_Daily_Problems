class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        # Sort folders lexicographically
        folder.sort()
        result = [folder[0]]  # Always keep the first folder

        for path in folder[1:]:
            # If the current path is not a subfolder of the last added one
            if not path.startswith(result[-1] + "/"):
                result.append(path)
        
        return result
