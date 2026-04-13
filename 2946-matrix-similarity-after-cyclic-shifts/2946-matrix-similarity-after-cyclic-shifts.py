class Solution:
    
    
    
        def areSimilar(self, mat: List[List[int]], k: int) -> bool:
            
                # Handle left shift and right shift separately
                mat_or=[]

                for j in mat:

                    lin=[]
                    for l in j:
                        lin.append(l)
                    
                    mat_or.append(lin)


                def left_shift(arr):

                    a=arr.pop(0)
                    arr.append(a)

                    return arr




                def right_shift(arr):

                    a=arr.pop()
                    arr.insert(0,a)

                    return arr

                for x in range (k):

                    for i in range (len (mat)):

                        if i%2==0:

                            rot_arr= left_shift(mat[i])

                            mat[i]=rot_arr

                        else:

                            rot_arr=right_shift(mat[i])
                            mat[i]=rot_arr

                print(mat)
                print("Mat_Ori",mat_or)
                return mat==mat_or

    



