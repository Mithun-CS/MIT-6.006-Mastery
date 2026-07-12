def count_anagram_substrings(T, S):
    '''
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    '''
def lower_ord(c):
    return ord(c) - ord('a')

def count_anagram_substrings(T, S):
    # m = length of text, n = number of queries, k = length of each query
    m, n, k = len(T), len(S), len(S[0])
    
    # D will map { Signature Tuple : Count of occurrences in T }
    D = {}
    
    # F is our active sliding window frequency table (26 slots for 'a'-'z')
    F = [0] * 26 
    
    # --- PHASE 1: SLIDING WINDOW OVER TEXT T ---
    for i in range(m):
        # 1. Add the new character entering the front of the window
        F[lower_ord(T[i])] += 1
        
        # 2. If window has exceeded size k, remove the character left behind
        if i >= k:
            F[lower_ord(T[i - k])] -= 1
            
        # 3. Once the window reaches exactly size k, record its signature
        if i >= k - 1:
            key = tuple(F)
            if key in D:
                D[key] += 1
            else:
                D[key] = 1
                
    # --- PHASE 2: BATCH QUERY PROCESSING ---
    A = [0] * n
    for i in range(n):
        # Build the frequency signature for the current query string S[i]
        F = [0] * 26
        for c in S[i]:
            F[lower_ord(c)] += 1
            
        # Check if this exact signature exists in our pre-computed dictionary
        key = tuple(F)
        if key in D:
            A[i] = D[key]
            
    return tuple(A)
