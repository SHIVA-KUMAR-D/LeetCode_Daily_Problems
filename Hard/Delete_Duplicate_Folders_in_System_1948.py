from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.deleted = False

class Solution:
    def deleteDuplicateFolder(self, paths):
        root = TrieNode()

        # Step 1: Build the trie
        for path in paths:
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = TrieNode()
                node = node.children[folder]

        serial_map = defaultdict(list)  # serialization -> list of nodes with that serialization

        # Step 2: Serialize subtrees and detect duplicates
        def serialize(node):
            if not node.children:
                return ""
            serials = []
            for name in sorted(node.children):
                child_serial = serialize(node.children[name])
                serials.append(f"{name}({child_serial})")
            full_serial = "".join(serials)
            serial_map[full_serial].append(node)
            return full_serial

        serialize(root)

        # Step 3: Mark duplicate folders
        for nodes in serial_map.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.deleted = True

        # Step 4: Collect remaining paths using DFS
        res = []

        def dfs(node, path):
            for name, child in node.children.items():
                if child.deleted:
                    continue
                path.append(name)
                res.append(list(path))
                dfs(child, path)
                path.pop()

        dfs(root, [])
        return res
