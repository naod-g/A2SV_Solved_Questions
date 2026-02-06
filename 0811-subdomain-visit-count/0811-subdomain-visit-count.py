class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mp = defaultdict(int)
        res = []

        for domain in cpdomains:
            count, dmn = domain.split()
            domain_list = dmn.split(".")

            for i in range(len(domain_list)):
                curr_domain = ".".join(domain_list[i:])
                mp[curr_domain] += int(count)

        for k, v in mp.items():
            res.append(f"{v} {k}")
        
        return res