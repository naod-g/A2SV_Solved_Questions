class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
        
        secret = list(secret)
        guess = list(guess)


        for num in guess:
            if num in secret:
                cow += 1
                secret.remove(num)

        cow -= bull

        return f"{bull}A{cow}B"