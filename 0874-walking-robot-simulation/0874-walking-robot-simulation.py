class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        directions=["north","east","south","west"]
        curr_dir_ind=0
        x=0
        y=0
        obs_dis=0

        obs_dic={}

        for obs in obstacles:
            
            if obs[0] in obs_dic:
                obs_dic[obs[0]].append(obs[1])
            
            else:
                obs_dic[obs[0]]=[obs[1]]


    






        for h in range(len(commands)):

                if commands[h]==-1:
                    curr_dir_ind=curr_dir_ind+1

                    if curr_dir_ind>3:
                        curr_dir_ind=curr_dir_ind%4
                    
                    continue

                if commands[h]==-2:
                    curr_dir_ind=curr_dir_ind-1

                    if curr_dir_ind<-3:
                        curr_dir_ind=-(curr_dir_ind%4)

                    continue

                
                for i in range(1, commands[h]+1):

                    if directions[curr_dir_ind]=="north":

                        x_= x   # Peeks at x
                        y_= y+1 # Peeks at the next location in Y

                        if x_ in obs_dic.keys():

                            if  y_ in obs_dic[x_]:
                                
                                    break # won't move forward

                            else:
                                x=x_  
                                y=y_ #moves updward.
                                continue

                            
                        else:
                            x=x_  
                            y=y_ #moves updward.
                            continue
                    
                    if directions[curr_dir_ind]=="east":


                        x_= x+1   # Peeks at x
                        y_= y # Peeks at the next location in Y

                        if x_ in obs_dic.keys():
                            if y_ in obs_dic[x_] :
                            
                           

                                break # won't move eastward
                            
                            else:
                                x=x_  
                                y=y_ 
                                continue
                        
                        else:
                            x=x_  
                            y=y_ #moves eastward.
                            continue
                    
                    if directions[curr_dir_ind]=="south":


                        x_= x   # Peeks at x
                        y_= y-1 # Peeks at the next location in Y

                        
                        if x_ in obs_dic.keys():
                        
                            if y_ in obs_dic[x_] :
                           
                                break # won't move southward

                            else:
                                x=x_  
                                y=y_ 
                                continue
                        
                        else:
                            x=x_  
                            y=y_ #moves southward.
                            continue


                    if directions[curr_dir_ind]=="west":


                            x_= x-1   # Peeks at x
                            y_= y # Peeks at the next location in Y

                            if x_ in obs_dic.keys():

                                if y_ in obs_dic[x_] :
                                
                                    break # won't move westward
                                
                                else:
                                    x=x_  
                                    y=y_ 
                                    continue
                        
                            else:
                                x=x_  
                                y=y_ #moves westward.
                                continue

                sd=y**2+x**2

                if sd>obs_dis:
                    obs_dis=sd
                       
        return obs_dis
                   

        