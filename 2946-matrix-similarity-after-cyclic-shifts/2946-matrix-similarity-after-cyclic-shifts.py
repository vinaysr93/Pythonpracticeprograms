class Solution:
    
    
    
        def areSimilar(self, mat: List[List[int]], k: int) -> bool:
            
                # Handle left shift and right shift separately
               
                col_len=len(mat[0])
                k=k%col_len
                m=len(mat)
                n=len(mat[0])


                for i in range(m):

                    for j in range(n):


                      

                            if mat[i][j]==mat[i][(j+k)%col_len]:
                                continue
                            else:
                                return False

                      
                return True



