import matplotlib.pyplot as plt
import matplotlib.animation as anm
import numpy as np

def spherePoints(rMag,resolution):
    theta = np.linspace(0,2*np.pi,resolution)
    phi = np.linspace(0,np.pi,resolution)
    x = rMag * np.outer(np.cos(theta),np.sin(phi))
    y = rMag * np.outer(np.sin(theta),np.sin(phi))
    z = rMag * np.outer(np.ones(np.size(theta)),np.cos(phi))
    return x,y,z

def plotOrbit(r,rSphere,resolution):

    x,y,z = spherePoints(rSphere,resolution)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.plot(r[0,:],r[1,:],r[2,:],color="orange")
    ax.plot_surface(x,y,z,color="cyan",alpha=0.4)

    ax.set_xlabel("x [km]")
    ax.set_ylabel("y [km]")
    ax.set_zlabel("z [km]")

    ax.set_aspect("equal")
    ax.view_init(elev=0, azim=-45)
    plt.show()

def animateOrbit(r,t,rSphere,resolution,speed):

    x,y,z = spherePoints(rSphere,resolution)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.plot_surface(x,y,z,color="cyan",alpha=0.4)
    ax.plot(r[0,:],r[1,:],r[2,:],color="orange")
    smallBody, = ax.plot([r[0,0]],[r[1,0]],[r[2,0]],marker="o",color='orange')

    ax.set_xlabel("x [km]")
    ax.set_ylabel("y [km]")
    ax.set_zlabel("z [km]")

    ax.set_aspect("equal")
    ax.view_init(elev=0, azim=-45)

    def update(frame):

        smallBody.set_data([r[0,frame]],[r[1,frame]])
        smallBody.set_3d_properties([r[2,frame]])
        return smallBody

    dt = t[1]-t[0]
    interval = 1000*dt/speed

    animation = anm.FuncAnimation(fig,update,frames=len(t),interval=interval,repeat=True)
    plt.show()
    return animation