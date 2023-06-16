import cv2

def findconnection(number, contours,q):

    cont = contours[number]
    connections = []
    for i in range(len(cont)):
        for j in range(len(contours)):
            for b in range(q//10):
                if ((number != j) and (cv2.pointPolygonTest(contours[j], (int(cont[i][0][0] - (b*10)), int(cont[i][0][1])), False) == 1)):
                    connections.append(j)
                if ((number != j) and (cv2.pointPolygonTest(contours[j], (int(cont[i][0][0]), int(cont[i][0][1] - (b*10))), False) == 1)):
                    connections.append(j)
                if ((number != j) and (cv2.pointPolygonTest(contours[j], (int(cont[i][0][0] + (b*10)), int(cont[i][0][1])), False) == 1)):
                    connections.append(j)
                if ((number != j) and (cv2.pointPolygonTest(contours[j], (int(cont[i][0][0]), int(cont[i][0][1] + (b*10))), False) == 1)):
                    connections.append(j)

    seen = set()
    seen_add = seen.add
    return [x for x in connections if not (x in seen or seen_add(x))]

def drawconnectionslines(imgcroped, contours, centersmass,q):
    # font = cv2.FONT_HERSHEY_SIMPLEX
    # bottomLeftCornerOfText = (10, 500)
    # fontScale = 2
    # fontColor = (255, 255, 255)
    # thickness = 2
    # lineType = 2
    croped1 = cv2.imread(imgcroped)
    connections = []
    for i in range(len(contours)):
        connections.append(findconnection(i,contours,q))

    for i in range(len(connections)):
        for j in (connections[i]):
            cv2.line(croped1, (centersmass[i][0],centersmass[i][1]), (centersmass[j][0],centersmass[j][1]), (255,255,255), 2)
            #text = str(dict.get(seq[j]))
            #cv2.putText(croped1, text, (int((centersmass[i][0] + centersmass[j][0])/2), int((centersmass[i][1] + centersmass[j][1])/2)), font, fontScale, fontColor, thickness, lineType)
    cv2.imwrite(imgcroped + 'auf.png', croped1)
    return connections
