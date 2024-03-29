import pygame
from RRTbasePy import RRTGraph
from RRTbasePy import RRTMap

def main () :
    dimensions = (600,1000)
    start = (50,50)
    goal = (800,500)
    obsdim = 10
    obsnum = 200
    iteration = 0

    pygame.init ()
    map = RRTMap(start , goal , dimensions , obsdim , obsnum)
    graph = RRTGraph(start , goal , dimensions , obsdim , obsnum)

    obstacles = graph.makeobs()
    map.drawMap(obstacles)

    while (iteration<500) :

        if iteration % 10 == 0 :
            X,Y,Parent = graph.bias(goal)
            pygame.draw.circle(map.map , map.grey , (X[-1] , Y[-1]) , map.nodeRad , 0 )
            pygame.draw.line (map.map , map.Blue , (X[-1] , Y[-1]) , (X[Parent[-1]] , Y[Parent[-1]]) , map.edgeThickness)

        else :
            X,Y,Parent = graph.expand()
            pygame.draw.circle(map.map , map.grey , (X[-1] , Y[-1]) , map.nodeRad , 0 )
            pygame.draw.line (map.map , map.Blue , (X[-1] , Y[-1]) , (X[Parent[-1]] , Y[Parent[-1]]) , map.edgeThickness)

        if iteration % 5 == 0 :
            pygame.display.update()

        iteration +=1

    pygame.display.update()
    pygame.event.clear()
    pygame.event.wait(0)



    # while (True) :
    #     x,y = graph.sample_envir()
    #     n = graph.number_of_nodes()
    #     graph.add_node(n , x , y )
    #     graph.add_edge(n-1 , n)
    #     x1 , y1 = graph.x[n] , graph.y[n]
    #     x2 , y2 = graph.x[n-1] , graph.y[n-1]

    #     if (graph.isFree()) :
    #         pygame.draw.circle(map.map , map.Red , (graph.x[n] , graph.y[n]) , map.nodeRad , map.nodeThickness )

    #         if not graph.crossObstacles(x1 , x2 , y1 , y2 ) :
    #             pygame.draw.line (map.map , map.Blue , (x1 ,y1) , (x2 , y2) , map.edgeThickness)

    #         pygame.display.update()


    # pygame.event.clear()
    # pygame.event.wait(0)

if __name__ == '__main__':
    main()

