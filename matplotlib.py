import matplotlib.pyplot as plt

#1
x=t=[1,2,3,4,5,6,7]
y=CA=[120,155,125,202,180,235,240]
plt.xlabel('temps')
plt.ylabel('CA')
plt.title('Nuage de points avec matplotlib ')
plt.scatter(x,y)
plt.show()

#2
'''
(1)CA[0]=a*t[0]+b
(2)CA[6]=a*t[6]+b
2-1 donne:
'''
a=(CA[6]-CA[0])/(t[6]-t[0])
print("a=",a)
'''
d'aprés l'equation n°1:
CA[0]=a*t[0]+b
'''
b=CA[0]-a*t[0]
print("b=",b)

#3
plt.plot([1,7],[120,240],color='red')
plt.scatter(x,y,s=30)

plt.title("Tracer un nuage de points avec matlolip")

plt.xlabel('temps')
plt.ylabel("CA")

plt.show()

#4
CA8=a*8+b
print("le cheiffre d'affire pour t=8 est:",CA8)

