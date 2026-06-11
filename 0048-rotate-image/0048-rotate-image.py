class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m= len(matrix) # Row length
        n= len (matrix[0]) # Column length

        # Approach is to find the transpose of a matrix and then reverse each row. 

        for x in range (0,m):

            for y in range (x,n):

                if x==y:
                    continue
                
                else:
                    t=matrix[x][y]
                    matrix[x][y]=matrix[y][x]
                    matrix[y][x]=t
        
        print("Transpose",matrix)
        for i in range (0,m):

            matrix[i][:]=matrix[i][::-1]
            print ("Matrix of i", matrix[i])

        return matrix
      