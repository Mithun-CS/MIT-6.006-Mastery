def short_company(C, P, n, k):
    '''
    Input:  C | Tuple of s = |C| strings representing names of companies
            P | Tuple of s lists each of size nk representing prices
            n | Number of days of price information
            k | Number of prices in one day
    Output: c | Name of a company with highest shorting value
            S | List containing a longest subsequence of 
              | decreasing prices from c that doesn't skip days
    '''
    c = C[0]
    S = []
    ##################
    def dec_subseqs(arr):
        res = []

        def dfs(i, path):
            if i == len(arr):
                if path:
                    res.append(tuple(path))
                return
            dfs(i + 1, path)
            if not path or arr[i] < path[-1]:
                dfs(i + 1, path + [arr[i]])

        dfs(0, [])
        return res

    best_len = 0
    for idx, prices in enumerate(P):
        days = [prices[d * k:(d + 1) * k] for d in range(n)]
        company_best = []

        for start in range(n):
            dp = {}
            for sub in dec_subseqs(days[start]):
                last = sub[-1]
                if last not in dp or len(sub) > dp[last][0]:
                    dp[last] = (len(sub), list(sub))

            if dp:
                length, seq = max(dp.values(), key=lambda x: x[0])
                if length > len(company_best):
                    company_best = seq

            for d in range(start + 1, n):
                new_dp = {}
                for last, (length, seq) in dp.items():
                    for sub in dec_subseqs(days[d]):
                        if sub[0] < last:
                            new_seq = seq + list(sub)
                            new_last = sub[-1]
                            new_len = len(new_seq)
                            if new_last not in new_dp or new_len > new_dp[new_last][0]:
                                new_dp[new_last] = (new_len, new_seq)
                dp = new_dp
                if not dp:
                    break
                length, seq = max(dp.values(), key=lambda x: x[0])
                if length > len(company_best):
                    company_best = seq

        if len(company_best) > best_len:
            best_len = len(company_best)
            c = C[idx]
            S = company_best
    ##################
    return (c, S)
