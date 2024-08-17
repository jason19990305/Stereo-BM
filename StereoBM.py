import numpy as np
import matplotlib.pyplot as plt
import cv2
import time

start = time.time()



imRef = cv2.imread("Camera2\\img1.png").astype(int)
imTarget = cv2.imread("Camera2\\img2.png").astype(int)

print(imRef.shape)
print(imTarget.shape)


fixed_windows_size = 25 # odd
dmax = 64 # disparity range


height = imRef.shape[0]
width = imRef.shape[1]



y_length = height - (fixed_windows_size - 1)
x_length = width - (fixed_windows_size - 1) - dmax


n = int((fixed_windows_size - 1) / 2)
start_point = int((fixed_windows_size - 1) / 2)

def GetDepth(ref,target): 

    SAD = np.zeros([height,width,dmax]) # height,wdith,d  :  intensity
    for j in range(x_length):
        x_min = j
        x_max = j + n*2 + 1
        ref_mat = ref[:,x_min:x_max] 
        for d in range(dmax):
            target_mat = target[:, x_min + d : x_max + d] 
            diff_mat = np.absolute(ref_mat - target_mat)
            for i in range(y_length):
                y_min = i
                y_max = i + n*2 + 1
                diff = diff_mat[y_min : y_max ]

                intensity = diff.sum()

                SAD[i,j,d] = intensity
                
    d_win = np.argmin(SAD,axis=2)
    
    if 0 :
        plt.bar(np.arange(dmax),SAD[0,0,:])
        plt.show()
    return d_win


def normalize(arr):
    arr = arr / float(dmax)
    

    return (arr * 255).astype(int)

depth_left = GetDepth(imRef,imTarget)
depth_left = normalize(depth_left)

end = time.time()

second = end - start
minute = second / 60

second = second % 60

print("Compute for %d:%d"%(minute,second))



cv2.imwrite("depth_left_box_filtering.png",depth_left)
cv2.waitKey(0)

# Plot 3d point

x_list = []
y_list = []
z_list = []
c_list = []

for y in range(height):
    for x in range(width):
        if depth_left[y,x] == 0:
            continue
        x_list.append(x)
        z_list.append(height - y)
        y_list.append(dmax - depth_left[y,x])
        color = [imRef[y,x,2].astype(float) / 255.0 , imRef[y,x,1].astype(float) / 255.0 , imRef[y,x,0].astype(float) / 255.0 ] # BGR to RGB
        
        c_list.append(color)
        
x_list = np.array(x_list)
y_list = np.array(y_list)
z_list = np.array(z_list)
c_list = np.array(c_list)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.grid(False) 

ax.scatter(x_list, y_list, z_list, c=c_list , marker=',',s=1)        
plt.show()