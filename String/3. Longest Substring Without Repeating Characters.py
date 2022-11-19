def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) in [0, 1]:
            return len(s)
        
        # Integer to keep track of the current length of unique characters
        curr_length = 0
        # Array to store all unique characters
        char_present = []
        # Array to store all lengths of unique characters
        all_lengths = []
        
        for i in range(len(s)):
            # If character not in char_present
            if s[i] not in char_present:
                # Add to char_present
                char_present.append(s[i])
                # Increment current length by 1
                curr_length += 1
            else:
                # Append current length to all_lengths
                all_lengths.append(curr_length)
                # Find first inded of repeated character in char_present
                ind = char_present.index(s[i])
                # Modfify char_present to contain all characters after repeated 
                char_present = char_present[ind+1::]
                # Add current character to char_present
                char_present.append(s[i])
                # Update curr_length to current length of char_present
                curr_length = len(char_present)
                
        # Add curr_length to all lengths
        all_lengths.append(curr_length)
        
        # Find max length from all_lengths
        return max(all_lengths)
