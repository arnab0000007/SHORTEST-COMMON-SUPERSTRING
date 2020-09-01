scs = ['']
def greedy_scs(reads, k):
     temp = reads.copy()
     best = max_overlap(reads,k)
     a = 0
     
     while scs:
         if len(scs[0])==1:
             break
         scs.remove(scs[0])   
         
         for a in range(len(best)):
                
                if best[0][2]!=0:
                    reads.remove(best[a][0])
                    reads.remove(best[a][1])
                    read_c=best[a][0] + best[a][1][best[a][2]:]
                    reads.append(read_c)
                    scs.append(reads)
                    reads=temp.copy()    
                    a=a+1
                else:
                    reads.remove(best[a][0])
                    reads.remove(best[a][1])
                    read_c=best[a][0] + best[a][1]
                    reads.append(read_c)
                    scs.append(reads)
                    reads=temp.copy()    
                    a=a+1
         
         i = scs[0]
         greedy_scs(i,k=0)
         
def main(reads):
    greedy_scs(reads,k=0)
    a=0
    x1 =' '.join(map(str, scs[a])) 
    minimum = len(x1)
    final=[]
    for a in range(len(scs)):
        x2 = ' '.join(map(str, scs[a]))
        l=len(x2)
        if l==minimum:
            temp = scs[a]
            if temp not in final:
                 final.append(scs[a])
        if l<minimum:
            minimum=l
            final = []
            final.append(scs[a])
                        
        a=a+1    
   
       
    print("SHORTEST COMMON SUPERSTRING : ",final)

def overlap(a, b, min_length):
    start = 0
    while True:
        start = a.find(b[:min_length], start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return len(a)-start          
        if b.startswith(a[start:(start+len(b))]):
            return len(b)
        start += 1  

def max_overlap(reads, k):
    best = [['', '',0]]
    for a in range(len(reads)):
        for b in range(len(reads)):
            if a!=b:
                olen =overlap(reads[a], reads[b], min_length=k)
                if olen>0:
                    if olen == best[0][2]:
                        temp = [reads[a], reads[b],olen]
                        if temp not in best:
                            best.append(temp)
                    if olen > best[0][2]:
                        best = []
                        temp2 = [reads[a], reads[b],olen] 
                        best.append(temp2)
                else:
                    if best[0][2]==0:
                        best = []
                        temp3=[reads[a],reads[b],olen]
                        best.append(temp3)
            b=b+1
        a=a+1    
    return best
