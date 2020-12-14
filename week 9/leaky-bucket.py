print("Enter the queue of packets lengths:")
queue=list(map(int,input().strip().split()))
output_rate = int(input("Enter output_rate: "))
bucket_size = int(input("Enter bucket size: "))
n=0
while len(queue):
    if queue[0]>bucket_size:
        print("Bucket Overflow!")
        break
    print("packet number "+str(n)+" , packet size ="+str(queue[0]))
    print("Bucket output successful")
    while queue[0]>output_rate:
        print(str(output_rate)+" output")
        queue[0]-=output_rate
    if queue[0]:
        print(str(queue[0])+" sent")
    print("Packet sent")
    queue.pop(0)
    n+=1
   
        