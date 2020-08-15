import matplotlib.pyplot as plt
from matplotlib.patches import Arc

## Function that returns a football pitch plot.
## Length, Width, Pitch colour, Line Colour and axis parameters can all be set.

def createPitch(length, width, pitchColour, lineColour, axis):

    #Create figure
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.set_facecolor(pitchColour)


    #Pitch Outline & Centre Line
    plt.plot([0,0],[0,width], color=lineColour)
    plt.plot([0,length],[width,width], color=lineColour)
    plt.plot([length,length],[width,0], color=lineColour)
    plt.plot([length,0],[0,0], color=lineColour)
    plt.plot([length / 2,length / 2],[0,width], color=lineColour)

    #Left Penalty Area
    plt.plot([16.5,16.5],[width/ 2 + 20, width / 2 - 20],color=lineColour)
    plt.plot([0,16.5],[width/ 2 + 20,width/ 2 + 20],color=lineColour)
    plt.plot([16.5,0],[width/ 2 - 20,width/ 2 - 20],color=lineColour)

    #Right Penalty Area
    plt.plot([length, length - 16.5],[width/ 2 + 20,width/ 2 + 20],color=lineColour)
    plt.plot([length - 16.5,length - 16.5],[width/ 2 + 20, width / 2 - 20],color=lineColour)
    plt.plot([length - 16.5, length],[width/ 2 - 20,width/ 2 - 20],color=lineColour)

    #Left 6-yard Box
    plt.plot([0,5.5],[width / 2 + 9, width / 2 + 9],color=lineColour)
    plt.plot([5.5,5.5],[width / 2 + 9,width / 2 - 9],color=lineColour)
    plt.plot([5.5,0],[width / 2 - 9,width / 2 - 9],color=lineColour)

    #Right 6-yard Box
    plt.plot([length,length - 5.5],[width / 2 + 9,width / 2 + 9],color=lineColour)
    plt.plot([length - 5.5, length - 5.5],[width / 2 + 9, width / 2 - 9],color=lineColour)
    plt.plot([length - 5.5,length],[width / 2 - 9,width / 2 - 9],color=lineColour)

    #Prepare Circles
    centreCircle = plt.Circle((length / 2,width / 2),9.15,color=lineColour,fill=False)
    centreSpot = plt.Circle((length / 2,width / 2),0.8,color=lineColour)
    leftPenSpot = plt.Circle((11, width / 2),0.8,color=lineColour)
    rightPenSpot = plt.Circle((length - 11,width / 2),0.8,color=lineColour)

    #Draw Circles
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
    ax.add_patch(leftPenSpot)
    ax.add_patch(rightPenSpot)

    #Prepare Arcs
    leftArc = Arc((11,width / 2),height=18.3,width=18.3,angle=0,theta1=308,theta2=52,color=lineColour)
    rightArc = Arc((length - 11,width / 2),height=18.3,width=18.3,angle=0,theta1=126,theta2=234,color=lineColour)

    #Draw Arcs
    ax.add_patch(leftArc)
    ax.add_patch(rightArc)

    #Left Goal
    plt.plot([0,-2.5],[width / 2 + 3.65,width / 2 + 3.65],color=lineColour)
    plt.plot([-2.5,-2.5],[width / 2 + 3.65,width / 2 - 3.65],color=lineColour)
    plt.plot([-2.5,0],[width / 2 - 3.65,width / 2 - 3.65],color=lineColour)

    #Right Goal
    plt.plot([length + 2.5,length],[width / 2 + 3.65,width / 2 + 3.65],color=lineColour)
    plt.plot([length + 2.5,length + 2.5],[width / 2 + 3.65,width / 2 - 3.65],color=lineColour)
    plt.plot([length,length + 2.5],[width / 2 - 3.65,width / 2 - 3.65],color=lineColour)

    #Tidy Axes
    plt.axis(axis)

    #Return Pitch
    return plt
