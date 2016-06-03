from scipy import misc

a=misc.imread('facebook.png')
b=a.copy()
b.shape=-1
b[a.ravel()==255] = 162
b.shape = a.shape
b[:,:,3]=a[:,:,3]
misc.imsave('facebook_gray.png', b)
