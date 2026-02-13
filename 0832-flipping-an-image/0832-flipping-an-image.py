class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [ [1-bit for bit in rows[::-1]] for rows in image ]
        
        # for row in range(len(image)):
        #     for col in range(len(image)):
        #         if image[row][col] == 0:
        #             image[row][col] = 1
        #         else:
        #             image[row][col] = 0
        #     image[row] = image[row][::-1]
        # return image
            
            
        

        
