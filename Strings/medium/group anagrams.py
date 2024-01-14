def groupAnagrams(strs: list[str]) -> list[list[str]]:
        table = {}

        for word in strs:
            #get the key for adding values to it in the dcitionary
            word_key = ''.join(sorted(word))
            
            #create an empty dict for each new sorted word which acts as a key
            if word_key not in table:
                table[word_key] = []
            
            #if after sorting a word matches to its word key add it to the value of that word_key
            table[word_key].append(word)

        return sorted(list(table.values()))

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))